#
# TEST I: A look command.
#
# Currently only implements look with no parameters,
# everything else is passed through the game's look on
# the master command table
#

__name__ = "Look at room command"
__date__ = "Feb 2004"
__deps__ = []

from mud import *

def __init__() :
	register_command("look", { 
		  "position" : POS_DEAD,
		  "function" : do_look,
		  "level" : 0,
		  "subcmd" : 0,
		  "override" : 1,
		  "priority" : 25}
		)

def __end__() :
	deregister_command(do_look)


def do_look(ch,cmd,args,subcmd,rawtext) :
	ch.send("OK")
	if ch.level >= LVL_IMMORT :
		return 0 # Return an integer to continue executing
	                 # an internal command.
			 #
			 # Return None or anything not an integer to override.
			 #
			 # This means that the internal look command is used
			 # for imms.

	if len(args) == 0 :
		room = ch.in_room
		exits = room.exits
		vis_exits = [y for y in exits if not (exits[y].flags & EX_CLOSED)]
	
		ch.write(ch.cyn(NRM))
		ch.write(room.name)
		ch.send(ch.nrm(NRM))
		ch.write(room.description)
		if len(vis_exits) > 0 :
			ch.send("%s[ %s ]%s" % (ch.cyn(NRM), " ".join(vis_exits), ch.nrm(NRM)))
		else :
			ch.send("%s[ None! ]%s" % (ch.cyn(NRM), ch.nrm(NRM)))

		ch.write(ch.yel(NRM))
		for x in room.people :
			if ch.can_see(x) == 0 :
				continue
			if x != ch:
				ch.list_one_char(x)
		ch.write(ch.nrm(NRM))
		ch.write(ch.grn(NRM))
		for x in room.contents :
			ch.list_one_obj(x, SHOW_OBJ_SHORT)
		ch.write(ch.nrm(NRM))
			
		
	else :
		return 0 # Defer processing to mud for now
