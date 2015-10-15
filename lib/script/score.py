#
# A score command
#

from mud import *
import locale
import time

__name__ = "Score command"
__author__ = "Test"
__date__ = "Feb 2004"
__version__ = "1.0"
__deps__ = []


def __init__() :
	register_command("score",       { "position" : POS_DEAD,
			                  "function" : do_score,
					  "level" : 0,
					  "subcmd" : 0,
					  "override" : 1,
					  "priority" : 25 })

def __end__() :
	deregister_command(do_score)


def do_score(ch, cmd, args, subcmd, rawtext) :
	age = ch.age
	years = ch.get_age()
	s = "."

	if age["day"] == 0 and age["month"] == 0 :  
		s = ", and It's your birthday!" #Zero month offset, add to content

	if years > 1 :
		ch.send("You are %d years old%s" % (years,s))
	else :
		ch.send("You are 1 year old (Is this possible??) %s" % s)
	ch.send("You have %d/%d hit, %d/%d mana , and %d/%d move."
			  % (ch.hit, ch.max_hit, ch.mana, ch.max_mana,
			     ch.move, ch.max_move));
	if ch.level >= LVL_IMMORT :
		ch.send("Str(%2d+%3d), Int(%2d), Wis(%2d), Dex(%2d), Con(%2d), Cha(%2d)"
			% (ch.str, ch.add, ch.int, ch.wis, ch.dex, ch.con, ch.cha))
	ch.send("Hitroll [%+d], Damroll [%+d]"
			% (ch.hitroll, ch.damroll))
	ch.send("Your AC class is %s and your alignment is %d." % (ch.ac, ch.alignment))
        ch.send("You've scored %s exp, and have %s gold coins" 
			% (locale.format("%.0f", ch.exp,1),
			   locale.format("%.0f", ch.gold,1)))
	ch.send("And have %d/%d items in inventory and are carrying %d/%d units of weight."
			% (ch.carrying_n, ch.can_carry_n, ch.carrying_w, ch.can_carry_w))

	secs = (time.time() - ch.login_time) + ch.played_time
	hours = (secs / 3600) % 24	
	secs -= 3600 * hours
	days = secs / (86400)  # secs/60*60*24 = secs/3600*24 = secs/3600*3*4*2
	                       #  = secs/86400

	ch.send("You've wasted %d days and %d hours on this mud."
			% (days, hours))

	ch.send("And are %s %s (level %d)" % (ch.get_name(), ch.title, ch.level));

	# Player's position
	pos = ch.position
	if   pos == POS_DEAD:		ch.send("You're DEAD!")
	elif pos == POS_MORTALLYW:	ch.send("You're mortally wounded!  Dying!")
	elif pos == POS_INCAP:		ch.send("You're incapacitated, dying...")
	elif pos == POS_STUNNED:	ch.send("You're quite *stunned*!")
	elif pos == POS_SLEEPING:	ch.send("You're taking a little nap.")
	elif pos == POS_RESTING:	ch.send("You're resting but awake.")
	elif pos == POS_SITTING:	ch.send("You're sitting on the ground.")
	elif pos == POS_FIGHTING:	ch.send("You're fighting %s." % (ch.fighting and PERS(ch.fighting, ch) or "thin air"))
	elif pos == POS_STANDING:	ch.send("You are standing.")
	else :				ch.send("You are ???")

	# Bad effects
	if ch.is_affected(AFF_BLIND) : ch.send("You are blind!")
	if ch.is_affected(AFF_POISON) : ch.send("You are poisoned!")
	if ch.is_affected(AFF_CHARM) : ch.send("You have been charmed!")

	# Detection effects
	if ch.is_affected(AFF_DETECT_INVIS) : ch.send("You can see invisible things")
	if ch.is_affected(AFF_INFRAVISION) : ch.send("You have infravision.")

	#Protective effects
	if ch.is_affected(AFF_INVISIBLE) : ch.send("You are invisible.")
	if ch.is_affected(AFF_SANCTUARY) : ch.send("You are protected by Sanctuary.")
	if ch.affected_by_spell(SPELL_ARMOR) : ch.send("You are protected.")

	#!SUMMON
	if ch.prf_flagged(PRF_SUMMONABLE) : ch.send("Note: You have enabled summon by other players")

