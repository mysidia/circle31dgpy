#1
Mob Memory - test trigger~
0 o 100
~
* assign this to a mob, force the mob to mremember you, then enter the
* room the mob is in while visible (not via goto)
say I remember you, %actor.name%!
~
#2
Mob Greet - test trigger~
0 g 100
~
if %direction%
  say Hello, %actor.name%, how are things to the %direction%?
else
* if the character popped in (word of recall, etc) this will be hit
  say Where did YOU come from, %actor.name%?
end
~
#3
Obj Get - test trigger~
1 g 100
~
%echo% You hear, 'Please put me down, %actor.name%'
~
#4
Room Enter - test trigger~
2 g 100
~
wait 50
wsend %actor% you enter a room
~
#5
Mob Speech - car/cdr test~
0 d 100
test~
say speech: %speech%
say car: %speech.car%
say cdr: %speech.cdr%
~
#6
Mob Command - subfield test~
0 c 100
test~
* test to make sure %actor.skill(skillname)% works
say your hide ability is %actor.skill(hide)% percent.
*
* make sure %actor.eq(name)% works too
eval headgear %actor.eq(head)%
if %headgear%
  say You have some sort of helmet on
else
  say Where's your headgear?
  halt
end
say Fix your %headgear.name%
~
#7
Obj Remove - %transform% test~
1 jl 7
test~
* test of object transformation (and remove trigger)
* test is designed for objects 3020 and 3021
* assign the trigger then wear/remove the item
* repeatedly.
%echo% Beginning object transform.
if %self.vnum% == 3020
  %transform% 3021
else
  %transform% 3020
end
%echo% Transform complete.
~
#8
Room Command - makeuid and remote testing~
2 c 100
test~
* makeuid test ---- assuming your MOBOBJ_ID_BASE is 200000,
* this will display the names of the first 10 mobs loaded on your MUD,
* if they are still around.
eval counter 0
while (%counter% < 10)
  makeuid mob 200000+%counter%
  %echo% #%counter%      %mob.id%   %mob.name%
  eval counter %counter% + 1
done
%echoaround% %actor% %actor.name% cannot see this line.
*
*
* this will also serve as a test of getting a remote mob's globals.
* we know that puff, when initially loaded, is id 200000. We'll use remote
* to give her a global, then %mob.globalname% to read it.
makeuid mob 200000
eval globalname 12345
remote globalname %mob.id%
%echo% %mob.name%'s "globalname" value is %mob.globalname%
~
#9
Mob Greet - %transform% test~
0 g 100
~
* %transform% test
* as a greet trigger, entering the room will cause
* the mob this is attached to, to toggle between mob 1 and 99.
%echo% Beginning transform.
if %self.vnum%==1
  %transform% -99
else
  %transform% -1
end
%echo% Transform complete.
~
#10
Mob Speech - attach test~
0 d 100
attach~
attach 9 %self.id%
~
#11
Mob Speech - detach test~
0 d 100
detach~
detach 9 %self.id%
~
#12
Mob Command - spellcasting test~
0 c 100
kill~
* This command trigger will disallow anyone from trying to
* use the kill command, and will toss a magic missile at them
* for trying.
dg_cast 'magic missile' %actor%
return 0
~
#13
Obj Wear 12 - Staff of Sanctum~
1 j 100
~
wait 1 sec
if %actor.level% < 30
  %send% %actor% The Staff of Sanctum whispers: I will not serve you!
  %echoaround% %actor% The Staff of Sanctum exclaims: 'I will not serve those without honour.'
  %purge% self
else
  %send% %actor% The Staff of Sanctum whispers: I was made to serve, great one!
  %echoaround% %actor% The Staff of Sanctus exclaims: 'I will serve you honourable one..'
end
~
#14
Room Command - Anti-quit~
2 c 100
quit~
   %send% %actor% Powerful forces keep you here. 
~
#15
Room Command - No Recall~
2 c 100
recall ~
   %send% %actor% Divine forces prevent you from doing that.
~
#16
Mob Fight - generic poison~
0 k 10
~
dg_cast 'poison' %actor%
~
#17
Mob Fight - generic chill touch~
0 k 10
~
   dg_cast 'chill touch' %actor%
~
#18
Mob Fight - generic heal self~
0 k 10
~
dg_cast 'heal'
~
#19
Mob Fight - generic dispel evil~
0 k 10
~
dg_cast 'dispel evil' %actor%
~
#20
Mob Fight - generic disarm~
0 k 10
~
disarm %actor%
~
#21
Mob Fight - generic lightning bolt~
0 k 10
~
dg_cast 'lightning' %actor%
~
#22
Mob Fight - generic kick~
0 k 10
~
kick %actor%
~
#23
Mob Fight - generic bash~
0 k 10
~
bash %actor%
~
#24
Mob Fight - generic curse~
0 k 10
~
dg_cast 'curse' %actor%
~
#25
Mob Fight - generic dispel good~
0 k 10
~
dg_cast 'dispel good' %actor%
~
#26
Mob Fight - generic burning hands~
0 k 10
~
dg_cast 'burning hands' %actor%
~
#27
Mob Fight - generic call lightning~
0 k 10
~
dg_cast 'call lightning' %actor%
~
#28
Mob Fight - generic earthquake~
0 k 10
~
dg_cast 'earthquake'
~
#29
Mob Fight - generic silence~
0 k 10
~
dg_cast 'silence' %actor%
~
#30
Mob Speech - Hunt Example~
0 d 100
hunt~
* By Welcor
if %speech.car% != hunt
  return 0
  halt
end
eval target %speech.cdr%
if !%target% || %target% == hunt
  return 0
  halt
end
if %actor.gold% < 4000
  tell %actor.name% You cannot afford my services - go away!
  halt
end
nop %actor.gold(-4000)%
mhunt %target%
tell %actor.name% I'll charge you 4000 gold for that. I'll hunt %target% as long as I can.
~
#31
Obj Timer - Spoil meat~
1 f 100
~
%transform% 131
~
#32
Room Drop - Dg_cast for dropping objects by cost~
2 h 100
~
%%send%% %actor% As you drop the %object.shortdesc%, a loud humming starts to come from the walls.
wait 1
eval worth %object.cost% / 100
switch %worth%
  case 0
    %send% %actor% Your offering was NOT sufficient.
    dg_cast 'magic missile' %actor%
    break
  case 1
    %send% %actor% Your offering was just sufficient.
    dg_cast 'cure light' %actor%
    dg_cast 'clot minor' %actor%
    %purge% %object%
    break
  case 2
    %send% %actor% Your offering was sufficient.
    dg_cast 'refresh' %actor%
    %purge% %object%
    break
  default
    %send% %actor% Your offering was as it must be.
    dg_cast 'invisibility' %actor%
    %purge% %object%
    break
done
~
#33
Obj Command - Cast spell when eating.~
1 c 2
eat~
return 0
wait 2
if %self.carried_by% == 0
  switch %self.vnum%
    case 201
      %damage% %actor% -10
      break 
    case 202
      %damage% %actor% 10
      %send% %actor% Ouch, that hurt a little!
      break
  done
end
~
#80
new trigger~
0 g 2
~
say My trigger commandlist is not complete!
~
#95
Mob Greet 9 - Eating its own stool~
0 g 100
~
if %actor.vnum% == -1
  wait 2 sec
  %echo% %self.name% sniffs a pile of steaming stool.
  wait 2 sec
  take stool
  wait 2 sec
  %echo% %self.name% devours the steaming pile of stool
  wait 3 sec
  %echo% %self.name% walks around in a circle, stops, then squats.
  wait 2 sec
  drop stool
end
~
#96
Obj Command 81 - Paintball Shoot Blue~
1 c 2
~
* No Script
~
#97
Obj Command 80 - Paintball Shoot Red~
1 c 2
shoot~
eval inroom %actor.room%
if (%arg.room% != %actor.room%) || (%arg% == %actor.name%)
  halt
end
if %arg.inventory(81)%
  %echoaround% %actor.name% %actor.name% blasts %arg% with his paintball gun.
  %send% %actor% You blast %arg%.
  %send% %arg% You lose!
  %purge% %arg.inventory(81)%
  %zoneecho% %inroom.vnum% %actor.name% shoots %arg%. A score for the Red Team.
elseif %arg.inventory(80)%
  %send% %actor% They are on your team!
elseif
  %send% %actor% %arg% is not playing.
end
~
#98
Mob Act - 98 Teleporter Give~
0 e 0
has entered the game.~
if !(%actor.inventory(82)%)
  wait 1 sec
  say You are not prepared to travel these realms to their fullest.
  wait 1 sec
  say Maybe I can help you.
  %load% obj 82
  give teleporter %actor.name%
  wait 2 sec
  say With this you may teleport to areas that may not be accessible in any other way.
wait 2 sec
say HELP AREAS
end
~
#99
Obj Command 82 - Teleporter~
1 c 3
teleport~
      %send% %actor% You attempt to manipulate space and time.
      %echoaround% %actor.name% %actor.name% attempts to manipulate space and time.
      wait 3 sec
      switch "%arg%"
        case "Sanctus"
         %teleport% %actor% 100
         break
        case "jade"
         %teleport% %actor% 400
          break
        case "newbie"
         %teleport% %actor% 500
          break
        case "sea"
         %teleport% %actor% 600
          break
        case "camelot"
         %teleport% %actor% 775
          break
        case "nuclear"
         %teleport% %actor% 1800
          break
        case "arena"
         %teleport% %actor% 2000
          break
        case "tower"
         %teleport% %actor% 2200
          break
        case "Orc"
         %teleport% %actor% 4401
          break
        case "monastery"
         %teleport% %actor% 4512
          break
        case "ant"
         %teleport% %actor% 4600
          break
        case "zodiac"
         %teleport% %actor% 5701
          break
        case "graveyard"
         %teleport% %actor% 7401
          break
        case "zamba"
         %teleport% %actor% 7500
          break
        case "oasis"
         %teleport% %actor% 9000
          break
        case "northern"
         %teleport% %actor% 10004
          break
        case "south"
         %teleport% %actor% 10101
          break
        case "elcardo"
         %teleport% %actor% 10604
          break
        case "iuel"
         %teleport% %actor% 10701
          break
        case "omega"
         %teleport% %actor% 11501
          break
        case "hannah"
         %teleport% %actor% 12500
          break
        case "wyvern"
         %teleport% %actor% 14000
          break
        case "cardinal"
         %teleport% %actor% 17501
          break
        case "circus"
         %teleport% %actor% 18700
          break
        case "wester"
         %teleport% %actor% 20001
          break
        case "terringham"
         %teleport% %actor% 23200
          break
        case "dragon"
         %teleport% %actor% 23300
          break
        case "school"
         %teleport% %actor% 23400
          break
        case "mines"
         %teleport% %actor% 23500
          break
        case "aldin"
         %teleport% %actor% 23600
          break
        case "crystal"
         %teleport% %actor% 23800
          break
        case "pass"
         %teleport% %actor% 23901
          break
        case "maura"
         %teleport% %actor% 24000
          break
        case "enterprise"
         %teleport% %actor% 24100
          break
        case "midgaard"
         %teleport% %actor% 24200
          break
        case "valley"
         %teleport% %actor% 24303
          break
        case "prison"
         %teleport% %actor% 24450
          break
        case "nether"
         %teleport% %actor% 24500
          break
        case "yard"
         %teleport% %actor% 24700
          break
        case "elven"
         %teleport% %actor% 24801
          break
        case "jedi"
         %teleport% %actor% 24901
          break
        case "dragonspyre"
         %teleport% %actor% 25000
          break
        case "ape"
         %teleport% %actor% 25100
          break
        case "Vampyre"
         %teleport% %actor% 25200
          break
        case "windmill"
         %teleport% %actor% 25300
          break
        case "village"
         %teleport% %actor% 25400
          break
        case "shipwreck"
         %teleport% %actor% 25516
          break
        case "keep"
         %teleport% %actor% 25645
          break
        case "jareth"
         %teleport% %actor% 25705
          break
        case "mansion"
         %teleport% %actor% 25900
          break
        case "igor's"
         %teleport% %actor% 26100
          break
        case "forest"
         %teleport% %actor% 26201
          break
        case "banshide"
         %teleport% %actor% 26400
          break
        case "ankou"
         %teleport% %actor% 26600
          break
        case "vice"
         %teleport% %actor% 26728
          break
        case "desert"
         %teleport% %actor% 26900
          break
        case "wasteland"
         %teleport% %actor% 27000
          break
        case "sundhaven"
         %teleport% %actor% 27119
          break
        case "station"
         %teleport% %actor% 27300
          break
        case "smurfville"
         %teleport% %actor% 27400
          break
        case "sparta"
         %teleport% %actor% 27501
          break
        case "shire"
         %teleport% %actor% 27700
          break
        case "oceania"
         %teleport% %actor% 27800
          break
        case "notre"
         %teleport% %actor% 27900
          break
        case "motherboard"
         %teleport% %actor% 28000
          break
        case "khanjar"
         %teleport% %actor% 28100
          break
        case "kerjim"
         %teleport% %actor% 28200
          break
        case "haunted"
         %teleport% %actor% 28300
          break
        case "ghenna"
         %teleport% %actor% 28400
          break
        case "hell"
         %teleport% %actor% 28601
          break
        case "goblin"
         %teleport% %actor% 28700
          break
        case "galaxy"
         %teleport% %actor% 28801
          break
        case "werith's"
         %teleport% %actor% 28900
          break
        case "lizard"
         %teleport% %actor% 29000
          break
        case "black"
         %teleport% %actor% 29100
          break
        case "kerofk"
         %teleport% %actor% 29202
          break
        case "froboz"
         %teleport% %actor% 29600
          break
        case "enclave"
         %teleport% %actor% 29700
          break
        case "desire"
         %teleport% %actor% 29801
          break
        case "ancalador"
         %teleport% %actor% 30000
          break
        case "campus"
         %teleport% %actor% 30100
          break
        case "bull"
         %teleport% %actor% 30401
          break
        case "chessboard"
         %teleport% %actor% 30537
          break
        case "castle"
         %teleport% %actor% 30700
          break
        case "baron"
         %teleport% %actor% 30800
          break
        case "westlawn"
         %teleport% %actor% 30900
          break
        case "graye"
         %teleport% %actor% 31003
          break
        case "teeth"
         %teleport% %actor% 31100
          break
        case "leper"
         %teleport% %actor% 31200
          break
        case "ofingia"
         %teleport% %actor% 31300
          break
        case "altar"
         %teleport% %actor% 31400
          break
        case "pale"
         %teleport% %actor% 32300
          break
        case "army"
         %teleport% %actor% 32400
          break
       case "revelry"
         %teleport% %actor% 32600
          break
        default
         %send% %actor% You fail.
         %echoaround% %actor.name% %actor.name% fails.
         halt
         break
        done
         %force% %actor% look
         %echoaround% %actor% %actor.name% steps out of space and time.
~
$~
