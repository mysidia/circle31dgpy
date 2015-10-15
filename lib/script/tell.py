#
# TEST II: A tell command
#

__name__ = "Tell Command"
__date__ = "Feb 2004"
__version__ = "1.0"
__deps__ = []


from mud import *

def __init__() :
	register_command("tell", \
		{ 
		  "position" : POS_DEAD,
		  "function" : do_tell,
		  "level" : 0,
		  "subcmd" : 0,
		  "override" : 1,
		  "priority" : 25}
		)

def __end__() :
	deregister_command(do_tell)


def do_tell(ch,cmd,args,subcmd,rawtext) :
	if len(args) < 2 :
		ch.send("Tell who what?x")
		return None

	if ch.isnpc :
		return 1

	target = ch.find_player_world(args[0])
	if target == None :
		target = ch.find_char(args[0])
		if target == None :
			if ch.level < LVL_IMMORT :
				ch.send("That player isn't here.")
				return None
			else :
				target = ch.find_char_world(args[0])
				if target == None :
					ch.send("That player isn't here.")
					return None
	if target == ch :
		ch.send("Having fun talking to yourself?")
		return None
	if target.prf_flagged(PRF_NOTELL) and ch.level < LVL_IMPL :
		ch.send("They aren't accepting tells right now.")
		return
	content = " ".join(args[1:])

	if ch.plr_flagged(PLR_NOSHOUT) :
		ch.send("You can't do that right now.")
		return

	if not ch.prf_flagged(PRF_NOREPEAT) :
		ch.write(ch.cyn())
		ch.write("You tell %s, '%s'" % (target.get_name(), content))
		ch.send(ch.nrm())
	else :
		ch.send(MESSG_OK)
	target.write(ch.cyn())
	target.write("%s tells you, '%s'" % (ch.get_name(), content))
	target.send(ch.nrm())
