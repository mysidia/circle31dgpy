/* ************************************************************************
*   File: interpreter.c                                 Part of CircleMUD *
*  Usage: parse user commands, search for specials, call ACMD functions   *
*                                                                         *
*  All rights reserved.  See license.doc for complete information.        *
*                                                                         *
*  Copyright (C) 1993, 94 by the Trustees of the Johns Hopkins University *
*  CircleMUD is based on DikuMUD, Copyright (C) 1990, 1991.               *
************************************************************************ */

#define __INTERPRETER_C__

#include "conf.h"
#include "sysdep.h"

#include "structs.h"
#include "comm.h"
#include "interpreter.h"
#include "db.h"
#include "utils.h"
#include "spells.h"
#include "handler.h"
#include "mail.h"
#include "screen.h"
#include "genolc.h"
#include "oasis.h"
#include "tedit.h"
#include "improved-edit.h"
#include "genscript.h"
#include "constants.h"

/* external variables */
extern room_rnum r_mortal_start_room;
extern room_rnum r_immort_start_room;
extern room_rnum r_frozen_start_room;
extern const char *class_menu;
extern char *motd;
extern char *imotd;
extern char *background;
extern struct player_index_element *player_table;
extern int top_of_p_table;
extern int circle_restrict;
extern int no_specials;

/* external functions */
void echo_on(struct descriptor_data *d);
void echo_off(struct descriptor_data *d);
void do_start(struct char_data *ch);
int parse_class(char arg);
int special(struct char_data *ch, CMD_DATA* cmdp, int cmd_flags, char *arg);
int isbanned(char *hostname);
int Valid_Name(char *newname);
void read_aliases(struct char_data *ch);
void delete_aliases(const char *charname);
void read_saved_vars(struct char_data *ch);

/* local functions */
int perform_dupe_check(struct descriptor_data *d);
struct alias_data *find_alias(struct alias_data *alias_list, char *str);
void free_alias(struct alias_data *a);
void perform_complex_alias(struct txt_q *input_q, char *orig, struct alias_data *a);
int perform_alias(struct descriptor_data *d, char *orig, size_t maxlen);
int reserved_word(char *argument);
int _parse_name(char *arg, char *name);
void free_command_handler(CMD_DATA* cmdSpec);
bool has_call_fun(CMD_DATA* cmdSpec);
static void free_command(CMD_DATA* cmdSpec);
	
	


/* prototypes for all do_x functions. */
#include "interpreter.cmdfuns.h"

extern const struct command_info cmd_info[];
const char* cmdfunc_name(CMD_FUN* ptr);

ACMD(do_invalid)
{
}

/* Thisi s the command function list*/
struct { CMD_FUN *func; const char *name; }
cmdfun_table[] =
{
#define CMD_FUN(x)          { x, #x }
CMD_FUN(do_action),
CMD_FUN(do_advance),
CMD_FUN(do_alias),
CMD_FUN(do_assist),
CMD_FUN(do_at),
CMD_FUN(do_backstab),
CMD_FUN(do_ban),
CMD_FUN(do_bash),
CMD_FUN(do_cast),
CMD_FUN(do_color),
CMD_FUN(do_commands),
CMD_FUN(do_consider),
CMD_FUN(do_date),
CMD_FUN(do_dc),
CMD_FUN(do_diagnose),
CMD_FUN(do_dig),
CMD_FUN(do_display),
CMD_FUN(do_drink),
CMD_FUN(do_drop),
CMD_FUN(do_eat),
CMD_FUN(do_echo),
CMD_FUN(do_edit),		/* Mainly intended as a test function. */
CMD_FUN(do_enter),
CMD_FUN(do_equipment),
CMD_FUN(do_examine),
CMD_FUN(do_exits),
CMD_FUN(do_flee),
CMD_FUN(do_follow),
CMD_FUN(do_force),
CMD_FUN(do_gecho),
CMD_FUN(do_gen_comm),
CMD_FUN(do_gen_door),
CMD_FUN(do_gen_ps),
CMD_FUN(do_gen_tog),
CMD_FUN(do_gen_write),
CMD_FUN(do_get),
CMD_FUN(do_give),
CMD_FUN(do_gold),
CMD_FUN(do_goto),
CMD_FUN(do_grab),
CMD_FUN(do_group),
CMD_FUN(do_gsay),
CMD_FUN(do_hcontrol),
CMD_FUN(do_help),
CMD_FUN(do_hide),
CMD_FUN(do_hit),
CMD_FUN(do_house),
CMD_FUN(do_insult),
CMD_FUN(do_inventory),
CMD_FUN(do_invis),
CMD_FUN(do_kick),
CMD_FUN(do_kill),
CMD_FUN(do_last),
CMD_FUN(do_leave),
CMD_FUN(do_levels),
CMD_FUN(do_load),
CMD_FUN(do_look),
CMD_FUN(do_move), 
CMD_FUN(do_not_here),
CMD_FUN(do_oasis),
CMD_FUN(do_olc),
CMD_FUN(do_order),
CMD_FUN(do_page),
CMD_FUN(do_poofset),
CMD_FUN(do_pour),
CMD_FUN(do_practice),
CMD_FUN(do_purge),
CMD_FUN(do_put),
CMD_FUN(do_qcomm),
CMD_FUN(do_quit),
CMD_FUN(do_reboot),
CMD_FUN(do_remove),
CMD_FUN(do_reply),
CMD_FUN(do_report),
CMD_FUN(do_rescue),
CMD_FUN(do_rest),
CMD_FUN(do_restore),
CMD_FUN(do_return),
CMD_FUN(do_save),
CMD_FUN(do_saveall),
CMD_FUN(do_say),
CMD_FUN(do_score),
CMD_FUN(do_send),
CMD_FUN(do_set),
CMD_FUN(do_show),
CMD_FUN(do_shutdown),
CMD_FUN(do_sit),
CMD_FUN(do_skillset),
CMD_FUN(do_sleep),
CMD_FUN(do_sneak),
CMD_FUN(do_snoop),
CMD_FUN(do_spec_comm),
CMD_FUN(do_split),
CMD_FUN(do_stand),
CMD_FUN(do_stat),
CMD_FUN(do_steal),
CMD_FUN(do_switch),
CMD_FUN(do_syslog),
CMD_FUN(do_teleport),
CMD_FUN(do_tell),
CMD_FUN(do_time),
CMD_FUN(do_title),
CMD_FUN(do_toggle),
CMD_FUN(do_track),
CMD_FUN(do_trans),
CMD_FUN(do_unban),
CMD_FUN(do_ungroup),
CMD_FUN(do_use),
CMD_FUN(do_users),
CMD_FUN(do_visible),
CMD_FUN(do_vnum),
CMD_FUN(do_vstat),
CMD_FUN(do_wake),
CMD_FUN(do_wear),
CMD_FUN(do_weather),
CMD_FUN(do_where),
CMD_FUN(do_who),
CMD_FUN(do_wield),
CMD_FUN(do_wimpy),
CMD_FUN(do_wizlock),
CMD_FUN(do_wiznet),
CMD_FUN(do_wizutil),
CMD_FUN(do_write),
CMD_FUN(do_zreset),
CMD_FUN(do_attach),
CMD_FUN(do_detach),
CMD_FUN(do_tstat),
CMD_FUN(do_masound),
CMD_FUN(do_mkill),
CMD_FUN(do_mjunk),
CMD_FUN(do_mdoor),
CMD_FUN(do_mechoaround),
CMD_FUN(do_msend),
CMD_FUN(do_mecho),
CMD_FUN(do_mload),
CMD_FUN(do_mpurge),
CMD_FUN(do_mgoto),
CMD_FUN(do_mat),
CMD_FUN(do_mdamage),
CMD_FUN(do_mteleport),
CMD_FUN(do_mforce),
CMD_FUN(do_mhunt),
CMD_FUN(do_mremember),
CMD_FUN(do_mforget),
CMD_FUN(do_mtransform),
CMD_FUN(do_mzoneecho),
CMD_FUN(do_vdelete),
CMD_FUN(do_mfollow),
CMD_FUN(do_py_mcall),
CMD_FUN(do_invalid),
CMD_FUN(do_script_credits)
};

const char* cmdfunc_name(CMD_FUN* ptr)
{
	int i;

	for(i = 0; i < sizeof(cmdfun_table)/sizeof(cmdfun_table[0]);i++) {
		if (ptr == cmdfun_table[i].func)
			return cmdfun_table[i].name;
	}
	return cmdfunc_name(do_invalid);
}

CMD_FUN * cmdfunc_lookup(const char* name)
{
	int i;

	if (!str_cmp(name, "<null>"))
			return 0;

	for(i = 0; i < sizeof(cmdfun_table)/sizeof(cmdfun_table[0]);i++) {
		if (!str_cmp(cmdfun_table[i].name, name))
			return cmdfun_table[i].func;
	}
	return 0;
}

struct _command_head cmd_hash[256];
struct _command_head sorted_cmd_list;

unsigned int 
hash_command(const char* cmd) {
	return !cmd ? 0 : ((unsigned char)UPPER(cmd[0]))%256; 
}

/*
 * Save the command table
 */
void save_commands()
{
	FILE* fp = fopen(COMMANDS_FILE".new", "w");
	struct command_info* cmd;
	long slot;

	if (!fp)
	{
		mudlog(BRF, LVL_IMMORT, TRUE, "SYSERR: error opening %s for writing", COMMANDS_FILE);
		return;
	}


	for (slot = 0; slot < 256; slot++)
	{	  
		for (cmd = LIST_FIRST(&cmd_hash[slot]); cmd; cmd = LIST_NEXT(cmd, cmd_lst))
		{
			/*
			 * Only commands that actually came from etc/commands
			 * get saved back to it.
			 */
			if (!IS_SET(cmd->flags, CMD_FIXED))
				continue;

			fprintf(fp, "#COMMAND\n");
			fprintf(fp, "Number    %d\n"
				    "Priority  %d\n"
				    "Name      \"%s\"\n"
				    "Position  %d\n"
				    "Code      %s\n"
				    "Level     %d\n"
				    "Subcmd    %d\n"
				    "Flags     %d\n"
				    "Language  NATIVE\n",			   
				      	   cmd->number, 49, cmd->name, 
					   cmd->minimum_position,
					   cmd->native_callfun ? 
					        cmdfunc_name(cmd->native_callfun) : "<null>",
					   cmd->minimum_level,
					   cmd->subcmd, cmd->flags);
			fprintf(fp, "End\n\n");
		}		  
	}

	fprintf(fp, "#END\n");
	fclose(fp);
	rename(COMMANDS_FILE".new", COMMANDS_FILE);
}


void
file_skip_line(FILE* fp, char* file, bool errors_fatal)
{
	int letter;

	for ( ;; ) {
		letter = fgetc(fp);
		if (letter == EOF || feof(fp)) {
			log("SYSERR: unexpected eof in %s", file);

			if (errors_fatal)
				exit(2);
			return;
		}

		if (letter != '\n') {
			ungetc(letter, fp);
			break;
		}
	}
}


/*
 * Skip whitespace characters
 */
void
file_skip_whitespace(FILE* fp, const char* file, bool errors_fatal)
{
	int letter;

	for ( ;; ) {
		letter = fgetc(fp);
		if (letter == EOF || feof(fp)) {
			log("SYSERR: unexpected eof in %s", file);

			if (errors_fatal)
				exit(2);
			return;
		}

		if (!isspace(letter)) {
			ungetc(letter, fp);
			break;
		}
	}
}


/* Get just one word*/
char* 
file_get_word(FILE* fp, const char* file, bool errors_fatal)
{
	static char buf[MAX_STRING_LENGTH];
	int letter, i = 0;

	/* Skip whitespace */
	file_skip_whitespace(fp, file, errors_fatal);

	for ( ;; ) {					
		letter = fgetc(fp);
		if (letter == EOF || feof(fp)) {
			log("SYSERR: unexpected eof in %s", file);

			if (errors_fatal)
				exit(2);
			return "";
		}

		if (isspace(letter))
			break;	

		if (!isspace(letter))
			continue;
		buf[i++] = letter;

		if (i >= MAX_STRING_LENGTH) {
			log("SYSERR: word too long in %s", file);

			if (errors_fatal)
				exit(2);
			return "";
		}
	}
	return buf;
}

/* Get the command hash */
struct _command_head* 
chash_get(unsigned int slot) {
	return &cmd_hash[slot];
}

/*
 * Perform a checked insertion.. this means that a FIXED command
 * (stored in the master table) will be filled in instead of a new
 * command being inserted
 */
bool
check_insert_command(CMD_DATA* cmdp, t_language lang)
{
	long slot;
	CMD_DATA* srch;
       
	if (cmdp == NULL)
		return FALSE;
	if (cmdp->override == 1) {
		return insert_command(cmdp, lang);
	}
	slot = hash_command(cmdp->name);

	for(srch = LIST_FIRST(&cmd_hash[slot]); srch;
			srch = LIST_NEXT(srch, cmd_lst))
	{
		if (srch->language != lang || !IS_SET(srch->flags, CMD_FIXED))
			continue;

		if (has_call_fun(srch))
			continue;

		if (strcmp(cmdp->name, srch->name))
			continue;

		switch(lang)
		{
#ifdef HAVE_PYTHON
			case PYTHON:
				srch->py_callfun = cmdp->py_callfun;
				cmdp->py_callfun = NULL;
				Py_INCREF(srch->py_callfun);
				free_command(cmdp);
				return TRUE;
#endif
			case NATIVE:
				srch->native_callfun = cmdp->native_callfun;
				free_command(cmdp);
				return TRUE;
			default: return FALSE;
		}
	}

	return insert_command(cmdp, lang);
}

CMD_DATA* find_sorted_command_before(CMD_DATA* ptr, long slot)
{
	CMD_DATA* search = NULL, *n, *o;
	long slot_search = slot;
	int cmp;
	
	while(search == NULL && slot_search >= 0)
	{
		for(search = LIST_FIRST(&cmd_hash[slot_search]); search;
                     search = LIST_NEXT(search, cmd_lst))
		{
			cmp = strcasecmp(ptr->name, search->name);
			if (cmp <= 0)
				break;
		}
		slot_search--;
	}

	if (search != NULL) {
		for( ; LIST_NEXT(search, cmd_sorted_lst) ; search = n ) 
		{
			n = LIST_NEXT(search, cmd_sorted_lst);

			if (n == NULL)
				return search;

			if (strcasecmp(ptr->name, n->name) >= 0)
				return search;
		}
	}

	for(search = LIST_FIRST(&sorted_cmd_list); search; search = n)
	{
		n = LIST_NEXT(search, cmd_sorted_lst);

		if (n == NULL)
			return search;

		if (strcasecmp(ptr->name, n->name) < 0)
			return search;

		if (strcasecmp(ptr->name, n->name) <= 0)
			return search;
	}

	return LIST_FIRST(&sorted_cmd_list);
}


bool
insert_command(struct command_info* cmdSpec,
               t_language lang)
{
	struct command_info* p, *p2;
	unsigned int slot = hash_command(cmdSpec->name);
	int c;

	LIST_ENTRY_INIT(cmdSpec, cmd_lst);
	LIST_ENTRY_INIT(cmdSpec, cmd_sorted_lst);
	cmdSpec->hashcode = slot;
	cmdSpec->language = lang;

	for(p = LIST_FIRST(&cmd_hash[slot]); p && LIST_NEXT(p, cmd_lst);
            p = LIST_NEXT(p, cmd_lst))
	{
		if (!cmdSpec->override && !str_cmp(p->name, cmdSpec->name))
		{
			free_command(cmdSpec);
			return FALSE;
		}
		if (LIST_NEXT(p, cmd_lst)->priority > cmdSpec->priority)
			break;
	}

	for(p2 = p; p2; p2 = LIST_NEXT(p2, cmd_lst))
	{
		if (!cmdSpec->override && !str_cmp(p2->name, cmdSpec->name)) {
			free_command(cmdSpec);
			return FALSE;
		}
	}

#ifdef HAVE_PYTHON
	if (cmdSpec->py_callfun) {
		Py_INCREF(cmdSpec->py_callfun);
	}
#endif

	/* Maintain the sorted list*/
	p2 = find_sorted_command_before(cmdSpec, slot);

	if (p2 == NULL) {
		LIST_INSERT_HEAD(&sorted_cmd_list, cmdSpec, cmd_sorted_lst);
	}
	else {
		c = strcasecmp(cmdSpec->name, p2->name);

		if (c < 0) {
			LIST_INSERT_BEFORE(p2, cmdSpec, cmd_sorted_lst);
		}
		else {
			LIST_INSERT_AFTER(p2, cmdSpec, cmd_sorted_lst);		
		}
	}


	if (!p)
	{
		LIST_INSERT_HEAD(&cmd_hash[slot], cmdSpec, cmd_lst);
	}
	else
	{
		if (cmdSpec->priority >= p->priority)
			LIST_INSERT_AFTER(p, cmdSpec, cmd_lst);
		else
			LIST_INSERT_BEFORE(p, cmdSpec, cmd_lst);
	}
	
	return TRUE;
}

bool
has_call_fun(CMD_DATA* cmdSpec)
{
	if (cmdSpec->native_callfun)
		return TRUE;
#ifdef HAVE_PYTHON
	if (cmdSpec->py_callfun)
		return TRUE;
#endif
	return FALSE;
}

void
free_command_handler(CMD_DATA* cmdSpec)
{
#ifdef HAVE_PYTHON
	if (cmdSpec->py_callfun != NULL) {
		Py_DECREF(cmdSpec->py_callfun);
		cmdSpec->py_callfun = 0;
	}
#endif
}

static void 
free_command(CMD_DATA* cmdSpec)
{
	free_command_handler(cmdSpec);
	free(cmdSpec->name);
	free(cmdSpec);
}


void 
clear_commands(t_language lang)
{
	struct command_info *c, *c_next;
	long slot;

	for(slot = 0; slot < 256; slot++) {
		if (LIST_FIRST(&cmd_hash[slot]) == NULL)
			continue;
		for(c = LIST_FIRST(&cmd_hash[slot]); c; c = c_next)
		{
			c_next = LIST_NEXT(c, cmd_lst);

			if (c->language != lang)
				continue;

			if (IS_SET(c->flags, CMD_FIXED))
			{
				free_command_handler(c);
				continue;
			}
			LIST_REMOVE(c, cmd_lst);
			LIST_REMOVE(c, cmd_sorted_lst);
			free_command(c);
		}
	}
}

void 
deregister_command_byname(const char* command_name, t_language lang)
{
	long slot;
	struct command_info *c, *c_next;

	if (!command_name)
		return;

	slot = hash_command(command_name);
	for(c = LIST_FIRST(&cmd_hash[slot]); c; c = c_next)
	{
		c_next = LIST_NEXT(c, cmd_lst);

		if (c->language == lang && !str_cmp(command_name, c->name))
		{
			LIST_REMOVE(c, cmd_lst);
			LIST_REMOVE(c, cmd_sorted_lst);
			free_command(c);
		}		
	}
}

void
deregister_command_predicate(bool (* dereg_predicate)(CMD_DATA *, void*), void *data,
                             t_language lang)
{
	long slot;
	struct command_info *c, *c_next;

	for(slot = 0; slot < 256; slot++)
		for(c = LIST_FIRST(&cmd_hash[slot]); c; c = c_next)
		{
			c_next = LIST_NEXT(c, cmd_lst);

			if (c->language == lang && dereg_predicate(c, data))
			{
				LIST_REMOVE(c, cmd_lst);
				LIST_REMOVE(c, cmd_sorted_lst);
				free_command(c);
			}		
		}
}


#ifdef HAVE_PYTHON
void 
deregister_command_pyfunc(PyObject* fun, t_language lang)
{
	long slot;
	struct command_info *c, *c_next;

	if (fun == NULL)
		return;

	for(slot = 0; slot < 256; slot++)
	{
		for(c = LIST_FIRST(&cmd_hash[slot]); c; c = c_next)
		{
			c_next = LIST_NEXT(c, cmd_lst);
	
			if (c->language == PYTHON && c->py_callfun == fun)
			{
				LIST_REMOVE(c, cmd_lst);
				LIST_REMOVE(c, cmd_sorted_lst);
				free_command(c);
			}		
		}
	}
}
#endif


void 
deregister_command_cfunc(
	CMD_FUN* fun,
	t_language lang)
{
	long slot;
	struct command_info *c, *c_next;

	for(slot = 0; slot < 256; slot++)
	{
		for(c = LIST_FIRST(&cmd_hash[slot]); c; c = c_next)
		{
			c_next = LIST_NEXT(c, cmd_lst);
	
			if (c->language == PYTHON && c->native_callfun == fun)
			{
				LIST_REMOVE(c, cmd_lst);
				free_command(c);
			}		
		}
	}
}

int 
check_command(
		struct char_data* ch, 
		char* arg, 
		char* text, 
		int flags,
		int subcmd, 
		int override
		)
{
	unsigned int slot = hash_command(arg), length;
	struct command_info* cmd, *cmd_next;
	int cant_choose = 0;

	length = strlen(arg);

	if (!IS_NPC(ch) && PLR_FLAGGED(ch, PLR_FROZEN) && GET_LEVEL(ch) < LVL_IMPL) 
	{
		send_to_char(ch, "You try, but the mind-numbing cold prevents you...\r\n");
		return 1;
	}
	
	for(cmd = LIST_FIRST(&cmd_hash[slot]); cmd; cmd = cmd_next)
	{
		cmd_next = LIST_NEXT(cmd, cmd_lst);

		cant_choose = 0;
		
		if (override) {
			if (cmd->override == 0)
				cant_choose = 1;
		}
		else {
			if (cmd->override == 1)
				cant_choose = 1;
		}	
		if (cmd->minimum_level > GET_LEVEL(ch))
			continue;
		if (IS_SET(cmd->flags, CMD_NOABBREV) && strlen(cmd->name) != length)
			continue;
		
		if (!strncmp(cmd->name, arg, length)) {
			if (cant_choose)
				return 0;
			break;
		}
	}
	
	if (cmd)
	{
		if (IS_NPC(ch) && cmd->minimum_level >= LVL_IMMORT)
		{
			send_to_char(ch, "You can't use immortal commands while switched.\r\n");
			return 1;
		}
		  
		if (cmd->minimum_position > GET_POS(ch)) {
			send_bad_position_message(ch);
			return 1;
		}

		switch(cmd->language)
		{
#ifdef HAVE_PYTHON
			case PYTHON:
				if (cmd->py_callfun == Py_None)
					return 0;
				py_command_execute(ch, arg, text, cmd, subcmd, 1);

				return 1;
				break;
#endif

			case NATIVE:
				if (no_specials || !special(ch, cmd, flags, text)) {
					if (cmd->native_callfun == 0)
					{
						send_to_char(ch, "Sorry, that command is"
								 " not available.\r\n");
					}
					else
					cmd->native_callfun(ch, text, cmd, flags, cmd->subcmd);
				}
				return 1;
			default:
				return 0;
		}
	}
	return 0;
}


const char *fill[] =
{
  "in",
  "from",
  "with",
  "the",
  "on",
  "at",
  "to",
  "\n"
};

const char *reserved[] =
{
  "a",
  "an",
  "self",
  "me",
  "all",
  "room",
  "someone",
  "something",
  "\n"
};

void invalid_command_message(struct char_data* ch)
{
	send_to_char(ch, "Huh?!?\r\n");
}


void send_bad_position_message(struct char_data* ch)
{
    switch (GET_POS(ch)) {
    case POS_DEAD:
      send_to_char(ch, "Lie still; you are DEAD!!! :-(\r\n");
      break;
    case POS_INCAP:
    case POS_MORTALLYW:
      send_to_char(ch, "You are in a pretty bad shape, unable to do anything!\r\n");
      break;
    case POS_STUNNED:
      send_to_char(ch, "All you can do right now is think about the stars!\r\n");
      break;
    case POS_SLEEPING:
      send_to_char(ch, "In your dreams, or what?\r\n");
      break;
    case POS_RESTING:
      send_to_char(ch, "Nah... You feel too relaxed to do that..\r\n");
      break;
    case POS_SITTING:
      send_to_char(ch, "Maybe you should get on your feet first?\r\n");
      break;
    case POS_FIGHTING:
      send_to_char(ch, "No way!  You're fighting for your life!\r\n");
      break;
  }
}

/*
 * This is the actual command interpreter called from game_loop() in comm.c
 * It makes sure you are the proper level and position to execute the command,
 * then calls the appropriate function.
 */
void command_interpreter(struct char_data *ch, char *argument, int cmd_flags)
{
  char *line;
  char arg[MAX_INPUT_LENGTH];

  REMOVE_BIT(AFF_FLAGS(ch), AFF_HIDE);

  /* just drop to next line for hitting CR */
  skip_spaces(&argument);
  if (!*argument)
    return;

  /*
   * special case to handle one-character, non-alphanumeric commands;
   * requested by many people so "'hi" or ";godnet test" is possible.
   * Patch sent by Eric Green and Stefan Wasilewski.
   */
  if (!isalpha(*argument)) {
    arg[0] = argument[0];
    arg[1] = '\0';
    line = argument + 1;
  } else
    line = any_one_arg(argument, arg);

  /* Since all command triggers check for valid_dg_target before acting, the levelcheck
   * here has been removed. 
   */
  /* otherwise, find the command */
  {
    if (script_hook_command(HOOK_COMMAND_OVERRIDE, ch, str_to_param(arg), str_to_param(line))) 
	    return;
  }

  if ( check_command(ch, arg, line, cmd_flags, 0, 1) ||
       check_command(ch, arg, line, cmd_flags, 0, 0))
  {
	  return;
  }
  
/*  for (length = strlen(arg), cmd = 0; *cmd_info[cmd].command != '\n'; cmd++)
    if (!strncmp(cmd_info[cmd].command, arg, length))
      if (GET_LEVEL(ch) >= cmd_info[cmd].minimum_level)
	break;*/
  
    if (script_hook_command(HOOK_COMMAND_ENTERED, ch, str_to_param(arg), 
                           str_to_param(line)))
	    return;
    invalid_command_message(ch);
}

/**************************************************************************
 * Routines to handle aliasing                                             *
  **************************************************************************/


struct alias_data *find_alias(struct alias_data *alias_list, char *str)
{
  while (alias_list != NULL) {
    if (*str == *alias_list->alias)	/* hey, every little bit counts :-) */
      if (!strcmp(str, alias_list->alias))
	return (alias_list);

    alias_list = alias_list->next;
  }

  return (NULL);
}


void free_alias(struct alias_data *a)
{
  if (a->alias)
    free(a->alias);
  if (a->replacement)
    free(a->replacement);
  free(a);
}


/* The interface to the outside world: do_alias */
ACMD(do_alias)
{
  char arg[MAX_INPUT_LENGTH];
  char *repl;
  struct alias_data *a, *temp;

  if (IS_NPC(ch))
    return;

  repl = any_one_arg(argument, arg);

  if (!*arg) {			/* no argument specified -- list currently defined aliases */
    send_to_char(ch, "Currently defined aliases:\r\n");
    if ((a = GET_ALIASES(ch)) == NULL)
      send_to_char(ch, " None.\r\n");
    else {
      while (a != NULL) {
	send_to_char(ch, "%-15s %s\r\n", a->alias, a->replacement);
	a = a->next;
      }
    }
  } else {			/* otherwise, add or remove aliases */
    /* is this an alias we've already defined? */
    if ((a = find_alias(GET_ALIASES(ch), arg)) != NULL) {
      REMOVE_FROM_LIST(a, GET_ALIASES(ch), next);
      free_alias(a);
    }
    /* if no replacement string is specified, assume we want to delete */
    if (!*repl) {
      if (a == NULL)
	send_to_char(ch, "No such alias.\r\n");
      else
	send_to_char(ch, "Alias deleted.\r\n");
    } else {			/* otherwise, either add or redefine an alias */
      if (!str_cmp(arg, "alias")) {
	send_to_char(ch, "You can't alias 'alias'.\r\n");
	return;
      }
      CREATE(a, struct alias_data, 1);
      a->alias = strdup(arg);
      delete_doubledollar(repl);
      a->replacement = strdup(repl);
      if (strchr(repl, ALIAS_SEP_CHAR) || strchr(repl, ALIAS_VAR_CHAR))
	a->type = ALIAS_COMPLEX;
      else
	a->type = ALIAS_SIMPLE;
      a->next = GET_ALIASES(ch);
      GET_ALIASES(ch) = a;
      send_to_char(ch, "Alias added.\r\n");
    }
  }
}

/*
 * Valid numeric replacements are only $1 .. $9 (makes parsing a little
 * easier, and it's not that much of a limitation anyway.)  Also valid
 * is "$*", which stands for the entire original line after the alias.
 * ";" is used to delimit commands.
 */
#define NUM_TOKENS       9

void perform_complex_alias(struct txt_q *input_q, char *orig, struct alias_data *a)
{
  struct txt_q temp_queue;
  char *tokens[NUM_TOKENS], *temp, *write_point;
  char buf2[MAX_RAW_INPUT_LENGTH], buf[MAX_RAW_INPUT_LENGTH];	/* raw? */
  int num_of_tokens = 0, num;

  /* First, parse the original string */
  strcpy(buf2, orig);	/* strcpy: OK (orig:MAX_INPUT_LENGTH < buf2:MAX_RAW_INPUT_LENGTH) */
  temp = strtok(buf2, " ");
  while (temp != NULL && num_of_tokens < NUM_TOKENS) {
    tokens[num_of_tokens++] = temp;
    temp = strtok(NULL, " ");
  }

  /* initialize */
  write_point = buf;
  temp_queue.head = temp_queue.tail = NULL;

  /* now parse the alias */
  for (temp = a->replacement; *temp; temp++) {
    if (*temp == ALIAS_SEP_CHAR) {
      *write_point = '\0';
      buf[MAX_INPUT_LENGTH - 1] = '\0';
      write_to_q(buf, &temp_queue, 1);
      write_point = buf;
    } else if (*temp == ALIAS_VAR_CHAR) {
      temp++;
      if ((num = *temp - '1') < num_of_tokens && num >= 0) {
	strcpy(write_point, tokens[num]);	/* strcpy: OK */
	write_point += strlen(tokens[num]);
      } else if (*temp == ALIAS_GLOB_CHAR) {
	strcpy(write_point, orig);		/* strcpy: OK */
	write_point += strlen(orig);
      } else if ((*(write_point++) = *temp) == '$')	/* redouble $ for act safety */
	*(write_point++) = '$';
    } else
      *(write_point++) = *temp;
  }

  *write_point = '\0';
  buf[MAX_INPUT_LENGTH - 1] = '\0';
  write_to_q(buf, &temp_queue, 1);

  /* push our temp_queue on to the _front_ of the input queue */
  if (input_q->head == NULL)
    *input_q = temp_queue;
  else {
    temp_queue.tail->next = input_q->head;
    input_q->head = temp_queue.head;
  }
}


/*
 * Given a character and a string, perform alias replacement on it.
 *
 * Return values:
 *   0: String was modified in place; call command_interpreter immediately.
 *   1: String was _not_ modified in place; rather, the expanded aliases
 *      have been placed at the front of the character's input queue.
 */
int perform_alias(struct descriptor_data *d, char *orig, size_t maxlen)
{
  char first_arg[MAX_INPUT_LENGTH], *ptr;
  struct alias_data *a, *tmp;

  /* Mobs don't have alaises. */
  if (IS_NPC(d->character))
    return (0);

  /* bail out immediately if the guy doesn't have any aliases */
  if ((tmp = GET_ALIASES(d->character)) == NULL)
    return (0);

  /* find the alias we're supposed to match */
  ptr = any_one_arg(orig, first_arg);

  /* bail out if it's null */
  if (!*first_arg)
    return (0);

  /* if the first arg is not an alias, return without doing anything */
  if ((a = find_alias(tmp, first_arg)) == NULL)
    return (0);

  if (a->type == ALIAS_SIMPLE) {
    strlcpy(orig, a->replacement, maxlen);
    return (0);
  } else {
    perform_complex_alias(&d->input, ptr, a);
    return (1);
  }
}



/***************************************************************************
 * Various other parsing utilities                                         *
 **************************************************************************/

/*
 * searches an array of strings for a target string.  "exact" can be
 * 0 or non-0, depending on whether or not the match must be exact for
 * it to be returned.  Returns -1 if not found; 0..n otherwise.  Array
 * must be terminated with a '\n' so it knows to stop searching.
 */
int search_block(char *arg, const char **list, int exact)
{
  int i, l;

  /*  We used to have \r as the first character on certain array items to
   *  prevent the explicit choice of that point.  It seems a bit silly to
   *  dump control characters into arrays to prevent that, so we'll just
   *  check in here to see if the first character of the argument is '!',
   *  and if so, just blindly return a '-1' for not found. - ae.
   */
  if (*arg == '!')
    return (-1);

  /* Make into lower case, and get length of string */
  for (l = 0; *(arg + l); l++)
    *(arg + l) = LOWER(*(arg + l));

  if (exact) {
    for (i = 0; **(list + i) != '\n'; i++)
      if (!strcmp(arg, *(list + i)))
	return (i);
  } else {
    if (!l)
      l = 1;			/* Avoid "" to match the first available
				 * string */
    for (i = 0; **(list + i) != '\n'; i++)
      if (!strncmp(arg, *(list + i), l))
	return (i);
  }

  return (-1);
}


int is_number(const char *str)
{
  while (*str)
    if (!isdigit(*(str++)))
      return (0);

  return (1);
}

/*
 * Function to skip over the leading spaces of a string.
 */
void skip_spaces(char **string)
{
  for (; **string && isspace(**string); (*string)++);
}


/*
 * Given a string, change all instances of double dollar signs ($$) to
 * single dollar signs ($).  When strings come in, all $'s are changed
 * to $$'s to avoid having users be able to crash the system if the
 * inputted string is eventually sent to act().  If you are using user
 * input to produce screen output AND YOU ARE SURE IT WILL NOT BE SENT
 * THROUGH THE act() FUNCTION (i.e., do_gecho, do_title, but NOT do_say),
 * you can call delete_doubledollar() to make the output look correct.
 *
 * Modifies the string in-place.
 */
char *delete_doubledollar(char *string)
{
  char *ddread, *ddwrite;

  /* If the string has no dollar signs, return immediately */
  if ((ddwrite = strchr(string, '$')) == NULL)
    return (string);

  /* Start from the location of the first dollar sign */
  ddread = ddwrite;


  while (*ddread)   /* Until we reach the end of the string... */
    if ((*(ddwrite++) = *(ddread++)) == '$') /* copy one char */
      if (*ddread == '$')
	ddread++; /* skip if we saw 2 $'s in a row */

  *ddwrite = '\0';

  return (string);
}


int fill_word(char *argument)
{
  return (search_block(argument, fill, TRUE) >= 0);
}


int reserved_word(char *argument)
{
  return (search_block(argument, reserved, TRUE) >= 0);
}


/*
 * copy the first non-fill-word, space-delimited argument of 'argument'
 * to 'first_arg'; return a pointer to the remainder of the string.
 */
char *one_argument(char *argument, char *first_arg)
{
  char *begin = first_arg;

  if (!argument) {
    log("SYSERR: one_argument received a NULL pointer!");
    *first_arg = '\0';
    return (NULL);
  }

  do {
    skip_spaces(&argument);

    first_arg = begin;
    while (*argument && !isspace(*argument)) {
      *(first_arg++) = LOWER(*argument);
      argument++;
    }

    *first_arg = '\0';
  } while (fill_word(begin));

  return (argument);
}


/*
 * one_word is like one_argument, except that words in quotes ("") are
 * considered one word.
 */
char *one_word(char *argument, char *first_arg)
{
  char *begin = first_arg;

  do {
    skip_spaces(&argument);

    first_arg = begin;

    if (*argument == '\"') {
      argument++;
      while (*argument && *argument != '\"') {
        *(first_arg++) = LOWER(*argument);
        argument++;
      }
      argument++;
    } else {
      while (*argument && !isspace(*argument)) {
        *(first_arg++) = LOWER(*argument);
        argument++;
      }
    }

    *first_arg = '\0';
  } while (fill_word(begin));

  return (argument);
}


/* same as one_argument except that it doesn't ignore fill words */
char *any_one_arg(char *argument, char *first_arg)
{
  skip_spaces(&argument);

  while (*argument && !isspace(*argument)) {
    *(first_arg++) = LOWER(*argument);
    argument++;
  }

  *first_arg = '\0';

  return (argument);
}


/*
 * Same as one_argument except that it takes two args and returns the rest;
 * ignores fill words
 */
char *two_arguments(char *argument, char *first_arg, char *second_arg)
{
  return (one_argument(one_argument(argument, first_arg), second_arg)); /* :-) */
}



/*
 * determine if a given string is an abbreviation of another
 * (now works symmetrically -- JE 7/25/94)
 *
 * that was dumb.  it shouldn't be symmetrical.  JE 5/1/95
 * 
 * returns 1 if arg1 is an abbreviation of arg2
 */
int is_abbrev(const char *arg1, const char *arg2)
{
  if (!*arg1)
    return (0);

  for (; *arg1 && *arg2; arg1++, arg2++)
    if (LOWER(*arg1) != LOWER(*arg2))
      return (0);

  if (!*arg1)
    return (1);
  else
    return (0);
}



/*
 * Return first space-delimited token in arg1; remainder of string in arg2.
 *
 * NOTE: Requires sizeof(arg2) >= sizeof(string)
 */
void half_chop(char *string, char *arg1, char *arg2)
{
  char *temp;

  temp = any_one_arg(string, arg1);
  skip_spaces(&temp);
  strcpy(arg2, temp);	/* strcpy: OK (documentation) */
}



/* Used in specprocs, mostly.  (Exactly) matches "command" to cmd number */
CMD_DATA* find_command(const char *command)
{
  long slot = hash_command(command);
  CMD_DATA* cmdp;

  for(cmdp = LIST_FIRST(&cmd_hash[slot]); cmdp; cmdp = LIST_NEXT(cmdp, cmd_lst))
	  if (!str_cmp(cmdp->name, command))
		  return cmdp;
  return NULL;
}


int special(struct char_data *ch, CMD_DATA* commandp, int cmd_flags, char *arg)
{
  struct obj_data *i;
  struct char_data *k;
  int j;

  /* special in room? */
  if (GET_ROOM_SPEC(IN_ROOM(ch)) != NULL)
    if (GET_ROOM_SPEC(IN_ROOM(ch)) (ch, world + IN_ROOM(ch), commandp, arg, cmd_flags))
      return (1);

  /* special in equipment list? */
  for (j = 0; j < NUM_WEARS; j++)
    if (GET_EQ(ch, j) && GET_OBJ_SPEC(GET_EQ(ch, j)) != NULL)
      if (GET_OBJ_SPEC(GET_EQ(ch, j)) (ch, GET_EQ(ch, j), commandp, arg, cmd_flags))
	return (1);

  /* special in inventory? */
  for (i = ch->carrying; i; i = i->next_content)
    if (GET_OBJ_SPEC(i) != NULL)
      if (GET_OBJ_SPEC(i) (ch, i, commandp, arg, cmd_flags))
	return (1);

  /* special in mobile present? */
  for (k = world[IN_ROOM(ch)].people; k; k = k->next_in_room)
    if (!MOB_FLAGGED(k, MOB_NOTDEADYET))
      if (GET_MOB_SPEC(k) && GET_MOB_SPEC(k) (ch, k, commandp, arg, cmd_flags))
	return (1);

  /* special in object present? */
  for (i = world[IN_ROOM(ch)].contents; i; i = i->next_content)
    if (GET_OBJ_SPEC(i) != NULL)
      if (GET_OBJ_SPEC(i) (ch, i, commandp, arg, cmd_flags))
	return (1);

  return (0);
}



/* *************************************************************************
*  Stuff for controlling the non-playing sockets (get name, pwd etc)       *
************************************************************************* */


/* This function needs to die. */
int _parse_name(char *arg, char *name)
{
  int i;

  skip_spaces(&arg);
  for (i = 0; (*name = *arg); arg++, i++, name++)
    if (!isalpha(*arg))
      return (1);

  if (!i)
    return (1);

  return (0);
}


#define RECON		1
#define USURP		2
#define UNSWITCH	3

/* This function seems a bit over-extended. */
int perform_dupe_check(struct descriptor_data *d)
{
  struct descriptor_data *k, *next_k;
  struct char_data *target = NULL, *ch, *next_ch;
  int mode = 0;

  int id = GET_IDNUM(d->character);

  /*
   * Now that this descriptor has successfully logged in, disconnect all
   * other descriptors controlling a character with the same ID number.
   */

  for (k = descriptor_list; k; k = next_k) {
    next_k = k->next;

    if (k == d)
      continue;

    if (k->original && (GET_IDNUM(k->original) == id)) {
      /* Original descriptor was switched, booting it and restoring normal body control. */

      write_to_output(d, "\r\nMultiple login detected -- disconnecting.\r\n");
      STATE(k) = CON_CLOSE;
      if (!target) {
	target = k->original;
	mode = UNSWITCH;
      }
      if (k->character)
	k->character->desc = NULL;
      k->character = NULL;
      k->original = NULL;
    } else if (k->character && GET_IDNUM(k->character) == id && k->original) {
      /* Character taking over their own body, while an immortal was switched to it. */

      do_return(k->character, NULL, 0, 0, 0);
    } else if (k->character && GET_IDNUM(k->character) == id) {
      /* Character taking over their own body. */

      if (!target && STATE(k) == CON_PLAYING) {
	write_to_output(k, "\r\nThis body has been usurped!\r\n");
	target = k->character;
	mode = USURP;
      }
      k->character->desc = NULL;
      k->character = NULL;
      k->original = NULL;
      write_to_output(k, "\r\nMultiple login detected -- disconnecting.\r\n");
      STATE(k) = CON_CLOSE;
    }
  }

 /*
  * now, go through the character list, deleting all characters that
  * are not already marked for deletion from the above step (i.e., in the
  * CON_HANGUP state), and have not already been selected as a target for
  * switching into.  In addition, if we haven't already found a target,
  * choose one if one is available (while still deleting the other
  * duplicates, though theoretically none should be able to exist).
  */

  for (ch = character_list; ch; ch = next_ch) {
    next_ch = ch->next;

    if (IS_NPC(ch))
      continue;
    if (GET_IDNUM(ch) != id)
      continue;

    /* ignore chars with descriptors (already handled by above step) */
    if (ch->desc)
      continue;

    /* don't extract the target char we've found one already */
    if (ch == target)
      continue;

    /* we don't already have a target and found a candidate for switching */
    if (!target) {
      target = ch;
      mode = RECON;
      continue;
    }

    /* we've found a duplicate - blow him away, dumping his eq in limbo. */
    if (IN_ROOM(ch) != NOWHERE)
      char_from_room(ch);
    char_to_room(ch, 1);
    extract_char(ch);
  }

  /* no target for switching into was found - allow login to continue */
  if (!target)
    return (0);

  /* Okay, we've found a target.  Connect d to target. */
  free_char(d->character); /* get rid of the old char */
  d->character = target;
  d->character->desc = d;
  d->original = NULL;
  d->character->char_specials.timer = 0;
  REMOVE_BIT(PLR_FLAGS(d->character), PLR_MAILING | PLR_WRITING);
  REMOVE_BIT(AFF_FLAGS(d->character), AFF_GROUP);
  STATE(d) = CON_PLAYING;

  switch (mode) {
  case RECON:
    write_to_output(d, "Reconnecting.\r\n");
    act("$n has reconnected.", TRUE, d->character, 0, 0, TO_ROOM);
    mudlog(NRM, MAX(LVL_IMMORT, GET_INVIS_LEV(d->character)), TRUE, "%s [%s] has reconnected.", GET_NAME(d->character), d->host);
    break;
  case USURP:
    write_to_output(d, "You take over your own body, already in use!\r\n");
    act("$n suddenly keels over in pain, surrounded by a white aura...\r\n"
	"$n's body has been taken over by a new spirit!",
	TRUE, d->character, 0, 0, TO_ROOM);
    mudlog(NRM, MAX(LVL_IMMORT, GET_INVIS_LEV(d->character)), TRUE,
	"%s has re-logged in ... disconnecting old socket.", GET_NAME(d->character));
    break;
  case UNSWITCH:
    write_to_output(d, "Reconnecting to unswitched char.");
    mudlog(NRM, MAX(LVL_IMMORT, GET_INVIS_LEV(d->character)), TRUE, "%s [%s] has reconnected.", GET_NAME(d->character), d->host);
    break;
  }

  return (1);
}



/* deal with newcomers and other non-playing sockets */
void nanny(struct descriptor_data *d, char *arg)
{
  int load_result;	/* Overloaded variable */
  int player_i;

  /* OasisOLC states */
  struct {
    int state;
    void (*func)(struct descriptor_data *, char *);
  } olc_functions[] = {
    { CON_OEDIT, oedit_parse },
    { CON_ZEDIT, zedit_parse },
    { CON_SEDIT, sedit_parse },
    { CON_MEDIT, medit_parse },
    { CON_REDIT, redit_parse },
    { CON_CEDIT, cedit_parse },
    { CON_TRIGEDIT, trigedit_parse },
    { -1, NULL }
  };

  skip_spaces(&arg);

  /*
   * Quick check for the OLC states.
   */
  for (player_i = 0; olc_functions[player_i].state >= 0; player_i++)
    if (STATE(d) == olc_functions[player_i].state) {
      /* send context-sensitive help if need be */
      if (context_help(d, arg)) return;

      (*olc_functions[player_i].func)(d, arg);
      return;
    }

  /* Not in OLC. */
  switch (STATE(d)) {
  case CON_GET_NAME:		/* wait for input of name */
    if (d->character == NULL) {
      CREATE(d->character, struct char_data, 1);
      clear_char(d->character);
      CREATE(d->character->player_specials, struct player_special_data, 1);
      d->character->desc = d;
    }
    if (!*arg)
      STATE(d) = CON_CLOSE;
    else {
      char buf[MAX_INPUT_LENGTH], tmp_name[MAX_INPUT_LENGTH];
      struct char_file_u tmp_store;
      int player_i;

      if ((_parse_name(arg, tmp_name)) || strlen(tmp_name) < 2 ||
	  strlen(tmp_name) > MAX_NAME_LENGTH || !Valid_Name(tmp_name) ||
	  fill_word(strcpy(buf, tmp_name)) || reserved_word(buf)) {	/* strcpy: OK (mutual MAX_INPUT_LENGTH) */
	write_to_output(d, "Invalid name, please try another.\r\nName: ");
	return;
      }
      if ((player_i = load_char(tmp_name, &tmp_store)) > -1) {
	store_to_char(&tmp_store, d->character);
	GET_PFILEPOS(d->character) = player_i;

	if (PLR_FLAGGED(d->character, PLR_DELETED)) {
	  /* We get a false positive from the original deleted character. */
	  free_char(d->character);
	  /* Check for multiple creations... */
	  if (!Valid_Name(tmp_name)) {
	    write_to_output(d, "Invalid name, please try another.\r\nName: ");
	    return;
	  }
	  CREATE(d->character, struct char_data, 1);
	  clear_char(d->character);
	  CREATE(d->character->player_specials, struct player_special_data, 1);
	  d->character->desc = d;
	  CREATE(d->character->player.name, char, strlen(tmp_name) + 1);
	  strcpy(d->character->player.name, CAP(tmp_name));	/* strcpy: OK (size checked above) */
	  GET_PFILEPOS(d->character) = player_i;
	  write_to_output(d, "Did I get that right, %s (Y/N)? ", tmp_name);
	  STATE(d) = CON_NAME_CNFRM;
	} else {
	  /* undo it just in case they are set */
	  REMOVE_BIT(PLR_FLAGS(d->character),
		     PLR_WRITING | PLR_MAILING | PLR_CRYO);
	  REMOVE_BIT(AFF_FLAGS(d->character), AFF_GROUP);
	  write_to_output(d, "Password: ");
	  echo_off(d);
	  d->idle_tics = 0;
	  STATE(d) = CON_PASSWORD;
	}
      } else {
	/* player unknown -- make new character */

	/* Check for multiple creations of a character. */
	if (!Valid_Name(tmp_name)) {
	  write_to_output(d, "Invalid name, please try another.\r\nName: ");
	  return;
	}
	CREATE(d->character->player.name, char, strlen(tmp_name) + 1);
	strcpy(d->character->player.name, CAP(tmp_name));	/* strcpy: OK (size checked above) */

	write_to_output(d, "Did I get that right, %s (Y/N)? ", tmp_name);
	STATE(d) = CON_NAME_CNFRM;
      }
    }
    break;

  case CON_NAME_CNFRM:		/* wait for conf. of new name    */
    if (UPPER(*arg) == 'Y') {
      if (isbanned(d->host) >= BAN_NEW) {
	mudlog(NRM, LVL_GOD, TRUE, "Request for new char %s denied from [%s] (siteban)", GET_PC_NAME(d->character), d->host);
	write_to_output(d, "Sorry, new characters are not allowed from your site!\r\n");
	STATE(d) = CON_CLOSE;
	return;
      }
      if (circle_restrict) {
	write_to_output(d, "Sorry, new players can't be created at the moment.\r\n");
	mudlog(NRM, LVL_GOD, TRUE, "Request for new char %s denied from [%s] (wizlock)", GET_PC_NAME(d->character), d->host);
	STATE(d) = CON_CLOSE;
	return;
      }
      write_to_output(d, "New character.\r\nGive me a password for %s: ", GET_PC_NAME(d->character));
      echo_off(d);
      STATE(d) = CON_NEWPASSWD;
    } else if (*arg == 'n' || *arg == 'N') {
      write_to_output(d, "Okay, what IS it, then? ");
      free(d->character->player.name);
      d->character->player.name = NULL;
      STATE(d) = CON_GET_NAME;
    } else
      write_to_output(d, "Please type Yes or No: ");
    break;

  case CON_PASSWORD:		/* get pwd for known player      */
    /*
     * To really prevent duping correctly, the player's record should
     * be reloaded from disk at this point (after the password has been
     * typed).  However I'm afraid that trying to load a character over
     * an already loaded character is going to cause some problem down the
     * road that I can't see at the moment.  So to compensate, I'm going to
     * (1) add a 15 or 20-second time limit for entering a password, and (2)
     * re-add the code to cut off duplicates when a player quits.  JE 6 Feb 96
     */

    echo_on(d);    /* turn echo back on */

    /* New echo_on() eats the return on telnet. Extra space better than none. */
    write_to_output(d, "\r\n");

    if (!*arg)
      STATE(d) = CON_CLOSE;
    else {
      if (strncmp(CRYPT(arg, GET_PASSWD(d->character)), GET_PASSWD(d->character), MAX_PWD_LENGTH)) {
	mudlog(BRF, LVL_GOD, TRUE, "Bad PW: %s [%s]", GET_NAME(d->character), d->host);
	GET_BAD_PWS(d->character)++;
	save_char(d->character);
	if (++(d->bad_pws) >= CONFIG_MAX_BAD_PWS) {	/* 3 strikes and you're out. */
	  write_to_output(d, "Wrong password... disconnecting.\r\n");
	  STATE(d) = CON_CLOSE;
	} else {
	  write_to_output(d, "Wrong password.\r\nPassword: ");
	  echo_off(d);
	}
	return;
      }

      /* Password was correct. */
      load_result = GET_BAD_PWS(d->character);
      GET_BAD_PWS(d->character) = 0;
      d->bad_pws = 0;

      if (isbanned(d->host) == BAN_SELECT &&
	  !PLR_FLAGGED(d->character, PLR_SITEOK)) {
	write_to_output(d, "Sorry, this char has not been cleared for login from your site!\r\n");
	STATE(d) = CON_CLOSE;
	mudlog(NRM, LVL_GOD, TRUE, "Connection attempt for %s denied from %s", GET_NAME(d->character), d->host);
	return;
      }
      if (GET_LEVEL(d->character) < circle_restrict) {
	write_to_output(d, "The game is temporarily restricted.. try again later.\r\n");
	STATE(d) = CON_CLOSE;
	mudlog(NRM, LVL_GOD, TRUE, "Request for login denied for %s [%s] (wizlock)", GET_NAME(d->character), d->host);
	return;
      }
      /* check and make sure no other copies of this player are logged in */
      if (perform_dupe_check(d))
	return;

      if (GET_LEVEL(d->character) >= LVL_IMMORT)
	write_to_output(d, "%s", imotd);
      else
	write_to_output(d, "%s", motd);

      mudlog(BRF, MAX(LVL_IMMORT, GET_INVIS_LEV(d->character)), TRUE, "%s [%s] has connected.", GET_NAME(d->character), d->host);

      if (load_result) {
        write_to_output(d, "\r\n\r\n\007\007\007"
		"%s%d LOGIN FAILURE%s SINCE LAST SUCCESSFUL LOGIN.%s\r\n",
		CCRED(d->character, C_SPR), load_result,
		(load_result > 1) ? "S" : "", CCNRM(d->character, C_SPR));
	GET_BAD_PWS(d->character) = 0;
      }
      write_to_output(d, "\r\n*** PRESS RETURN: ");
      STATE(d) = CON_RMOTD;
    }
    break;

  case CON_NEWPASSWD:
  case CON_CHPWD_GETNEW:
    if (!*arg || strlen(arg) > MAX_PWD_LENGTH || strlen(arg) < 3 ||
	!str_cmp(arg, GET_PC_NAME(d->character))) {
      write_to_output(d, "\r\nIllegal password.\r\nPassword: ");
      return;
    }
    strncpy(GET_PASSWD(d->character), CRYPT(arg, GET_PC_NAME(d->character)), MAX_PWD_LENGTH);	/* strncpy: OK (G_P:MAX_PWD_LENGTH+1) */
    *(GET_PASSWD(d->character) + MAX_PWD_LENGTH) = '\0';

    write_to_output(d, "\r\nPlease retype password: ");
    if (STATE(d) == CON_NEWPASSWD)
      STATE(d) = CON_CNFPASSWD;
    else
      STATE(d) = CON_CHPWD_VRFY;
    break;

  case CON_CNFPASSWD:
  case CON_CHPWD_VRFY:
    if (strncmp(CRYPT(arg, GET_PASSWD(d->character)), GET_PASSWD(d->character),
		MAX_PWD_LENGTH)) {
      write_to_output(d, "\r\nPasswords don't match... start over.\r\nPassword: ");
      if (STATE(d) == CON_CNFPASSWD)
	STATE(d) = CON_NEWPASSWD;
      else
	STATE(d) = CON_CHPWD_GETNEW;
      return;
    }
    echo_on(d);

    if (STATE(d) == CON_CNFPASSWD) {
      write_to_output(d, "\r\nWhat is your sex (M/F)? ");
      STATE(d) = CON_QSEX;
    } else {
      save_char(d->character);
      write_to_output(d, "\r\nDone.\r\n%s", CONFIG_MENU);
      STATE(d) = CON_MENU;
    }
    break;

  case CON_QSEX:		/* query sex of new user         */
    switch (*arg) {
    case 'm':
    case 'M':
      d->character->player.sex = SEX_MALE;
      break;
    case 'f':
    case 'F':
      d->character->player.sex = SEX_FEMALE;
      break;
    default:
      write_to_output(d, "That is not a sex..\r\n"
		"What IS your sex? ");
      return;
    }

    write_to_output(d, "%s\r\nClass: ", class_menu);
    STATE(d) = CON_QCLASS;
    break;

  case CON_QCLASS:
    load_result = parse_class(*arg);
    if (load_result == CLASS_UNDEFINED) {
      write_to_output(d, "\r\nThat's not a class.\r\nClass: ");
      return;
    } else
      GET_CLASS(d->character) = load_result;

    if (GET_PFILEPOS(d->character) < 0)
      GET_PFILEPOS(d->character) = create_entry(GET_PC_NAME(d->character));
    /* Now GET_NAME() will work properly. */
    init_char(d->character);
    save_char(d->character);
    write_to_output(d, "%s\r\n*** PRESS RETURN: ", motd);
    STATE(d) = CON_RMOTD;

    mudlog(NRM, LVL_IMMORT, TRUE, "%s [%s] new player.", GET_NAME(d->character), d->host);
    break;

  case CON_RMOTD:		/* read CR after printing motd   */
    write_to_output(d, "%s", CONFIG_MENU);
    STATE(d) = CON_MENU;
    break;

  case CON_MENU: {		/* get selection from main menu  */
    room_vnum load_room;

    switch (*arg) {
    case '0':
      write_to_output(d, "Goodbye.\r\n");
      STATE(d) = CON_CLOSE;
      break;

    case '1':
      reset_char(d->character);
      read_aliases(d->character);

      if (PLR_FLAGGED(d->character, PLR_INVSTART))
	GET_INVIS_LEV(d->character) = GET_LEVEL(d->character);

      /*
       * We have to place the character in a room before equipping them
       * or equip_char() will gripe about the person in NOWHERE.
       */
      if ((load_room = GET_LOADROOM(d->character)) != NOWHERE)
	load_room = real_room(load_room);

      /* If char was saved with NOWHERE, or real_room above failed... */
      if (load_room == NOWHERE) {
	if (GET_LEVEL(d->character) >= LVL_IMMORT)
	  load_room = r_immort_start_room;
	else
	  load_room = r_mortal_start_room;
      }

      if (PLR_FLAGGED(d->character, PLR_FROZEN))
	load_room = r_frozen_start_room;

      send_to_char(d->character, "%s", CONFIG_WELC_MESSG);
      d->character->next = character_list;
      character_list = d->character;
      char_to_room(d->character, load_room);
      load_result = Crash_load(d->character);

      /* with the copyover patch, this next line goes in enter_player_game() */
      GET_ID(d->character) = GET_IDNUM(d->character);

      /* Clear their load room if it's not persistant. */
      if (!PLR_FLAGGED(d->character, PLR_LOADROOM))
        GET_LOADROOM(d->character) = NOWHERE;
      save_char(d->character);

      /* with the copyover patch, this next line goes in enter_player_game() */
      read_saved_vars(d->character);
      check_null_hooks(HOOK_PLAYER_ENTERED_GAME, d->character, SNull, SNull);

      act("$n has entered the game.", TRUE, d->character, 0, 0, TO_ROOM);

      STATE(d) = CON_PLAYING;
      if (GET_LEVEL(d->character) == 0) {
	do_start(d->character);
	send_to_char(d->character, "%s", CONFIG_START_MESSG);
      }
      look_at_room(d->character, 0);
      if (has_mail(GET_IDNUM(d->character)))
	send_to_char(d->character, "You have mail waiting.\r\n");
      if (load_result == 2) {	/* rented items lost */
	send_to_char(d->character, "\r\n\007You could not afford your rent!\r\n"
		"Your possesions have been donated to the Salvation Army!\r\n");
      }
      d->has_prompt = 0;
      break;

    case '2':
      if (d->character->player.description) {
	write_to_output(d, "Current description:\r\n%s", d->character->player.description);
	/*
	 * Don't free this now... so that the old description gets loaded
	 * as the current buffer in the editor.  Do setup the ABORT buffer
	 * here, however.
	 *
	 * free(d->character->player.description);
	 * d->character->player.description = NULL;
	 */
	d->backstr = strdup(d->character->player.description);
      }
      write_to_output(d, "Enter the new text you'd like others to see when they look at you.\r\n");
      send_editor_help(d);
      d->str = &d->character->player.description;
      d->max_str = EXDSCR_LENGTH;
      STATE(d) = CON_EXDESC;
      break;

    case '3':
      page_string(d, background, 0);
      STATE(d) = CON_RMOTD;
      break;

    case '4':
      write_to_output(d, "\r\nEnter your old password: ");
      echo_off(d);
      STATE(d) = CON_CHPWD_GETOLD;
      break;

    case '5':
      write_to_output(d, "\r\nEnter your password for verification: ");
      echo_off(d);
      STATE(d) = CON_DELCNF1;
      break;

    default:
      write_to_output(d, "\r\nThat's not a menu choice!\r\n%s", CONFIG_MENU);
      break;
    }
    break;
  }

  case CON_CHPWD_GETOLD:
    if (strncmp(CRYPT(arg, GET_PASSWD(d->character)), GET_PASSWD(d->character), MAX_PWD_LENGTH)) {
      echo_on(d);
      write_to_output(d, "\r\nIncorrect password.\r\n%s", CONFIG_MENU);
      STATE(d) = CON_MENU;
    } else {
      write_to_output(d, "\r\nEnter a new password: ");
      STATE(d) = CON_CHPWD_GETNEW;
    }
    return;

  case CON_DELCNF1:
    echo_on(d);
    if (strncmp(CRYPT(arg, GET_PASSWD(d->character)), GET_PASSWD(d->character), MAX_PWD_LENGTH)) {
      write_to_output(d, "\r\nIncorrect password.\r\n%s", CONFIG_MENU);
      STATE(d) = CON_MENU;
    } else {
      write_to_output(d, "\r\nYOU ARE ABOUT TO DELETE THIS CHARACTER PERMANENTLY.\r\n"
		"ARE YOU ABSOLUTELY SURE?\r\n\r\n"
		"Please type \"yes\" to confirm: ");
      STATE(d) = CON_DELCNF2;
    }
    break;

  case CON_DELCNF2:
    if (!strcmp(arg, "yes") || !strcmp(arg, "YES")) {
      if (PLR_FLAGGED(d->character, PLR_FROZEN)) {
	write_to_output(d, "You try to kill yourself, but the ice stops you.\r\n"
		"Character not deleted.\r\n\r\n");
	STATE(d) = CON_CLOSE;
	return;
      }
      if (GET_LEVEL(d->character) < LVL_GRGOD)
	SET_BIT(PLR_FLAGS(d->character), PLR_DELETED);
      save_char(d->character);
      Crash_delete_file(GET_NAME(d->character));
      delete_aliases(GET_NAME(d->character));
      write_to_output(d, "Character '%s' deleted!\r\n"
	      "Goodbye.\r\n", GET_NAME(d->character));
      mudlog(NRM, LVL_GOD, TRUE, "%s (lev %d) has self-deleted.", GET_NAME(d->character), GET_LEVEL(d->character));
      STATE(d) = CON_CLOSE;
      return;
    } else {
      write_to_output(d, "\r\nCharacter not deleted.\r\n%s", CONFIG_MENU);
      STATE(d) = CON_MENU;
    }
    break;

  /*
   * It's possible, if enough pulses are missed, to kick someone off
   * while they are at the password prompt. We'll just defer to let
   * the game_loop() axe them.
   */
  case CON_CLOSE:
    break;

  default:
    log("SYSERR: Nanny: illegal state of con'ness (%d) for '%s'; closing connection.",
	STATE(d), d->character ? GET_NAME(d->character) : "<unknown>");
    STATE(d) = CON_DISCONNECT;	/* Safest to do. */
    break;
  }
}
