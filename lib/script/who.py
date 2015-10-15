#
# EXAMPLE: A primitive who command
#

__name__ = "who Command"
__author__ = "jh"
__date__ = "Feb 2004"
__version__ = "1.0"
__text__ = "blah blah blah"
__deps__ = []


from mud import *
import server

def __init__() :
	register_command("who", \
		{ 
		  "position" : POS_DEAD,
		  "function" : do_who,
		  "level" : 0,
		  "subcmd" : 0,
		  "priority" : 25,
		  "override" : 1
		  }
		)

def __end__() :
	deregister_command(do_who)

def class_abbr(num) :
	return server.class_abbreviate(num)


#
# Get the flag string of a bottled char
#
def who_flag_str(ch) :
	s = []

	if ch.prf_flagged(PRF_NOTELL) :
		s.append("(notell)")
	
	return " ".join(s)


def do_who(ch,cmd,args,subcmd,rawtext) :
	d = server.cvar.descriptor_list
	show = []
	

	while d != None :
		c = d.character
		if c == None :
			continue
		them = server.py_Bottle_Char(c)
		if them == None :
			continue
		if ch.can_see(them) :
			show.append(c)
		d = d.next
	ch.send("Players")
	ch.send("-------")
	for them in show :
		ch.write(ch.yel(NRM))
		if ch.isnpc :
			a = "--"
		else :
			a = class_abbr(them.player.chclass)
		ch.write("[%2d %s] %s %s %s" % (them.player.level, a, them.player.name, them.player.title, who_flag_str(server.py_Bottle_Char(them))))
		ch.send(ch.nrm(NRM))
	ch.send("")
	if len(show) != 1 :
		ch.send("%d characters shown" % len(show))
	else :
		ch.send("1 character shown")
	
