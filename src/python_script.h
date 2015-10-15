/**
 * Header file for Python scripting support
 *
 * Attribution Notice:
 *
 *    Copyright (c) 2004 ***REMOVED***
 *    All Rights Reserved
 *
 *    Licensed under the Academic Free License version 2.0
 *    See ../doc/afl-2.0.txt
 *
 */
#ifndef __python_script_h__
#define __python_script_h__

#define PYSCRIPTS_VERSION CIRCLEMUD_VERSION(0,0,1)
#define PYSCRIPTS_VERSION_STRING "Python scripts module, version 0.0.1"

#undef log
/*#ifdef HAVE_PYTHON2_3_PYTHON_H*/
#undef _POSIX_C_SOURCE
#include "Python.h"
#include "structmember.h"
/*#elif defined(HAVE_PYTHON2_2_PYTHON_H)
#include <python2.2/Python.h>
#include <python2.2/structmember.h>
#endif*/
#define log basic_mud_log

void py_pulse(int beat);
void shutdown_python();
void boot_python();

//////
// A structure for keeping track of registered python commands
//
struct py_command_info
{
	unsigned int hashcode, number;
	char *name;                 // Name of the command
	int minimum_position;       // etc..
	PyObject* py_callfun;
	void (*native_callfun)
		(struct char_data *ch, char* arg, char *text, int cmd, int subcmd);
	int minimum_level;
	int subcmd;
	int priority;
	int override;
	struct py_command_info* next;
};

typedef struct _py_MudModule {
        char* name;
        PyObject* obj;
        struct _py_MudModule* next;
} py_MudModule;

struct room_data room_deref(struct room_data* ptr);
struct descriptor_data descriptor_deref(struct descriptor_data* ptr);
struct char_data char_deref(struct char_data* ptr);
PyObject* py_Bottle_Char(struct char_data* ch);
PyObject* py_Bottle_Room_vnum(room_vnum vnum);
PyObject* py_Bottle_Exit(room_vnum from_room_vnum, int dir);
PyObject* py_Bottle_Obj(struct obj_data* obj);
PyObject *py_char_getname(PyObject *self, PyObject *args);

void python_obj_call(struct obj_data* obj, char* argument, const char*, int subcmd);
void python_wld_call(struct room_data* room, char* argument, const char*, int subcmd);
void python_mob_call(struct char_data* mob, char* argument, const char*, int subcmd);

extern const char *class_abbrevs[];
#endif
