/******************************************************************************/
/** OasisOLC - InGame OLC Listings                                     v2.0  **/
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
#include "oasis.h"
#include "improved-edit.h"
#include "shop.h"
#include "screen.h"
#include "constants.h"

/******************************************************************************/
/** External Variables                                                       **/
/******************************************************************************/
extern struct shop_data *shop_index;
extern int top_shop;


/******************************************************************************/
/** Internal Functions                                                       **/
/******************************************************************************/
void list_rooms(struct char_data *ch  , zone_rnum rnum, room_vnum vmin, room_vnum vmax);
void list_mobiles(struct char_data *ch, zone_rnum rnum, mob_vnum vmin , mob_vnum vmax );
void list_objects(struct char_data *ch, zone_rnum rnum, obj_vnum vmin , obj_vnum vmax );
void list_shops(struct char_data *ch  , zone_rnum rnum, shop_vnum vmin, shop_vnum vmax);
void list_zones(struct char_data *ch);
void print_zone(struct char_data *ch, zone_vnum vnum);


/******************************************************************************/
/** Ingame Commands                                                          **/
/******************************************************************************/
ACMD(do_oasis_rlist)
{
  zone_rnum rzone;
  room_rnum vmin = NOWHERE;
  room_rnum vmax = NOWHERE;
  char smin[MAX_INPUT_LENGTH];
  char smax[MAX_INPUT_LENGTH];
  
  /****************************************************************************/
  /** Split the arguments into smin and smax.                                **/
  /****************************************************************************/
  two_arguments(argument, smin, smax);
  
  if (!*smin || *smin == '.') {
    rzone = world[IN_ROOM(ch)].zone;
    
    list_rooms(ch, rzone, NOWHERE, NOWHERE);

  } else if (!*smax) {
    rzone = real_zone(atoi(smin));
    
    if (rzone == NOWHERE) {
      send_to_char(ch, "Sorry, there's no zone with that number\r\n");
      return;
    }
    
    list_rooms(ch, rzone, NOWHERE, NOWHERE);
    
  } else {
    /****************************************************************************/
    /** Listing by min vnum / max vnum.  Retrieve the numeric values.          **/
    /****************************************************************************/
    vmin = atoi(smin);
    vmax = atoi(smax);
    
    list_rooms(ch, NOWHERE, vmin, vmax);
  }
}

ACMD(do_oasis_mlist)
{
  zone_rnum rzone;
  room_rnum vmin = NOWHERE;
  room_rnum vmax = NOWHERE;
  char smin[MAX_INPUT_LENGTH];
  char smax[MAX_INPUT_LENGTH];
  
  /****************************************************************************/
  /** Split the arguments into smin and smax.                                **/
  /****************************************************************************/
  two_arguments(argument, smin, smax);
  
  if (!*smin || *smin == '.') {
    rzone = world[IN_ROOM(ch)].zone;
    
    list_mobiles(ch, rzone, NOWHERE, NOWHERE);

  } else if (!*smax) {
    rzone = real_zone(atoi(smin));
    
    if (rzone == NOWHERE) {
      send_to_char(ch, "Sorry, there's no zone with that number\r\n");
      return;
    }
    
    list_mobiles(ch, rzone, NOWHERE, NOWHERE);
    
  } else {
    /****************************************************************************/
    /** Listing by min vnum / max vnum.  Retrieve the numeric values.          **/
    /****************************************************************************/
    vmin = atoi(smin);
    vmax = atoi(smax);
    
    list_mobiles(ch, NOWHERE, vmin, vmax);
  }
}

ACMD(do_oasis_olist)
{
  zone_rnum rzone;
  room_rnum vmin = NOWHERE;
  room_rnum vmax = NOWHERE;
  char smin[MAX_INPUT_LENGTH];
  char smax[MAX_INPUT_LENGTH];
  
  /****************************************************************************/
  /** Split the arguments into smin and smax.                                **/
  /****************************************************************************/
  two_arguments(argument, smin, smax);
  
  if (!*smin || *smin == '.') {
    rzone = world[IN_ROOM(ch)].zone;
    
    list_objects(ch, rzone, NOWHERE, NOWHERE);

  } else if (!*smax) {
    rzone = real_zone(atoi(smin));
    
    if (rzone == NOWHERE) {
      send_to_char(ch, "Sorry, there's no zone with that number\r\n");
      return;
    }
    
    list_objects(ch, rzone, NOWHERE, NOWHERE);
    
  } else {
    /****************************************************************************/
    /** Listing by min vnum / max vnum.  Retrieve the numeric values.          **/
    /****************************************************************************/
    vmin = atoi(smin);
    vmax = atoi(smax);
    
    list_objects(ch, NOWHERE, vmin, vmax);
  }
}

ACMD(do_oasis_slist)
{
  zone_rnum rzone;
  room_rnum vmin = NOWHERE;
  room_rnum vmax = NOWHERE;
  char smin[MAX_INPUT_LENGTH];
  char smax[MAX_INPUT_LENGTH];
  
  /****************************************************************************/
  /** Split the arguments into smin and smax.                                **/
  /****************************************************************************/
  two_arguments(argument, smin, smax);
  
  if (!*smin || *smin == '.') {
    rzone = world[IN_ROOM(ch)].zone;
    
    list_shops(ch, rzone, NOWHERE, NOWHERE);

  } else if (!*smax) {
    rzone = real_zone(atoi(smin));
    
    /**************************************************************************/
    /** Make sure the zone exists.                                           **/
    /**************************************************************************/
    if (rzone == NOWHERE) {
      send_to_char(ch, "Sorry, there's no zone with that number\r\n");
      return;
    }
    
    list_shops(ch, rzone, NOWHERE, NOWHERE);
    
  } else {
    /****************************************************************************/
    /** Listing by min vnum / max vnum.  Retrieve the numeric values.          **/
    /****************************************************************************/
    vmin = atoi(smin);
    vmax = atoi(smax);
    
    list_shops(ch, NOWHERE, vmin, vmax);
  }
}


ACMD(do_oasis_zlist)
{
  skip_spaces(&argument);
  if (argument && *argument && is_number(argument)) 
    print_zone(ch, atoi(argument));
  else
    list_zones(ch);  
}


/******************************************************************************/
/** Helper Functions                                                         **/
/******************************************************************************/


/******************************************************************************/
/**                                                                          **/
/** Function       : list_rooms()                                            **/
/**                                                                          **/
/** Description    : Lists all rooms in a zone.                              **/
/**                                                                          **/
/** Arguments      :                                                         **/
/**   ch                                                                     **/
/**     The character whom is listing the rooms.                             **/
/**   rnum                                                                   **/
/**     The real number of the zone to list the rooms of.                    **/
/**   vmin                                                                   **/
/**     The virtual number of the minimum room number to list.               **/
/**   vmax                                                                   **/
/**     The virtual number of the maximum room number to list.               **/
/**                                                                          **/
/** Returns        : Nothing.                                                **/
/**                                                                          **/
/******************************************************************************/
void list_rooms(struct char_data *ch, zone_rnum rnum, zone_vnum vmin, zone_vnum vmax)
{
  int i, j, bottom, top, counter = 0;
  /****************************************************************************/
  /** Expect a minimum / maximum number if the rnum for the zone is NOWHERE. **/
  /****************************************************************************/
  if (rnum != NOWHERE) {
    bottom = zone_table[rnum].bot;
    top    = zone_table[rnum].top;
  } else {
    bottom = vmin;
    top    = vmax;
  }
  
  /****************************************************************************/
  /** Store the header for the room listing.                                 **/
  /****************************************************************************/
  send_to_char (ch,
  "Index VNum    Room Name                                Exits\r\n"
  "----- ------- ---------------------------------------- -----\r\n");
  
  /****************************************************************************/
  /** Loop through the world and find each room.                             **/
  /****************************************************************************/
  for (i = 0; i <= top_of_world; i++) {
    
    /**************************************************************************/
    /** Check to see if this room is one of the ones needed to be listed.    **/
    /**************************************************************************/
    if ((world[i].number >= bottom) && (world[i].number <= top)) {
      counter++;
      
      send_to_char(ch, "%4d) [%s%-5d%s] %s%-40.40s%s ",
        counter, QGRN, world[i].number, QNRM, QCYN, world[i].name, QNRM);

      for (j = 0; j < NUM_OF_DIRS; j++) {
        if (W_EXIT(i, j) == NULL)
          continue;
        
        if (world[W_EXIT(i, j)->to_room].zone != rnum) 
          send_to_char(ch, "(%s%d%s)", QYEL, world[W_EXIT(i, j)->to_room].number, QNRM);
     
      }
    
      send_to_char(ch, "\r\n");
    }
  }
  
  if (counter == 0)
    send_to_char(ch, "No rooms found for zone #%d\r\n", zone_table[rnum].number);
}


/******************************************************************************/
/**                                                                          **/
/** Function       : list_mobiles()                                          **/
/**                                                                          **/
/** Description    : Lists all mobiles in a zone.                            **/
/**                                                                          **/
/** Arguments      :                                                         **/
/**   ch                                                                     **/
/**     The character whom is listing the mobiles.                           **/
/**   rnum                                                                   **/
/**     The real number of the zone to list the objects of.                  **/
/**   vmin                                                                   **/
/**     The virtual number of the minimum mobile number to list.             **/
/**   vmax                                                                   **/
/**     The virtual number of the maximum mobile number to list.             **/
/**                                                                          **/
/** Returns        : Nothing.                                                **/
/**                                                                          **/
/******************************************************************************/
void list_mobiles(struct char_data *ch, zone_rnum rnum, zone_vnum vmin, zone_vnum vmax)
{
  int i, bottom, top, counter = 0;
  
  if (rnum != NOWHERE) {
    bottom = zone_table[rnum].bot;
    top    = zone_table[rnum].top;
  } else {
    bottom = vmin;
    top    = vmax;
  }
  
  /****************************************************************************/
  /** Store the header for the mobile listing.                               **/
  /****************************************************************************/
  send_to_char(ch,
  "Index VNum    Mobile Name                                   Level\r\n"
  "----- ------- --------------------------------------------- -----\r\n");
  
  for (i = 0; i <= top_of_mobt; i++) {
    if (mob_index[i].vnum >= bottom && mob_index[i].vnum <= top) {
      counter++;
      
      send_to_char(ch, "%s%4d%s) [%s%-5d%s] %s%-44.44s %s%4d%s\r\n",
        QGRN, counter, QNRM, QGRN, mob_index[i].vnum, QNRM,
        QCYN, mob_proto[i].player.short_descr, 
        QYEL, mob_proto[i].player.level, QNRM);
      
    }
  }
  
  /****************************************************************************/
  /** Page the string only if there were mobiles found in this zone.         **/
  /****************************************************************************/
  if (counter == 0)
    send_to_char(ch, "None found.\r\n");
}


/******************************************************************************/
/**                                                                          **/
/** Function       : list_objects()                                          **/
/**                                                                          **/
/** Description    : Lists all objects in a zone.                            **/
/**                                                                          **/
/** Arguments      :                                                         **/
/**   ch                                                                     **/
/**     The character whom is listing the objects.                           **/
/**   rnum                                                                   **/
/**     The real number of the zone to list the objects of.                  **/
/**   vmin                                                                   **/
/**     The virtual number of the minimum object number to list.             **/
/**   vmax                                                                   **/
/**     The virtual number of the maximum object number to list.             **/
/**                                                                          **/
/** Returns        : Nothing.                                                **/
/**                                                                          **/
/******************************************************************************/
void list_objects(struct char_data *ch, zone_rnum rnum, room_vnum vmin, room_vnum vmax)
{
  int i, bottom, top, counter = 0;
  
  if (rnum != NOWHERE) {
    bottom = zone_table[rnum].bot;
    top    = zone_table[rnum].top;
  } else {
    bottom = vmin;
    top    = vmax;
  }
  
  /****************************************************************************/
  /** Store the header for the object listing.                               **/
  /****************************************************************************/
  send_to_char(ch,
  "Index VNum    Object Name                                  Object Type\r\n"
  "----- ------- -------------------------------------------- ----------------\r\n");
  
  for (i = 0; i <= top_of_objt; i++) {
    if (obj_index[i].vnum >= bottom && obj_index[i].vnum <= top) {
      counter++;
      
      send_to_char(ch, "%s%4d%s) [%s%-5d%s] %s%-44.44s %s[%s]%s\r\n",
        QGRN, counter, QNRM, QGRN, obj_index[i].vnum, QNRM,
        QCYN, obj_proto[i].short_description, QYEL,
        item_types[obj_proto[i].obj_flags.type_flag], QNRM);
      
    }
  }
  
  if (counter == 0)
    send_to_char(ch, "None found.\r\n");
}


/******************************************************************************/
/**                                                                          **/
/** Function       : list_shops()                                            **/
/**                                                                          **/
/** Description    : Lists all shops in a zone.                              **/
/**                                                                          **/
/** Arguments      :                                                         **/
/**   ch                                                                     **/
/**     The character whom is listing the objects.                           **/
/**   rnum                                                                   **/
/**     The real number of the zone to list the objects of.                  **/
/**   vmin                                                                   **/
/**     The virtual number of the minimum shop number to list.               **/
/**   vmax                                                                   **/
/**     The virtual number of the maximum shop number to list.               **/
/**                                                                          **/
/** Returns        : Nothing.                                                **/
/**                                                                          **/
/******************************************************************************/
void list_shops(struct char_data *ch, zone_rnum rnum, shop_vnum vmin, shop_vnum vmax)
{
  int i, j, bottom, top, counter = 0;
  
  if (rnum != NOWHERE) {
    bottom = zone_table[rnum].bot;
    top    = zone_table[rnum].top;
  } else {
    bottom = vmin;
    top    = vmax;
  }
  
  /****************************************************************************/
  /** Store the header for the shop listing.                                 **/
  /****************************************************************************/
  send_to_char (ch,
  "Index VNum    Shop Room(s)\r\n"
  "----- ------- ---------------------------------------------\r\n");
  
  for (i = 0; i <= top_shop; i++) {
    if (SHOP_NUM(i) >= bottom && SHOP_NUM(i) <= top) {
      counter++;
      
      send_to_char(ch, "%s%4d%s) [%s%-5d%s]",
        QGRN, counter, QNRM, QGRN, SHOP_NUM(i), QNRM);

      /************************************************************************/
      /** Retrieve the list of rooms for this shop.                          **/
      /************************************************************************/
      
      for (j = 0; SHOP_ROOM(i, j) != NOWHERE; j++)
        send_to_char(ch, "%s[%s%d%s]%s", QCYN, QYEL, SHOP_ROOM(i, j), QCYN, QNRM);
      
      if (j == 0)
        send_to_char(ch, "%sNone.%s", QCYN, QNRM);
      
      send_to_char(ch, "\r\n");
    }
  }
  
  /****************************************************************************/
  /** Check to see if a shop or more were found, if not, display the 'No     **/
  /** Shops' message.                                                        **/
  /****************************************************************************/
  if (counter == 0)
    send_to_char(ch, "None found.\r\n");
}


/******************************************************************************/
/**                                                                          **/
/** Function       : list_zones()                                            **/
/**                                                                          **/
/** Description    : Lists all of the zones in the world.                    **/
/**                                                                          **/
/** Arguments      :                                                         **/
/**   ch                                                                     **/
/**     The character whom is listing the zones.                             **/
/**                                                                          **/
/** Returns        : Nothing.                                                **/
/**                                                                          **/
/******************************************************************************/
void list_zones(struct char_data *ch)
{
  int i;
  
  /****************************************************************************/
  /** Store the header for the zone listing.                                 **/
  /****************************************************************************/
  send_to_char(ch,
  "VNum  Zone Name                      Builder(s)\r\n"
  "----- ------------------------------ --------------------------------------\r\n");
  
  for (i = 0; i <= top_of_zone_table; i++)
    send_to_char(ch, "[%s%3d%s] %s%-30.30s %s%-1s%s\r\n",
      QGRN, zone_table[i].number, QNRM, QCYN, zone_table[i].name,
      QYEL, zone_table[i].builders ? zone_table[i].builders : "None.", QNRM);
}



/******************************************************************************/
/**                                                                          **/
/** Function       : print_zone()                                            **/
/**                                                                          **/
/** Description    : Prints all of the zone information for the selected     **/
/**                  zone.                                                   **/
/**                                                                          **/
/** Arguments      :                                                         **/
/**   ch                                                                     **/
/**     The character whom is listing the zones.                             **/
/**   vnum                                                                   **/
/**     The virtual number of the zone to print.                             **/
/**                                                                          **/
/** Returns        : Nothing.                                                **/
/**                                                                          **/
/******************************************************************************/
void print_zone(struct char_data *ch, zone_vnum vnum)
{
  zone_rnum rnum;
  int size_rooms, size_objects, size_mobiles, i;
  room_vnum top, bottom;
  int largest_table;
  
  /****************************************************************************/
  /** Make sure the zone exists.                                             **/
  /****************************************************************************/
  if ((rnum = real_zone(vnum)) == NOWHERE) {
    send_to_char(ch, "Zone #%d does not exist in the database.\r\n", vnum);
    return;
  }
  
  /****************************************************************************/
  /** Locate the largest of the three, top_of_world, top_of_mobt, or         **/
  /** top_of_objt.                                                           **/
  /****************************************************************************/
  if (top_of_world >= top_of_objt && top_of_world >= top_of_mobt)
    largest_table = top_of_world;
  else if (top_of_objt >= top_of_mobt && top_of_objt >= top_of_world)
    largest_table = top_of_objt;
  else
    largest_table = top_of_mobt;
  
  /****************************************************************************/
  /** Initialize some of the variables.                                      **/
  /****************************************************************************/
  size_rooms   = 0;
  size_objects = 0;
  size_mobiles = 0;
  top          = zone_table[rnum].top;
  bottom       = zone_table[rnum].bot;
  
  for (i = 0; i <= largest_table; i++) {
    if (i <= top_of_world)
      if (world[i].zone == rnum)
        size_rooms++;
    
    if (i <= top_of_objt)
      if (obj_index[i].vnum >= bottom && obj_index[i].vnum <= top)
        size_objects++;
    
    if (i <= top_of_mobt)
      if (mob_index[i].vnum >= bottom && mob_index[i].vnum <= top)
        size_mobiles++;
  }
  
  /****************************************************************************/
  /** Display all of the zone information at once.                           **/
  /****************************************************************************/
  send_to_char(ch,
    "%sVirtual Number = %s%d\r\n"
    "%sName of zone   = %s%s\r\n"
    "%sBuilders       = %s%s\r\n"
    "%sLifespan       = %s%d\r\n"
    "%sAge            = %s%d\r\n"
    "%sBottom of Zone = %s%d\r\n"
    "%sTop of Zone    = %s%d\r\n"
    "%sReset Mode     = %s%s\r\n"
    "%sSize\r\n"
    "%s   Rooms       = %s%d\r\n"
    "%s   Objects     = %s%d\r\n"
    "%s   Mobiles     = %s%d%s\r\n",
    QGRN, QCYN, zone_table[rnum].number,
    QGRN, QCYN, zone_table[rnum].name,
    QGRN, QCYN, zone_table[rnum].builders,
    QGRN, QCYN, zone_table[rnum].lifespan,
    QGRN, QCYN, zone_table[rnum].age,
    QGRN, QCYN, zone_table[rnum].bot, 
    QGRN, QCYN, zone_table[rnum].top,
    QGRN, QCYN, zone_table[rnum].reset_mode ? ((zone_table[rnum].reset_mode == 1) ?
    "Reset when no players are in zone." : "Normal reset.") : "Never reset",
    QGRN,
    QGRN, QCYN, size_rooms,
    QGRN, QCYN, size_objects,
    QGRN, QCYN, size_mobiles, QNRM);
}
