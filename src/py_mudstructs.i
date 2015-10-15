%module server

%{
#include "conf.h"
#include "sysdep.h"

#include "structs.h"
#include "handler.h"
#include "db.h"
#include "utils.h"
#include "interpreter.h"
#include "constants.h"
#include "spells.h"
#include "genscript.h"
#include "python_script.h"

#define true 1
#define false 0

#ifndef SWIG_NOINCLUDE
struct room_data room_deref(struct room_data* ptr) {return *ptr;}
struct descriptor_data descriptor_deref(struct descriptor_data* ptr) {return *ptr;}
struct char_data char_deref(struct char_data* ptr) {return *ptr;}

const char* class_abbreviate(int i) {return class_abbrevs[i];}
char  double_deref_doublechar(char** x, int y, int z) { return x[y][z]; }
char* deref_doublechar(char** x, int y) { return x[y]; }
char  deref_char(char* x, int y) { return x[y]; }
#endif

%}

struct char_data;
struct obj_data;
struct room_data;

%include "cpointer.i"
%include "structs.h"
%include "handler.h"
%include "utils.h"
%include "db.h"
%include "interpreter.h"
%include "constants.h"
%include "spells.h"
%include "genscript.h"
%include "python_script.h"

%pointer_class(char, charp);

#ifndef SWIG_NOINCLUDE
const char* class_abbreviate(int i) ;
char double_deref_doublechar(char** x, int y, int z) ;
char* deref_doublechar(char** x, int y) ;
char  deref_char(char* x, int y) ;

#endif
