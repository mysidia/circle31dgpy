/**
 * Header file for more generic scripting support
 * $Id: genscript.h,v 1.1.1.1 2004/03/07 16:14:16 root Exp $
 *
 * Attribution Notice:
 *
 *    Copyright (c) 2003-2004 Mysidia <mysidia at qmud dot org>
 *    All Rights Reserved
 *
 *    Licensed under the Academic Free License version 2.0
 *    See ../doc/afl-2.0.txt
 *    And http://www.opensource.org/licenses/afl-2.0.php
 *
 * OR: Alternatively, you may distribute the original contents of this interface
 * definition (genscript.h) under the terms of the GNU Lesser General Public License,
 * as published by the Free Software Foundation, version 2 or (at your option),
 * any later version.
 *
 *  Please List any changes below:
 *     * Initial version 1.0
 */

#ifndef __genscript_h__
#define __genscript_h__

#define GENSCRIPTS_VERSION CIRCLEMUD_VERSION(0,0,1)
#define GENSCRIPTS_VERSION_STRING "Genscripts module version 0.0.1"


#include "dg_scripts.h"

#ifdef HAVE_PYTHON
#include "python_script.h"
#endif

typedef enum Game_Event_Hook_Types t_script_event;
typedef enum Script_Execution_Flags t_script_flags;
typedef int t_script_return;

#define SCRIPT_RET_CANCEL		0x01 // Caller needs to cancel operation
#define SCRIPT_RET_INTERCEPT		0x01
#define SCRIPT_RET_ACTOR_DEAD		0x04 // TRIGGER killed/extracted actor
#define SCRIPT_RET_SUBJECT_DEAD		0x08 // TRIGGER killed/extracted subject
#define SCRIPT_RET_VICT_DEAD		0x10 // TRIGGER killed/extracted victim
#define SCRIPT_RET_OBJ_DEAD		0x20 // TRIGGER killed/extracted object
#define SCRIPT_RET_OK			0x40 // Continue normally
#define SCRIPT_RET_UPDATED		0x80 // Value updated

#define SCRIPT_RET_OBJECT_DEAD  SCRIPT_RET_OBJ_DEAD

typedef enum Game_Script_Container_Types
{
	SCRIPT_PLAYER, SCRIPT_MOBILE, SCRIPT_OBJECT, SCRIPT_ROOM,
	SCRIPT_ZONE, SCRIPT_SPELL, SCRIPT_SKILL, SCRIPT_COMMAND,
	SCRIPT_NULL
} t_script_cont;


typedef unsigned char t_mutability;
#define MUT_R 0x1
#define MUT_W 0x2
#define MUT_X 0x4

typedef struct _script_cont_type {
	void* data;
	t_mutability write_level;
	t_script_cont cont_type;
	long cont_id;
} SCRIPT_CONT;

typedef enum Script_Param_Types {
	GSP_CHARACTER,
	GSP_INTEGER,
	GSP_LONG,
	GSP_LONGLONG,
	GSP_STRING,
	GSP_VOID_DATA,
	GSP_OBJECT,
	GSP_INVALID
} t_script_param_kind;

typedef struct Script_Param_Type {
	union _script_param_field_data {
		long			l_val;
		int			i_val;
		char			c_val;
	   	long long		ll_val;
		char*			str;
		void*			ptr;
		struct obj_data* 	obj;
	} data;
	t_script_param_kind type;
} t_script_param;

extern const t_script_param SNull;

enum Game_Event_Hook_Types
{
	HOOK_RANDOM_CHANCE, HOOK_COMMAND_ENTERED, HOOK_COMMAND_OVERRIDE,
       	HOOK_SPEECH, HOOK_ACTION,
	HOOK_CONT_DIED, HOOK_CHAR_ENTERED, HOOK_CONT_ENTERED,
	HOOK_RECEIVED_ITEM, HOOK_FIGHTING, HOOK_HITPERCENT_LESSTHAN,
	HOOK_GIVEN_CASH, HOOK_CONT_LOADED, HOOK_CONT_ENEMY_SEEN,
	HOOK_CONT_SPELLHIT, HOOK_CHAR_LEFT, HOOK_DOOR_CHANGED,
	HOOK_DECAYTIMER, HOOK_CONT_GET, HOOK_CONT_DROP, HOOK_CONT_GIVEN, 
	HOOK_CONT_WORN, HOOK_CONT_REMOVED, HOOK_CONT_RESET, HOOK_CONT_PUT,
	HOOK_CONT_TELEPORTED, HOOK_PLAYER_ENTERED_GAME,
	HOOK_CAST
};

typedef struct _event_args_structure
{
	SCRIPT_CONT sender;
	struct char_data* actor;
	t_script_param arg1, arg2;
	
} ScriptEventArgs;

typedef struct _script_listener_registration
{
	char* module;
	t_language language;
	t_script_event actionType;
	t_script_return (* handler)(ScriptEventArgs* e);

	struct _script_listener_registration* next;
#ifndef SWIG
	LIST_ENTRY(_script_listener_registration)  listener_list;
#endif
} ScriptListener;


/* Script functions */
SCRIPT_CONT obj_script_cont(struct obj_data* obj);
SCRIPT_CONT ch_script_cont(struct char_data* ch);
int check_hooks(t_script_event, SCRIPT_CONT, struct char_data*, 
			t_script_param x, t_script_param y);
t_script_return check_cast_hooks(t_script_event, struct char_data*, int, int, int, 
		struct char_data**, struct obj_data**, t_script_param);
int script_hook_command(t_script_event event_type, struct char_data* actor,
			t_script_param param1, t_script_param param2);
int check_null_hooks(t_script_event event_type, struct char_data* actor,
			t_script_param param1, t_script_param param2);
int check_mob_hooks(t_script_event event_type, SCRIPT_CONT subj,
			struct char_data* actor, t_script_param param1,
			t_script_param param2);

t_script_param str_to_param(char* string);
t_script_param int_to_param(int);
t_script_param obj_to_param(struct obj_data*);
void script_greet_memory(struct char_data* ch);
t_script_return script_mob_loaded(struct char_data** ch);
t_script_return script_obj_loaded(struct obj_data** obj);
int script_mob_leave_trigger(struct char_data* mob, int dir);
int script_char_left_room_trigger(struct room_data *room, struct char_data *actor, int dir);
int script_char_door_trigger(struct char_data* ch, int subcmd, int dir);
int script_enter_trigger(struct char_data* ch, struct room_data* from_room, int dir);
void script_act_trigger(const struct char_data *, char *, struct char_data *,
   	struct char_data *, struct obj_data *, struct obj_data *, char *);
int script_cast_trigger(struct char_data* caster, struct char_data* TARGET_MOB,
		        struct obj_data* TARGET_OBJ, int spellnum);
void script_random_mob_trigger(struct char_data*);
int  script_char_enter_room_trigger(struct room_data* room, struct char_data* ch, int dir);
int  script_drop_trigger(struct obj_data** dropped, struct char_data** dropper);
int  script_drop_o_trigger(struct obj_data**, struct char_data**);
int  script_get_o_trigger(struct obj_data**, struct char_data**);
int  script_give_o_trigger(struct obj_data** thing, struct char_data** from, struct char_data** to);
int  script_wear_o_trigger(struct obj_data** obj, struct char_data** actor, int where);
int  script_remove_o_trigger(struct obj_data** obj, struct char_data** actor);
void script_random_o_trigger(struct obj_data** obj);
void script_timer_o_trigger(struct obj_data** obj);
void script_random_w_trigger(struct room_data** rp);
t_script_return script_compute_kill_exp(struct char_data** killer, struct char_data** victim,
		                        int group_size, int* amount);

t_script_return script_char_damage_char(struct char_data**, struct char_data**, int*, int*, int*);
void script_char_compute_armor_class(struct char_data** ch, int *armorclass);
int script_char_compute_damroll(struct char_data** ch, int*);
int script_char_compute_hitroll(struct char_data** ch, int*);
void script_char_compute_thaco(struct char_data** ch, struct char_data** victim, 
		int* calc_thaco);
void script_pulse(int beat);
	

int script_char_hitmiss_catch(struct char_data** ch, struct char_data** victim, int* type,
	                       int* diceroll, int* calc_thaco, int* victim_ac, int* does_hit);
void send_bad_position_message(struct char_data* ch);

void script_mobread(struct char_data* mob);
void script_objread(struct obj_data* obj);
void script_roomread(struct room_data* room);


typedef t_script_return scriptHandler(ScriptEventArgs*);
typedef scriptHandler* scriptHandlerPtr;


void script_add_system_listener(const char* module, t_language, t_script_event actionType,
                                t_script_return (*handler)(ScriptEventArgs*) );
	
void script_del_system_listener(const char* module, t_language, t_script_event actionType,
                                t_script_return (*handler)(ScriptEventArgs*));

t_script_return script_check_system_listeners(t_script_event actionType,
		                       ScriptEventArgs* args);
void script_clear_listeners_language(struct _script_listener_ghead* head, t_language lang);
void script_free_listener(ScriptListener* l);

ScriptListener* script_make_listener(const char* module,
 t_language lang, t_script_event actionType, t_script_return (*handler)(ScriptEventArgs*));

t_script_return script_check_listeners(struct _script_listener_ghead* head, 
	t_script_event actionType, ScriptEventArgs* args);


#ifdef HAVE_PYTHON
t_script_return python_event_driver(t_script_event, ScriptEventArgs*);
#endif


/* */

enum Script_Execution_Flags
{
	SCRIPTFLAG_GLOBAL,
	SCRIPTFLAG_OBJ_EQUIPPED,
	SCRIPTFLAG_OBJ_INVENTORY,
	SCRIPTFLAG_OBJ_ROOM
};
#endif
