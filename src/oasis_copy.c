/******************************************************************************/
/** OasisOLC - InGame OLC Copying                                      v2.0  **/
/** Original author: Levork                                                  **/
/** Copyright 1996 Harvey Gilpin                                             **/
/** Copyright 1997-2001 George Greer (greerga@circlemud.org)                 **/
/** Copyright 2002 Kip Potter [Mythran] (kip_potter@hotmail.com)             **/
/******************************************************************************/
#include "conf.h"
#include "sysdep.h"

#include "structs.h"
#include "utils.h"
#include "comm.h"
#include "interpreter.h"
#include "handler.h"
#include "db.h"
#include "genolc.h"
#include "genzon.h"
#include "oasis.h"
#include "improved-edit.h"
#include "constants.h"


/******************************************************************************/
/** Internal Functions                                                       **/
/******************************************************************************/
ACMD(do_dig);

/******************************************************************************/
/** Commands                                                                 **/
/******************************************************************************/
ACMD(do_dig)
{
  char sdir[MAX_INPUT_LENGTH], sroom[MAX_INPUT_LENGTH], *new_room_name;
  room_vnum rvnum = NOWHERE;
  room_rnum rrnum = NOWHERE;
  zone_rnum zone;
  int dir = 0;
  struct descriptor_data *d = ch->desc; /* will save us some typing */
  
  /* Grab the room's name (if available). */
  new_room_name = two_arguments(argument, sdir, sroom);
  skip_spaces(&new_room_name);
  
  /* Can't dig if we don't know where to go. */
  if (!*sdir || !*sroom) {
    send_to_char(ch, "Format: dig <direction> <room> - to create an exit\r\n"
                     "        dig <direction> -1     - to delete an exit\r\n");
    return;
  }

  rvnum = atoi(sroom);
  rrnum = real_room(rvnum);  
  dir = search_block(sdir, dirs, FALSE);
  zone = world[IN_ROOM(ch)].zone;

  if (dir < 0) {
    send_to_char(ch, "Can not create an exit to the '%s'.\r\n", sdir);
    return;
  }
  /* Make sure that the builder has access to the zone he's in. */
  if ((zone == NOWHERE) || !can_edit_zone(ch, zone)) {
    send_to_char(ch, "You do not have permission to edit this zone.\r\n");
    return;
  }
  /*
   * Lets not allow digging to limbo. 
   * After all, it'd just get us more errors on 'show errors'
   */
  if (rvnum == 0) {
   send_to_char(ch, "The target exists, but you can't dig to limbo!\r\n");
   return;
  }
  /*
   * target room == -1 removes the exit 
   */
  if (rvnum == -1) { 
    if (W_EXIT(IN_ROOM(ch), dir)) {
      /* free the old pointers, if any */
      if (W_EXIT(IN_ROOM(ch), dir)->general_description)
        free(W_EXIT(IN_ROOM(ch), dir)->general_description);
      if (W_EXIT(IN_ROOM(ch), dir)->keyword)
        free(W_EXIT(IN_ROOM(ch), dir)->keyword);
      free(W_EXIT(IN_ROOM(ch), dir));
      W_EXIT(IN_ROOM(ch), dir) = NULL;
      add_to_save_list(zone_table[world[IN_ROOM(ch)].zone].number, SL_WLD);
      send_to_char(ch, "You remove the exit to the %s.\r\n", dirs[dir]);
      return;
    }
    send_to_char(ch, "There is no exit to the %s.\r\n"
                     "No exit removed.\r\n", dirs[dir]);
    return;
  }  
  /*
   * Can't dig in a direction, if it's already a door. 
   */
  if (W_EXIT(IN_ROOM(ch), dir)) {
      send_to_char(ch, "There already is an exit to the %s.\r\n", dirs[dir]);
      return;
  }
  
  /* Make sure that the builder has access to the zone he's linking to. */
  zone = real_zone_by_thing(rvnum);  
  if (zone == NOWHERE) {
    send_to_char(ch, "You cannot link to a non-existing zone!\r\n");
    return;
  }
  if (!can_edit_zone(ch, zone)) {
    send_to_char(ch, "You do not have permission to edit room #%d.\r\n", rvnum);
    return;
  }
  /*
   * Now we know the builder is allowed to make the link 
   */
  /* If the room doesn't exist, create it.*/
  if (rrnum == NOWHERE) {
    /*
     * Give the descriptor an olc struct.
     * This way we can let redit_save_internally handle the room adding.
     */
    if (d->olc) {
      mudlog(BRF, LVL_IMMORT, TRUE, "SYSERR: do_dig: Player already had olc structure.");
      free(d->olc);
    }
    CREATE(d->olc, struct oasis_olc_data, 1);
    OLC_ZNUM(d) = zone;
    OLC_NUM(d) = rvnum;
    CREATE(OLC_ROOM(d), struct room_data, 1);
    
    
    /* Copy the room's name. */
    if (*new_room_name)
     OLC_ROOM(d)->name = strdup(new_room_name);
    else
     OLC_ROOM(d)->name = strdup("An unfinished room");
    
    /* Copy the room's description.*/
    OLC_ROOM(d)->description = strdup("You are in an unfinished room.\r\n");
    OLC_ROOM(d)->zone = OLC_ZNUM(d);
    OLC_ROOM(d)->number = NOWHERE;
    
    /*
     * Save the new room to memory.
     * redit_save_internally handles adding the room in the right place, etc.
     */
    redit_save_internally(d);
    OLC_VAL(d) = 0;
    
    send_to_char(ch, "New room (%d) created.\r\n", rvnum);
    cleanup_olc(d, CLEANUP_STRUCTS);
    /* 
     * update rrnum to the correct room rnum after adding the room 
     */
    rrnum = real_room(rvnum);
  }

  /*
   * Now dig.
   */
  CREATE(W_EXIT(IN_ROOM(ch), dir), struct room_direction_data, 1);
  W_EXIT(IN_ROOM(ch), dir)->general_description = NULL;
  W_EXIT(IN_ROOM(ch), dir)->keyword = NULL;
  W_EXIT(IN_ROOM(ch), dir)->to_room = rrnum;
  add_to_save_list(zone_table[world[IN_ROOM(ch)].zone].number, SL_WLD);
  
  send_to_char(ch, "You make an exit %s to room %d (%s).\r\n", 
                   dirs[dir], rvnum, world[rrnum].name);

  /* 
   * check if we can dig from there to here. 
   */
  if (W_EXIT(rrnum, rev_dir[dir])) 
    send_to_char(ch, "Can not dig from %d to here. The target room already has an exit to the %s.\r\n",
                     rvnum, dirs[rev_dir[dir]]);
  else {
    CREATE(W_EXIT(rrnum, rev_dir[dir]), struct room_direction_data, 1);
    W_EXIT(rrnum, rev_dir[dir])->general_description = NULL;
    W_EXIT(rrnum, rev_dir[dir])->keyword = NULL;
    W_EXIT(rrnum, rev_dir[dir])->to_room = IN_ROOM(ch);
    add_to_save_list(zone_table[world[rrnum].zone].number, SL_WLD);
  }

}

/******************************************************************************/
/** Helper Functions                                                         **/
/******************************************************************************/
