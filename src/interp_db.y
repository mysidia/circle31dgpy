/*
 * GRAMMAR FOR Command Table Parser
 * $Id: interp_db.y,v 1.1.1.1 2004/03/07 16:14:16 root Exp $
 *
 * Attribution Notice:
 *
 *    Copyright (c) 2003-2004 Mysidia <mysidia at qmud dot org> / mysidia of darkfire IRC
 *    All Rights Reserved
 *
 *    Licensed under the Academic Free License version 2.0
 *    See ../doc/afl-2.0.txt
 *    And http://www.opensource.org/licenses/afl-2.0.php
 *
 * Alternativeely, you may distribute the original contents of this library
 * code (interp_db.y) under the terms of the GNU Lesser General Public License,
 * as published by the Free Software Foundation, version 2 or (at your option),
 * any later version.
 *
 *    Please List any changes below:
 *      * Initial version 1.0
 */
%{
#include "conf.h"
#include "sysdep.h"
#include "structs.h"
#include "interpreter.h"
#include "utils.h"

#include "interp_db.tab.h"

#define YYERROR_VERBOSE

void yyerror(char* s);
int interp_dblex();
static CMD_DATA build;
CMD_FUN * cmdfunc_lookup(const char* name);
bool insert_command(struct command_info*, t_language);

static void cmd_start() {
	memset(&build, 0, sizeof(CMD_DATA));
	build.language = NATIVE;
	build.flags = CMD_FIXED;
	build.priority = 49;
}

static void cmd_done() {
	CMD_DATA* n;

	CREATE(n, CMD_DATA, 1);
	memcpy(n, &build, sizeof(CMD_DATA));

	insert_command(n, n->language);
}

static void cmd_number(int i) {
	build.number = i;
}

static void cmd_flags(int i) {
	build.flags = i | CMD_FIXED;
}

static void cmd_priority(int i) {
	build.priority = i;
}

static void cmd_name(const char* s) {
	build.name = strdup(s+1);
	build.name[strlen(build.name) - 1] = '\0';
}

static void cmd_position(int i) {
	build.minimum_position = i;
}

static void cmd_code(const char* s) {
	char buf[256];
	build.native_callfun = 0;

	strncpy(buf, s+1, 255);
	buf[255] = '\0';
	buf[strlen(buf) - 1] = '\0';

	if (build.language == NATIVE) {
		build.native_callfun = cmdfunc_lookup(buf);
	}
}

static void cmd_subcmd(int i) {
	build.subcmd = i;
}

static void cmd_level(int i) {
	build.minimum_level = i;
}

static void cmd_language(t_language i) {
	build.language = i;
}

%}

%union {
        const char* s;
        int i;
	t_language l;
}

%token <i> TOK_INT
%token <i> TOK_LEVEL
%token <s> TOK_QUOTED_WORD
%token <l> TOK_LANGTYPE

%token TOK_HASH TOK_COMMAND TOK_END
%token TOK_KEY_NUMBER TOK_KEY_PRIORITY TOK_KEY_NAME 
%token TOK_KEY_POSITION TOK_KEY_CODE TOK_KEY_LEVEL
%token TOK_KEY_SUBCMD TOK_KEY_LANGUAGE TOK_KEY_FLAGS
%token TOK_INVALID

%%

db
  : command TOK_HASH TOK_END
  | command db
  ;

command
  : TOK_HASH TOK_COMMAND { cmd_start(); } key_list TOK_END { cmd_done(); }
  ;

key_list
  : key
  | key key_list

key
  : TOK_KEY_NUMBER TOK_INT   { cmd_number($2); }
  | TOK_KEY_PRIORITY TOK_INT  { cmd_priority($2); }
  | TOK_KEY_NAME TOK_QUOTED_WORD { cmd_name($2); }
  | TOK_KEY_POSITION TOK_INT { cmd_position($2); }
  | TOK_KEY_CODE TOK_QUOTED_WORD { cmd_code($2); }
  | TOK_KEY_SUBCMD TOK_INT { cmd_subcmd($2); }
  | TOK_KEY_LEVEL TOK_LEVEL { cmd_level($2); }
  | TOK_KEY_LEVEL TOK_INT { cmd_level($2); }
  | TOK_KEY_LANGUAGE TOK_LANGTYPE { cmd_language($2); }
  | TOK_KEY_FLAGS TOK_INT { cmd_flags($2); }
  ;
%%

extern int cmdread_line_no;

void yyerror(char* s)
{
	log("SYSERR: Error parsing commands file: %d:%s", cmdread_line_no, s);
}
