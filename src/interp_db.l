/*
 * LEXER SPECIFICATION for Command Table Parser
 * $Id: interp_db.l,v 1.1.1.1 2004/03/07 16:14:16 root Exp $
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
 * Alternativeely, you may distribute the original contents of this library
 * code (interp_db.l) under the terms of the GNU Lesser General Public License,
 * as published by the Free Software Foundation, version 2 or (at your option),
 * any later version.
 *
 *  Please List any changes below:
 *    * Initial version 1.0
 */

%{
 #include "conf.h"
 #include "sysdep.h"
 #include "structs.h"

 #include "interp_db.tab.h"
 #define yyerror interp_dberror
 #define yylval  interp_dblval

 extern void yyerror(char* s);
 extern const char *script_languages[];

 int cmdread_line_no = 1;

 void error(char *s) {
    yy_fatal_error(s);
 }

 t_language get_language(const char* string)
 {
	int i;

	for(i = 0; *script_languages[i] != '\n'; i++)
	{
		if (!str_cmp(string, script_languages[i]))
			return (t_language)i;
	}
	return INVALID_LANG;
 }
%}

quot \"
newl \n
word_element [^ \r\n\v\t\"]

%%
"#"      { return TOK_HASH; }
"End"    { return TOK_END; }

\"{word_element}*\" { yylval.s = yytext; return TOK_QUOTED_WORD; }

"COMMAND" { return TOK_COMMAND;  }
"Number" { return TOK_KEY_NUMBER;  }
"Priority" { return TOK_KEY_PRIORITY;  }
"Name" { return TOK_KEY_NAME;  }
"Position" { return TOK_KEY_POSITION;  }
"Code" { return TOK_KEY_CODE;  }
"Level" { return TOK_KEY_LEVEL;  }
"Subcmd" { return TOK_KEY_SUBCMD;  }
"Flags" { return TOK_KEY_FLAGS; }
"Language" { return TOK_KEY_LANGUAGE; }
(-)?[0-9]+ { yylval.i = atoi(yytext); return TOK_INT; }
"LVL_IMMORT" { yylval.i = LVL_IMMORT; return TOK_LEVEL; }
"LVL_GOD" { yylval.i = LVL_GOD; return TOK_LEVEL; }
"LVL_GRGOD" { yylval.i = LVL_GRGOD; return TOK_LEVEL;  }
"LVL_IMPL" { yylval.i = LVL_IMPL; return TOK_LEVEL; }
"LVL_FREEZE" { yylval.i = LVL_FREEZE; return TOK_LEVEL;  }
"LVL_BUILDER" { yylval.i = LVL_BUILDER; return TOK_LEVEL;  }
"NATIVE" { yylval.l = NATIVE; return TOK_LANGTYPE; }
"PYTHON" { yylval.l = PYTHON; return TOK_LANGTYPE; }
\n { cmdread_line_no++; }
\t|" "|\v|\r  {}
.        { /*char buf[80];
            sprintf(buf, "%d: Invalid character (%s) in commands file", cmdread_line_no, yytext); 
            error(buf); */
            return TOK_INVALID;
         }
<<EOF>>  { cmdread_line_no = 1; yyterminate(); }
%%

int yywrap( ) { 
	return 1; 
}

