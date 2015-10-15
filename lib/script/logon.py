import server
import mud
import event

def __init__() :
	event.add_null_system_listener("logon.enter",server.HOOK_PLAYER_ENTERED_GAME,do_q)

def __end__() :
	event.remove_null_system_listener("logon.enter")


def do_q(type, args) :
	mud.log("Player login (%s) detected (python event)" % args.actor.player.name)
	return 0
