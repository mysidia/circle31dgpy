/* A Bison parser, made by GNU Bison 1.875.  */

/* Skeleton parser for Yacc-like parsing with Bison,
   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002 Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 59 Temple Place - Suite 330,
   Boston, MA 02111-1307, USA.  */

/* As a special exception, when this file is copied by Bison into a
   Bison output file, you may use that output file without restriction.
   This special exception was added by the Free Software Foundation
   in version 1.24 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     TOK_INT = 258,
     TOK_LEVEL = 259,
     TOK_QUOTED_WORD = 260,
     TOK_LANGTYPE = 261,
     TOK_HASH = 262,
     TOK_COMMAND = 263,
     TOK_END = 264,
     TOK_KEY_NUMBER = 265,
     TOK_KEY_PRIORITY = 266,
     TOK_KEY_NAME = 267,
     TOK_KEY_POSITION = 268,
     TOK_KEY_CODE = 269,
     TOK_KEY_LEVEL = 270,
     TOK_KEY_SUBCMD = 271,
     TOK_KEY_LANGUAGE = 272,
     TOK_KEY_FLAGS = 273,
     TOK_INVALID = 274
   };
#endif
#define TOK_INT 258
#define TOK_LEVEL 259
#define TOK_QUOTED_WORD 260
#define TOK_LANGTYPE 261
#define TOK_HASH 262
#define TOK_COMMAND 263
#define TOK_END 264
#define TOK_KEY_NUMBER 265
#define TOK_KEY_PRIORITY 266
#define TOK_KEY_NAME 267
#define TOK_KEY_POSITION 268
#define TOK_KEY_CODE 269
#define TOK_KEY_LEVEL 270
#define TOK_KEY_SUBCMD 271
#define TOK_KEY_LANGUAGE 272
#define TOK_KEY_FLAGS 273
#define TOK_INVALID 274




#if ! defined (YYSTYPE) && ! defined (YYSTYPE_IS_DECLARED)
#line 102 "interp_db.y"
typedef union YYSTYPE {
        const char* s;
        int i;
	t_language l;
} YYSTYPE;
/* Line 1240 of yacc.c.  */
#line 80 "interp_db.tab.h"
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE interp_dblval;



