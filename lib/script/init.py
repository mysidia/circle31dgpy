# $Id: init.py,v 1.3 2004/03/07 17:06:55 mysidia Exp $
#
# Python Initialization
#
# Attribution Notice:
#
#    Copyright (c) 2004 Mysidia <***REMOVED***>
#    All Rights Reserved
#
#    Licensed under the Academic Free License version 2.0
#
#    See ../../doc/afl-2.0.txt
#    And http://www.opensource.org/licenses/afl-2.0.php
#

#
# Warning: any syntax/compile/other error in modules loaded from init.py
# may prevent mud from starting, or may crash mud if py.restart is executed
#

import time
from mud import *
from restart import *
import server
from tell import *
import locale
import event
import credits

# Choose a local
locale.setlocale(locale.LC_ALL, "") 

# Reset the events table
event.clear_system_listeners()

# Setup the script constants
SCRIPT_RET_CANCEL=0x01
SCRIPT_RET_INTERCEPT=0x01
SCRIPT_RET_ACTOR_DEAD=0x04
SCRIPT_RET_SUBJECT_DEAD=0x08
SCRIPT_RET_VICT_DEAD=0x10
SCRIPT_RET_OBJ_DEAD=0x20
SCRIPT_RET_OK=0x40

# Handle events
def event_driver(event_type,args) :
	return event.event_driver(event_type,args)

# Calls from dg scripts
def object_call(obj, text, cmd, subcmd) :
	log("Python object#%d call " % obj.vnum)

def room_call(room, text, cmd, subcmd) :
	log("Python room#%d call" % room.vnum)
	
def mob_call(mob, text, cmd, subcmd) :
	log("Python mob call %s" % mob.get_name())

def show_credits(ch) :
	ch.writeln("----------------------------------------------------------")
	ch.writeln("init.py version 1.0")
	credits.dispatch(ch)




#
# Load a module, and trap any exception, so maybe a compile error won't crash
# the mud.
#
def safe_load(module) :
	try:
		mod = load_module(module)
		try:
			credits.addmod(module, mod)
		except:
			pass
	except:
		log("SYSERR: PY: exception occured while loading module: %s" % module)

MESSG_OK="Okay."

#
# Primitive commands
#

def do_whoami(ch,cmd,args,subcmd,rawtext) :
	ch.send("You are %s, Level %d" % (ch.get_name(), ch.get_level()))

def do_shutdown_python(ch,cmd,args,subcmd,rawtext) :
	log("(GC) %s shutting down the python system" % ch.get_name(), NRM, LVL_IMMORT, TRUE)
	py_die()

def do_python_help(ch,cmd,args,subcmd,rawtext) :
	content = ""
	content = content + "Python Commands help:" + "\r\n"
	content = content + "py.help              This screen" + "\r\n"
	content = content + "py.restart           Restart python (reload scripts)" + "\r\n"
	content = content + "py.whoami            Whoami command" + "\r\n"
	content = content + "py.lsmod             List loaded python modules" + "\r\n"
	content = content + "script.credits       Show credits info for loaded modules" + "\r\n"
	content = content + "py.lscmd             List all python registered commands" + "\r\n"
	content = content + "py.rmmod             Ask that a command module be unloaded" + "\r\n"
	content = content + "py.shutdown          Kill off python system until next mud boot" + "\r\n"
	ch.send(content)
	
command_table = { 
# Command         # Min Position      Function                Level Subcmd  O Fl Pri
 "py.help" :      [ POS_STANDING, do_python_help,          0,          0, 1, 0, 24 ],
 "py.restart" :   [ POS_STANDING, do_restart_python,       LVL_IMMORT, 0, 0, server.CMD_NOABBREV ],
 "py.whoami" :    [ POS_STANDING, do_whoami,               0,          0   ],
 "py.shutdown" :  [ POS_STANDING, do_shutdown_python,      LVL_IMPL,   0, 0, server.CMD_NOABBREV ],
}
register_commands(command_table)


# Test
safe_load("compile_error")


# Wizard commands for managing modules
safe_load("modules")

# Score Example
safe_load("score")

# Tell Example
safe_load("tell")

# Who command
safe_load("who")

safe_load("logon")

