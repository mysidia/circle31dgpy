/**
 * Python Scripting Interface
 *
 * Attribution Notice:
 *
 *    Copyright (c) 2003-2004 ***REMOVED***  <mysidia-pyci@darkfire.net>
 *    All Rights Reserved
 *
 *    Licensed under the Academic Free License version 2.0
 *    See ../doc/afl-2.0.txt
 *    And http://www.opensource.org/licenses/afl-2.0.php
 *
 *    Please List any changes below:
 *      * Initial version 1.0
 */
/*#include "conf.h"
#include "sysdep.h"

#include "structs.h"
#include "utils.h"
#include "db.h"
#include "comm.h"
#include "handler.h"
#include "spells.h"
#include "mail.h"
#include "interpreter.h"
#include "constants.h"
#include "screen.h"
#include "genscript.h"
*/

/* I need one of the wrappers so I can make Python wrapped  EventArgs  pointers*/
#include "py_mudstructs_wrap.c"

#include "screen.h"
#include "comm.h"


PyObject *SWIG_Python_NewPointerObj(void *, swig_type_info *,int own);

extern const struct command_info cmd_info[];
	

static int need_python_restart;
static PyObject* mud_module = NULL;
static PyObject* init_module = NULL;
static PyTypeObject* char_class_type = NULL;
struct char_data *find_char(long n);
extern PyTypeObject py_chType;
extern PyTypeObject py_roomType;
extern PyTypeObject py_exitType;
extern PyTypeObject py_objType;
void signal_setup();
static void unload_module(struct _py_MudModule* pym);
void list_one_char(struct char_data *i, struct char_data *ch);
void show_obj_to_char(struct obj_data *obj, struct char_data *ch, int mode);
extern struct obj_data* find_obj(long);
void check_insert_command(CMD_DATA* cmdp, t_language lang);

/*********************************************************************************/

#define WERR \
	if(PyErr_Occurred()){PyErr_Print(); PyErr_Clear();}
	
	

static py_MudModule* modules;

static void py_insert_module(const char* name, PyObject* mod)
{
	py_MudModule* ps = modules;

	for(; ps; ps = ps->next) {
		if (!str_cmp(ps->name, name)) {
			ps->obj = mod; /* Pointer already there, just adjust it */
			return;
		}
	}

	/* Create a new structure */
	{

	py_MudModule* pm = malloc(sizeof(py_MudModule));
	pm->next = NULL;

	pm->name = strdup(name);
	pm->obj = mod;
	if (modules)
		pm->next = modules;
	modules = pm;
	}
}


/*
 * A python class for a pointer to a character
 */
typedef struct {
    PyObject_HEAD
    PyObject* x_attr;
    int char_type;
    int char_id, idnum;
} py_Character;


/*
 * A class for a pointer to a room
 */
typedef struct {
    PyObject_HEAD
    room_vnum vnum;
} py_Room;


/*
 * Python Type for a pointer to an exit
 */
typedef struct {
	PyObject_HEAD
	room_vnum vnum;
	int dir;
} py_Exit;

/*
 * Python Type for exits
 */
typedef struct {
	PyObject_HEAD
	obj_vnum vnum;
	int id;
} py_Obj;

struct obj_data* py_objinfo(py_Obj *p);

/*********************************************************************************/


/*
 * Convert a python room ptr to a mud room pointer
 */
struct room_data* py_roominfo(py_Room *p)
{
	room_rnum rn = real_room(p->vnum);

	if (rn == NOWHERE)
		return NULL;
	return  &world[rn];
}


/* Convert an exit object to an exit pointer */
struct room_direction_data* py_exitinfo(py_Exit *p)
{
	room_rnum rn = real_room(p->vnum);

	if (rn == NOWHERE || p->dir >= NUM_OF_DIRS || p->dir < 0)
		return NULL;
	return (world[rn].dir_option[p->dir]);
}

/* Convert an obj object to an obj_data pointer */
struct obj_data* py_objinfo(py_Obj *p)
{
	room_rnum rn = real_object(p->vnum);
	struct obj_data* obj = find_obj(p->id);

	if (rn == NOWHERE)
		return NULL;
	return obj;
}


/*
 * Send a message to a character object (including \r\n)
 */
PyObject* 
py_send_to_char(PyObject *self, PyObject *args)
{
	char* message;
	py_Character* pch = (py_Character *)self;
	struct char_data *ch;
		

	if(!PyArg_ParseTuple(args, "s:message", &message))
		return NULL;

	ch = find_char(pch->char_id);

	if (ch == NULL)
		return NULL;
	if (ch->desc) 
		write_to_output(ch->desc, "%s\r\n", message);
	
	Py_INCREF(Py_None);
	return Py_None;
}

/*
 *  Same as py_send_to_char but no extra line end.
 */
PyObject*
py_write_to_char(PyObject *self, PyObject *args)
{
	char* message;
	py_Character* pch = (py_Character *)self;
	struct char_data *ch;

	if(!PyArg_ParseTuple(args, "s:message", &message))
		return NULL;

	ch = find_char(pch->char_id);

	if (ch == NULL)
		return NULL;
	if (ch->desc)
		write_to_output(ch->desc, "%s", message);

	Py_INCREF(Py_None);
	return Py_None;
}

/* Create an mud.Character object representing a char */
PyObject* 
py_Bottle_Char(struct char_data* ch)
{
	py_Character* pch = PyObject_New(py_Character,&py_chType);
	pch->x_attr = NULL;
	pch->char_id = GET_ID(ch);
	return (PyObject *)pch;
}

PyObject*
py_Bottle_Char_void(void *ch)
{
	return py_Bottle_Char((struct char_data *) ch);
}

/* Represent a room as a mud.Room */
PyObject*
py_Bottle_Room_vnum(room_vnum vnum)
{
	py_Room* proom = PyObject_New(py_Room, &py_roomType);
	proom->vnum = vnum;
	return (PyObject *)proom;
}

PyObject*
py_Bottle_Room_void(void *room)
{
	py_Room* proom = PyObject_New(py_Room, &py_roomType);

	proom->vnum = ((struct room_data *)room)->number;

	return (PyObject *)proom;
}


/* Represent an exit as a mud.Exit */
PyObject*
py_Bottle_Exit(room_vnum from_room_vnum, int dir)
{
	py_Exit* pex = PyObject_New(py_Exit, &py_exitType);
	pex->vnum = from_room_vnum;
	pex->dir = dir;
	return (PyObject *)pex;
}

/* Represent an obj as a mud.Obj */
PyObject*
py_Bottle_Obj(struct obj_data* obj)
{
	py_Obj* po = PyObject_New(py_Obj, &py_objType);
	po->vnum = GET_OBJ_VNUM(obj);
	po->id = GET_ID(obj);
	return (PyObject *)po;
}

PyObject*
py_Bottle_obj_void(void *obj)
{
	return py_Bottle_Obj((struct obj_data *) obj);
}


/*********************************************************************************/
static void python_gen_call(char* name, void* data, 
		PyObject *(* bottler)(void*),
		char* argument, const char* cmd, int subcmd)
{
	PyObject* object_command, *result, *params;

	if (init_module == NULL)
		return;

	object_command = PyObject_GetAttrString(init_module, name);

	if (object_command == NULL) {
		return;
	}
	
	if (!PyCallable_Check(object_command))
	{
		PyErr_SetString (PyExc_ValueError, "__main__.object_call not a function");
		PyErr_Print();

		return;		
	}

	params = Py_BuildValue("Ossi", bottler(data), argument, cmd, subcmd);
	if (params == NULL) {
		PyErr_Print();

		return;
	}

	result = PyObject_CallObject(object_command, params);

	Py_DECREF(params);
	if (result != NULL) {
		Py_DECREF(result);
	}
}

void python_obj_call(struct obj_data* obj, char* argument, const char* cmd, int subcmd)
{
	python_gen_call("object_call", obj, py_Bottle_obj_void, argument, cmd, subcmd );
}


void python_wld_call(struct room_data* room, char* argument, const char* cmd, int subcmd)
{
	python_gen_call("room_call", room, py_Bottle_Room_void, argument, cmd, subcmd );
}


void python_mob_call(struct char_data* mob, char* argument, const char* cmd, int subcmd)
{
	python_gen_call("mob_call", mob, py_Bottle_Char_void, argument, cmd, subcmd );
}


/*********************************************************************************/
	
/* Get character's name */
PyObject * 
py_char_getname(PyObject *self, PyObject *args)
{
	py_Character* pch = (py_Character *)self;
	struct char_data* ch = find_char(pch->char_id);

	if (ch == NULL)
		return NULL;
	return PyString_FromString(GET_NAME(ch)); /* New reference */
}

PyObject * 
py_char_getlevel(PyObject *self, PyObject *args)
{
        py_Character* pch = (py_Character *)self;
        struct char_data* ch = find_char(pch->char_id);

        if (ch == NULL)
                return NULL;
        return PyInt_FromLong(GET_LEVEL(ch)); /* New reference */
}

PyObject *
py_char_setlevel(PyObject *self, PyObject *args)
{
	py_Character* pch = (py_Character *)self;
	struct char_data* ch = find_char(pch->char_id);
	int l;

	if (ch == NULL || !PyArg_ParseTuple(args, "i:new_level", &l))
		return NULL;

	GET_LEVEL(ch) = l;

	Py_INCREF(Py_None);
	return Py_None;
}
	
/* Get a char's age in years */
PyObject * 
py_char_get_age(PyObject *self, PyObject *args)
{
	py_Character* pch = (py_Character *)self;
	struct char_data* ch = find_char(pch->char_id);

	if (ch == NULL)
		return NULL;
	return PyInt_FromLong(GET_AGE(ch)); /* New reference */
}

/* Is ch affected with given bits? */
PyObject * 
py_is_affected(PyObject *self, PyObject* args)
{
	py_Character* pch = (py_Character *)self;
	struct char_data* ch = find_char(pch->char_id);
	int l;

	if (ch == NULL)
		return NULL;
	if (!PyArg_ParseTuple(args, "i:affected_flags", &l))
		return NULL;
						
	return PyInt_FromLong(IS_AFFECTED(ch, l)); /* New reference */
}

/* Chan a given Character object see another Character object? */
PyObject * 
py_can_see(PyObject *self, PyObject* args)
{
	py_Character* pch = (py_Character *)self, *pvict;
	py_Obj* pobj;
	struct char_data* ch = find_char(pch->char_id);
	struct char_data* vict;
	PyObject* pogen;
	struct obj_data* obj;
	
	if (ch == NULL)
		return NULL;
	if (!PyArg_ParseTuple(args, "O:victim", &pogen))
		return NULL;

	if (PyObject_TypeCheck(pogen, &py_chType))
	{
		if (!PyArg_ParseTuple(args, "O!:character_victim", &py_chType, &pvict))
			return NULL;
		if ((vict = find_char(pvict->char_id)) == NULL)
			return NULL;
		return PyInt_FromLong(CAN_SEE(ch, vict) ? 1 : 0);
	}

	if (!PyArg_ParseTuple(args, "O!:object_victim", &py_objType, &pobj))
		return NULL;
	if ((obj  = find_obj(pobj->id)) == NULL)
		return NULL;
	return PyInt_FromLong(CAN_SEE_OBJ(ch, obj) ? 1 : 0);
}

PyObject * 
py_find_char_where(PyObject *self, PyObject* args, int x)
{
	py_Character* pch = (py_Character *)self;
	struct char_data* ch = find_char(pch->char_id), *vict;
	char* arg=0;

	 if (ch == NULL)
		 return NULL;
	 if (!PyArg_ParseTuple(args, "s:character_name", &arg))
		 return NULL;
	 
	if ((vict = get_char_vis(ch, arg, NULL, x)) == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}
	return py_Bottle_Char(vict);
}

PyObject * 
py_find_player_where(PyObject *self, PyObject* args, int x)
{
	py_Character* pch = (py_Character *)self;
	struct char_data* ch = find_char(pch->char_id), *vict;
	char* arg;

	 if (ch == NULL)
		 return NULL;
	 if (!PyArg_ParseTuple(args, "s:character_name", &arg))
		 return NULL;
	 
	if ((vict = get_player_vis(ch, arg, NULL, x)) == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}
	return py_Bottle_Char(vict);
}

PyObject * 
py_find_char(PyObject *self, PyObject* args)
{
	return py_find_char_where(self, args, FIND_CHAR_ROOM);
}

PyObject * 
py_find_player(PyObject *self, PyObject* args)
{
	return py_find_player_where(self, args, FIND_CHAR_ROOM);
}

PyObject * 
py_find_char_world(PyObject *self, PyObject* args)
{
	return py_find_char_where(self, args, FIND_CHAR_WORLD);
}

PyObject * 
py_find_player_world(PyObject *self, PyObject* args)
{
	return py_find_player_where(self, args, FIND_CHAR_WORLD);
}

PyObject * 
py_mob_flagged(PyObject *self, PyObject* args)
{
	py_Character* pch = (py_Character *)self;
	struct char_data* ch = find_char(pch->char_id);
	int l;

	if (ch == NULL)
		    return NULL;
	if (!PyArg_ParseTuple(args, "i:mob_flag", &l))
		    return NULL;

	return PyInt_FromLong(IS_NPC(ch) && MOB_FLAGGED(ch, l));
}

PyObject *
py_plr_flagged(PyObject *self, PyObject* args)
{
	py_Character* pch = (py_Character *)self;
	struct char_data* ch = find_char(pch->char_id);
	int l;

	if (ch == NULL)
		    return NULL;
	if (!PyArg_ParseTuple(args, "i:player_flags", &l))
		    return NULL;

	return PyInt_FromLong(!IS_NPC(ch) && PLR_FLAGGED(ch, l));

}

PyObject *
py_prf_flagged(PyObject *self, PyObject* args)
{
	py_Character* pch = (py_Character *)self;
	struct char_data* ch = find_char(pch->char_id);
	int l;

	if (ch == NULL)
		    return NULL;
	if (!PyArg_ParseTuple(args, "i:prf_flags", &l))
		    return NULL;

	if (IS_NPC(ch) && ch->desc && ch->desc->original && !IS_NPC(ch->desc->original)) {
		ch = ch->desc->original;
	}

	return PyInt_FromLong(IS_NPC(ch) ? 0 : PRF_FLAGGED(ch, l));
}

PyObject *
py_list_one_obj(PyObject *self, PyObject* args)
{
	py_Character* pch = (py_Character *)self;
	py_Obj* pobj;
	struct char_data* ch = find_char(pch->char_id);
	struct obj_data* obj;
	int mode;
	
	if (!args || !ch)
		return NULL;
	 if (!PyArg_ParseTuple(args, "O!i:prf_flags", &py_objType, &pobj, &mode))
		return NULL;
	 obj = py_objinfo(pobj);
	 if (!obj)
		 return NULL;
	 show_obj_to_char(obj, ch, mode);

	 Py_INCREF(Py_None);
	 return Py_None;
}

PyObject *
py_list_one_char(PyObject *self, PyObject* args)
	
{
	py_Character* pch = (py_Character *)self, *pvict;
	struct char_data* ch = find_char(pch->char_id);
	struct char_data* vict;

	if (ch == NULL)
		return NULL;
	if (!PyArg_ParseTuple(args, "O!:character_victim", &py_chType, &pvict))
		return NULL;
	if ((vict = find_char(pvict->char_id)) == NULL)
		return NULL;

	list_one_char(vict, ch);

	Py_INCREF(Py_None);
	return Py_None;
							
}
	

PyObject * 
py_col_code(PyObject *self, PyObject* args, char* code)
{
	py_Character* pch = (py_Character *)self;
	struct char_data* ch = find_char(pch->char_id);
	int l=NRM;

	if (ch == NULL)
		    return NULL;
	if (!PyArg_ParseTuple(args, "|i:color_type", &l))
		    return NULL;
	
	if (COLOR_LEV(ch) < l)
		code = "";

	return PyString_FromString(code);

}

PyObject * 
py_col_normal(PyObject *self, PyObject* args) { return py_col_code(self, args, KNRM); }

PyObject * 
py_col_red(PyObject *self, PyObject* args) { return py_col_code(self, args, KRED); }

PyObject * 
py_col_green(PyObject *self, PyObject* args) { return py_col_code(self, args, KGRN); }

PyObject * 
py_col_yellow(PyObject *self, PyObject* args) { return py_col_code(self, args, KYEL); }

PyObject * 
py_col_blue(PyObject *self, PyObject* args) { return py_col_code(self, args, KBLU); }

PyObject * 
py_col_cyan(PyObject *self, PyObject* args) { return py_col_code(self, args, KCYN); }

PyObject * 
py_col_white(PyObject *self, PyObject* args) { return py_col_code(self, args, KWHT); }

PyObject * 
py_col_magenta(PyObject *self, PyObject* args) { return py_col_code(self, args, KMAG); }

PyObject *
py_affected_by_spell(PyObject *self, PyObject* args)
{
	py_Character* pch = (py_Character *)self;
	struct char_data* ch = find_char(pch->char_id);
	int spellnum;
	
	if (ch == NULL)
		return NULL;	
	if (!PyArg_ParseTuple(args, "i:spell_num", &spellnum))
		return NULL;
	return PyInt_FromLong(affected_by_spell(ch,spellnum) ? 1 : 0);
}

PyObject *
py_affect_from_char(PyObject *self, PyObject* args)
{
	py_Character* pch = (py_Character *)self;
	struct char_data* ch = find_char(pch->char_id);
	int spellnum;

	if (ch == NULL)
		return NULL;
	if (!PyArg_ParseTuple(args, "i:affect_num", &spellnum))
		return NULL;
	affect_from_char(ch,spellnum);

	Py_INCREF(Py_None);
	return Py_None;
}

/*********************************************************************************/

static PyMethodDef Obj_methods[] = {
	        {NULL}
};

static PyMethodDef Exit_methods[] = {
	        {NULL}
};


static PyMethodDef Room_methods[] = {
	{NULL}
};


static PyMethodDef Char_methods[] = {
        {"send",        py_send_to_char,        METH_VARARGS,
	                PyDoc_STR("send a line of text to the character plus the CR-LF")},
        {"writeln",     py_send_to_char,        METH_VARARGS,
		        PyDoc_STR("send a line of text to the character plus the CR-LF")},
	{"write",        py_write_to_char,        METH_VARARGS,
			PyDoc_STR("send some text to the character")},
	{"get_name",	py_char_getname,	METH_VARARGS,
			PyDoc_STR("get the name of the payer")},
	{"get_level",   py_char_getlevel,       METH_VARARGS,
			PyDoc_STR("get the level of the player")},
	{"set_level",	py_char_setlevel,	METH_VARARGS,
			PyDoc_STR("set the level of the player")},
	{"get_age",     py_char_get_age,       METH_VARARGS,
			PyDoc_STR("get the age in years")},
	{"is_affected", py_is_affected,		METH_VARARGS,
			PyDoc_STR("is char affected by effect XXX?")},
        {"mob_flagged", py_mob_flagged,         METH_VARARGS,
                        PyDoc_STR("does mob have flag XXX?")},
        {"plr_flagged", py_plr_flagged,         METH_VARARGS,
                        PyDoc_STR("does player have flag XXX?")},
        {"prf_flagged", py_prf_flagged,         METH_VARARGS,
                        PyDoc_STR("does player have pref flag XXX?")},
	{"list_one_char", py_list_one_char,	METH_VARARGS,
			PyDoc_STR("list one char to another")},
	{"list_one_obj", py_list_one_obj,	METH_VARARGS,
			PyDoc_STR("list one object to a character")},
	{"can_see",	py_can_see,		METH_VARARGS,
			PyDoc_STR("can char see the given char?")},
        {"find_char",   py_find_char,             METH_VARARGS,
                        PyDoc_STR("ch looks for a char in the current room")},
        {"find_player", py_find_player,             METH_VARARGS,
                        PyDoc_STR("ch looks for a polayer in the current room")},
	{"find_char_world",   py_find_char_world,   METH_VARARGS,
			PyDoc_STR("ch looks for a char anywhere")},
	{"find_player_world",   py_find_player_world,  METH_VARARGS,
			PyDoc_STR("ch looks for a player anywhere")},
	{"affected_by_spell",  py_affected_by_spell,  METH_VARARGS,
			PyDoc_STR("char affected by given spell?")},
	{"affect_from_char",  py_affect_from_char,  METH_VARARGS,
			PyDoc_STR("char affected by given spell?")},		
	{"nrm",		py_col_normal,                    METH_VARARGS,
		        PyDoc_STR("generate format for color red")},
        {"red",         py_col_red,                    METH_VARARGS,
                        PyDoc_STR("generate format for color red")},
        {"grn",          py_col_green,                   METH_VARARGS,
                        PyDoc_STR("generate format for color green")},
        {"yel",         py_col_yellow,                    METH_VARARGS,
                        PyDoc_STR("generate format for color yellow")},
        {"blu",         py_col_blue,                    METH_VARARGS,
                        PyDoc_STR("generate format for color blue")},
        {"mag",         py_col_magenta,                  METH_VARARGS,
                        PyDoc_STR("generate format for color magenta")},
        {"cyn",         py_col_cyan,                    METH_VARARGS,
                        PyDoc_STR("generate format for color cyan")},
        {"wht",         py_col_white,                    METH_VARARGS,
                        PyDoc_STR("generate format for color white")},	
	{NULL}
};

static PyMemberDef Char_members[] = {
        {NULL}	
};

static PyMemberDef Room_members[] = {
        {NULL}	
};

static PyMemberDef Exit_members[] = {
	{NULL}
};

static PyMemberDef Obj_members[] = {
	{NULL}
};

/*********************************************************************************/
	
/* For now, no making new instances of these things. */

static void
py_Char_dealloc(py_Character* self)
{
		/*Py_XDECREF(self->q);
		 * * self->ob_type->tp_free((PyObject*)self);*/
}

static void
py_Room_dealloc(py_Room* self) {}

static void
py_Exit_dealloc(py_Room* self) { }

static void
py_Obj_dealloc(py_Room* self) { }


static int
py_Char_init(py_Character *self, PyObject *args, PyObject *kwds)
{
	return -1;
}

static int
py_Room_init(py_Room *self, PyObject *args, PyObject *kwds)
{
	return -1;
}

static int
py_Exit_init(py_Room* self, PyObject *args, PyObject* kwds)
{
	return -1;
}

static int
py_Obj_init(py_Room* self, PyObject *args, PyObject* kwds)
{
	return -1;
}


static PyObject*
py_Char_new(PyTypeObject* type, PyObject *args, PyObject *kwds)
{
	py_Character* self;

	return NULL; 
	
	/* NOTREACHED */
		
	self = (py_Character *)type->tp_alloc(type, 0);

	return (PyObject *) self;
}

static PyObject*
py_Exit_new(PyTypeObject* type, PyObject *args, PyObject *kwds)
{
	py_Exit* self;
	return NULL;
	
	/* NOTREACHED */
	
	self = (py_Exit *)type->tp_alloc(type, 0);
	return (PyObject *)self;
}

static PyObject*
py_Obj_new(PyTypeObject* type, PyObject *args, PyObject *kwds)
{
	py_Obj* self;
	return NULL;

	/* NOTREACHED */
	
	self = (py_Obj *)type->tp_alloc(type, 0);
	return (PyObject *)self;
}

static PyObject*
py_Room_new(PyTypeObject* type, PyObject *args, PyObject *kwds)
{
	py_Room* self;
	return NULL;

	/* NOTREACHED */
		
	self = (py_Room *)type->tp_alloc(type, 0);
	return (PyObject *) self;
}

/*********************************************************************/
/* Attribute Implementations */

static PyObject*
py_Obj_getattr(py_Obj *self, char *name)
{
	struct obj_data* obj;
	
	if (self == NULL || name == NULL)
		return NULL;

	obj = py_objinfo(self);
	if (!obj)
		return NULL;

	/* Vnums*/
	if (!strcmp(name, "vnum")) { return PyInt_FromLong(obj->item_number); }

	/* Return a bottled room pointer */
	if (!strcmp(name, "in_room")) { 
	       if (IN_ROOM(obj) != NOWHERE)
	       	       return py_Bottle_Room_vnum(IN_ROOM(obj));
       		else {
			Py_INCREF(Py_None);
			
			return Py_None;
		}
	}

	/* Object name */
	if (!strcmp(name, "name")) { 
		if (!obj->name || !*obj->name) {
			Py_INCREF(Py_None);
			
			return Py_None;
		}
		return PyString_FromString(obj->name); 
	}

	/* Description */
	if (!strcmp(name, "description")) { 
		if (!obj->description) {
			Py_INCREF(Py_None);
			
			return Py_None;
		}
		return PyString_FromString(obj->description); 
	}

	/* Short D */
	if (!strcmp(name, "short_description")) { 
		if (!obj->short_description) {
			Py_INCREF(Py_None);
			
			return Py_None;
		}
		return PyString_FromString(obj->short_description); 
	}
	
	/* Action D */
	if (!strcmp(name, "action_description")) {
		if (!obj->action_description) {
			Py_INCREF(Py_None);

			return Py_None;
		}
		return PyString_FromString(obj->action_description);
			
	}

	/* Carried By */
	if (!strcmp(name, "carried_by")) {
		if (!obj->carried_by) {
			Py_INCREF(Py_None);
			
			return Py_None;
		}
		return py_Bottle_Char(obj->carried_by);
	}

	if (!strcmp(name, "worn_by")) {
		if (!obj->worn_by) {
			Py_INCREF(Py_None);
			
			return Py_None;
		}
		return py_Bottle_Char(obj->worn_by);
	}

	if (!strcmp(name, "in_obj")) {
		if (!obj->in_obj) {
			Py_INCREF(Py_None);
			
			return Py_None;
		}
		return py_Bottle_Obj(obj->in_obj);
	}

	if (!strcmp(name, "contains")) {
		PyObject* list = PyList_New(0);
		struct obj_data* so = obj->contains;

		if (!obj->contains) {
			Py_INCREF(Py_None);

			return Py_None;
		}
		
		if (!list) {
			return NULL;
		}
		for(; so; so = so->next_content) {
			if ( PyList_Append(list, py_Bottle_Obj(so)) < 0) {
				log("SYSERR: XXX: Leaking memory, fix later");

				return NULL;
			}
		}
		return list;
	}
	
	if (!strcmp(name, "id")) { return PyInt_FromLong(obj->id); }
	if (!strcmp(name, "worn_on")) { return PyInt_FromLong(obj->worn_on); }
	if (!strcmp(name, "type")) { return PyInt_FromLong(obj->obj_flags.type_flag); }
	if (!strcmp(name, "level")) { return PyInt_FromLong(obj->obj_flags.level); }
	if (!strcmp(name, "wear")) { return PyInt_FromLong(obj->obj_flags.wear_flags); }
	if (!strcmp(name, "extra_flags")) { return PyInt_FromLong(obj->obj_flags.extra_flags); }
	if (!strcmp(name, "weight")) { return PyInt_FromLong(obj->obj_flags.weight); }
	if (!strcmp(name, "cost")) { return PyInt_FromLong(obj->obj_flags.cost); }
	if (!strcmp(name, "cost_per_day")) { return PyInt_FromLong(obj->obj_flags.cost_per_day); }
	if (!strcmp(name, "timer")) { return PyInt_FromLong(obj->obj_flags.timer); }
	if (!strcmp(name, "bitvector")) { return PyInt_FromLong(obj->obj_flags.bitvector); }
	if (!strcmp(name, "value")) { 
		PyObject* list = PyList_New( 0 );
		int i;
		
		if (!list)
			return NULL;
		for(i = 0; i < NUM_OBJ_VAL_POSITIONS; i++)
			if (PyList_Append(list, PyInt_FromLong(obj->obj_flags.value[i])) < 0)
			{
				log("SYSERR: XXX: leaking memory, fix later");
				return NULL;
			}
		return list;
	}

	if (!strcmp(name, "affected")) {
		PyObject* list = PyList_New(0);
		int i;

		if (!list)
			return NULL;
		for(i = 0; i < MAX_OBJ_AFFECT; i++) {
			if (obj->affected[i].location == APPLY_NONE)
				continue;
			{
				PyObject* dict = PyDict_New();
				if (!dict)
					return NULL;
				PyDict_SetItemString(dict, "location", 
						PyInt_FromLong(obj->affected[i].location));
				PyDict_SetItemString(dict, "modifier",
						PyInt_FromLong(obj->affected[i].modifier));
				if (PyList_Append(list, dict) < 0) {
					log("SYSERR: XXX: leaking memory, fix later");
					return NULL;
				}
			}
		}
		
		return list;
	}

	return Py_FindMethod(Obj_methods, (PyObject *)self, name);
}

static PyObject*
py_Exit_getattr(py_Exit *self, char *name)
{
	struct room_direction_data* exit;

	
	if (self == NULL || name == NULL)
		return NULL;

	exit = py_exitinfo(self);
	if (exit == NULL)
		return NULL;

	
	if (!strcmp(name, "description")) {
		return PyString_FromString(exit->general_description);
	}
	if (!strcmp(name, "keyword")) {
		return PyString_FromString(exit->keyword);
	}
	if (!strcmp(name, "key")) {
		return PyInt_FromLong(exit->key);
	}
	if (!strcmp(name, "to_room")) {
		if (exit->to_room != NOWHERE)
			return py_Bottle_Room_vnum(GET_ROOM_VNUM(exit->to_room));
		else
		{
			Py_INCREF(Py_None);

			return Py_None;
		}
	}
	if (!strcmp(name, "exit_info") || !strcmp(name, "flags")) {
		return PyInt_FromLong(exit->exit_info);
	}
	return Py_FindMethod(Char_methods, (PyObject *)self, name);
}
	

static PyObject*
py_Room_getattr(py_Room *self, char *name)
{
	struct room_data* room = py_roominfo(self);

	if (room == NULL)
		return NULL;
	if (!strcmp(name, "vnum")) {
		return PyInt_FromLong(room->number);
	}
	
	if (!strcmp(name, "name")) {
		return PyString_FromString(room->name);
	}

        if (!strcmp(name, "people")) {
                PyObject* list = PyList_New( 0 );
                struct char_data* ch;

		if (!room->people) {
			Py_INCREF(Py_None);

			return Py_None;
		}

                if (!list)
                        return NULL;
                for(ch = room->people; ch; ch = ch->next_in_room) {
			if (PyList_Append(list, py_Bottle_Char(ch)) < 0) {
				log("SYSERR: XXX: leaking memory, fix later");

				return NULL;
			}
				
		}
		return list;
        }

	if (!strcmp(name, "contents")) {
		if (!room->contents) {
			Py_INCREF(Py_None);
			
			return Py_None;
		}

		{
			PyObject* list = PyList_New(0);
			struct obj_data* so = room->contents;
			if (!list) {
				return NULL;
			}
			for(; so; so = so->next_content) {
				if (PyList_Append(list, py_Bottle_Obj(so)) < 0)
				{
					log("SYSERR: XXX: leaking memory, fix later");
					return NULL;
				}
			}
			return list;
		}	
		return NULL;
	}


	if (!strcmp(name, "zone_num")) {
		if (room->zone != NOWHERE)
			return PyInt_FromLong(zone_table[room->zone].number);
		return PyInt_FromLong(-1);
	}

	if (!strcmp(name, "sector")) {
		return PyInt_FromLong(room->sector_type);
	}

	if (!strcmp(name, "description")) {
		return PyString_FromString(room->description);
	}

	if (!strcmp(name, "flags")) {
		return PyInt_FromLong(room->room_flags);
	}

	if (!strcmp(name, "light")) {
		return PyInt_FromLong(room->light);
	}

	if (!strcmp(name, "dirs")) {
		PyObject* l = PyList_New(NUM_OF_DIRS);
		int i;
		
		if (!l)
			return NULL;

		for(i = 0; i < NUM_OF_DIRS; i++)
		{
			if (room->dir_option[i] && room->dir_option[i]->to_room != NOWHERE)
			{
				if (PyList_Append(l, py_Bottle_Room_vnum(room->dir_option[i]->to_room)) < 0)
				{
					return NULL; /* XXX: memory leak, fix later */
				}
			}
			else
			{
				Py_INCREF(Py_None);
				
				if (PyList_Append(l, Py_None) < 0)
				{
					Py_DECREF(Py_None);

					return NULL; /* XXX: memory leak, fix later */
				}
			}
			
		}
		return l;
	}

	if (!strcmp(name, "exits")) {
		PyObject* l = PyDict_New();
		int i;

		if (!l)
			return NULL;
		
		for(i = 0; i < NUM_OF_DIRS; i++)
		{
			if (room->dir_option[i] == NULL || room->dir_option[i]->to_room == NOWHERE)
				continue;
			if (PyDict_SetItemString(l, dirs[i], py_Bottle_Exit(room->number ,i)) < 0)
			{
				continue;
			}
		}
		return l;
	}

	
	return Py_FindMethod(Char_methods, (PyObject *)self, name);
}

int
py_Exit_setattr(py_Room *self, char* name, PyObject* new_value)
{
	return 1;
}


int
py_Obj_setattr(py_Obj *self, char* name, PyObject* new_value)
{
	struct obj_data *obj = py_objinfo(self);

	if (obj == NULL || name == NULL || new_value == NULL)
		return 1;
	/* Return 0 on success */

	return 1;
}

int
py_Room_setattr(py_Room *self, char* name, PyObject* new_value)
{
	struct room_data *room = py_roominfo(self);

	if (room == NULL || name == NULL || new_value == NULL)
		return 1;
	/* Return 0 on success */

	return 1;
}

static PyObject*
py_Char_getattr(py_Character *self, char *name)
{
	struct char_data* ch = find_char(self->char_id);

	if (!strcmp(name, "isvalid")) {
		if (ch == NULL) 
			return PyInt_FromLong(0);
		return PyInt_FromLong(1);
	}

	if (ch == NULL)
		return NULL;

	if (!strcmp(name, "isnpc")) 
		return PyInt_FromLong(IS_NPC(ch) ? 1 : 0);

	if (!strcmp(name, "vnum") && IS_NPC(ch)) {
		return PyInt_FromLong(GET_MOB_VNUM(ch));		
	}

	if (!strcmp(name, "ispc"))
		return PyInt_FromLong(IS_NPC(ch) ? 0 : 1);

	if (!strcmp(name, "isimm"))
		return PyInt_FromLong(GET_REAL_LEVEL(ch) >= LVL_IMMORT ? 0 : 1);
		
	if (!strcmp(name, "fighting")) {
		if (FIGHTING(ch)) {
			return py_Bottle_Char(FIGHTING(ch));
		}
		Py_INCREF(Py_None);

		return Py_None;
	}

	if (!strcmp(name, "in_room")) {
		if (IN_ROOM(ch) == NOWHERE) {
			Py_INCREF(Py_None);

			return Py_None;
		}
		return py_Bottle_Room_vnum(GET_ROOM_VNUM(IN_ROOM(ch)));
	}

	if (!strcmp(name, "in_room_num")) {
		if (IN_ROOM(ch) == NOWHERE)
			return PyInt_FromLong(-1);
		return PyInt_FromLong(GET_ROOM_VNUM(IN_ROOM(ch)));
	}

	if (!strcmp(name, "was_in_room_num")) {
		if (GET_WAS_IN(ch) == NOWHERE)
			return PyInt_FromLong(-1);
		return PyInt_FromLong(GET_ROOM_VNUM(GET_WAS_IN(ch)));
	}

	if (!strcmp(name, "age")) {
		PyObject* age_dict = PyDict_New();
                if(age_dict == NULL){
			return NULL;
		}

		if (PyDict_SetItem(age_dict, PyString_FromString("hours"), 
				PyInt_FromLong(age(ch)->hours)) < 0)
		{
			Py_XDECREF(age_dict);
			
			return NULL;
		}
		
		if (PyDict_SetItem(age_dict, PyString_FromString("day"), 
				PyInt_FromLong(age(ch)->day)) < 0)
		{
			Py_XDECREF(age_dict);
			
			return NULL;
		}
		
		if (PyDict_SetItem(age_dict, PyString_FromString("month"), 
				PyInt_FromLong(age(ch)->month)) < 0)
		{
			Py_XDECREF(age_dict);
			
			return NULL;
		}
		
		if (PyDict_SetItem(age_dict, PyString_FromString("year"), 
				PyInt_FromLong(age(ch)->year)) < 0)
		{
			Py_XDECREF(age_dict);
			
			return NULL;
		}

		return age_dict;
	}
	
#define _C(x,y) if (!strcmp(name, #x)) { return PyInt_FromLong(y(ch)); }
#define _C_RW(x,y) _C(x,y)
#define _CS(x,y) if (!strcmp(name, #x)) { return PyString_FromString(y(ch)); }	
#include "pycattr.h"
#undef _C
#undef _C_RW
#undef _CS
		
	if (self->x_attr != NULL) {	
		PyObject *v = PyDict_GetItemString(self->x_attr, name);

		if (v != NULL) {
			Py_INCREF(v);

			return v;
		}
	}
	return Py_FindMethod(Char_methods, (PyObject *)self, name);	
}

int
py_Char_setattr(py_Character *self, char* name, PyObject* new_value)
{
	struct char_data *ch = find_char(self->char_id);
	int l;
	room_rnum rn;

	if (ch == NULL || name == NULL || new_value == NULL)
		return 1;

        if (!strcmp(name, "was_in_room_num")) {
		if (!PyInt_Check(new_value))
			return 1;
		l = PyInt_AsLong(new_value);
		if ((rn = real_room(l)) == NOWHERE)
			return 1;
		
		GET_WAS_IN(ch) = GET_ROOM_VNUM(rn);
		return 0;
	}
	
#define _C(x,y)
#define _C_RW(x,y) if (!strcmp(name, #x)) { \
		if (!PyInt_Check(new_value)) \
		        return 1; \
			\
       		y(ch) = PyInt_AsLong(new_value);  \
		return 0; \
			}
#define _CS(x,y)
#include "pycattr.h"
#undef _C
#undef _C_RW
#undef _CS
	
	return 1;
}

static int
py_Exit_cmp(py_Exit* c1, py_Exit* c2)
{
	if (c1->vnum == c2->vnum && c1->dir == c2->dir)
		return 0;
	return -1;
}

static int
py_Obj_cmp(py_Obj* c1, py_Obj* c2)
{
	if (GET_ID(c1) == GET_ID(c2))
		return 0;
	return -1;
}

static int
py_Char_cmp(py_Character* c1, py_Character* c2)
{
	if (c1->char_id == c2->char_id)
		return 0;
	return -1;
}

static int
py_Room_cmp(py_Room* c1, py_Room* c2)
{
	if (c1->vnum == c2->vnum)
		return 0;
	return -1;
}

/*********************************************************************************/

/* Character type */
PyTypeObject py_objType = {
	PyObject_HEAD_INIT(NULL)
	0,                         /*ob_size*/
	"mud.Object",           /*tp_name*/
	sizeof(py_Obj),      /*tp_basicsize*/
	0,                         /*tp_itemsize*/
	
	/* METHODS */
	(destructor)py_Obj_dealloc, /*tp_dealloc*/
	0,                         /*tp_print*/
	(getattrfunc)py_Obj_getattr, /*tp_getattr*/
	(setattrfunc)py_Obj_setattr,/*tp_setattr*/
	(cmpfunc)py_Obj_cmp,       /*tp_compare*/
	0,                         /*tp_repr*/
	0,                         /*tp_as_number*/
	0,                         /*tp_as_sequence*/
	0,                         /*tp_as_mapping*/
	0,                         /*tp_hash */
	0,                         /*tp_call*/
	0,                         /*tp_str*/
	0,                         /*tp_getattro*/
	0,                         /*tp_setattro*/
	0,                         /*tp_as_buffer*/
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,        /*tp_flags*/
	"Mud Object Object",    /* tp_doc */
	/* BASETYPE */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    Obj_methods,             /* tp_methods */
    Obj_members,             /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)py_Obj_init,    /* tp_init */
    0,                         /* tp_alloc */
    py_Obj_new,               /* tp_new */
    0,				/* free */
    0 /* tp_is_gc? */
};


/* Character type */
PyTypeObject py_chType = {
	PyObject_HEAD_INIT(NULL)
	0,                         /*ob_size*/
	"mud.Character",           /*tp_name*/
	sizeof(py_Character),      /*tp_basicsize*/
	0,                         /*tp_itemsize*/
	
	/* METHODS */
	(destructor)py_Char_dealloc, /*tp_dealloc*/
	0,                         /*tp_print*/
	(getattrfunc)py_Char_getattr, /*tp_getattr*/
	(setattrfunc)py_Char_setattr,/*tp_setattr*/
	(cmpfunc)py_Char_cmp,       /*tp_compare*/
	0,                         /*tp_repr*/
	0,                         /*tp_as_number*/
	0,                         /*tp_as_sequence*/
	0,                         /*tp_as_mapping*/
	0,                         /*tp_hash */
	0,                         /*tp_call*/
	0,                         /*tp_str*/
	0,                         /*tp_getattro*/
	0,                         /*tp_setattro*/
	0,                         /*tp_as_buffer*/
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,        /*tp_flags*/
	"Mud Character Object",    /* tp_doc */
	/* BASETYPE */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    Char_methods,             /* tp_methods */
    Char_members,             /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)py_Char_init,    /* tp_init */
    0,                         /* tp_alloc */
    py_Char_new,               /* tp_new */
    0,				/* free */
    0 /* tp_is_gc? */
};


PyTypeObject py_roomType = {
	PyObject_HEAD_INIT(NULL)
	0,                         /*ob_size*/
	"mud.Room",           /*tp_name*/
	sizeof(py_Room),      /*tp_basicsize*/
	0,                         /*tp_itemsize*/
	
	/* METHODS */
	(destructor)py_Room_dealloc, /*tp_dealloc*/
	0,                         /*tp_print*/
	(getattrfunc)py_Room_getattr, /*tp_getattr*/
	(setattrfunc)py_Room_setattr,/*tp_setattr*/
	(cmpfunc)py_Room_cmp,       /*tp_compare*/
	0,                         /*tp_repr*/
	0,                         /*tp_as_number*/
	0,                         /*tp_as_sequence*/
	0,                         /*tp_as_mapping*/
	0,                         /*tp_hash */
	0,                         /*tp_call*/
	0,                         /*tp_str*/
	0,                         /*tp_getattro*/
	0,                         /*tp_setattro*/
	0,                         /*tp_as_buffer*/
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,        /*tp_flags*/
	"Mud Room Object",    /* tp_doc */
	/* BASETYPE */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    Room_methods,             /* tp_methods */
    Room_members,             /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)py_Room_init,    /* tp_init */
    0,                         /* tp_alloc */
    py_Room_new,               /* tp_new */
    0,				/* free */
    0 /* tp_is_gc? */
};

/********************/
PyTypeObject py_exitType = {
        PyObject_HEAD_INIT(NULL)
        0,                         /*ob_size*/
        "mud.Exit",           /*tp_name*/
        sizeof(py_Exit),      /*tp_basicsize*/
        0,                         /*tp_itemsize*/

        /* METHODS */
        (destructor)py_Exit_dealloc, /*tp_dealloc*/
        0,                         /*tp_print*/
        (getattrfunc)py_Exit_getattr, /*tp_getattr*/
        (setattrfunc)py_Exit_setattr,/*tp_setattr*/
        (cmpfunc)py_Exit_cmp,       /*tp_compare*/
        0,                         /*tp_repr*/
        0,                         /*tp_as_number*/
        0,                         /*tp_as_sequence*/
        0,                         /*tp_as_mapping*/
        0,                         /*tp_hash */
        0,                         /*tp_call*/
        0,                         /*tp_str*/
        0,                         /*tp_getattro*/
        0,                         /*tp_setattro*/
        0,                         /*tp_as_buffer*/
        Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,        /*tp_flags*/
        "Mud Exit Object",    /* tp_doc */
        /* BASETYPE */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    Exit_methods,             /* tp_methods */
    Exit_members,             /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)py_Exit_init,    /* tp_init */
    0,                         /* tp_alloc */
    py_Exit_new,               /* tp_new */
    0,                          /* free */
    0 /* tp_is_gc? */
};

/*********************************************************************************/


void initObjType(PyObject* module)
{
	py_objType.tp_new = PyType_GenericNew;
	if (PyType_Ready(&py_objType) < 0)
		abort();
	Py_INCREF(&py_objType);

	PyModule_AddObject(module, "Object", (PyObject *)(&py_objType));
}

void initExitType(PyObject* module)
{
	py_exitType.tp_new = PyType_GenericNew;
	if (PyType_Ready(&py_exitType) < 0)
		abort();
	Py_INCREF(&py_exitType);
	PyModule_AddObject(module, "Exit", (PyObject *)&py_exitType);
}

void initCharType(PyObject* module)
{
	py_chType.tp_new = PyType_GenericNew;
	if (PyType_Ready(&py_chType) < 0)
		abort();
	Py_INCREF(&py_chType);
	PyModule_AddObject(module, "Character", (PyObject *)&py_chType);
	char_class_type = &py_chType;
}

void initRoomType(PyObject* module)
{
	py_chType.tp_new = PyType_GenericNew;
	if (PyType_Ready(&py_roomType) < 0)
		abort();
	Py_INCREF(&py_roomType);
	PyModule_AddObject(module, "Room", (PyObject *)&py_roomType);
}


/*********************************************************************************/

/* Clear the python command table */
static void py_clear_commands()
{
	clear_commands(PYTHON);
}

extern void deregister_command_predicate(bool (* dereg_predicate)(CMD_DATA *, void*), void *data,
 t_language lang);

extern bool cmdfunc_is_pyfunc(CMD_DATA* cmdFunc, void* pyFunc)
{
	return (cmdFunc->py_callfun == pyFunc) ? 1 : 0;
}


static PyObject*
py_deregister_command(PyObject *self, PyObject *args)
{
	PyObject* cmd_obj = 0;
	char* cmd = 0;

	if (!PyArg_ParseTuple(args, "O:command", &cmd_obj))
		return NULL;

	if (PyString_Check(cmd_obj)) {
		if (!PyArg_ParseTuple(args, "s:command_name", &cmd))
			return NULL;		
	}

	if (PyCallable_Check(cmd_obj)) {
		if (!PyArg_ParseTuple(args, "O:command_obj", &cmd_obj))
			return NULL;
	}


	if (cmd != NULL) {
		deregister_command_byname(cmd, PYTHON);
	}
	else {
		deregister_command_predicate(cmdfunc_is_pyfunc, cmd_obj, PYTHON);
	}


	Py_INCREF(Py_None);
	return Py_None;
}

int py_command_execute(struct char_data* ch, char* arg, char* text,
                        struct command_info* cmd, int subcmd, int override)
{
	PyObject *p_arg, *p_rawtext, *p_args=0, *p_cmd, *p_subcmd, *p_fnparams, *p_result;
	py_Character* p_char;
	char buf[1024];
			
	if (cmd->minimum_position > GET_POS(ch)) {
		send_bad_position_message(ch);
		return 1;
	}

	if (cmd->py_callfun == Py_None) {
		return 0;
	}

	/*
	 * Now call the python function that registered as the
	 * command handler.
	 */
	if (! PyType_Check(char_class_type)) {
		abort();
	}
			 
				
	p_char = PyObject_New(py_Character,&py_chType);	
	p_char->x_attr = NULL;
	p_char->char_id = GET_ID(ch);

		
	if (!IS_NPC(ch)) {
		(p_char)->char_type = 0;
		(p_char)->idnum = GET_IDNUM(ch);
	}

	/* Print Err */ WERR;
		  
	/*  Need To provide enough INFO TO BUILD the character type */
	p_rawtext = PyString_FromString(text);
	p_cmd = PyString_FromString(arg);
	p_subcmd = PyInt_FromLong(cmd->subcmd);
	if (!p_char || !p_rawtext || !p_cmd || !p_subcmd) {
		mudlog(NRM, LVL_IMMORT, TRUE, "SYSERR: python_script: allocating args for command");
		return 1;
	}
	p_fnparams = PyTuple_New(5);
	p_args = PyList_New(0);
	do {			
		text = any_one_arg(text, buf);
		if (!*buf) {
			break;
		}
		p_arg = PyString_FromString(buf);
		PyList_Append(p_args, p_arg);
	} while(1);
	
	PyTuple_SetItem(p_fnparams, 0, (PyObject *)p_char);
	PyTuple_SetItem(p_fnparams, 1, p_cmd);
	PyTuple_SetItem(p_fnparams, 2, p_args);
	PyTuple_SetItem(p_fnparams, 3, p_subcmd);
	PyTuple_SetItem(p_fnparams, 4, p_rawtext);
	
	if (cmd->py_callfun != Py_None)	
	{
		p_result = PyObject_CallObject(cmd->py_callfun, p_fnparams);
		if (PyErr_Occurred()) {
			send_to_char(ch, "BUG: %s command raised an exception\r\n",
					cmd->name);
			mudlog(NRM, LVL_IMMORT, TRUE, "SYSERR: python interpreter raised "
				"exception inside %s command used by %s",
				cmd->name, GET_NAME(ch));
				PyErr_Print();
		}

		if (p_result && PyInt_Check(p_result)) {
			Py_DECREF(p_result);
			Py_DECREF(p_fnparams);
			return 0;
		}
				
		if (p_result != NULL) { Py_DECREF(p_result); }
	}
	Py_DECREF(p_fnparams);
	return 1;
}


/**
 * Write a log message
 */
static PyObject*
py_log(PyObject *self, PyObject *args)
{
	int log_type = -1, level = LVL_IMMORT, put_in_file = TRUE;
	char* message;
	if(!PyArg_ParseTuple(args, "s|bbb:message, type, level, file?",
			       	&message, &log_type, &level, &put_in_file))
		return NULL;

	if (log_type == -1)
		log("%s", message);
	else
		mudlog(log_type, level, put_in_file, "%s", message);
	
	
	return Py_BuildValue("");
}

/**
 * Clear command handlers
 */
static PyObject*
py_script_clear_commands(PyObject *self, PyObject *args)
{
	py_clear_commands();

	Py_INCREF(Py_None);
	return Py_None;
}



CMD_DATA py_list_to_cmdstruct(char* cmd_name, PyObject* datap, int* code)
{
		CMD_DATA cmd_struct = {};
		PyObject* pos=0, *fn=0, *lev=0, *sub=0, *pri=0, *ovr=0, *flg=0;
		int priority = 100, override = 0;

		*code = 0;

		if (PyDict_Check(datap)) {
			pos = PyDict_GetItemString(datap, "position");
			fn = PyDict_GetItemString(datap, "function");
			lev = PyDict_GetItemString(datap, "level");
			sub = PyDict_GetItemString(datap, "subcmd");
			pri = PyDict_GetItemString(datap, "priority");
			ovr = PyDict_GetItemString(datap, "override");
			flg = PyDict_GetItemString(datap, "flags");

			if (!pos || pos == Py_None) pos = NULL;
			if (!lev || lev == Py_None) lev = NULL;
			if (!sub || sub == Py_None) sub = NULL;
			if (!pri || pri == Py_None) pri = NULL;
			if (!ovr || ovr == Py_None) ovr = NULL;
			if (!flg || flg == Py_None) flg = NULL;
		}

		if (!PyList_Check(datap) && !PyDict_Check(datap)) {
			*code = -1;
			PyErr_SetString(datap, "command data must be list or dictionary type.");
			return cmd_struct;
		}		


		if (PyList_Check(datap))
		{
			if (PyList_GET_SIZE(datap) < 4) {
				log("SYSERR: Invalid table entry for command %s : Less than 4 args",
						cmd_name);
				*code = -1;
				return cmd_struct;
			}
			pos = PyList_GET_ITEM(datap, 0);
			fn = PyList_GET_ITEM(datap, 1);
			lev = PyList_GET_ITEM(datap, 2);
			sub = PyList_GET_ITEM(datap, 3);

			if (PyList_GET_SIZE(datap) >= 5)
			{
				ovr = PyList_GET_ITEM(datap, 4);

				if (PyList_GET_SIZE(datap) >= 6)
					flg = PyList_GET_ITEM(datap, 5);

				 if (PyList_GET_SIZE(datap) >= 7)
					pri = PyList_GET_ITEM(datap, 6);
			}	
		}

		if (pos != NULL && !PyInt_Check(pos)) {
			log("SYSERR: minimum position has invalid datatype in command "
			    "registration for %s", cmd_name);
			*code = -1;
			return cmd_struct;
		}

                if (fn != NULL && fn != Py_None && !PyCallable_Check(fn)) {
			log("SYSERR: command function has invalid datatype in command "
			    "registration for %s", cmd_name);
			*code = -1;
			return cmd_struct;
		}

                if (lev != NULL && !PyInt_Check(lev)) {
			log("SYSERR: minimum level has invalid datatype in command "
			    "registration for %s", cmd_name);
			*code = -1;
			return cmd_struct;
		}

                if (sub != NULL && !PyInt_Check(sub)) {
			log("SYSERR: sub command has invalid datatype in command "
			    "registration for %s", cmd_name);
			*code = -1;
			return cmd_struct;
		}

		if (flg != NULL && !PyInt_Check(flg)) {
			log("SYSERR: command['flags'] has invalid datatype in command "
					"registration for %s", cmd_name);
			*code = -1;
			return cmd_struct;
		}

		if (pri != 0 && pri != Py_None) 
			priority = PyInt_AS_LONG(pri);

		if (ovr != 0 && ovr != Py_None) 
			override = PyInt_AS_LONG(ovr);
		cmd_struct.name = strdup(cmd_name);

		if (pos != NULL) 
			cmd_struct.minimum_position = (byte)PyInt_AS_LONG(pos);
		else pos = 0;

		cmd_struct.py_callfun = fn;
		cmd_struct.language = PYTHON;
		
		if (lev != NULL) 
			cmd_struct.minimum_level = PyInt_AS_LONG(lev);
		else cmd_struct.minimum_level = 0;
	
		if (sub != NULL) 
			cmd_struct.subcmd = PyInt_AS_LONG(sub);
		else cmd_struct.subcmd = 0;

		if (flg != NULL)
			cmd_struct.flags = PyInt_AS_LONG(flg);

		cmd_struct.priority = priority;
		cmd_struct.override = override;
		return cmd_struct;
}

/**
 * Register a command handler
 */
static PyObject*
py_register_commands(PyObject *self, PyObject *args)
{
	char* cmd_name;
	PyObject* cmd_table, *cmd_list, *cmdp, *datap;
	CMD_DATA cmd_struct, *cp;
	int i;
	
	if (!PyArg_ParseTuple(args, "O!:cmd_table", &PyDict_Type, &cmd_table))
		return NULL;
        cmd_list = PyDict_Keys(cmd_table); /* New reference */
	if (cmd_list == NULL)
		return NULL;
	if (PyList_Size(cmd_list) < 1)
	{
		Py_DECREF(cmd_list);

		return Py_BuildValue("");
	}

	for(i = 0; i < PyList_Size(cmd_list); i++) {
		int v = 0;
		cmdp = PyList_GetItem(cmd_list, i); /* Borrowed reference */
		if (!cmdp || !PyString_Check(cmdp))
			continue;
		cmd_name = PyString_AsString(cmdp); /* New reference */
		if (cmd_name == NULL)
			continue;
		datap = PyDict_GetItemString(cmd_table, cmd_name); 
		if (!datap) {
			continue;
		}
		cmd_struct = py_list_to_cmdstruct(cmd_name, datap, &v);
		if (v == -1) {
			Py_DECREF(cmd_list);
			if (cmd_struct.name) {
				free(cmd_struct.name);
			}
			cmd_struct.name = NULL;

			return NULL;
		}
		CREATE(cp, CMD_DATA, 1);
		*cp = cmd_struct;
		cp->language = PYTHON;
		check_insert_command(cp, PYTHON);
		cp = NULL;
	}

	Py_DECREF(cmd_list);
	
	return Py_BuildValue("");
}

static PyObject*
py_register_command(PyObject *self, PyObject *args)
{
	char* cmd_name;
	CMD_DATA cmd_struct, *p;
	PyObject* datap;
	int v;

	if (!PyArg_ParseTuple(args, "sO:command name, list",
				&cmd_name, &datap))
		return NULL;
	cmd_struct = py_list_to_cmdstruct(cmd_name, datap, &v);
	if (v == -1) {
		if (cmd_struct.name)
			free(cmd_struct.name);
		cmd_struct.name = NULL;
		return NULL;
	}
	CREATE(p, CMD_DATA, 1);
	*p = cmd_struct;
	check_insert_command(p, PYTHON);
	Py_INCREF(Py_None);
	
	return Py_None;
}

/*********************************************************************************/

static PyObject* py_restart(PyObject *self, PyObject* args)
{
	need_python_restart = 1;
	
	return Py_BuildValue("");
}

static PyObject* py_die(PyObject *self, PyObject* args)
{
	need_python_restart = 2;

	return Py_BuildValue("");
}


/*********************************************************************************/

static PyObject* 
py_pers(PyObject *self, PyObject* args)
{
	PyObject* target, *see_er;
	struct char_data* vict, *ch;

	if (!PyArg_ParseTuple(args, "O!O!:victim, see_er",
		&py_chType, &target, &py_chType, &see_er) || !target || !see_er)
		return NULL;
	vict = find_char(((py_Character *)target)->char_id);
	ch = find_char(((py_Character *)see_er)->char_id);
	if (!vict || !ch)
		return NULL;
	return PyString_FromString(PERS(vict, ch));
}

/*********************************************************************************/

static void unload_module(py_MudModule* pym)
{
	PyObject *fun, *result, *obj_v = pym->obj, *dict, *params;
	py_MudModule* p, *p_next, *p_tmp = 0;

	for(p = modules; p; p = p_next)
	{
		p_next = p->next;

		if (pym == p) {
			if (p_tmp) p_tmp->next = p_next;
			else modules = p_next;
			break;
		}
		else p_tmp = p;
	}
	if (p) {
		p->obj = NULL;	   
		if (p->name)
			free(p->name);
		free(p);
	}

	dict = PyModule_GetDict(obj_v);
	if (!dict) {
		PyErr_Print();
		return;
	}

	fun = PyDict_GetItemString(dict, "__end__");
	if (fun == NULL)
	{
		PyErr_Print();
		return;
	}
	if (!PyCallable_Check(fun)) {
		PyErr_SetString(fun, "__end__ not callable");
		return;
	}
	
	params = Py_BuildValue("()");
	
	if (params == NULL) {
		return;
	}
	
	result = PyObject_CallObject(fun, params);
	if (params != NULL) { Py_DECREF(params); }
	if (result != NULL) { Py_DECREF(result); }

	Py_DECREF(obj_v);

	/* No return value expected from __end__ */
}

static PyObject*
py_unload_module(PyObject *self, PyObject* args)
{
	py_MudModule* pym;
	char* mod_name;

	if (!PyArg_ParseTuple(args, "s:module_name", &mod_name)) {
		return NULL;
	}

	for(pym = modules; pym; pym = pym->next)
	{
		if (pym->name && pym->obj && !str_cmp(mod_name, pym->name)) {
			unload_module(pym);

			Py_INCREF(Py_None);
			return Py_None;
		}
	}

	PyErr_SetObject (PyExc_ValueError, args);
	return NULL;
}


static PyObject*
py_load_module(PyObject *self, PyObject* args)
{
	py_MudModule* pym;
	PyObject* mod=0, *fun, *result, *params;
	PyObject* dict=0;
	char* mod_name;
	int reloaded = 0;

	if (!PyArg_ParseTuple(args, "s:module_name", &mod_name)) {
		return NULL;
	}

	for(pym = modules; pym; pym = pym->next)
	{
		if (pym->name && pym->obj && !str_cmp(mod_name, pym->name)) {
			/*PyObject* obj_v = pym->obj;*/
			char *name = strdup(pym->name);

			unload_module(pym);
			mod = result = PyImport_ImportModule(mod_name); /* New reference */
			if (!result) {
				PyErr_Print();
				return NULL;
			}
			py_insert_module(name, result);
			free(name);
			reloaded = 1;
			break;
		}
	}

	if (reloaded == 0)
		mod = PyImport_ImportModule(mod_name); /* New reference */

	if (mod == NULL || (dict = PyModule_GetDict(mod)) == NULL) {
		return NULL;
	}
	
	fun = PyDict_GetItemString(dict, "__init__");
	if (fun == NULL || !PyCallable_Check(fun)) {
		if (PyErr_Occurred()) {
			PyErr_Print();
		}
		else {
			PyErr_SetObject (PyExc_ValueError, args);
			PyErr_SetString(args, "Unable to find __init__ function defined in module.");
		}
		return NULL;
	}

	params = Py_BuildValue("()");
	if (params == NULL) {
		return NULL;
	}

	result = PyObject_CallObject(fun, params);
	Py_DECREF(params);
	
	if (PyErr_Occurred()) 
	{
		PyErr_Print();		
	}
	if (result != NULL) { 
		Py_DECREF(result);  /* New reference */

		/* 
		 * No return value expected, but now we own a reference
		 * to something or Py_None that we need to dispose of.
		 */
	}

	py_insert_module(mod_name, mod);
	
	return Py_BuildValue("O", mod);	
}

static PyObject*
py_get_modules(PyObject *self, PyObject* args)
{
	PyObject* ml = PyList_New(0);
	py_MudModule *mm;

	if (ml == NULL)
		return NULL;
	for(mm = modules; mm; mm = mm->next)
		if ( PyList_Append(ml, PyString_FromString(mm->name)) < 0 ) {
			/* XXX: memleak here, will fix later */
			return NULL;
		}
	return ml;	
}

static PyObject*
py_get_commands(PyObject *self, PyObject* args)
{
	PyObject* command_list = PyList_New(0);
	PyObject* command_dict;
	CMD_DATA* pyc;
	unsigned int slot;

	if (!command_list)
		return NULL;

	for(slot = 0; slot < 256; slot++)
	{
		for(pyc = LIST_FIRST(&cmd_hash[slot]); pyc; pyc = LIST_NEXT(pyc, cmd_lst)) {
			if (pyc->language != PYTHON)
				continue;
			command_dict = PyDict_New();
			if (!command_dict)
				goto cmd_error;

			
			if (PyList_Append(command_list, command_dict) < 0)
				goto cmd_error;

			while(0)
			{
				cmd_error: /* Had to abort creating the list, release
					      the references. */

				if (command_dict) {
					Py_DECREF(command_dict);
				}
				Py_DECREF(command_list);

				// XXX: Prob. Memleak

				return NULL;
			}
			
			if (PyDict_SetItemString(command_dict, "position",
					PyInt_FromLong(pyc->minimum_position)) < 0)
				goto cmd_error;
			
			if (PyDict_SetItemString(command_dict, "name",
					PyString_FromString(pyc->name)) < 0)
				goto cmd_error;
			
			if (PyDict_SetItemString(command_dict, "level",
					PyInt_FromLong(pyc->minimum_level)) < 0)
				goto cmd_error;
			
			if (PyDict_SetItemString(command_dict, "subcmd",
					PyInt_FromLong(pyc->subcmd)) < 0)
				goto cmd_error;
			
			if (PyDict_SetItemString(command_dict, "priority",
					PyInt_FromLong(pyc->priority)) < 0)
				goto cmd_error;
			
			if (PyDict_SetItemString(command_dict, "priority",
					PyInt_FromLong(pyc->priority)) < 0)
				goto cmd_error;
			
			if (PyDict_SetItemString(command_dict, "function",
					pyc->py_callfun) < 0)
				goto cmd_error;
		}
	}	
	return command_list;
}

/*********************************************************************************/
	
PyObject*
hook_call_fun(PyObject *self, PyObject* args)
{
	PyObject* hook_obj, *result;
	
	if (!PyArg_ParseTuple(args, "O:command", &hook_obj))
		return NULL;

	if (!PyCallable_Check(hook_obj)) {
		PyErr_SetString(PyExc_ValueError, "The given handler is not a function.");		
		return NULL;
	}

	result = PyObject_CallObject(hook_obj, args);

	return result;
}

/*********************************************************************************/

t_script_return python_event_driver(t_script_event evt, ScriptEventArgs* eventArgs)
{
	PyObject* get_py_driver, *params, *eao, *result;
	t_script_return resultCode;
	static int errCount=0;

	if (init_module == NULL) /* Python inactive */
	{
		return 0;
	}

	/* Print Err */ WERR;
	
	get_py_driver = PyObject_GetAttrString(init_module, "event_driver");
	if (get_py_driver == NULL) {
		if (errCount < 1) {
			log("SYSERR: python_event_driver: event_driver function not "
				"defined in __main__");

			shutdown_python();
			errCount++;
		}
		/* Print Err */ WERR;
		
		return 0;
	}
	if (!PyCallable_Check(get_py_driver))
	{
		if (errCount < 10) {
			log("SYSERR: event_driver not a function");
			errCount++;
		}
		/* Print Err */ WERR;
		
		return 0;
	}

	if(PyErr_Occurred()){PyErr_Print();}

	eao = SWIG_Python_NewPointerObj((void *) eventArgs, SWIGTYPE_p_ScriptEventArgs, 0);
	if (eao == NULL) {
		if (errCount < 10) {
			PyErr_Print();
			errCount++;
		}
		/* Print Err */ WERR;
		
		return 0;
	}
	
	params = Py_BuildValue("iO", (int)evt, eao);
	if (params == NULL) {
		Py_DECREF(eao);
		/* Print Err */ WERR;

		return 0;
	}
	/* XXX: should eao's refcount be decremented now? */

	result = PyObject_CallObject(get_py_driver, params);
	if (result == NULL) {
		Py_DECREF(params);
		/* Print Err */ WERR;

		return 0;
	}

	/* Print Err */ WERR;

	Py_DECREF(params);
	Py_DECREF(result);

	if (!PyInt_Check(result)) {
		mudlog(NRM, LVL_IMMORT, TRUE, "SYSERR: Python: __main__.event_driver returned a non-integer");
		return 0;
	}
	
	resultCode = PyInt_AsLong(result);
	WERR;

	return resultCode;
}
	


static PyMethodDef MUD_Server_Methods[] = {
	{"log", py_log, METH_VARARGS, 
		"Send a message to the system log"},
	{"get_modules", py_get_modules, METH_VARARGS, "Get the list of modules"},
	{"get_commands", py_get_commands, METH_NOARGS, "Get the list of commands."},
	{"load_module", py_load_module, METH_VARARGS, 
		"Load a game module"},
	{"unload_module", py_unload_module, METH_VARARGS,
		                "Remove a game module"},
				
/*	{"unload_module", py_unload_module, METH_VARARGS,
		"Unload a game module"},
	{"reload_module", py_reload_module, METH_VARARGS,
		"Reload a game module"},*/
	{"register_commands", py_register_commands, METH_VARARGS,
		"Register a player command"},
	{"deregister_command", py_deregister_command, METH_VARARGS,
		"Deregister a player command"},
/*	{"null_hook_fun", py_null_hook_fun, METH_VARARGS,
		"Get the function pointer for a null hook"},*/
	{"register_command", py_register_command, METH_VARARGS,
		"Register a player command"},
	{"py_clear_commands", py_script_clear_commands, METH_NOARGS, 
		"Clear all registered python commands"},
	{"py_restart", py_restart, METH_NOARGS, "Restart the python system" },
	{"py_die", py_die, METH_NOARGS, "Shut down the python system" },
	{"PERS", py_pers, METH_VARARGS, "Name of target as ch will see it" },
	{NULL, NULL, 0, NULL}
};

void py_pulse(int beat)
{
	if (need_python_restart) {
		if (init_module != NULL)
		{
			WERR;

			while(modules)
				unload_module(modules);
			if(PyErr_Occurred()) {
				printf("While unloading modules:\n");
				PyErr_Print();
				PyErr_Clear();
			 }
		
			shutdown_python();	
		}

		if (need_python_restart != 2)
			boot_python();
		else
		{
			mudlog(NRM, LVL_IMMORT, TRUE, "Python scripting now offline");
		}

		need_python_restart = 0;
	}
}

void initialize_python()
{
	boot_python();
}

void boot_python()
{
	void init_server();

	need_python_restart = 0;

/*	PyObject* r;
	int k = fork(); */
	int k  =0 ;

	if (k > 0) 
		return;
	if (k < 0) {
		perror("fork");
		abort();
	}
	Py_Initialize();
	mud_module = Py_InitModule("mud", MUD_Server_Methods);
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('../lib/script')");
	initCharType(mud_module);
	initRoomType(mud_module);
	initExitType(mud_module);
	initObjType(mud_module);
	init_server();
/*********************************************************************************/
/* Constant Definitions */	

	PyModule_AddIntConstant(mud_module, "SHOW_OBJ_LONG", 0);
	PyModule_AddIntConstant(mud_module, "SHOW_OBJ_SHORT", 1);
	PyModule_AddIntConstant(mud_module, "SHOW_OBJ_ACTION", 2);

#define _C(x) PyModule_AddIntConstant(mud_module, #x, x);
#include "pydefs.h"
#undef _C
	
/*********************************************************************************/	

	/* if (PyRun_SimpleString("import init") < 0) { */

        if ((init_module = PyImport_ImportModule("init")) == NULL) {
           PyErr_Print();

	   mudlog(NRM, LVL_IMMORT, TRUE, "SYSERR: Error initializing python. "
			   " Shutting it down.");
	   shutdown_python();
	}
}

void shutdown_python()
{
	struct char_data* ch;
	struct obj_data* obj;
	/* ScriptListener* l; */
	
	if (mud_module != 0) {
		Py_DECREF(mud_module);
	}
	if (init_module != 0) {
		Py_DECREF(init_module);
	}
	
	mud_module = NULL;
	char_class_type = NULL;
	init_module = NULL;
	py_clear_commands();
	if ( mud_module != 0 ) {
		Py_DECREF(mud_module);
	}

	for(ch = character_list; ch; ch = ch->next)
	{
		script_clear_listeners_language(&ch->script_listeners, PYTHON);
		script_clear_listeners_language(&ch->proto_script_listeners, PYTHON);
	}

	for(obj = object_list; obj; obj = obj->next)
	{
		script_clear_listeners_language(&obj->script_listeners, PYTHON);
		script_clear_listeners_language(&obj->proto_script_listeners, PYTHON);
	}
	
	Py_Finalize();
	signal_setup();
}


void py_show_credits(struct char_data* ch)
{
	PyObject* command, *result, *params;

	send_to_char(ch, "Python scripting module, version %d\r\n", PYSCRIPTS_VERSION);
	send_to_char(ch, "Created by J. Hess, Copyr. 2004, All Rights Reserved.\r\n");

	if (init_module == NULL)
		return;

	command = PyObject_GetAttrString(init_module, "show_credits");

	if (command == NULL) {
		PyErr_Print();
		
		return;
	}
	if (!PyCallable_Check(command))
	{
		return;
	}

	params = Py_BuildValue("(O)", py_Bottle_Char(ch));
	if (params == NULL) {
		PyErr_Print();
		
		return;
	}

	result = PyObject_CallObject(command, params);
	Py_DECREF(params);
	if (result != NULL) {
		Py_DECREF(result);		
	}
}
