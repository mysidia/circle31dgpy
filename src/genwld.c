/************************************************************************
 * Generic OLC Library - Rooms / genwld.c			v1.0	*
 * Original author: Levork						*
 * Copyright 1996 by Harvey Gilpin					*
 * Copyright 1997-2001 by George Greer (greerga@circlemud.org)		*
 ************************************************************************/

#include "conf.h"
#include "sysdep.h"

#include "structs.h"
#include "utils.h"
#include "db.h"
#include "handler.h"
#include "comm.h"
#include "genolc.h"
#include "genwld.h"
#include "genzon.h"

extern struct room_data *world;
extern struct zone_data *zone_table;
extern struct index_data *mob_index;
extern zone_rnum top_of_zone_table;
extern room_rnum r_mortal_start_room;
extern room_rnum r_immort_start_room;
extern room_rnum r_frozen_start_room;

/*
 * This function will copy the strings so be sure you free your own
 * copies of the description, title, and such.
 */
room_rnum add_room(struct room_data *room)
{
  struct char_data *tch;
  struct obj_data *tobj;
  int i, j, found = FALSE;

  if (room == NULL)
    return NOWHERE;

  if ((i = real_room(room->number)) != NOWHERE) {
    copy_room(&world[i], room);
    add_to_save_list(zone_table[room->zone].number, SL_WLD);
    log("GenOLC: add_room: Updated existing room #%d.", room->number);
    return i;
  }

  RECREATE(world, struct room_data, top_of_world + 2);
  top_of_world++;

  for (i = top_of_world; i > 0; i--) {
    if (room->number > world[i - 1].number) {
      world[i] = *room;
      copy_room_strings(&world[i], room);
      found = i;
      break;
    } else {
      /* Copy the room over now. */
      world[i] = world[i - 1];

      /* People in this room must have their in_rooms moved up one. */
      for (tch = world[i].people; tch; tch = tch->next_in_room)
	IN_ROOM(tch) += (IN_ROOM(tch) != NOWHERE);

      /* Move objects too. */
      for (tobj = world[i].contents; tobj; tobj = tobj->next_content)
	IN_ROOM(tobj) += (IN_ROOM(tobj) != NOWHERE);
    }
  }
  if (!found) {
    world[0] = *room;	/* Last place, in front. */
    copy_room_strings(&world[0], room);
  }

  log("GenOLC: add_room: Added room %d at index #%d.", room->number, found);

  /* found is equal to the array index where we added the room. */

  /*
   * Find what zone that room was in so we can update the loading table.
   */
  for (i = room->zone; i <= top_of_zone_table; i++)
    for (j = 0; ZCMD(i, j).command != 'S'; j++)
      switch (ZCMD(i, j).command) {
      case 'M':
      case 'O':
	ZCMD(i, j).arg3 += (ZCMD(i, j).arg3 >= found);
	break;
      case 'D':
      case 'R':
	ZCMD(i, j).arg1 += (ZCMD(i, j).arg1 >= found);
      case 'G':
      case 'P':
      case 'E':
      case '*':
	/* Known zone entries we don't care about. */
        break;
      default:
        mudlog(BRF, LVL_GOD, TRUE, "SYSERR: GenOLC: add_room: Unknown zone entry found!");
      }
      
  /*
   * Update the loadroom table. Adds 1 or 0.
   */
  r_mortal_start_room += (r_mortal_start_room >= found);
  r_immort_start_room += (r_immort_start_room >= found);
  r_frozen_start_room += (r_frozen_start_room >= found);

  /*
   * Update world exits.
   */
  for (i = top_of_world; i >= 0; i--)
    for (j = 0; j < NUM_OF_DIRS; j++)
      if (W_EXIT(i, j))
	W_EXIT(i, j)->to_room += (W_EXIT(i, j)->to_room >= found);

  add_to_save_list(zone_table[room->zone].number, SL_WLD);

  /*
   * Return what array entry we placed the new room in.
   */
  return found;
}

/* -------------------------------------------------------------------------- */

int delete_room(room_rnum rnum)
{
  int i, j;
  struct char_data *ppl, *next_ppl;
  struct obj_data *obj, *next_obj;
  struct room_data *room;

  if (rnum <= 0 || rnum > top_of_world)	/* Can't delete void yet. */
    return FALSE;

  room = &world[rnum];

  add_to_save_list(zone_table[room->zone].number, SL_WLD);

  /* This is something you might want to read about in the logs. */
  log("GenOLC: delete_room: Deleting room #%d (%s).", room->number, room->name);

  if (r_mortal_start_room == rnum) {
    log("WARNING: GenOLC: delete_room: Deleting mortal start room!");
    r_mortal_start_room = 0;	/* The Void */
  }
  if (r_immort_start_room == rnum) {
    log("WARNING: GenOLC: delete_room: Deleting immortal start room!");
    r_immort_start_room = 0;	/* The Void */
  }
  if (r_frozen_start_room == rnum) {
    log("WARNING: GenOLC: delete_room: Deleting frozen start room!");
    r_frozen_start_room = 0;	/* The Void */
  }

  /*
   * Dump the contents of this room into the Void.  We could also just
   * extract the people, mobs, and objects here.
   */
  for (obj = world[rnum].contents; obj; obj = next_obj) {
    next_obj = obj->next_content;
    obj_from_room(obj);
    obj_to_room(obj, 0);
  }
  for (ppl = world[rnum].people; ppl; ppl = next_ppl) {
    next_ppl = ppl->next_in_room;
    char_from_room(ppl);
    char_to_room(ppl, 0);
  }

  free_room_strings(room);

  /*
   * Change any exit going to this room to go the void.
   * Also fix all the exits pointing to rooms above this.
   */
  for (i = top_of_world; i >= 0; i--)
    for (j = 0; j < NUM_OF_DIRS; j++)
      if (W_EXIT(i, j) == NULL)
        continue;
      else if (W_EXIT(i, j)->to_room > rnum)
        W_EXIT(i, j)->to_room--;
      else if (W_EXIT(i, j)->to_room == rnum)
        W_EXIT(i, j)->to_room = 0;	/* Some may argue -1. */

  /*
   * Find what zone that room was in so we can update the loading table.
   */
  for (i = 0; i <= top_of_zone_table; i++)
    for (j = 0; ZCMD(i , j).command != 'S'; j++)
      switch (ZCMD(i, j).command) {
      case 'M':
      case 'O':
	if (ZCMD(i, j).arg3 == rnum)
	  ZCMD(i, j).command = '*';	/* Cancel command. */
	else if (ZCMD(i, j).arg3 > rnum)
	  ZCMD(i, j).arg3--;
	break;
      case 'D':
      case 'R':
	if (ZCMD(i, j).arg1 == rnum)
	  ZCMD(i, j).command = '*';	/* Cancel command. */
	else if (ZCMD(i, j).arg1 > rnum)
	  ZCMD(i, j).arg1--;
      case 'G':
      case 'P':
      case 'E':
      case '*':
        /* Known zone entries we don't care about. */
        break;
      default:
        mudlog(BRF, LVL_GOD, TRUE, "SYSERR: GenOLC: delete_room: Unknown zone entry found!");
      }

  /*
   * Now we actually move the rooms down.
   */
  for (i = rnum; i < top_of_world; i++) {
    world[i] = world[i + 1];

    for (ppl = world[i].people; ppl; ppl = ppl->next_in_room)
      IN_ROOM(ppl) -= (IN_ROOM(ppl) != NOWHERE);	/* Redundant check? */

    for (obj = world[i].contents; obj; obj = obj->next_content)
      IN_ROOM(obj) -= (IN_ROOM(obj) != NOWHERE);	/* Redundant check? */
  }

  top_of_world--;
  RECREATE(world, struct room_data, top_of_world + 1);

  return TRUE;
}


int save_rooms(zone_rnum rzone)
{
  int i;
  struct room_data *room;
  FILE *sf;
  char filename[128];
  char buf[MAX_STRING_LENGTH];
  char buf1[MAX_STRING_LENGTH];
  char bit[64];

#if CIRCLE_UNSIGNED_INDEX
  if (rzone == NOWHERE || rzone > top_of_zone_table) {
#else
  if (rzone < 0 || rzone > top_of_zone_table) {
#endif
    log("SYSERR: GenOLC: save_rooms: Invalid zone number %d passed! (0-%d)", rzone, top_of_zone_table);
    return FALSE;
  }

  log("GenOLC: save_rooms: Saving rooms in zone #%d (%d-%d).",
	zone_table[rzone].number, genolc_zone_bottom(rzone), zone_table[rzone].top);

  snprintf(filename, sizeof(filename), "%s/%d.new", WLD_PREFIX, zone_table[rzone].number);
  if (!(sf = fopen(filename, "w"))) {
    perror("SYSERR: save_rooms");
    return FALSE;
  }

  for (i = genolc_zone_bottom(rzone); i <= zone_table[rzone].top; i++) {
    room_rnum rnum;

    if ((rnum = real_room(i)) != NOWHERE) {
      int j;

      room = (world + rnum);

      /*
       * Copy the description and strip off trailing newlines.
       */
      strncpy(buf, room->description ? room->description : "Empty room.", sizeof(buf)-1 );
      strip_cr(buf);

      /*
       * Save the numeric and string section of the file.
       */
      sprintascii(bit, room->room_flags);
      fprintf(sf, 	"#%d\n"
			"%s%c\n"
			"%s%c\n"
			"%d %s %d\n",
		room->number,
		room->name ? room->name : "Untitled", STRING_TERMINATOR,
		buf, STRING_TERMINATOR,
		zone_table[room->zone].number, bit, room->sector_type
      );

      /*
       * Now you write out the exits for the room.
       */
      for (j = 0; j < NUM_OF_DIRS; j++) {
	if (R_EXIT(room, j)) {
	  int dflag;
	  if (R_EXIT(room, j)->general_description) {
	    strncpy(buf, R_EXIT(room, j)->general_description, sizeof(buf)-1);
	    strip_cr(buf);
	  } else
	    *buf = '\0';

	  /*
	   * Figure out door flag.
	   */
	  if (IS_SET(R_EXIT(room, j)->exit_info, EX_ISDOOR)) {
	    if (IS_SET(R_EXIT(room, j)->exit_info, EX_PICKPROOF))
	      dflag = 2;
	    else
	      dflag = 1;
	  } else
	    dflag = 0;

	  if (R_EXIT(room, j)->keyword)
	    strncpy(buf1, R_EXIT(room, j)->keyword, sizeof(buf1)-1 );
	  else
	    *buf1 = '\0';

	  /*
	   * Now write the exit to the file.
	   */
	  fprintf(sf,	"D%d\n"
			"%s~\n"
			"%s~\n"
			"%d %d %d\n", j, buf, buf1, dflag,
		R_EXIT(room, j)->key, R_EXIT(room, j)->to_room != -1 ?
		world[R_EXIT(room, j)->to_room].number : -1);

	}
      }

      if (room->ex_description) {
        struct extra_descr_data *xdesc;

	for (xdesc = room->ex_description; xdesc; xdesc = xdesc->next) {
	  strncpy(buf, xdesc->description, sizeof(buf));
	  strip_cr(buf);
	  fprintf(sf,	"E\n"
			"%s~\n"
			"%s~\n", xdesc->keyword, buf);
	}
      }
      fprintf(sf, "S\n");
    }
  }

  /*
   * Write the final line and close it.
   */
  fprintf(sf, "$~\n");
  fclose(sf);

  /* Old file we're replacing. */
  snprintf(buf, sizeof(buf), "%s/%d.wld", WLD_PREFIX, zone_table[rzone].number);

  remove(buf);
  rename(filename, buf);

  if (in_save_list(zone_table[rzone].number, SL_WLD))
    remove_from_save_list(zone_table[rzone].number, SL_WLD);
  return TRUE;
}

int copy_room(struct room_data *to, struct room_data *from)
{
  free_room_strings(to);
  *to = *from;
  copy_room_strings(to, from);

  /* Don't put people and objects in two locations.
     Am thinking this shouldn't be done here... */
  from->people = NULL;
  from->contents = NULL;

  return TRUE;
}

/*
 * Idea by: Cris Jacobin <jacobin@bellatlantic.net>
 */
room_rnum duplicate_room(room_vnum dest_vnum, room_rnum orig)
{
  int new_rnum, znum;
  struct room_data nroom;

#if CIRCLE_UNSIGNED_INDEX
  if (orig == NOWHERE || orig > top_of_world) {
#else
  if (orig < 0 || orig > top_of_world) {
#endif
    log("SYSERR: GenOLC: copy_room: Given bad original real room.");
    return NOWHERE;
  } else if ((znum = real_zone_by_thing(dest_vnum)) == NOWHERE) {
    log("SYSERR: GenOLC: copy_room: No such destination zone.");
    return NOWHERE;
  }

  /*
   * add_room will make its own copies of strings.
   */
  if ((new_rnum = add_room(&nroom)) == NOWHERE) {
    log("SYSERR: GenOLC: copy_room: Problem adding room.");
    return NOWHERE;
  }

  nroom = world[new_rnum]; 
  nroom.number = dest_vnum;
  nroom.zone = znum;

  /* So the people and objects aren't in two places at once... */
  nroom.contents = NULL;
  nroom.people = NULL;

  return new_rnum;
}

/* -------------------------------------------------------------------------- */

/*
 * Copy strings over so bad things don't happen.  We do not free the
 * existing strings here because copy_room() did a shallow copy previously
 * and we'd be freeing the very strings we're copying.  If this function
 * is used elsewhere, be sure to free_room_strings() the 'dest' room first.
 */
int copy_room_strings(struct room_data *dest, struct room_data *source)
{
  int i;

  if (dest == NULL || source == NULL) {
    log("SYSERR: GenOLC: copy_room_strings: NULL values passed.");
    return FALSE;
  }

  dest->description = strdup(source->description);
  dest->name = strdup(source->name);

  for (i = 0; i < NUM_OF_DIRS; i++) {
    if (!R_EXIT(source, i))
      continue;

    CREATE(R_EXIT(dest, i), struct room_direction_data, 1);
    *R_EXIT(dest, i) = *R_EXIT(source, i);
    if (R_EXIT(source, i)->general_description)
      R_EXIT(dest, i)->general_description = strdup(R_EXIT(source, i)->general_description);
    if (R_EXIT(source, i)->keyword)
      R_EXIT(dest, i)->keyword = strdup(R_EXIT(source, i)->keyword);
  }

  if (source->ex_description)
    copy_ex_descriptions(&dest->ex_description, source->ex_description);

  return TRUE;
}

int free_room_strings(struct room_data *room)
{
  int i;

  /* Free descriptions. */
  if (room->name)
    free(room->name);
  if (room->description)
    free(room->description);
  if (room->ex_description)
    free_ex_descriptions(room->ex_description);

  /* Free exits. */
  for (i = 0; i < NUM_OF_DIRS; i++) {
    if (room->dir_option[i]) {
      if (room->dir_option[i]->general_description)
        free(room->dir_option[i]->general_description);
      if (room->dir_option[i]->keyword)
        free(room->dir_option[i]->keyword);
      free(room->dir_option[i]);
    }
  }

  return TRUE;
}