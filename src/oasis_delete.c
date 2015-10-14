/************************************************************************
 *  OasisOLC - InGame OLC Deletion				v2.0	*
 *  Original author: Levork						*
 *  Copyright 1996 Harvey Gilpin					*
 *  Copyright 1997-2001 George Greer (greerga@circlemud.org)		*
 *  Copyright 2002 Kip Potter [Mythran] (kip_potter@hotmail.com)	*
 ************************************************************************/
 
/* 
   +-----------------------------------------------------------------------+
   | As of right now, all I have made is the ability to delete rooms.      |
   | Deleting the rest of the area (objects, zones, mobiles) will be       |
   | a little more difficult.  This is because they are broader and        |
   | deleting one is more tedious (but not impossible).  I will (hopefully)|
   | be adding more deletion code after this patch.                        |
   |   -- Mythran                                                          |
   +-----------------------------------------------------------------------+
*/                                                                       



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

/* Internal Functions */
int remove_room_from_memory(room_rnum rnum);
int free_strings(void *data, int type);


/************************************************************************\
 ** Description :                                                      **
 **   Removes a room from memory, updates the world list, and moves    **
 **   all of the objects, mobiles, and players to the void.            **
 **                                                                    **
 ** Return Value:                                                      **
 **   TRUE if successful...otherwise, FALSE.                           **
 **                                                                    **
 ** Parameters  :                                                      **
 **   rnum      : The real number of the room requested to delete.     **
\************************************************************************/
int remove_room_from_memory(room_rnum rnum)
{
  struct char_data *tch;
  struct obj_data *obj;
  struct room_data *room;
  int i, j;
  
  if (rnum <= 0 || rnum > top_of_world)
    return FALSE;
  
  room = &world[rnum];
  
  add_to_save_list(zone_table[room->zone].number, SL_WLD);
  
  log("GenOLC: delete_room: Deleting room #%d (%s).", room->number, room->name);
  
  /*
   * Dump the contents of this room into the void.  We could also just
   * exract the people, mobs, and objects here.
   */
  for (obj = world[rnum].contents; obj; obj = obj->next_content) {
    obj_from_room(obj);
    obj_to_room(obj, 0);
  }
  
  for (tch = world[rnum].people; tch; tch = tch->next_in_room) {
    char_from_room(tch);
    char_to_room(tch, 0);
  }
  
  free_room(room);
  
  /*
   * Change any exit going to this room to go to the void.  This way,
   * the builders know when they type show errors.
   */
  for (i = top_of_world; i >= 0; i--)
    for (j = 0; j < NUM_OF_DIRS; j++)
      if (W_EXIT(i, j) == NULL)
        continue;
      else if (W_EXIT(i, j)->to_room > rnum)
        W_EXIT(i, j)->to_room--;
      else if (W_EXIT(i, j)->to_room == rnum)
        W_EXIT(i, j)->to_room = 0;
  
  /*
   * Find what zone the room was in so we can update the loading table.
   */
  for (i = 0; i <= top_of_zone_table; i++)
    for (j = 0; ZCMD(i, j).command != 'S'; j++)
      switch (ZCMD(i, j).command) {
        case 'M':
        case 'O':
          if (ZCMD(i, j).arg3 == rnum)
            ZCMD(i, j).command = '*'; 		/* Cancel Command */
          else if (ZCMD(i, j).arg3 > rnum)
            ZCMD(i, j).arg3--;
          break;
        case 'D':
        case 'R':
          if (ZCMD(i, j).arg1 == rnum)
            ZCMD(i, j).command = '*';		/* Cancel Command */
          else if (ZCMD(i, j).arg1 > rnum)
            ZCMD(i, j).arg1--;
          break;
        case 'G':
        case 'P':
        case 'E':
        case '*':
          /* Known zone entries we don't use here. */
          break;
        default:
          mudlog(BRF, LVL_GOD, TRUE, "SYSERR: GenOLC: delete_room: Unknown zone entry found!");
      }
  
  /*
   * Now we actually move the rooms down.
   */
  for (i = rnum; i < top_of_world; i++) {
    world[i] = world[i + 1];
    
    for (tch = world[i].people; tch; tch = tch->next_in_room)
      IN_ROOM(tch) -= (IN_ROOM(tch) != NOWHERE);  	/* Redundant Check? */
    
    for (obj = world[i].contents; obj; obj = obj->next_content)
      IN_ROOM(obj) -= (IN_ROOM(obj) != NOWHERE);
  }
  
  top_of_world--;
  RECREATE(world, struct room_data, top_of_world + 1);
  return (TRUE);
}


/************************************************************************\
 ** Description :                                                      **
 **   Free's strings from any object, room, mobiles, or player.        **
 **                                                                    **
 ** Return Value:                                                      **
 **   TRUE if successful, otherwise, it returns FALSE.                 **
 **                                                                    **
 ** Parameters  :                                                      **
 **   type - The OLC type constant relating to the data type of data.  **
\************************************************************************/
int free_strings(void *data, int type)
{
  struct room_data *room;
  struct config_data *config;
  int i;
  
  switch (type) {
    case OASIS_WLD:
      room = (struct room_data *) data;
      
      /* Free Descriptions */
      if (room->name)
        free(room->name);
      
      if (room->description)
        free(room->description);
      
      if (room->ex_description)
	free_ex_descriptions(room->ex_description);
      
      /* Return the return value of free_strings(). */
      return (free_strings(room, OASIS_EXI));
    
    case OASIS_EXI:
      room = (struct room_data *) data;
      
      for (i = 0; i < NUM_OF_DIRS; i++) {
        if (room->dir_option[i]) {
          if (room->dir_option[i]->general_description)
            free(room->dir_option[i]->general_description);
            
          if (room->dir_option[i]->keyword)
            free(room->dir_option[i]->keyword);
          
          free(room->dir_option[i]);
        }
      }
      
      return (TRUE);
    
    case OASIS_MOB:
    case OASIS_OBJ:
      return (FALSE);		/* For now... */
    
    case OASIS_CFG:
      config = (struct config_data *) data;
      
      if (config->play.OK)
        free(config->play.OK);
        
      if (config->play.NOPERSON)
        free(config->play.NOPERSON);
        
      if (config->play.NOEFFECT)
        free(config->play.NOEFFECT);
      
      if (config->operation.DFLT_IP)
        free(config->operation.DFLT_IP);
        
      if (config->operation.DFLT_DIR)
        free(config->operation.DFLT_DIR);
        
      if (config->operation.LOGNAME)
        free(config->operation.LOGNAME);
        
      if (config->operation.MENU)
        free(config->operation.MENU);
        
      if (config->operation.WELC_MESSG)
        free(config->operation.WELC_MESSG);
        
      if (config->operation.START_MESSG)
        free(config->operation.START_MESSG);
      
      return (TRUE);
    
    default:
      mudlog(BRF, LVL_GOD, TRUE, "SYSERR: oasis_delete.c: free_strings: Invalid type handled (Type %d).", type);
      return (FALSE);
  }
}
