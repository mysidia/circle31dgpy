#1
memory test trigger~
49 o 100
~
* assign this to a mob, force the mob to mremember you, then enter the
* room the mob is in while visible (not via goto)
say I remember you, %actor.name%!
~
#2
mob greet test~
0 g 100
~
say Hello, %actor.name%, how are things to the %direction%?
~
#3
obj get test~
1 g 100
~
oecho You hear, 'Please put me down, %actor.name%'
~
#4
room test~
2 g 100
~
wait 50
wsend %actor% you enter a room
~
#5
car/cdr test~
0 d 100
test~
say speech: %speech%
say car: %speech.car%
say cdr: %speech.cdr%
~
#6
subfield test~
0 c 100
test~
* test to make sure %actor.skill(skillname)% works
say your hide ability is %actor.skill(hide)% percent.
~
#7
object otransform test~
1 jl 7
test~
* test of object transformation (and remove trigger)
* test is designed for objects 3020 and 3021
* assign the trigger then wear/remove the item
* repeatedly.
oecho Beginning object transform.
if %self.vnum% == 3020
  otransform 3021
else
  otransform 3020
end
oecho Transform complete.
~
#8
makeuid and remote testing~
2 c 100
test~
* makeuid test ---- assuming your MOBOBJ_ID_BASE is 200000,
* this will display the names of the first 10 mobs loaded on your MUD,
* if they are still around.
eval counter 0
while (%counter% < 10)
  makeuid mob 200000+%counter%
  wecho #%counter%      %mob.id%   %mob.name%
  eval counter %counter% + 1
done
*
*
* this will also serve as a test of getting a remote mob's globals.
* we know that puff, when initially loaded, is id 200000. We'll use remote
* to give her a global, then %mob.globalname% to read it.
makeuid mob 200000
eval globalname 12345
remote globalname %mob.id%
wecho %mob.name%'s "globalname" value is %mob.globalname%
~
#9
mtransform test~
0 g 100
~
* mtransform test
* as a greet trigger, entering the room will cause
* the mob this is attached to, to toggle between mob 1 and 99.
mecho Beginning transform.
if %self.vnum%==1
  mtransform 99
else
  mtransform 1
end
mecho Transform complete.
~
#10
bleah test~
0 c 100
blist~
growl %actor.name%
say blah
~
#11
GoldtoPass(5 of 5)~
0 m 10
~
wait 1
say %actor.name%, you have given me %amount% coins. You and your party may pass.
wait 2
unlock gate
wait 5
open gate
wait 5
emote waves you through.
~
#12
GoldtoPass(1 of 5)~
0 g 100
~
wait 3
emote snaps to attention as you approach!
wait 3
say By edict of the Mayor, It will cost you 10 gold coins to enter the city.
~
#13
GoldtoPass(2 of 5)~
0 m 0
~
wait 3
say This is not enough! You may not pass this gate.
wait 5
give %amount% coins to %actor%
wait 5
say Get lost before I haul you before the Magistrate!
~
#14
GoldtoPass(3 of 5)~
0 e 0
leaves east~
wait 10
close gate
lock gate
~
#15
GoldtoPass(4 of 5)~
0 e 100
opened from the other side~
wait 20
close gate
lock gate
~
#16
new trigger~
1 j 100
~
oecho The Singing Sword musics, 'la dee dah, la dah dee dah dah dah'
~
$~
