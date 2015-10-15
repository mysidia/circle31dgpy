/**
 * Module more general scripting support
 * $Id: genscript.c,v 1.1.1.1 2004/03/07 16:14:16 root Exp $ 
 *
 * * Scripting engines can register HOOKS with this module
 *   to receive callbacks on certain events. 
 *  (Or they will be able to do so, eventually)
 *
 * Attribution Notice:
 *
 *    Copyright (c) 2003-2004 ***REMOVED*** <mysidia-pyci@darkfire.net>
 *    All Rights Reserved
 *
 *    Licensed under the Academic Free License version 2.0
 *    See ../doc/afl-2.0.txt
 *    And http://www.opensource.org/licenses/afl-2.0.php
 *
 * Alternatively, you may distribute the original contents of this library
 * code (genscript.c) under the terms of the GNU Lesser General Public License,
 * as published by the Free Software Foundation, version 2 or (at your option),
 * any later version.
 *
 * Please List any changes below:
 *     * Initial version 1.0
 */


#include "conf.h"
#include "sysdep.h"

#include "structs.h"
#include "utils.h"
#include "db.h"
#include "comm.h"
#include "handler.h"
#include "spells.h"
#include "mail.h"
#include "interpreter.h"
#include "genscript.h"

void invalid_command_message(struct char_data* ch);
struct char_data *find_char(long n);
void py_show_credits(struct char_data*);

const t_script_param SNull = { {0}, GSP_INVALID };

/* Convert a string into a script parameter */
t_script_param str_to_param(char* string) {
	t_script_param x;
	x.data.str = string;
	x.type = GSP_STRING;

	return x;
}

/* Convert an integer to a script parameter */
t_script_param int_to_param(int val) {
	t_script_param x;

	x.data.i_val = val;
	x.type = GSP_INTEGER;

	return x;
}

/* Convert an object to a script parameter */
t_script_param obj_to_param(struct obj_data* obj)
{
	t_script_param x;

	x.data.obj = obj;
	x.type = GSP_OBJECT;
	return x;
}

/* Convert a long to a script parameter */
t_script_param int_to_long(long val) {
	t_script_param x;

	x.data.l_val = val;
	x.type = GSP_LONG;
	return x;
}

/*********************************************************************************/

ACMD(do_script_credits)
{
	/* Begin Attribution Notice: */
	send_to_char(ch, "Script system based on Genscripts, Copyr. 2004 J. Hess, "
			 "All Rights Reserved\r\n");
	send_to_char(ch, "       Licensed under the Academic Free License version 2.0\r\n");
	/* End Attribution Notice */

#ifdef HAVE_PYTHON
	py_show_credits(ch);
#endif
}


/**
 * Convert a pointer to a char to a script reference to it
 */
SCRIPT_CONT ch_script_cont(struct char_data* ch) {
	SCRIPT_CONT x;

	x.write_level = 0;

	if (!ch) {
		x.data = NULL;
		x.cont_id = 0;
		x.cont_type = SCRIPT_NULL;
		return x;
	}

	x.write_level = MUT_R|MUT_W;
	x.data = ch;
	x.cont_id = GET_ID(ch);
	
	if (!IS_NPC(ch)) 
		x.cont_type = SCRIPT_PLAYER;
	else
		x.cont_type = SCRIPT_MOBILE;
	return x;
}

/**
 * Convert a pointer to an object to a script reference to it
 */
SCRIPT_CONT obj_script_cont(struct obj_data* obj) {
	SCRIPT_CONT x;

	x.write_level = 0;

	if (!obj) {
		x.data = NULL;
		x.cont_id = 0;
		x.cont_type = SCRIPT_NULL;

		return x;
	}

	x.write_level = MUT_R|MUT_W;
	x.data = obj;
	x.cont_type = SCRIPT_OBJECT;
	x.cont_id = GET_ID(obj);
	return x;
}

/**
 * Unbottle a script reference to a character
 */
struct char_data* cont_to_ch( SCRIPT_CONT x )
{
	if (x.cont_id == 0)
		return NULL;
	return find_char(x.cont_id);
}



/**
 * Search for mob event hooks
 */
int check_mob_hooks(t_script_event event_type, SCRIPT_CONT subj,
	            struct char_data* actor, t_script_param param1,
		    t_script_param param2)
{
	struct char_data* ch = cont_to_ch( subj );
	ScriptEventArgs builtArgs = {};
	int ret = 0;

#ifdef HAVE_PYTHON
	builtArgs.actor = actor;
	builtArgs.sender = subj;
	builtArgs.arg1 = param1;
	builtArgs.arg2 = param2;

	ret = python_event_driver(event_type, &builtArgs);
		
	if (IS_SET(ret, SCRIPT_RET_ACTOR_DEAD) || IS_SET(ret, SCRIPT_RET_INTERCEPT))
		return ret;

	ret = script_check_listeners(&(ch->script_listeners), event_type, &builtArgs);
	if (IS_SET(ret, SCRIPT_RET_ACTOR_DEAD) || IS_SET(ret, SCRIPT_RET_INTERCEPT))
		return ret;

	ret = script_check_listeners(&(ch->proto_script_listeners), event_type, &builtArgs);
	if (IS_SET(ret, SCRIPT_RET_ACTOR_DEAD) || IS_SET(ret, SCRIPT_RET_INTERCEPT))
		return ret;
#endif

	
	switch(event_type) {
		case HOOK_CONT_DIED:
			return death_mtrigger(ch, actor);
			break;
		case HOOK_CONT_TELEPORTED:
			entry_memory_mtrigger(ch);
			greet_mtrigger(ch, -1);
			greet_memory_mtrigger(ch);
			break;
		case HOOK_GIVEN_CASH:
			if (param1.type != GSP_INTEGER) {
				log("SYSERR: HOOK_GIVEN_CASH, param1.type!=GSP_INTEGER");
				return 0;
			}
			bribe_mtrigger(ch, actor, param1.data.i_val);
			break;
		case HOOK_RECEIVED_ITEM:
			if (param1.type != GSP_OBJECT) {
				log("SYSERR: HOOK_RECEIVED_ITEM, param1.type!=GSP_OBJECT");
			}
			return receive_mtrigger(ch, actor, param1.data.obj);
			break;
		case HOOK_FIGHTING:
		case HOOK_HITPERCENT_LESSTHAN:
			return check_null_hooks(event_type, actor, param1, param2);
			break;
		default:
			break;
	}
	return 0;
}

int script_hook_command(
	t_script_event event_type, struct char_data* actor,
	t_script_param param1, t_script_param param2)
{
	char* arg = 0, *line = 0;
	int val = FALSE;

	if (param1.type != GSP_STRING) {
		log("SYSERR: script_hook_command "
		   " [HOOK_COMMAND_ENTERED]: param1.type != GSP_STRING");
		return 0;
	}

	if (param2.type != GSP_STRING) {
		log("SYSERR: script_hook_command "
		   " [HOOK_COMMAND_ENTERED]: param2.type != GSP_STRING");
		return 0;
	}
	arg = param1.data.str;
	line = param2.data.str;

	val = command_wtrigger(actor, arg, line);
	if (!val)
		val = command_mtrigger(actor, arg, line);
	if (!val)
		val = command_otrigger(actor, arg, line);
	return val;
}

/*********************************************************************************/

void script_act_trigger(const struct char_data *ch, char *str,
	struct char_data *actor, struct char_data *act_target_ch, struct obj_data *object,
	struct obj_data *act_target_obj, char *arg)
{
	act_mtrigger(ch, str, actor, act_target_ch, object, act_target_obj, arg);
}

int script_cast_trigger(struct char_data *caster, struct char_data *target_mob,
		        struct obj_data *target_obj, int spellnum)
{
	if (cast_wtrigger(caster, target_mob, target_obj, spellnum) == 0)
		return 0;
		  
	if (target_mob != 0)
		if (cast_mtrigger(caster, target_mob, spellnum) == 0)
			return 0;

	if (target_obj != 0)
		if (cast_otrigger(caster, target_obj, spellnum) == 0)
			return 0;
	  
	return 1;
}


t_script_return script_mob_loaded(struct char_data** mob) {
	load_mtrigger(*mob);	

	// Can return SCRIPT_RET_CANCEL.  Should extract mob in that case.
	return SCRIPT_RET_OK;
}

t_script_return script_obj_loaded(struct obj_data** obj) {
	load_otrigger(*obj);

	return SCRIPT_RET_OK;
}

void script_greet_memory(struct char_data* ch) {
	greet_memory_mtrigger(ch);
}

int script_mob_leave_trigger(struct char_data* mob, int dir) {
	return leave_mtrigger(mob, dir);
}

int script_char_left_room_trigger(struct room_data *room, struct char_data *actor, int dir)
{
	return leave_wtrigger(&world[IN_ROOM(actor)], actor, dir);
}

void script_random_mob_trigger(struct char_data* mob)
{
	random_mtrigger(mob);
}


/*********************************************************************************/

int script_char_door_trigger(struct char_data* ch, int subcmd, int dir)
{
	if (door_mtrigger(ch, subcmd, dir) == 0)
		return 0;
	if (door_wtrigger(ch, subcmd, dir) == 0)
		return 0;
	return 1;
}

int script_enter_trigger(struct char_data* ch, struct room_data* from_room, int dir)
{
	if (!entry_mtrigger(ch) || !enter_wtrigger(from_room, ch, dir))
		return 0;
	return 1;
}

int  script_char_enter_room_trigger(struct room_data* room, struct char_data* ch, int dir)
{
	return enter_wtrigger(room, ch, dir);
}

int  script_drop_trigger(struct obj_data** dropped, struct char_data** dropper)
{
	return drop_wtrigger(*dropped, *dropper);
}

int script_drop_o_trigger(struct obj_data** dropped, struct char_data** dropper)
{
	return drop_otrigger(*dropped, *dropper);
}

int script_get_o_trigger(struct obj_data** obj, struct char_data** actor)
{
	return get_otrigger(*obj, *actor);
}

int  script_give_o_trigger(struct obj_data** thing, struct char_data** from, struct char_data** to)
{
	return give_otrigger(*thing, *from, *to);
}

int  script_wear_o_trigger(struct obj_data** obj, struct char_data** actor, int where)
{
	return wear_otrigger(*obj, *actor, where);
}

int  script_remove_o_trigger(struct obj_data** obj, struct char_data** actor)
{
	return remove_otrigger(*obj, *actor);
}

void  script_random_o_trigger(struct obj_data** obj)
{
	random_otrigger(*obj);
}

void  script_timer_o_trigger(struct obj_data** obj)
{
	timer_otrigger(*obj);
}

void  script_random_w_trigger(struct room_data** rp)
{
	random_wtrigger(*rp);
}



/*********************************************************************************/

/*
 * A hook with  actor == subject  or subject == Null, or actor = Null
 * Or actor == subject && subject == Null
 */
int check_null_hooks(t_script_event event_type, struct char_data* actor,
		t_script_param param1, t_script_param param2)
{
	char* text = NULL;
	int v, ret;

	ScriptEventArgs builtArgs = {};

	builtArgs.sender.cont_type = SCRIPT_NULL;
	builtArgs.actor = actor;
	builtArgs.arg1 = param1;
	builtArgs.arg2 = param2;

	/* SCRIPT_CONT sender; */	

	ret = script_check_system_listeners(event_type, &builtArgs);

	if (IS_SET(ret, SCRIPT_RET_ACTOR_DEAD) || IS_SET(ret, SCRIPT_RET_INTERCEPT))
		return ret;

#ifdef HAVE_PYTHON
	ret = python_event_driver(event_type, &builtArgs);
		
	if (IS_SET(ret, SCRIPT_RET_ACTOR_DEAD) || IS_SET(ret, SCRIPT_RET_INTERCEPT))
		return ret;
#endif
	
	
	switch(event_type) {
		case HOOK_CHAR_ENTERED: /* (optional) param1=direction */
			v = -1;
			entry_memory_mtrigger(actor);
			if (param1.type == GSP_INTEGER)
				v = param1.data.i_val;
			ret = greet_mtrigger(actor, v);
			break;
		case HOOK_COMMAND_ENTERED: /* param1=text */
		case HOOK_COMMAND_OVERRIDE:
			return script_hook_command(event_type, actor, param1, param2);
			break;
		case HOOK_SPEECH: /* param1 = text */
			if (param1.type != GSP_STRING) {
				log("SYSERR: check_null_hooks: param1.type != GSP_STRING");
				return 0;
			}
			text = param1.data.str;
			speech_mtrigger(actor, text);
			speech_wtrigger(actor, text);
			break;
		case HOOK_PLAYER_ENTERED_GAME: /* No args */
			greet_mtrigger(actor, -1);
			greet_memory_mtrigger(actor);
			break;
		case HOOK_FIGHTING: /* No args */
			fight_mtrigger(actor);
			break;
		case HOOK_HITPERCENT_LESSTHAN: /* No args */
			hitprcnt_mtrigger(actor);
			break;
		case HOOK_CAST: /* Cast a spell ID##XXX */
			return SCRIPT_RET_OK;
			break;
		default:
			log("SYSERR: check_null_hooks: default case %d", event_type);
			break;
	}
	return 0;
}

/**
 * Check for script hooks
 */
int check_hooks(t_script_event event_type,
		 SCRIPT_CONT subj, 		 
		 struct char_data* actor,
		 t_script_param param1,
		 t_script_param param2) 
{
	switch(subj.cont_type) {
		case SCRIPT_NULL:
			return check_null_hooks(event_type, actor, param1,
					        param2);
			break;
		case SCRIPT_MOBILE:
			return check_mob_hooks(event_type, subj,
					       actor, param1, param2);
			break;
		default:
			break;
	}
	return 0;
}

t_script_return script_compute_kill_exp(struct char_data** killer, struct char_data** victim,
		                        int group_size, int *amount)
{
	return SCRIPT_RET_OK;
}


t_script_return
check_cast_hooks(t_script_event subj, struct char_data* caster, int spellnum,
		 int level, int casttype, struct char_data** cvict, 
		 struct obj_data** ovict, t_script_param other_target)
{
	return SCRIPT_RET_OK;
}

t_script_return script_char_damage_char(struct char_data** ch, struct char_data** victim, 
		int* dam, int* attacktype, int* ret)
{
	return SCRIPT_RET_OK;
}

void script_char_compute_armor_class(struct char_data** ch, int *armorclass)
{
}

int script_char_compute_damroll(struct char_data** ch, int* ret)
{
	int result = GET_DAMROLL(*ch);
	
	if (ret != 0)
		*ret = result;
	return result;
}

int script_char_compute_hitroll(struct char_data** ch, int* ret)
{
	int result = GET_HITROLL(*ch);
		
	if (ret != 0)
		*ret = result;
	return result;
}

void script_pulse(int beat)
{
#ifdef HAVE_DGSCRIPT
  if (!(beat % PULSE_DG_SCRIPT))
      script_trigger_check();
#endif
  
#ifdef HAVE_PYTHON
	py_pulse( beat);
#endif
}

void script_char_compute_thaco(struct char_data** ch, struct char_data** victim,
	       	int* calc_thaco)
{
}

int script_char_hitmiss_catch(struct char_data** ch, struct char_data** victim, int* type,
 int* diceroll, int* calc_thaco, int* victim_ac, int* does_hit)
{
	return 0;
}


/******************************************************************************/
/* Listener Management Code */

struct _script_listener_ghead globalListeners;
      
void script_clear_listeners_language(struct _script_listener_ghead* head,
	       	t_language lang)
{
	ScriptListener* l, *l_next;
	
	for(l = LIST_FIRST(head); l; l = l_next)
	{
		l_next = LIST_NEXT(l, listener_list);

		if (l->language != lang)
			continue;
		LIST_REMOVE(l, listener_list);
	}
}


void script_del_listeners(
		struct _script_listener_ghead* head,
	       	t_language lang, 
		t_script_event actionType)
{
	ScriptListener* l, *l_next;
	
	for(l = LIST_FIRST(head); l != NULL; l = l_next)
	{
		l_next = LIST_NEXT(l, listener_list);

		if (l->language != lang || l->actionType != actionType)
			continue;

		LIST_REMOVE(l, listener_list);
		script_free_listener(l);
	}
}


void script_free_listener(ScriptListener* l)
{
	if (l->module)
		free(l->module);
	free(l);
}

ScriptListener* script_make_listener(const char* module,
		t_language lang,
		t_script_event actionType,
	       	t_script_return (*handler)(ScriptEventArgs*))
{
	ScriptListener* q;

	CREATE(q, ScriptListener, 1);
	q->handler = handler;
	q->actionType = actionType;
	q->module = strdup(module);
	q->language = lang;
	LIST_ENTRY_INIT(q, listener_list);

	return q;
}

void script_add_system_listener(const char* module,
				t_language lang,
				t_script_event actionType,
		                t_script_return (*handler)(ScriptEventArgs*) )
{
	ScriptListener *l = script_make_listener(module, lang, actionType, handler);

	LIST_INSERT_HEAD(&globalListeners, l, listener_list);
}

void script_del_proto_char_listener(
	struct char_data* ch,
	const char* module,
	t_language lang,
	t_script_event actionType,
	t_script_return (*handler)(ScriptEventArgs*))
{
	script_clear_listeners_language(&(ch->proto_script_listeners), lang);
}

/*void script_clear_listeners_language(ScriptListener** head, t_language lang)*/


void script_add_proto_char_listener(
	struct char_data* ch,
	const char* module,
	t_language lang,
	t_script_event actionType,
	t_script_return (*handler)(ScriptEventArgs*) )
{
	ScriptListener *l = script_make_listener(module, lang, actionType, handler);

	LIST_INSERT_HEAD(&(ch->proto_script_listeners), l, listener_list);
}


void script_del_system_listener(const char* module,
				t_language lang,
		                t_script_event actionType,
				t_script_return (*handler)(ScriptEventArgs*))
{
	ScriptListener *l_next, *l;

	for(l = LIST_FIRST(&globalListeners); l; l = l_next)
	{
		l_next = LIST_NEXT(l, listener_list);

		if (lang != l->language 
				|| actionType != l->actionType 
				|| strcmp(module, l->module))
				continue;

		LIST_REMOVE(l, listener_list);
		script_free_listener(l);
	}
}

t_script_return script_check_system_listeners(t_script_event actionType,
      ScriptEventArgs* args)
{
	ScriptListener *l, *l_next;
	int result;

	for(l = LIST_FIRST(&globalListeners); l; l = l_next)
	{
		l_next = LIST_NEXT(l, listener_list);

		if (actionType != l->actionType)
			continue;

		result = l->handler(args);
	       
		if (result && result != SCRIPT_RET_OK)
			return result;
	}
	return 0;
}

t_script_return script_check_listeners(
                struct _script_listener_ghead* head,
                t_script_event actionType,
                ScriptEventArgs* args)
{
        ScriptListener *l, *l_next;
        int result;

        for(l = LIST_FIRST(head); l; l = l_next)
        {
                l_next = LIST_NEXT(l, listener_list);

                if (actionType != l->actionType)
                        continue;
                result = l->handler(args);

                if (result && result != SCRIPT_RET_OK)
                        return result;
        }
        return 0;
}



void script_mobread(struct char_data* mob)
{
}

void script_objread(struct obj_data* obj)
{
}

void script_roomread(struct room_data* room)
{
}

ACMD(do_py_mcall)
{
	if (!IS_NPC(ch) || CHECK_MOB_CALL(cmd_flags)) {
		invalid_command_message(ch);
		return;
	}
	
#ifdef HAVE_PYTHON
	python_mob_call(ch, argument, commandp->name, subcmd);
#endif
}

/*********************************************************************************/

