# $Id: modules.py,v 1.2 2004/03/07 16:16:52 mysidia Exp $
# Python side of command modules implementation
#
# Attribution Notice:
#
#    Copyright (c) 2004 Mysidia <mysidia at qmud dot org>
#    All Rights Reserved
#
#    Licensed under the Academic Free License version 2.0
#
#    See ../../doc/afl-2.0.txt
#    And http://www.opensource.org/licenses/afl-2.0.php
#

#
# TODO: Support dependencies
#

#
# Unloading a module will call its __end__()  method, remove its
# reference from the modules table, and decrease its refcount.
#
# But it won't recompile the module, if you make changes to a loaded
# module, then you need 'py.restart' or a mud reboot
#

from mud import *
import credits

__name__ = "Python Command Modules"
__author__ = "jh"
__date__ = "Feb 2004"
__version__ = "1.0"
__deps__ = []

required_by = {}
required_by["init"]=["init"]
required_by["modules"]=["init"]


def __init__() :

	# Command to list modules
	register_command("py.lsmod",  { "position" : POS_DEAD,
					  "function" : do_list_modules,
					  "level" : LVL_IMMORT,
					  "subcmd" : 0,
					  })

	# Command to list commands
	register_command("py.lscmd",  { "position" : POS_DEAD,
					   "function" : do_list_commands,
					   "level" : LVL_IMMORT,
					   "subcmd" : 0 })
	register_command("py.insmod",  {
					  "position" : POS_DEAD,
					  "function" : do_load_module,
					  "level" : LVL_IMPL,
					  "subcmd" : 0
					})
	register_command("py.rmmod",  {
					"position" : POS_DEAD,
					"function" : do_unload_module,
					"level" : LVL_IMPL
					})

def __end__() :
        deregister_command(do_list_modules)
	deregister_command(do_list_commands)
	deregister_command(do_unload_module)

# Interface to list the loaded modules
def do_list_modules(ch, cmd, args, subcmd, rawtext) :
	ch.send("modules = %s" % str(get_modules()))

# Interface to list the loaded commands
def do_list_commands(ch, cmd, args, subcmd, rawtext) :
	command_names = [x["name"] for x in get_commands()]
	command_names.sort()
	ch.send("commands  = %s" % str(command_names))

# Interface to load a module
def do_load_module(ch, cmd, args, subcmd, rawtext) :
	if len(args) < 1 :
		ch.send("Load what module?")
		return
	ch.send("Attempting to load module, %s" % args[0])
	try:
		m = load_module(args[0])
		try:
			credits.addmod(args[0], m)
		except:
			pass
	except:
		ch.send("Unable to load module %s" % args[0])

# Interface to "unload" a module
def do_unload_module(ch, cmd, args, subcmd, rawtext) :
	if len(args) < 1 :
		ch.send("Unload what module?")
		return
	if args[0] in required_by and required_by[args[0]] != None \
			and len(required_by[args[0]]) > 0:
		ch.send("Sorry, other modules depend on this one: " %
				str(required_by[args[0]]) )
		return
	try:
		unload_module(args[0])
		credits.remove(args[0])
	except:
		ch.send("Unable to unload module %s" % args[0])
		
		 
		 
	
