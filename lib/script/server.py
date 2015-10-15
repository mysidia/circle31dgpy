# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _server

def _swig_setattr(self,class_type,name,value):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    self.__dict__[name] = value

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


_CIRCLEMUD = _server._CIRCLEMUD
USE_AUTOEQ = _server.USE_AUTOEQ
CIRCLE_UNSIGNED_INDEX = _server.CIRCLE_UNSIGNED_INDEX
NOWHERE = _server.NOWHERE
NOTHING = _server.NOTHING
NOBODY = _server.NOBODY
NORTH = _server.NORTH
EAST = _server.EAST
SOUTH = _server.SOUTH
WEST = _server.WEST
UP = _server.UP
DOWN = _server.DOWN
ROOM_DARK = _server.ROOM_DARK
ROOM_DEATH = _server.ROOM_DEATH
ROOM_NOMOB = _server.ROOM_NOMOB
ROOM_INDOORS = _server.ROOM_INDOORS
ROOM_PEACEFUL = _server.ROOM_PEACEFUL
ROOM_SOUNDPROOF = _server.ROOM_SOUNDPROOF
ROOM_NOTRACK = _server.ROOM_NOTRACK
ROOM_NOMAGIC = _server.ROOM_NOMAGIC
ROOM_TUNNEL = _server.ROOM_TUNNEL
ROOM_PRIVATE = _server.ROOM_PRIVATE
ROOM_GODROOM = _server.ROOM_GODROOM
ROOM_HOUSE = _server.ROOM_HOUSE
ROOM_HOUSE_CRASH = _server.ROOM_HOUSE_CRASH
ROOM_ATRIUM = _server.ROOM_ATRIUM
ROOM_OLC = _server.ROOM_OLC
ROOM_BFS_MARK = _server.ROOM_BFS_MARK
EX_ISDOOR = _server.EX_ISDOOR
EX_CLOSED = _server.EX_CLOSED
EX_LOCKED = _server.EX_LOCKED
EX_PICKPROOF = _server.EX_PICKPROOF
SECT_INSIDE = _server.SECT_INSIDE
SECT_CITY = _server.SECT_CITY
SECT_FIELD = _server.SECT_FIELD
SECT_FOREST = _server.SECT_FOREST
SECT_HILLS = _server.SECT_HILLS
SECT_MOUNTAIN = _server.SECT_MOUNTAIN
SECT_WATER_SWIM = _server.SECT_WATER_SWIM
SECT_WATER_NOSWIM = _server.SECT_WATER_NOSWIM
SECT_FLYING = _server.SECT_FLYING
SECT_UNDERWATER = _server.SECT_UNDERWATER
CLASS_UNDEFINED = _server.CLASS_UNDEFINED
CLASS_MAGIC_USER = _server.CLASS_MAGIC_USER
CLASS_CLERIC = _server.CLASS_CLERIC
CLASS_THIEF = _server.CLASS_THIEF
CLASS_WARRIOR = _server.CLASS_WARRIOR
NUM_CLASSES = _server.NUM_CLASSES
CLASS_OTHER = _server.CLASS_OTHER
CLASS_UNDEAD = _server.CLASS_UNDEAD
CLASS_HUMANOID = _server.CLASS_HUMANOID
CLASS_ANIMAL = _server.CLASS_ANIMAL
CLASS_DRAGON = _server.CLASS_DRAGON
CLASS_GIANT = _server.CLASS_GIANT
SEX_NEUTRAL = _server.SEX_NEUTRAL
SEX_MALE = _server.SEX_MALE
SEX_FEMALE = _server.SEX_FEMALE
POS_DEAD = _server.POS_DEAD
POS_MORTALLYW = _server.POS_MORTALLYW
POS_INCAP = _server.POS_INCAP
POS_STUNNED = _server.POS_STUNNED
POS_SLEEPING = _server.POS_SLEEPING
POS_RESTING = _server.POS_RESTING
POS_SITTING = _server.POS_SITTING
POS_FIGHTING = _server.POS_FIGHTING
POS_STANDING = _server.POS_STANDING
PLR_KILLER = _server.PLR_KILLER
PLR_THIEF = _server.PLR_THIEF
PLR_FROZEN = _server.PLR_FROZEN
PLR_DONTSET = _server.PLR_DONTSET
PLR_WRITING = _server.PLR_WRITING
PLR_MAILING = _server.PLR_MAILING
PLR_CRASH = _server.PLR_CRASH
PLR_SITEOK = _server.PLR_SITEOK
PLR_NOSHOUT = _server.PLR_NOSHOUT
PLR_NOTITLE = _server.PLR_NOTITLE
PLR_DELETED = _server.PLR_DELETED
PLR_LOADROOM = _server.PLR_LOADROOM
PLR_NOWIZLIST = _server.PLR_NOWIZLIST
PLR_NODELETE = _server.PLR_NODELETE
PLR_INVSTART = _server.PLR_INVSTART
PLR_CRYO = _server.PLR_CRYO
PLR_NOTDEADYET = _server.PLR_NOTDEADYET
MOB_SPEC = _server.MOB_SPEC
MOB_SENTINEL = _server.MOB_SENTINEL
MOB_SCAVENGER = _server.MOB_SCAVENGER
MOB_ISNPC = _server.MOB_ISNPC
MOB_AWARE = _server.MOB_AWARE
MOB_AGGRESSIVE = _server.MOB_AGGRESSIVE
MOB_STAY_ZONE = _server.MOB_STAY_ZONE
MOB_WIMPY = _server.MOB_WIMPY
MOB_AGGR_EVIL = _server.MOB_AGGR_EVIL
MOB_AGGR_GOOD = _server.MOB_AGGR_GOOD
MOB_AGGR_NEUTRAL = _server.MOB_AGGR_NEUTRAL
MOB_MEMORY = _server.MOB_MEMORY
MOB_HELPER = _server.MOB_HELPER
MOB_NOCHARM = _server.MOB_NOCHARM
MOB_NOSUMMON = _server.MOB_NOSUMMON
MOB_NOSLEEP = _server.MOB_NOSLEEP
MOB_NOBASH = _server.MOB_NOBASH
MOB_NOBLIND = _server.MOB_NOBLIND
MOB_NOTDEADYET = _server.MOB_NOTDEADYET
PRF_BRIEF = _server.PRF_BRIEF
PRF_COMPACT = _server.PRF_COMPACT
PRF_DEAF = _server.PRF_DEAF
PRF_NOTELL = _server.PRF_NOTELL
PRF_DISPHP = _server.PRF_DISPHP
PRF_DISPMANA = _server.PRF_DISPMANA
PRF_DISPMOVE = _server.PRF_DISPMOVE
PRF_AUTOEXIT = _server.PRF_AUTOEXIT
PRF_NOHASSLE = _server.PRF_NOHASSLE
PRF_QUEST = _server.PRF_QUEST
PRF_SUMMONABLE = _server.PRF_SUMMONABLE
PRF_NOREPEAT = _server.PRF_NOREPEAT
PRF_HOLYLIGHT = _server.PRF_HOLYLIGHT
PRF_COLOR_1 = _server.PRF_COLOR_1
PRF_COLOR_2 = _server.PRF_COLOR_2
PRF_NOWIZ = _server.PRF_NOWIZ
PRF_LOG1 = _server.PRF_LOG1
PRF_LOG2 = _server.PRF_LOG2
PRF_NOAUCT = _server.PRF_NOAUCT
PRF_NOGOSS = _server.PRF_NOGOSS
PRF_NOGRATZ = _server.PRF_NOGRATZ
PRF_ROOMFLAGS = _server.PRF_ROOMFLAGS
PRF_DISPAUTO = _server.PRF_DISPAUTO
PRF_CLS = _server.PRF_CLS
AFF_BLIND = _server.AFF_BLIND
AFF_INVISIBLE = _server.AFF_INVISIBLE
AFF_DETECT_ALIGN = _server.AFF_DETECT_ALIGN
AFF_DETECT_INVIS = _server.AFF_DETECT_INVIS
AFF_DETECT_MAGIC = _server.AFF_DETECT_MAGIC
AFF_SENSE_LIFE = _server.AFF_SENSE_LIFE
AFF_WATERWALK = _server.AFF_WATERWALK
AFF_SANCTUARY = _server.AFF_SANCTUARY
AFF_GROUP = _server.AFF_GROUP
AFF_CURSE = _server.AFF_CURSE
AFF_INFRAVISION = _server.AFF_INFRAVISION
AFF_POISON = _server.AFF_POISON
AFF_PROTECT_EVIL = _server.AFF_PROTECT_EVIL
AFF_PROTECT_GOOD = _server.AFF_PROTECT_GOOD
AFF_SLEEP = _server.AFF_SLEEP
AFF_NOTRACK = _server.AFF_NOTRACK
AFF_UNUSED16 = _server.AFF_UNUSED16
AFF_UNUSED17 = _server.AFF_UNUSED17
AFF_SNEAK = _server.AFF_SNEAK
AFF_HIDE = _server.AFF_HIDE
AFF_UNUSED20 = _server.AFF_UNUSED20
AFF_CHARM = _server.AFF_CHARM
CON_PLAYING = _server.CON_PLAYING
CON_CLOSE = _server.CON_CLOSE
CON_GET_NAME = _server.CON_GET_NAME
CON_NAME_CNFRM = _server.CON_NAME_CNFRM
CON_PASSWORD = _server.CON_PASSWORD
CON_NEWPASSWD = _server.CON_NEWPASSWD
CON_CNFPASSWD = _server.CON_CNFPASSWD
CON_QSEX = _server.CON_QSEX
CON_QCLASS = _server.CON_QCLASS
CON_RMOTD = _server.CON_RMOTD
CON_MENU = _server.CON_MENU
CON_EXDESC = _server.CON_EXDESC
CON_CHPWD_GETOLD = _server.CON_CHPWD_GETOLD
CON_CHPWD_GETNEW = _server.CON_CHPWD_GETNEW
CON_CHPWD_VRFY = _server.CON_CHPWD_VRFY
CON_DELCNF1 = _server.CON_DELCNF1
CON_DELCNF2 = _server.CON_DELCNF2
CON_DISCONNECT = _server.CON_DISCONNECT
CON_OEDIT = _server.CON_OEDIT
CON_REDIT = _server.CON_REDIT
CON_ZEDIT = _server.CON_ZEDIT
CON_MEDIT = _server.CON_MEDIT
CON_SEDIT = _server.CON_SEDIT
CON_TEDIT = _server.CON_TEDIT
CON_CEDIT = _server.CON_CEDIT
CON_TRIGEDIT = _server.CON_TRIGEDIT
WEAR_LIGHT = _server.WEAR_LIGHT
WEAR_FINGER_R = _server.WEAR_FINGER_R
WEAR_FINGER_L = _server.WEAR_FINGER_L
WEAR_NECK_1 = _server.WEAR_NECK_1
WEAR_NECK_2 = _server.WEAR_NECK_2
WEAR_BODY = _server.WEAR_BODY
WEAR_HEAD = _server.WEAR_HEAD
WEAR_LEGS = _server.WEAR_LEGS
WEAR_FEET = _server.WEAR_FEET
WEAR_HANDS = _server.WEAR_HANDS
WEAR_ARMS = _server.WEAR_ARMS
WEAR_SHIELD = _server.WEAR_SHIELD
WEAR_ABOUT = _server.WEAR_ABOUT
WEAR_WAIST = _server.WEAR_WAIST
WEAR_WRIST_R = _server.WEAR_WRIST_R
WEAR_WRIST_L = _server.WEAR_WRIST_L
WEAR_WIELD = _server.WEAR_WIELD
WEAR_HOLD = _server.WEAR_HOLD
NUM_WEARS = _server.NUM_WEARS
ITEM_LIGHT = _server.ITEM_LIGHT
ITEM_SCROLL = _server.ITEM_SCROLL
ITEM_WAND = _server.ITEM_WAND
ITEM_STAFF = _server.ITEM_STAFF
ITEM_WEAPON = _server.ITEM_WEAPON
ITEM_FIREWEAPON = _server.ITEM_FIREWEAPON
ITEM_MISSILE = _server.ITEM_MISSILE
ITEM_TREASURE = _server.ITEM_TREASURE
ITEM_ARMOR = _server.ITEM_ARMOR
ITEM_POTION = _server.ITEM_POTION
ITEM_WORN = _server.ITEM_WORN
ITEM_OTHER = _server.ITEM_OTHER
ITEM_TRASH = _server.ITEM_TRASH
ITEM_TRAP = _server.ITEM_TRAP
ITEM_CONTAINER = _server.ITEM_CONTAINER
ITEM_NOTE = _server.ITEM_NOTE
ITEM_DRINKCON = _server.ITEM_DRINKCON
ITEM_KEY = _server.ITEM_KEY
ITEM_FOOD = _server.ITEM_FOOD
ITEM_MONEY = _server.ITEM_MONEY
ITEM_PEN = _server.ITEM_PEN
ITEM_BOAT = _server.ITEM_BOAT
ITEM_FOUNTAIN = _server.ITEM_FOUNTAIN
ITEM_WEAR_TAKE = _server.ITEM_WEAR_TAKE
ITEM_WEAR_FINGER = _server.ITEM_WEAR_FINGER
ITEM_WEAR_NECK = _server.ITEM_WEAR_NECK
ITEM_WEAR_BODY = _server.ITEM_WEAR_BODY
ITEM_WEAR_HEAD = _server.ITEM_WEAR_HEAD
ITEM_WEAR_LEGS = _server.ITEM_WEAR_LEGS
ITEM_WEAR_FEET = _server.ITEM_WEAR_FEET
ITEM_WEAR_HANDS = _server.ITEM_WEAR_HANDS
ITEM_WEAR_ARMS = _server.ITEM_WEAR_ARMS
ITEM_WEAR_SHIELD = _server.ITEM_WEAR_SHIELD
ITEM_WEAR_ABOUT = _server.ITEM_WEAR_ABOUT
ITEM_WEAR_WAIST = _server.ITEM_WEAR_WAIST
ITEM_WEAR_WRIST = _server.ITEM_WEAR_WRIST
ITEM_WEAR_WIELD = _server.ITEM_WEAR_WIELD
ITEM_WEAR_HOLD = _server.ITEM_WEAR_HOLD
ITEM_GLOW = _server.ITEM_GLOW
ITEM_HUM = _server.ITEM_HUM
ITEM_NORENT = _server.ITEM_NORENT
ITEM_NODONATE = _server.ITEM_NODONATE
ITEM_NOINVIS = _server.ITEM_NOINVIS
ITEM_INVISIBLE = _server.ITEM_INVISIBLE
ITEM_MAGIC = _server.ITEM_MAGIC
ITEM_NODROP = _server.ITEM_NODROP
ITEM_BLESS = _server.ITEM_BLESS
ITEM_ANTI_GOOD = _server.ITEM_ANTI_GOOD
ITEM_ANTI_EVIL = _server.ITEM_ANTI_EVIL
ITEM_ANTI_NEUTRAL = _server.ITEM_ANTI_NEUTRAL
ITEM_ANTI_MAGIC_USER = _server.ITEM_ANTI_MAGIC_USER
ITEM_ANTI_CLERIC = _server.ITEM_ANTI_CLERIC
ITEM_ANTI_THIEF = _server.ITEM_ANTI_THIEF
ITEM_ANTI_WARRIOR = _server.ITEM_ANTI_WARRIOR
ITEM_NOSELL = _server.ITEM_NOSELL
APPLY_NONE = _server.APPLY_NONE
APPLY_STR = _server.APPLY_STR
APPLY_DEX = _server.APPLY_DEX
APPLY_INT = _server.APPLY_INT
APPLY_WIS = _server.APPLY_WIS
APPLY_CON = _server.APPLY_CON
APPLY_CHA = _server.APPLY_CHA
APPLY_CLASS = _server.APPLY_CLASS
APPLY_LEVEL = _server.APPLY_LEVEL
APPLY_AGE = _server.APPLY_AGE
APPLY_CHAR_WEIGHT = _server.APPLY_CHAR_WEIGHT
APPLY_CHAR_HEIGHT = _server.APPLY_CHAR_HEIGHT
APPLY_MANA = _server.APPLY_MANA
APPLY_HIT = _server.APPLY_HIT
APPLY_MOVE = _server.APPLY_MOVE
APPLY_GOLD = _server.APPLY_GOLD
APPLY_EXP = _server.APPLY_EXP
APPLY_AC = _server.APPLY_AC
APPLY_HITROLL = _server.APPLY_HITROLL
APPLY_DAMROLL = _server.APPLY_DAMROLL
APPLY_SAVING_PARA = _server.APPLY_SAVING_PARA
APPLY_SAVING_ROD = _server.APPLY_SAVING_ROD
APPLY_SAVING_PETRI = _server.APPLY_SAVING_PETRI
APPLY_SAVING_BREATH = _server.APPLY_SAVING_BREATH
APPLY_SAVING_SPELL = _server.APPLY_SAVING_SPELL
CONT_CLOSEABLE = _server.CONT_CLOSEABLE
CONT_PICKPROOF = _server.CONT_PICKPROOF
CONT_CLOSED = _server.CONT_CLOSED
CONT_LOCKED = _server.CONT_LOCKED
LIQ_WATER = _server.LIQ_WATER
LIQ_BEER = _server.LIQ_BEER
LIQ_WINE = _server.LIQ_WINE
LIQ_ALE = _server.LIQ_ALE
LIQ_DARKALE = _server.LIQ_DARKALE
LIQ_WHISKY = _server.LIQ_WHISKY
LIQ_LEMONADE = _server.LIQ_LEMONADE
LIQ_FIREBRT = _server.LIQ_FIREBRT
LIQ_LOCALSPC = _server.LIQ_LOCALSPC
LIQ_SLIME = _server.LIQ_SLIME
LIQ_MILK = _server.LIQ_MILK
LIQ_TEA = _server.LIQ_TEA
LIQ_COFFE = _server.LIQ_COFFE
LIQ_BLOOD = _server.LIQ_BLOOD
LIQ_SALTWATER = _server.LIQ_SALTWATER
LIQ_CLEARWATER = _server.LIQ_CLEARWATER
DRUNK = _server.DRUNK
FULL = _server.FULL
THIRST = _server.THIRST
SUN_DARK = _server.SUN_DARK
SUN_RISE = _server.SUN_RISE
SUN_LIGHT = _server.SUN_LIGHT
SUN_SET = _server.SUN_SET
SKY_CLOUDLESS = _server.SKY_CLOUDLESS
SKY_CLOUDY = _server.SKY_CLOUDY
SKY_RAINING = _server.SKY_RAINING
SKY_LIGHTNING = _server.SKY_LIGHTNING
RENT_UNDEF = _server.RENT_UNDEF
RENT_CRASH = _server.RENT_CRASH
RENT_RENTED = _server.RENT_RENTED
RENT_CRYO = _server.RENT_CRYO
RENT_FORCED = _server.RENT_FORCED
RENT_TIMEDOUT = _server.RENT_TIMEDOUT
LVL_IMPL = _server.LVL_IMPL
LVL_GRGOD = _server.LVL_GRGOD
LVL_GOD = _server.LVL_GOD
LVL_IMMORT = _server.LVL_IMMORT
LVL_BUILDER = _server.LVL_BUILDER
LVL_FREEZE = _server.LVL_FREEZE
NUM_OF_DIRS = _server.NUM_OF_DIRS
MAGIC_NUMBER = _server.MAGIC_NUMBER
OPT_USEC = _server.OPT_USEC
PASSES_PER_SEC = _server.PASSES_PER_SEC
PULSE_ZONE = _server.PULSE_ZONE
PULSE_MOBILE = _server.PULSE_MOBILE
PULSE_VIOLENCE = _server.PULSE_VIOLENCE
PULSE_AUTOSAVE = _server.PULSE_AUTOSAVE
PULSE_IDLEPWD = _server.PULSE_IDLEPWD
PULSE_SANITY = _server.PULSE_SANITY
PULSE_USAGE = _server.PULSE_USAGE
PULSE_TIMESAVE = _server.PULSE_TIMESAVE
MAX_SOCK_BUF = _server.MAX_SOCK_BUF
MAX_PROMPT_LENGTH = _server.MAX_PROMPT_LENGTH
GARBAGE_SPACE = _server.GARBAGE_SPACE
SMALL_BUFSIZE = _server.SMALL_BUFSIZE
LARGE_BUFSIZE = _server.LARGE_BUFSIZE
HISTORY_SIZE = _server.HISTORY_SIZE
MAX_STRING_LENGTH = _server.MAX_STRING_LENGTH
MAX_INPUT_LENGTH = _server.MAX_INPUT_LENGTH
MAX_RAW_INPUT_LENGTH = _server.MAX_RAW_INPUT_LENGTH
MAX_MESSAGES = _server.MAX_MESSAGES
MAX_NAME_LENGTH = _server.MAX_NAME_LENGTH
MAX_PWD_LENGTH = _server.MAX_PWD_LENGTH
MAX_TITLE_LENGTH = _server.MAX_TITLE_LENGTH
HOST_LENGTH = _server.HOST_LENGTH
EXDSCR_LENGTH = _server.EXDSCR_LENGTH
MAX_TONGUE = _server.MAX_TONGUE
MAX_SKILLS = _server.MAX_SKILLS
MAX_AFFECT = _server.MAX_AFFECT
MAX_OBJ_AFFECT = _server.MAX_OBJ_AFFECT
MAX_NOTE_LENGTH = _server.MAX_NOTE_LENGTH
MAX_CMD_LENGTH = _server.MAX_CMD_LENGTH
NATIVE = _server.NATIVE
PYTHON = _server.PYTHON
INVALID_LANG = _server.INVALID_LANG
class extra_descr_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, extra_descr_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, extra_descr_data, name)
    def __repr__(self):
        return "<C extra_descr_data instance at %s>" % (self.this,)
    __swig_setmethods__["keyword"] = _server.extra_descr_data_keyword_set
    __swig_getmethods__["keyword"] = _server.extra_descr_data_keyword_get
    if _newclass:keyword = property(_server.extra_descr_data_keyword_get, _server.extra_descr_data_keyword_set)
    __swig_setmethods__["description"] = _server.extra_descr_data_description_set
    __swig_getmethods__["description"] = _server.extra_descr_data_description_get
    if _newclass:description = property(_server.extra_descr_data_description_get, _server.extra_descr_data_description_set)
    __swig_setmethods__["next"] = _server.extra_descr_data_next_set
    __swig_getmethods__["next"] = _server.extra_descr_data_next_get
    if _newclass:next = property(_server.extra_descr_data_next_get, _server.extra_descr_data_next_set)
    def __init__(self, *args):
        _swig_setattr(self, extra_descr_data, 'this', _server.new_extra_descr_data(*args))
        _swig_setattr(self, extra_descr_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_extra_descr_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class extra_descr_dataPtr(extra_descr_data):
    def __init__(self, this):
        _swig_setattr(self, extra_descr_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, extra_descr_data, 'thisown', 0)
        _swig_setattr(self, extra_descr_data,self.__class__,extra_descr_data)
_server.extra_descr_data_swigregister(extra_descr_dataPtr)

NUM_OBJ_VAL_POSITIONS = _server.NUM_OBJ_VAL_POSITIONS
class obj_flag_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, obj_flag_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, obj_flag_data, name)
    def __repr__(self):
        return "<C obj_flag_data instance at %s>" % (self.this,)
    __swig_setmethods__["value"] = _server.obj_flag_data_value_set
    __swig_getmethods__["value"] = _server.obj_flag_data_value_get
    if _newclass:value = property(_server.obj_flag_data_value_get, _server.obj_flag_data_value_set)
    __swig_setmethods__["type_flag"] = _server.obj_flag_data_type_flag_set
    __swig_getmethods__["type_flag"] = _server.obj_flag_data_type_flag_get
    if _newclass:type_flag = property(_server.obj_flag_data_type_flag_get, _server.obj_flag_data_type_flag_set)
    __swig_setmethods__["level"] = _server.obj_flag_data_level_set
    __swig_getmethods__["level"] = _server.obj_flag_data_level_get
    if _newclass:level = property(_server.obj_flag_data_level_get, _server.obj_flag_data_level_set)
    __swig_setmethods__["wear_flags"] = _server.obj_flag_data_wear_flags_set
    __swig_getmethods__["wear_flags"] = _server.obj_flag_data_wear_flags_get
    if _newclass:wear_flags = property(_server.obj_flag_data_wear_flags_get, _server.obj_flag_data_wear_flags_set)
    __swig_setmethods__["extra_flags"] = _server.obj_flag_data_extra_flags_set
    __swig_getmethods__["extra_flags"] = _server.obj_flag_data_extra_flags_get
    if _newclass:extra_flags = property(_server.obj_flag_data_extra_flags_get, _server.obj_flag_data_extra_flags_set)
    __swig_setmethods__["weight"] = _server.obj_flag_data_weight_set
    __swig_getmethods__["weight"] = _server.obj_flag_data_weight_get
    if _newclass:weight = property(_server.obj_flag_data_weight_get, _server.obj_flag_data_weight_set)
    __swig_setmethods__["cost"] = _server.obj_flag_data_cost_set
    __swig_getmethods__["cost"] = _server.obj_flag_data_cost_get
    if _newclass:cost = property(_server.obj_flag_data_cost_get, _server.obj_flag_data_cost_set)
    __swig_setmethods__["cost_per_day"] = _server.obj_flag_data_cost_per_day_set
    __swig_getmethods__["cost_per_day"] = _server.obj_flag_data_cost_per_day_get
    if _newclass:cost_per_day = property(_server.obj_flag_data_cost_per_day_get, _server.obj_flag_data_cost_per_day_set)
    __swig_setmethods__["timer"] = _server.obj_flag_data_timer_set
    __swig_getmethods__["timer"] = _server.obj_flag_data_timer_get
    if _newclass:timer = property(_server.obj_flag_data_timer_get, _server.obj_flag_data_timer_set)
    __swig_setmethods__["bitvector"] = _server.obj_flag_data_bitvector_set
    __swig_getmethods__["bitvector"] = _server.obj_flag_data_bitvector_get
    if _newclass:bitvector = property(_server.obj_flag_data_bitvector_get, _server.obj_flag_data_bitvector_set)
    def __init__(self, *args):
        _swig_setattr(self, obj_flag_data, 'this', _server.new_obj_flag_data(*args))
        _swig_setattr(self, obj_flag_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_obj_flag_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class obj_flag_dataPtr(obj_flag_data):
    def __init__(self, this):
        _swig_setattr(self, obj_flag_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, obj_flag_data, 'thisown', 0)
        _swig_setattr(self, obj_flag_data,self.__class__,obj_flag_data)
_server.obj_flag_data_swigregister(obj_flag_dataPtr)

class obj_affected_type(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, obj_affected_type, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, obj_affected_type, name)
    def __repr__(self):
        return "<C obj_affected_type instance at %s>" % (self.this,)
    __swig_setmethods__["location"] = _server.obj_affected_type_location_set
    __swig_getmethods__["location"] = _server.obj_affected_type_location_get
    if _newclass:location = property(_server.obj_affected_type_location_get, _server.obj_affected_type_location_set)
    __swig_setmethods__["modifier"] = _server.obj_affected_type_modifier_set
    __swig_getmethods__["modifier"] = _server.obj_affected_type_modifier_get
    if _newclass:modifier = property(_server.obj_affected_type_modifier_get, _server.obj_affected_type_modifier_set)
    def __init__(self, *args):
        _swig_setattr(self, obj_affected_type, 'this', _server.new_obj_affected_type(*args))
        _swig_setattr(self, obj_affected_type, 'thisown', 1)
    def __del__(self, destroy=_server.delete_obj_affected_type):
        try:
            if self.thisown: destroy(self)
        except: pass

class obj_affected_typePtr(obj_affected_type):
    def __init__(self, this):
        _swig_setattr(self, obj_affected_type, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, obj_affected_type, 'thisown', 0)
        _swig_setattr(self, obj_affected_type,self.__class__,obj_affected_type)
_server.obj_affected_type_swigregister(obj_affected_typePtr)

class obj_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, obj_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, obj_data, name)
    def __repr__(self):
        return "<C obj_data instance at %s>" % (self.this,)
    __swig_setmethods__["item_number"] = _server.obj_data_item_number_set
    __swig_getmethods__["item_number"] = _server.obj_data_item_number_get
    if _newclass:item_number = property(_server.obj_data_item_number_get, _server.obj_data_item_number_set)
    __swig_setmethods__["in_room"] = _server.obj_data_in_room_set
    __swig_getmethods__["in_room"] = _server.obj_data_in_room_get
    if _newclass:in_room = property(_server.obj_data_in_room_get, _server.obj_data_in_room_set)
    __swig_setmethods__["obj_flags"] = _server.obj_data_obj_flags_set
    __swig_getmethods__["obj_flags"] = _server.obj_data_obj_flags_get
    if _newclass:obj_flags = property(_server.obj_data_obj_flags_get, _server.obj_data_obj_flags_set)
    __swig_setmethods__["affected"] = _server.obj_data_affected_set
    __swig_getmethods__["affected"] = _server.obj_data_affected_get
    if _newclass:affected = property(_server.obj_data_affected_get, _server.obj_data_affected_set)
    __swig_setmethods__["name"] = _server.obj_data_name_set
    __swig_getmethods__["name"] = _server.obj_data_name_get
    if _newclass:name = property(_server.obj_data_name_get, _server.obj_data_name_set)
    __swig_setmethods__["description"] = _server.obj_data_description_set
    __swig_getmethods__["description"] = _server.obj_data_description_get
    if _newclass:description = property(_server.obj_data_description_get, _server.obj_data_description_set)
    __swig_setmethods__["short_description"] = _server.obj_data_short_description_set
    __swig_getmethods__["short_description"] = _server.obj_data_short_description_get
    if _newclass:short_description = property(_server.obj_data_short_description_get, _server.obj_data_short_description_set)
    __swig_setmethods__["action_description"] = _server.obj_data_action_description_set
    __swig_getmethods__["action_description"] = _server.obj_data_action_description_get
    if _newclass:action_description = property(_server.obj_data_action_description_get, _server.obj_data_action_description_set)
    __swig_setmethods__["ex_description"] = _server.obj_data_ex_description_set
    __swig_getmethods__["ex_description"] = _server.obj_data_ex_description_get
    if _newclass:ex_description = property(_server.obj_data_ex_description_get, _server.obj_data_ex_description_set)
    __swig_setmethods__["carried_by"] = _server.obj_data_carried_by_set
    __swig_getmethods__["carried_by"] = _server.obj_data_carried_by_get
    if _newclass:carried_by = property(_server.obj_data_carried_by_get, _server.obj_data_carried_by_set)
    __swig_setmethods__["worn_by"] = _server.obj_data_worn_by_set
    __swig_getmethods__["worn_by"] = _server.obj_data_worn_by_get
    if _newclass:worn_by = property(_server.obj_data_worn_by_get, _server.obj_data_worn_by_set)
    __swig_setmethods__["worn_on"] = _server.obj_data_worn_on_set
    __swig_getmethods__["worn_on"] = _server.obj_data_worn_on_get
    if _newclass:worn_on = property(_server.obj_data_worn_on_get, _server.obj_data_worn_on_set)
    __swig_setmethods__["in_obj"] = _server.obj_data_in_obj_set
    __swig_getmethods__["in_obj"] = _server.obj_data_in_obj_get
    if _newclass:in_obj = property(_server.obj_data_in_obj_get, _server.obj_data_in_obj_set)
    __swig_setmethods__["contains"] = _server.obj_data_contains_set
    __swig_getmethods__["contains"] = _server.obj_data_contains_get
    if _newclass:contains = property(_server.obj_data_contains_get, _server.obj_data_contains_set)
    __swig_setmethods__["id"] = _server.obj_data_id_set
    __swig_getmethods__["id"] = _server.obj_data_id_get
    if _newclass:id = property(_server.obj_data_id_get, _server.obj_data_id_set)
    __swig_setmethods__["proto_script"] = _server.obj_data_proto_script_set
    __swig_getmethods__["proto_script"] = _server.obj_data_proto_script_get
    if _newclass:proto_script = property(_server.obj_data_proto_script_get, _server.obj_data_proto_script_set)
    __swig_setmethods__["script"] = _server.obj_data_script_set
    __swig_getmethods__["script"] = _server.obj_data_script_get
    if _newclass:script = property(_server.obj_data_script_get, _server.obj_data_script_set)
    __swig_setmethods__["next_content"] = _server.obj_data_next_content_set
    __swig_getmethods__["next_content"] = _server.obj_data_next_content_get
    if _newclass:next_content = property(_server.obj_data_next_content_get, _server.obj_data_next_content_set)
    __swig_setmethods__["next"] = _server.obj_data_next_set
    __swig_getmethods__["next"] = _server.obj_data_next_get
    if _newclass:next = property(_server.obj_data_next_get, _server.obj_data_next_set)
    __swig_setmethods__["script_listeners"] = _server.obj_data_script_listeners_set
    __swig_getmethods__["script_listeners"] = _server.obj_data_script_listeners_get
    if _newclass:script_listeners = property(_server.obj_data_script_listeners_get, _server.obj_data_script_listeners_set)
    __swig_setmethods__["proto_script_listeners"] = _server.obj_data_proto_script_listeners_set
    __swig_getmethods__["proto_script_listeners"] = _server.obj_data_proto_script_listeners_get
    if _newclass:proto_script_listeners = property(_server.obj_data_proto_script_listeners_get, _server.obj_data_proto_script_listeners_set)
    def __init__(self, *args):
        _swig_setattr(self, obj_data, 'this', _server.new_obj_data(*args))
        _swig_setattr(self, obj_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_obj_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class obj_dataPtr(obj_data):
    def __init__(self, this):
        _swig_setattr(self, obj_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, obj_data, 'thisown', 0)
        _swig_setattr(self, obj_data,self.__class__,obj_data)
_server.obj_data_swigregister(obj_dataPtr)

class obj_file_elem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, obj_file_elem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, obj_file_elem, name)
    def __repr__(self):
        return "<C obj_file_elem instance at %s>" % (self.this,)
    __swig_setmethods__["item_number"] = _server.obj_file_elem_item_number_set
    __swig_getmethods__["item_number"] = _server.obj_file_elem_item_number_get
    if _newclass:item_number = property(_server.obj_file_elem_item_number_get, _server.obj_file_elem_item_number_set)
    __swig_setmethods__["value"] = _server.obj_file_elem_value_set
    __swig_getmethods__["value"] = _server.obj_file_elem_value_get
    if _newclass:value = property(_server.obj_file_elem_value_get, _server.obj_file_elem_value_set)
    __swig_setmethods__["extra_flags"] = _server.obj_file_elem_extra_flags_set
    __swig_getmethods__["extra_flags"] = _server.obj_file_elem_extra_flags_get
    if _newclass:extra_flags = property(_server.obj_file_elem_extra_flags_get, _server.obj_file_elem_extra_flags_set)
    __swig_setmethods__["weight"] = _server.obj_file_elem_weight_set
    __swig_getmethods__["weight"] = _server.obj_file_elem_weight_get
    if _newclass:weight = property(_server.obj_file_elem_weight_get, _server.obj_file_elem_weight_set)
    __swig_setmethods__["timer"] = _server.obj_file_elem_timer_set
    __swig_getmethods__["timer"] = _server.obj_file_elem_timer_get
    if _newclass:timer = property(_server.obj_file_elem_timer_get, _server.obj_file_elem_timer_set)
    __swig_setmethods__["bitvector"] = _server.obj_file_elem_bitvector_set
    __swig_getmethods__["bitvector"] = _server.obj_file_elem_bitvector_get
    if _newclass:bitvector = property(_server.obj_file_elem_bitvector_get, _server.obj_file_elem_bitvector_set)
    __swig_setmethods__["affected"] = _server.obj_file_elem_affected_set
    __swig_getmethods__["affected"] = _server.obj_file_elem_affected_get
    if _newclass:affected = property(_server.obj_file_elem_affected_get, _server.obj_file_elem_affected_set)
    def __init__(self, *args):
        _swig_setattr(self, obj_file_elem, 'this', _server.new_obj_file_elem(*args))
        _swig_setattr(self, obj_file_elem, 'thisown', 1)
    def __del__(self, destroy=_server.delete_obj_file_elem):
        try:
            if self.thisown: destroy(self)
        except: pass

class obj_file_elemPtr(obj_file_elem):
    def __init__(self, this):
        _swig_setattr(self, obj_file_elem, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, obj_file_elem, 'thisown', 0)
        _swig_setattr(self, obj_file_elem,self.__class__,obj_file_elem)
_server.obj_file_elem_swigregister(obj_file_elemPtr)

class rent_info(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rent_info, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rent_info, name)
    def __repr__(self):
        return "<C rent_info instance at %s>" % (self.this,)
    __swig_setmethods__["time"] = _server.rent_info_time_set
    __swig_getmethods__["time"] = _server.rent_info_time_get
    if _newclass:time = property(_server.rent_info_time_get, _server.rent_info_time_set)
    __swig_setmethods__["rentcode"] = _server.rent_info_rentcode_set
    __swig_getmethods__["rentcode"] = _server.rent_info_rentcode_get
    if _newclass:rentcode = property(_server.rent_info_rentcode_get, _server.rent_info_rentcode_set)
    __swig_setmethods__["net_cost_per_diem"] = _server.rent_info_net_cost_per_diem_set
    __swig_getmethods__["net_cost_per_diem"] = _server.rent_info_net_cost_per_diem_get
    if _newclass:net_cost_per_diem = property(_server.rent_info_net_cost_per_diem_get, _server.rent_info_net_cost_per_diem_set)
    __swig_setmethods__["gold"] = _server.rent_info_gold_set
    __swig_getmethods__["gold"] = _server.rent_info_gold_get
    if _newclass:gold = property(_server.rent_info_gold_get, _server.rent_info_gold_set)
    __swig_setmethods__["account"] = _server.rent_info_account_set
    __swig_getmethods__["account"] = _server.rent_info_account_get
    if _newclass:account = property(_server.rent_info_account_get, _server.rent_info_account_set)
    __swig_setmethods__["nitems"] = _server.rent_info_nitems_set
    __swig_getmethods__["nitems"] = _server.rent_info_nitems_get
    if _newclass:nitems = property(_server.rent_info_nitems_get, _server.rent_info_nitems_set)
    __swig_setmethods__["spare0"] = _server.rent_info_spare0_set
    __swig_getmethods__["spare0"] = _server.rent_info_spare0_get
    if _newclass:spare0 = property(_server.rent_info_spare0_get, _server.rent_info_spare0_set)
    __swig_setmethods__["spare1"] = _server.rent_info_spare1_set
    __swig_getmethods__["spare1"] = _server.rent_info_spare1_get
    if _newclass:spare1 = property(_server.rent_info_spare1_get, _server.rent_info_spare1_set)
    __swig_setmethods__["spare2"] = _server.rent_info_spare2_set
    __swig_getmethods__["spare2"] = _server.rent_info_spare2_get
    if _newclass:spare2 = property(_server.rent_info_spare2_get, _server.rent_info_spare2_set)
    __swig_setmethods__["spare3"] = _server.rent_info_spare3_set
    __swig_getmethods__["spare3"] = _server.rent_info_spare3_get
    if _newclass:spare3 = property(_server.rent_info_spare3_get, _server.rent_info_spare3_set)
    __swig_setmethods__["spare4"] = _server.rent_info_spare4_set
    __swig_getmethods__["spare4"] = _server.rent_info_spare4_get
    if _newclass:spare4 = property(_server.rent_info_spare4_get, _server.rent_info_spare4_set)
    __swig_setmethods__["spare5"] = _server.rent_info_spare5_set
    __swig_getmethods__["spare5"] = _server.rent_info_spare5_get
    if _newclass:spare5 = property(_server.rent_info_spare5_get, _server.rent_info_spare5_set)
    __swig_setmethods__["spare6"] = _server.rent_info_spare6_set
    __swig_getmethods__["spare6"] = _server.rent_info_spare6_get
    if _newclass:spare6 = property(_server.rent_info_spare6_get, _server.rent_info_spare6_set)
    __swig_setmethods__["spare7"] = _server.rent_info_spare7_set
    __swig_getmethods__["spare7"] = _server.rent_info_spare7_get
    if _newclass:spare7 = property(_server.rent_info_spare7_get, _server.rent_info_spare7_set)
    def __init__(self, *args):
        _swig_setattr(self, rent_info, 'this', _server.new_rent_info(*args))
        _swig_setattr(self, rent_info, 'thisown', 1)
    def __del__(self, destroy=_server.delete_rent_info):
        try:
            if self.thisown: destroy(self)
        except: pass

class rent_infoPtr(rent_info):
    def __init__(self, this):
        _swig_setattr(self, rent_info, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, rent_info, 'thisown', 0)
        _swig_setattr(self, rent_info,self.__class__,rent_info)
_server.rent_info_swigregister(rent_infoPtr)

class room_direction_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, room_direction_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, room_direction_data, name)
    def __repr__(self):
        return "<C room_direction_data instance at %s>" % (self.this,)
    __swig_setmethods__["general_description"] = _server.room_direction_data_general_description_set
    __swig_getmethods__["general_description"] = _server.room_direction_data_general_description_get
    if _newclass:general_description = property(_server.room_direction_data_general_description_get, _server.room_direction_data_general_description_set)
    __swig_setmethods__["keyword"] = _server.room_direction_data_keyword_set
    __swig_getmethods__["keyword"] = _server.room_direction_data_keyword_get
    if _newclass:keyword = property(_server.room_direction_data_keyword_get, _server.room_direction_data_keyword_set)
    __swig_setmethods__["exit_info"] = _server.room_direction_data_exit_info_set
    __swig_getmethods__["exit_info"] = _server.room_direction_data_exit_info_get
    if _newclass:exit_info = property(_server.room_direction_data_exit_info_get, _server.room_direction_data_exit_info_set)
    __swig_setmethods__["key"] = _server.room_direction_data_key_set
    __swig_getmethods__["key"] = _server.room_direction_data_key_get
    if _newclass:key = property(_server.room_direction_data_key_get, _server.room_direction_data_key_set)
    __swig_setmethods__["to_room"] = _server.room_direction_data_to_room_set
    __swig_getmethods__["to_room"] = _server.room_direction_data_to_room_get
    if _newclass:to_room = property(_server.room_direction_data_to_room_get, _server.room_direction_data_to_room_set)
    def __init__(self, *args):
        _swig_setattr(self, room_direction_data, 'this', _server.new_room_direction_data(*args))
        _swig_setattr(self, room_direction_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_room_direction_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class room_direction_dataPtr(room_direction_data):
    def __init__(self, this):
        _swig_setattr(self, room_direction_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, room_direction_data, 'thisown', 0)
        _swig_setattr(self, room_direction_data,self.__class__,room_direction_data)
_server.room_direction_data_swigregister(room_direction_dataPtr)

class room_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, room_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, room_data, name)
    def __repr__(self):
        return "<C room_data instance at %s>" % (self.this,)
    __swig_setmethods__["number"] = _server.room_data_number_set
    __swig_getmethods__["number"] = _server.room_data_number_get
    if _newclass:number = property(_server.room_data_number_get, _server.room_data_number_set)
    __swig_setmethods__["zone"] = _server.room_data_zone_set
    __swig_getmethods__["zone"] = _server.room_data_zone_get
    if _newclass:zone = property(_server.room_data_zone_get, _server.room_data_zone_set)
    __swig_setmethods__["sector_type"] = _server.room_data_sector_type_set
    __swig_getmethods__["sector_type"] = _server.room_data_sector_type_get
    if _newclass:sector_type = property(_server.room_data_sector_type_get, _server.room_data_sector_type_set)
    __swig_setmethods__["name"] = _server.room_data_name_set
    __swig_getmethods__["name"] = _server.room_data_name_get
    if _newclass:name = property(_server.room_data_name_get, _server.room_data_name_set)
    __swig_setmethods__["description"] = _server.room_data_description_set
    __swig_getmethods__["description"] = _server.room_data_description_get
    if _newclass:description = property(_server.room_data_description_get, _server.room_data_description_set)
    __swig_setmethods__["ex_description"] = _server.room_data_ex_description_set
    __swig_getmethods__["ex_description"] = _server.room_data_ex_description_get
    if _newclass:ex_description = property(_server.room_data_ex_description_get, _server.room_data_ex_description_set)
    __swig_setmethods__["dir_option"] = _server.room_data_dir_option_set
    __swig_getmethods__["dir_option"] = _server.room_data_dir_option_get
    if _newclass:dir_option = property(_server.room_data_dir_option_get, _server.room_data_dir_option_set)
    __swig_setmethods__["room_flags"] = _server.room_data_room_flags_set
    __swig_getmethods__["room_flags"] = _server.room_data_room_flags_get
    if _newclass:room_flags = property(_server.room_data_room_flags_get, _server.room_data_room_flags_set)
    __swig_setmethods__["light"] = _server.room_data_light_set
    __swig_getmethods__["light"] = _server.room_data_light_get
    if _newclass:light = property(_server.room_data_light_get, _server.room_data_light_set)
    __swig_setmethods__["func"] = _server.room_data_func_set
    __swig_getmethods__["func"] = _server.room_data_func_get
    if _newclass:func = property(_server.room_data_func_get, _server.room_data_func_set)
    __swig_setmethods__["proto_script"] = _server.room_data_proto_script_set
    __swig_getmethods__["proto_script"] = _server.room_data_proto_script_get
    if _newclass:proto_script = property(_server.room_data_proto_script_get, _server.room_data_proto_script_set)
    __swig_setmethods__["script"] = _server.room_data_script_set
    __swig_getmethods__["script"] = _server.room_data_script_get
    if _newclass:script = property(_server.room_data_script_get, _server.room_data_script_set)
    __swig_setmethods__["contents"] = _server.room_data_contents_set
    __swig_getmethods__["contents"] = _server.room_data_contents_get
    if _newclass:contents = property(_server.room_data_contents_get, _server.room_data_contents_set)
    __swig_setmethods__["people"] = _server.room_data_people_set
    __swig_getmethods__["people"] = _server.room_data_people_get
    if _newclass:people = property(_server.room_data_people_get, _server.room_data_people_set)
    __swig_setmethods__["script_listeners"] = _server.room_data_script_listeners_set
    __swig_getmethods__["script_listeners"] = _server.room_data_script_listeners_get
    if _newclass:script_listeners = property(_server.room_data_script_listeners_get, _server.room_data_script_listeners_set)
    def __init__(self, *args):
        _swig_setattr(self, room_data, 'this', _server.new_room_data(*args))
        _swig_setattr(self, room_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_room_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class room_dataPtr(room_data):
    def __init__(self, this):
        _swig_setattr(self, room_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, room_data, 'thisown', 0)
        _swig_setattr(self, room_data,self.__class__,room_data)
_server.room_data_swigregister(room_dataPtr)

class memory_rec_struct(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, memory_rec_struct, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, memory_rec_struct, name)
    def __repr__(self):
        return "<C memory_rec_struct instance at %s>" % (self.this,)
    __swig_setmethods__["id"] = _server.memory_rec_struct_id_set
    __swig_getmethods__["id"] = _server.memory_rec_struct_id_get
    if _newclass:id = property(_server.memory_rec_struct_id_get, _server.memory_rec_struct_id_set)
    __swig_setmethods__["next"] = _server.memory_rec_struct_next_set
    __swig_getmethods__["next"] = _server.memory_rec_struct_next_get
    if _newclass:next = property(_server.memory_rec_struct_next_get, _server.memory_rec_struct_next_set)
    def __init__(self, *args):
        _swig_setattr(self, memory_rec_struct, 'this', _server.new_memory_rec_struct(*args))
        _swig_setattr(self, memory_rec_struct, 'thisown', 1)
    def __del__(self, destroy=_server.delete_memory_rec_struct):
        try:
            if self.thisown: destroy(self)
        except: pass

class memory_rec_structPtr(memory_rec_struct):
    def __init__(self, this):
        _swig_setattr(self, memory_rec_struct, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, memory_rec_struct, 'thisown', 0)
        _swig_setattr(self, memory_rec_struct,self.__class__,memory_rec_struct)
_server.memory_rec_struct_swigregister(memory_rec_structPtr)

class time_info_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, time_info_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, time_info_data, name)
    def __repr__(self):
        return "<C time_info_data instance at %s>" % (self.this,)
    __swig_setmethods__["hours"] = _server.time_info_data_hours_set
    __swig_getmethods__["hours"] = _server.time_info_data_hours_get
    if _newclass:hours = property(_server.time_info_data_hours_get, _server.time_info_data_hours_set)
    __swig_setmethods__["day"] = _server.time_info_data_day_set
    __swig_getmethods__["day"] = _server.time_info_data_day_get
    if _newclass:day = property(_server.time_info_data_day_get, _server.time_info_data_day_set)
    __swig_setmethods__["month"] = _server.time_info_data_month_set
    __swig_getmethods__["month"] = _server.time_info_data_month_get
    if _newclass:month = property(_server.time_info_data_month_get, _server.time_info_data_month_set)
    __swig_setmethods__["year"] = _server.time_info_data_year_set
    __swig_getmethods__["year"] = _server.time_info_data_year_get
    if _newclass:year = property(_server.time_info_data_year_get, _server.time_info_data_year_set)
    def __init__(self, *args):
        _swig_setattr(self, time_info_data, 'this', _server.new_time_info_data(*args))
        _swig_setattr(self, time_info_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_time_info_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class time_info_dataPtr(time_info_data):
    def __init__(self, this):
        _swig_setattr(self, time_info_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, time_info_data, 'thisown', 0)
        _swig_setattr(self, time_info_data,self.__class__,time_info_data)
_server.time_info_data_swigregister(time_info_dataPtr)

class time_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, time_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, time_data, name)
    def __repr__(self):
        return "<C time_data instance at %s>" % (self.this,)
    __swig_setmethods__["birth"] = _server.time_data_birth_set
    __swig_getmethods__["birth"] = _server.time_data_birth_get
    if _newclass:birth = property(_server.time_data_birth_get, _server.time_data_birth_set)
    __swig_setmethods__["logon"] = _server.time_data_logon_set
    __swig_getmethods__["logon"] = _server.time_data_logon_get
    if _newclass:logon = property(_server.time_data_logon_get, _server.time_data_logon_set)
    __swig_setmethods__["played"] = _server.time_data_played_set
    __swig_getmethods__["played"] = _server.time_data_played_get
    if _newclass:played = property(_server.time_data_played_get, _server.time_data_played_set)
    def __init__(self, *args):
        _swig_setattr(self, time_data, 'this', _server.new_time_data(*args))
        _swig_setattr(self, time_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_time_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class time_dataPtr(time_data):
    def __init__(self, this):
        _swig_setattr(self, time_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, time_data, 'thisown', 0)
        _swig_setattr(self, time_data,self.__class__,time_data)
_server.time_data_swigregister(time_dataPtr)

class char_player_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, char_player_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, char_player_data, name)
    def __repr__(self):
        return "<C char_player_data instance at %s>" % (self.this,)
    __swig_setmethods__["passwd"] = _server.char_player_data_passwd_set
    __swig_getmethods__["passwd"] = _server.char_player_data_passwd_get
    if _newclass:passwd = property(_server.char_player_data_passwd_get, _server.char_player_data_passwd_set)
    __swig_setmethods__["name"] = _server.char_player_data_name_set
    __swig_getmethods__["name"] = _server.char_player_data_name_get
    if _newclass:name = property(_server.char_player_data_name_get, _server.char_player_data_name_set)
    __swig_setmethods__["short_descr"] = _server.char_player_data_short_descr_set
    __swig_getmethods__["short_descr"] = _server.char_player_data_short_descr_get
    if _newclass:short_descr = property(_server.char_player_data_short_descr_get, _server.char_player_data_short_descr_set)
    __swig_setmethods__["long_descr"] = _server.char_player_data_long_descr_set
    __swig_getmethods__["long_descr"] = _server.char_player_data_long_descr_get
    if _newclass:long_descr = property(_server.char_player_data_long_descr_get, _server.char_player_data_long_descr_set)
    __swig_setmethods__["description"] = _server.char_player_data_description_set
    __swig_getmethods__["description"] = _server.char_player_data_description_get
    if _newclass:description = property(_server.char_player_data_description_get, _server.char_player_data_description_set)
    __swig_setmethods__["title"] = _server.char_player_data_title_set
    __swig_getmethods__["title"] = _server.char_player_data_title_get
    if _newclass:title = property(_server.char_player_data_title_get, _server.char_player_data_title_set)
    __swig_setmethods__["sex"] = _server.char_player_data_sex_set
    __swig_getmethods__["sex"] = _server.char_player_data_sex_get
    if _newclass:sex = property(_server.char_player_data_sex_get, _server.char_player_data_sex_set)
    __swig_setmethods__["chclass"] = _server.char_player_data_chclass_set
    __swig_getmethods__["chclass"] = _server.char_player_data_chclass_get
    if _newclass:chclass = property(_server.char_player_data_chclass_get, _server.char_player_data_chclass_set)
    __swig_setmethods__["level"] = _server.char_player_data_level_set
    __swig_getmethods__["level"] = _server.char_player_data_level_get
    if _newclass:level = property(_server.char_player_data_level_get, _server.char_player_data_level_set)
    __swig_setmethods__["hometown"] = _server.char_player_data_hometown_set
    __swig_getmethods__["hometown"] = _server.char_player_data_hometown_get
    if _newclass:hometown = property(_server.char_player_data_hometown_get, _server.char_player_data_hometown_set)
    __swig_setmethods__["time"] = _server.char_player_data_time_set
    __swig_getmethods__["time"] = _server.char_player_data_time_get
    if _newclass:time = property(_server.char_player_data_time_get, _server.char_player_data_time_set)
    __swig_setmethods__["weight"] = _server.char_player_data_weight_set
    __swig_getmethods__["weight"] = _server.char_player_data_weight_get
    if _newclass:weight = property(_server.char_player_data_weight_get, _server.char_player_data_weight_set)
    __swig_setmethods__["height"] = _server.char_player_data_height_set
    __swig_getmethods__["height"] = _server.char_player_data_height_get
    if _newclass:height = property(_server.char_player_data_height_get, _server.char_player_data_height_set)
    def __init__(self, *args):
        _swig_setattr(self, char_player_data, 'this', _server.new_char_player_data(*args))
        _swig_setattr(self, char_player_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_char_player_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class char_player_dataPtr(char_player_data):
    def __init__(self, this):
        _swig_setattr(self, char_player_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, char_player_data, 'thisown', 0)
        _swig_setattr(self, char_player_data,self.__class__,char_player_data)
_server.char_player_data_swigregister(char_player_dataPtr)

class char_ability_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, char_ability_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, char_ability_data, name)
    def __repr__(self):
        return "<C char_ability_data instance at %s>" % (self.this,)
    __swig_setmethods__["str"] = _server.char_ability_data_str_set
    __swig_getmethods__["str"] = _server.char_ability_data_str_get
    if _newclass:str = property(_server.char_ability_data_str_get, _server.char_ability_data_str_set)
    __swig_setmethods__["str_add"] = _server.char_ability_data_str_add_set
    __swig_getmethods__["str_add"] = _server.char_ability_data_str_add_get
    if _newclass:str_add = property(_server.char_ability_data_str_add_get, _server.char_ability_data_str_add_set)
    __swig_setmethods__["intel"] = _server.char_ability_data_intel_set
    __swig_getmethods__["intel"] = _server.char_ability_data_intel_get
    if _newclass:intel = property(_server.char_ability_data_intel_get, _server.char_ability_data_intel_set)
    __swig_setmethods__["wis"] = _server.char_ability_data_wis_set
    __swig_getmethods__["wis"] = _server.char_ability_data_wis_get
    if _newclass:wis = property(_server.char_ability_data_wis_get, _server.char_ability_data_wis_set)
    __swig_setmethods__["dex"] = _server.char_ability_data_dex_set
    __swig_getmethods__["dex"] = _server.char_ability_data_dex_get
    if _newclass:dex = property(_server.char_ability_data_dex_get, _server.char_ability_data_dex_set)
    __swig_setmethods__["con"] = _server.char_ability_data_con_set
    __swig_getmethods__["con"] = _server.char_ability_data_con_get
    if _newclass:con = property(_server.char_ability_data_con_get, _server.char_ability_data_con_set)
    __swig_setmethods__["cha"] = _server.char_ability_data_cha_set
    __swig_getmethods__["cha"] = _server.char_ability_data_cha_get
    if _newclass:cha = property(_server.char_ability_data_cha_get, _server.char_ability_data_cha_set)
    def __init__(self, *args):
        _swig_setattr(self, char_ability_data, 'this', _server.new_char_ability_data(*args))
        _swig_setattr(self, char_ability_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_char_ability_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class char_ability_dataPtr(char_ability_data):
    def __init__(self, this):
        _swig_setattr(self, char_ability_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, char_ability_data, 'thisown', 0)
        _swig_setattr(self, char_ability_data,self.__class__,char_ability_data)
_server.char_ability_data_swigregister(char_ability_dataPtr)

class char_point_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, char_point_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, char_point_data, name)
    def __repr__(self):
        return "<C char_point_data instance at %s>" % (self.this,)
    __swig_setmethods__["mana"] = _server.char_point_data_mana_set
    __swig_getmethods__["mana"] = _server.char_point_data_mana_get
    if _newclass:mana = property(_server.char_point_data_mana_get, _server.char_point_data_mana_set)
    __swig_setmethods__["max_mana"] = _server.char_point_data_max_mana_set
    __swig_getmethods__["max_mana"] = _server.char_point_data_max_mana_get
    if _newclass:max_mana = property(_server.char_point_data_max_mana_get, _server.char_point_data_max_mana_set)
    __swig_setmethods__["hit"] = _server.char_point_data_hit_set
    __swig_getmethods__["hit"] = _server.char_point_data_hit_get
    if _newclass:hit = property(_server.char_point_data_hit_get, _server.char_point_data_hit_set)
    __swig_setmethods__["max_hit"] = _server.char_point_data_max_hit_set
    __swig_getmethods__["max_hit"] = _server.char_point_data_max_hit_get
    if _newclass:max_hit = property(_server.char_point_data_max_hit_get, _server.char_point_data_max_hit_set)
    __swig_setmethods__["move"] = _server.char_point_data_move_set
    __swig_getmethods__["move"] = _server.char_point_data_move_get
    if _newclass:move = property(_server.char_point_data_move_get, _server.char_point_data_move_set)
    __swig_setmethods__["max_move"] = _server.char_point_data_max_move_set
    __swig_getmethods__["max_move"] = _server.char_point_data_max_move_get
    if _newclass:max_move = property(_server.char_point_data_max_move_get, _server.char_point_data_max_move_set)
    __swig_setmethods__["armor"] = _server.char_point_data_armor_set
    __swig_getmethods__["armor"] = _server.char_point_data_armor_get
    if _newclass:armor = property(_server.char_point_data_armor_get, _server.char_point_data_armor_set)
    __swig_setmethods__["gold"] = _server.char_point_data_gold_set
    __swig_getmethods__["gold"] = _server.char_point_data_gold_get
    if _newclass:gold = property(_server.char_point_data_gold_get, _server.char_point_data_gold_set)
    __swig_setmethods__["bank_gold"] = _server.char_point_data_bank_gold_set
    __swig_getmethods__["bank_gold"] = _server.char_point_data_bank_gold_get
    if _newclass:bank_gold = property(_server.char_point_data_bank_gold_get, _server.char_point_data_bank_gold_set)
    __swig_setmethods__["exp"] = _server.char_point_data_exp_set
    __swig_getmethods__["exp"] = _server.char_point_data_exp_get
    if _newclass:exp = property(_server.char_point_data_exp_get, _server.char_point_data_exp_set)
    __swig_setmethods__["hitroll"] = _server.char_point_data_hitroll_set
    __swig_getmethods__["hitroll"] = _server.char_point_data_hitroll_get
    if _newclass:hitroll = property(_server.char_point_data_hitroll_get, _server.char_point_data_hitroll_set)
    __swig_setmethods__["damroll"] = _server.char_point_data_damroll_set
    __swig_getmethods__["damroll"] = _server.char_point_data_damroll_get
    if _newclass:damroll = property(_server.char_point_data_damroll_get, _server.char_point_data_damroll_set)
    def __init__(self, *args):
        _swig_setattr(self, char_point_data, 'this', _server.new_char_point_data(*args))
        _swig_setattr(self, char_point_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_char_point_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class char_point_dataPtr(char_point_data):
    def __init__(self, this):
        _swig_setattr(self, char_point_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, char_point_data, 'thisown', 0)
        _swig_setattr(self, char_point_data,self.__class__,char_point_data)
_server.char_point_data_swigregister(char_point_dataPtr)

class char_special_data_saved(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, char_special_data_saved, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, char_special_data_saved, name)
    def __repr__(self):
        return "<C char_special_data_saved instance at %s>" % (self.this,)
    __swig_setmethods__["alignment"] = _server.char_special_data_saved_alignment_set
    __swig_getmethods__["alignment"] = _server.char_special_data_saved_alignment_get
    if _newclass:alignment = property(_server.char_special_data_saved_alignment_get, _server.char_special_data_saved_alignment_set)
    __swig_setmethods__["idnum"] = _server.char_special_data_saved_idnum_set
    __swig_getmethods__["idnum"] = _server.char_special_data_saved_idnum_get
    if _newclass:idnum = property(_server.char_special_data_saved_idnum_get, _server.char_special_data_saved_idnum_set)
    __swig_setmethods__["act"] = _server.char_special_data_saved_act_set
    __swig_getmethods__["act"] = _server.char_special_data_saved_act_get
    if _newclass:act = property(_server.char_special_data_saved_act_get, _server.char_special_data_saved_act_set)
    __swig_setmethods__["affected_by"] = _server.char_special_data_saved_affected_by_set
    __swig_getmethods__["affected_by"] = _server.char_special_data_saved_affected_by_get
    if _newclass:affected_by = property(_server.char_special_data_saved_affected_by_get, _server.char_special_data_saved_affected_by_set)
    __swig_setmethods__["apply_saving_throw"] = _server.char_special_data_saved_apply_saving_throw_set
    __swig_getmethods__["apply_saving_throw"] = _server.char_special_data_saved_apply_saving_throw_get
    if _newclass:apply_saving_throw = property(_server.char_special_data_saved_apply_saving_throw_get, _server.char_special_data_saved_apply_saving_throw_set)
    def __init__(self, *args):
        _swig_setattr(self, char_special_data_saved, 'this', _server.new_char_special_data_saved(*args))
        _swig_setattr(self, char_special_data_saved, 'thisown', 1)
    def __del__(self, destroy=_server.delete_char_special_data_saved):
        try:
            if self.thisown: destroy(self)
        except: pass

class char_special_data_savedPtr(char_special_data_saved):
    def __init__(self, this):
        _swig_setattr(self, char_special_data_saved, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, char_special_data_saved, 'thisown', 0)
        _swig_setattr(self, char_special_data_saved,self.__class__,char_special_data_saved)
_server.char_special_data_saved_swigregister(char_special_data_savedPtr)

class char_special_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, char_special_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, char_special_data, name)
    def __repr__(self):
        return "<C char_special_data instance at %s>" % (self.this,)
    __swig_setmethods__["fighting"] = _server.char_special_data_fighting_set
    __swig_getmethods__["fighting"] = _server.char_special_data_fighting_get
    if _newclass:fighting = property(_server.char_special_data_fighting_get, _server.char_special_data_fighting_set)
    __swig_setmethods__["hunting"] = _server.char_special_data_hunting_set
    __swig_getmethods__["hunting"] = _server.char_special_data_hunting_get
    if _newclass:hunting = property(_server.char_special_data_hunting_get, _server.char_special_data_hunting_set)
    __swig_setmethods__["position"] = _server.char_special_data_position_set
    __swig_getmethods__["position"] = _server.char_special_data_position_get
    if _newclass:position = property(_server.char_special_data_position_get, _server.char_special_data_position_set)
    __swig_setmethods__["carry_weight"] = _server.char_special_data_carry_weight_set
    __swig_getmethods__["carry_weight"] = _server.char_special_data_carry_weight_get
    if _newclass:carry_weight = property(_server.char_special_data_carry_weight_get, _server.char_special_data_carry_weight_set)
    __swig_setmethods__["carry_items"] = _server.char_special_data_carry_items_set
    __swig_getmethods__["carry_items"] = _server.char_special_data_carry_items_get
    if _newclass:carry_items = property(_server.char_special_data_carry_items_get, _server.char_special_data_carry_items_set)
    __swig_setmethods__["timer"] = _server.char_special_data_timer_set
    __swig_getmethods__["timer"] = _server.char_special_data_timer_get
    if _newclass:timer = property(_server.char_special_data_timer_get, _server.char_special_data_timer_set)
    __swig_setmethods__["saved"] = _server.char_special_data_saved_set
    __swig_getmethods__["saved"] = _server.char_special_data_saved_get
    if _newclass:saved = property(_server.char_special_data_saved_get, _server.char_special_data_saved_set)
    def __init__(self, *args):
        _swig_setattr(self, char_special_data, 'this', _server.new_char_special_data(*args))
        _swig_setattr(self, char_special_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_char_special_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class char_special_dataPtr(char_special_data):
    def __init__(self, this):
        _swig_setattr(self, char_special_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, char_special_data, 'thisown', 0)
        _swig_setattr(self, char_special_data,self.__class__,char_special_data)
_server.char_special_data_swigregister(char_special_dataPtr)

class player_special_data_saved(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, player_special_data_saved, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, player_special_data_saved, name)
    def __repr__(self):
        return "<C player_special_data_saved instance at %s>" % (self.this,)
    __swig_setmethods__["skills"] = _server.player_special_data_saved_skills_set
    __swig_getmethods__["skills"] = _server.player_special_data_saved_skills_get
    if _newclass:skills = property(_server.player_special_data_saved_skills_get, _server.player_special_data_saved_skills_set)
    __swig_setmethods__["PADDING0"] = _server.player_special_data_saved_PADDING0_set
    __swig_getmethods__["PADDING0"] = _server.player_special_data_saved_PADDING0_get
    if _newclass:PADDING0 = property(_server.player_special_data_saved_PADDING0_get, _server.player_special_data_saved_PADDING0_set)
    __swig_setmethods__["talks"] = _server.player_special_data_saved_talks_set
    __swig_getmethods__["talks"] = _server.player_special_data_saved_talks_get
    if _newclass:talks = property(_server.player_special_data_saved_talks_get, _server.player_special_data_saved_talks_set)
    __swig_setmethods__["wimp_level"] = _server.player_special_data_saved_wimp_level_set
    __swig_getmethods__["wimp_level"] = _server.player_special_data_saved_wimp_level_get
    if _newclass:wimp_level = property(_server.player_special_data_saved_wimp_level_get, _server.player_special_data_saved_wimp_level_set)
    __swig_setmethods__["freeze_level"] = _server.player_special_data_saved_freeze_level_set
    __swig_getmethods__["freeze_level"] = _server.player_special_data_saved_freeze_level_get
    if _newclass:freeze_level = property(_server.player_special_data_saved_freeze_level_get, _server.player_special_data_saved_freeze_level_set)
    __swig_setmethods__["invis_level"] = _server.player_special_data_saved_invis_level_set
    __swig_getmethods__["invis_level"] = _server.player_special_data_saved_invis_level_get
    if _newclass:invis_level = property(_server.player_special_data_saved_invis_level_get, _server.player_special_data_saved_invis_level_set)
    __swig_setmethods__["load_room"] = _server.player_special_data_saved_load_room_set
    __swig_getmethods__["load_room"] = _server.player_special_data_saved_load_room_get
    if _newclass:load_room = property(_server.player_special_data_saved_load_room_get, _server.player_special_data_saved_load_room_set)
    __swig_setmethods__["pref"] = _server.player_special_data_saved_pref_set
    __swig_getmethods__["pref"] = _server.player_special_data_saved_pref_get
    if _newclass:pref = property(_server.player_special_data_saved_pref_get, _server.player_special_data_saved_pref_set)
    __swig_setmethods__["bad_pws"] = _server.player_special_data_saved_bad_pws_set
    __swig_getmethods__["bad_pws"] = _server.player_special_data_saved_bad_pws_get
    if _newclass:bad_pws = property(_server.player_special_data_saved_bad_pws_get, _server.player_special_data_saved_bad_pws_set)
    __swig_setmethods__["conditions"] = _server.player_special_data_saved_conditions_set
    __swig_getmethods__["conditions"] = _server.player_special_data_saved_conditions_get
    if _newclass:conditions = property(_server.player_special_data_saved_conditions_get, _server.player_special_data_saved_conditions_set)
    __swig_setmethods__["spare0"] = _server.player_special_data_saved_spare0_set
    __swig_getmethods__["spare0"] = _server.player_special_data_saved_spare0_get
    if _newclass:spare0 = property(_server.player_special_data_saved_spare0_get, _server.player_special_data_saved_spare0_set)
    __swig_setmethods__["spare1"] = _server.player_special_data_saved_spare1_set
    __swig_getmethods__["spare1"] = _server.player_special_data_saved_spare1_get
    if _newclass:spare1 = property(_server.player_special_data_saved_spare1_get, _server.player_special_data_saved_spare1_set)
    __swig_setmethods__["spare2"] = _server.player_special_data_saved_spare2_set
    __swig_getmethods__["spare2"] = _server.player_special_data_saved_spare2_get
    if _newclass:spare2 = property(_server.player_special_data_saved_spare2_get, _server.player_special_data_saved_spare2_set)
    __swig_setmethods__["spare3"] = _server.player_special_data_saved_spare3_set
    __swig_getmethods__["spare3"] = _server.player_special_data_saved_spare3_get
    if _newclass:spare3 = property(_server.player_special_data_saved_spare3_get, _server.player_special_data_saved_spare3_set)
    __swig_setmethods__["spare4"] = _server.player_special_data_saved_spare4_set
    __swig_getmethods__["spare4"] = _server.player_special_data_saved_spare4_get
    if _newclass:spare4 = property(_server.player_special_data_saved_spare4_get, _server.player_special_data_saved_spare4_set)
    __swig_setmethods__["spare5"] = _server.player_special_data_saved_spare5_set
    __swig_getmethods__["spare5"] = _server.player_special_data_saved_spare5_get
    if _newclass:spare5 = property(_server.player_special_data_saved_spare5_get, _server.player_special_data_saved_spare5_set)
    __swig_setmethods__["spells_to_learn"] = _server.player_special_data_saved_spells_to_learn_set
    __swig_getmethods__["spells_to_learn"] = _server.player_special_data_saved_spells_to_learn_get
    if _newclass:spells_to_learn = property(_server.player_special_data_saved_spells_to_learn_get, _server.player_special_data_saved_spells_to_learn_set)
    __swig_setmethods__["olc_zone"] = _server.player_special_data_saved_olc_zone_set
    __swig_getmethods__["olc_zone"] = _server.player_special_data_saved_olc_zone_get
    if _newclass:olc_zone = property(_server.player_special_data_saved_olc_zone_get, _server.player_special_data_saved_olc_zone_set)
    __swig_setmethods__["spare8"] = _server.player_special_data_saved_spare8_set
    __swig_getmethods__["spare8"] = _server.player_special_data_saved_spare8_get
    if _newclass:spare8 = property(_server.player_special_data_saved_spare8_get, _server.player_special_data_saved_spare8_set)
    __swig_setmethods__["spare9"] = _server.player_special_data_saved_spare9_set
    __swig_getmethods__["spare9"] = _server.player_special_data_saved_spare9_get
    if _newclass:spare9 = property(_server.player_special_data_saved_spare9_get, _server.player_special_data_saved_spare9_set)
    __swig_setmethods__["spare10"] = _server.player_special_data_saved_spare10_set
    __swig_getmethods__["spare10"] = _server.player_special_data_saved_spare10_get
    if _newclass:spare10 = property(_server.player_special_data_saved_spare10_get, _server.player_special_data_saved_spare10_set)
    __swig_setmethods__["spare11"] = _server.player_special_data_saved_spare11_set
    __swig_getmethods__["spare11"] = _server.player_special_data_saved_spare11_get
    if _newclass:spare11 = property(_server.player_special_data_saved_spare11_get, _server.player_special_data_saved_spare11_set)
    __swig_setmethods__["spare12"] = _server.player_special_data_saved_spare12_set
    __swig_getmethods__["spare12"] = _server.player_special_data_saved_spare12_get
    if _newclass:spare12 = property(_server.player_special_data_saved_spare12_get, _server.player_special_data_saved_spare12_set)
    __swig_setmethods__["spare13"] = _server.player_special_data_saved_spare13_set
    __swig_getmethods__["spare13"] = _server.player_special_data_saved_spare13_get
    if _newclass:spare13 = property(_server.player_special_data_saved_spare13_get, _server.player_special_data_saved_spare13_set)
    __swig_setmethods__["spare14"] = _server.player_special_data_saved_spare14_set
    __swig_getmethods__["spare14"] = _server.player_special_data_saved_spare14_get
    if _newclass:spare14 = property(_server.player_special_data_saved_spare14_get, _server.player_special_data_saved_spare14_set)
    __swig_setmethods__["spare15"] = _server.player_special_data_saved_spare15_set
    __swig_getmethods__["spare15"] = _server.player_special_data_saved_spare15_get
    if _newclass:spare15 = property(_server.player_special_data_saved_spare15_get, _server.player_special_data_saved_spare15_set)
    __swig_setmethods__["spare16"] = _server.player_special_data_saved_spare16_set
    __swig_getmethods__["spare16"] = _server.player_special_data_saved_spare16_get
    if _newclass:spare16 = property(_server.player_special_data_saved_spare16_get, _server.player_special_data_saved_spare16_set)
    __swig_setmethods__["spare17"] = _server.player_special_data_saved_spare17_set
    __swig_getmethods__["spare17"] = _server.player_special_data_saved_spare17_get
    if _newclass:spare17 = property(_server.player_special_data_saved_spare17_get, _server.player_special_data_saved_spare17_set)
    __swig_setmethods__["spare18"] = _server.player_special_data_saved_spare18_set
    __swig_getmethods__["spare18"] = _server.player_special_data_saved_spare18_get
    if _newclass:spare18 = property(_server.player_special_data_saved_spare18_get, _server.player_special_data_saved_spare18_set)
    __swig_setmethods__["spare19"] = _server.player_special_data_saved_spare19_set
    __swig_getmethods__["spare19"] = _server.player_special_data_saved_spare19_get
    if _newclass:spare19 = property(_server.player_special_data_saved_spare19_get, _server.player_special_data_saved_spare19_set)
    __swig_setmethods__["spare20"] = _server.player_special_data_saved_spare20_set
    __swig_getmethods__["spare20"] = _server.player_special_data_saved_spare20_get
    if _newclass:spare20 = property(_server.player_special_data_saved_spare20_get, _server.player_special_data_saved_spare20_set)
    __swig_setmethods__["spare21"] = _server.player_special_data_saved_spare21_set
    __swig_getmethods__["spare21"] = _server.player_special_data_saved_spare21_get
    if _newclass:spare21 = property(_server.player_special_data_saved_spare21_get, _server.player_special_data_saved_spare21_set)
    def __init__(self, *args):
        _swig_setattr(self, player_special_data_saved, 'this', _server.new_player_special_data_saved(*args))
        _swig_setattr(self, player_special_data_saved, 'thisown', 1)
    def __del__(self, destroy=_server.delete_player_special_data_saved):
        try:
            if self.thisown: destroy(self)
        except: pass

class player_special_data_savedPtr(player_special_data_saved):
    def __init__(self, this):
        _swig_setattr(self, player_special_data_saved, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, player_special_data_saved, 'thisown', 0)
        _swig_setattr(self, player_special_data_saved,self.__class__,player_special_data_saved)
_server.player_special_data_saved_swigregister(player_special_data_savedPtr)

class player_special_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, player_special_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, player_special_data, name)
    def __repr__(self):
        return "<C player_special_data instance at %s>" % (self.this,)
    __swig_setmethods__["saved"] = _server.player_special_data_saved_set
    __swig_getmethods__["saved"] = _server.player_special_data_saved_get
    if _newclass:saved = property(_server.player_special_data_saved_get, _server.player_special_data_saved_set)
    __swig_setmethods__["poofin"] = _server.player_special_data_poofin_set
    __swig_getmethods__["poofin"] = _server.player_special_data_poofin_get
    if _newclass:poofin = property(_server.player_special_data_poofin_get, _server.player_special_data_poofin_set)
    __swig_setmethods__["poofout"] = _server.player_special_data_poofout_set
    __swig_getmethods__["poofout"] = _server.player_special_data_poofout_get
    if _newclass:poofout = property(_server.player_special_data_poofout_get, _server.player_special_data_poofout_set)
    __swig_setmethods__["aliases"] = _server.player_special_data_aliases_set
    __swig_getmethods__["aliases"] = _server.player_special_data_aliases_get
    if _newclass:aliases = property(_server.player_special_data_aliases_get, _server.player_special_data_aliases_set)
    __swig_setmethods__["last_tell"] = _server.player_special_data_last_tell_set
    __swig_getmethods__["last_tell"] = _server.player_special_data_last_tell_get
    if _newclass:last_tell = property(_server.player_special_data_last_tell_get, _server.player_special_data_last_tell_set)
    __swig_setmethods__["last_olc_targ"] = _server.player_special_data_last_olc_targ_set
    __swig_getmethods__["last_olc_targ"] = _server.player_special_data_last_olc_targ_get
    if _newclass:last_olc_targ = property(_server.player_special_data_last_olc_targ_get, _server.player_special_data_last_olc_targ_set)
    __swig_setmethods__["last_olc_mode"] = _server.player_special_data_last_olc_mode_set
    __swig_getmethods__["last_olc_mode"] = _server.player_special_data_last_olc_mode_get
    if _newclass:last_olc_mode = property(_server.player_special_data_last_olc_mode_get, _server.player_special_data_last_olc_mode_set)
    def __init__(self, *args):
        _swig_setattr(self, player_special_data, 'this', _server.new_player_special_data(*args))
        _swig_setattr(self, player_special_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_player_special_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class player_special_dataPtr(player_special_data):
    def __init__(self, this):
        _swig_setattr(self, player_special_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, player_special_data, 'thisown', 0)
        _swig_setattr(self, player_special_data,self.__class__,player_special_data)
_server.player_special_data_swigregister(player_special_dataPtr)

class mob_special_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, mob_special_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, mob_special_data, name)
    def __repr__(self):
        return "<C mob_special_data instance at %s>" % (self.this,)
    __swig_setmethods__["memory"] = _server.mob_special_data_memory_set
    __swig_getmethods__["memory"] = _server.mob_special_data_memory_get
    if _newclass:memory = property(_server.mob_special_data_memory_get, _server.mob_special_data_memory_set)
    __swig_setmethods__["attack_type"] = _server.mob_special_data_attack_type_set
    __swig_getmethods__["attack_type"] = _server.mob_special_data_attack_type_get
    if _newclass:attack_type = property(_server.mob_special_data_attack_type_get, _server.mob_special_data_attack_type_set)
    __swig_setmethods__["default_pos"] = _server.mob_special_data_default_pos_set
    __swig_getmethods__["default_pos"] = _server.mob_special_data_default_pos_get
    if _newclass:default_pos = property(_server.mob_special_data_default_pos_get, _server.mob_special_data_default_pos_set)
    __swig_setmethods__["damnodice"] = _server.mob_special_data_damnodice_set
    __swig_getmethods__["damnodice"] = _server.mob_special_data_damnodice_get
    if _newclass:damnodice = property(_server.mob_special_data_damnodice_get, _server.mob_special_data_damnodice_set)
    __swig_setmethods__["damsizedice"] = _server.mob_special_data_damsizedice_set
    __swig_getmethods__["damsizedice"] = _server.mob_special_data_damsizedice_get
    if _newclass:damsizedice = property(_server.mob_special_data_damsizedice_get, _server.mob_special_data_damsizedice_set)
    def __init__(self, *args):
        _swig_setattr(self, mob_special_data, 'this', _server.new_mob_special_data(*args))
        _swig_setattr(self, mob_special_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_mob_special_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class mob_special_dataPtr(mob_special_data):
    def __init__(self, this):
        _swig_setattr(self, mob_special_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, mob_special_data, 'thisown', 0)
        _swig_setattr(self, mob_special_data,self.__class__,mob_special_data)
_server.mob_special_data_swigregister(mob_special_dataPtr)

class affected_type(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, affected_type, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, affected_type, name)
    def __repr__(self):
        return "<C affected_type instance at %s>" % (self.this,)
    __swig_setmethods__["type"] = _server.affected_type_type_set
    __swig_getmethods__["type"] = _server.affected_type_type_get
    if _newclass:type = property(_server.affected_type_type_get, _server.affected_type_type_set)
    __swig_setmethods__["duration"] = _server.affected_type_duration_set
    __swig_getmethods__["duration"] = _server.affected_type_duration_get
    if _newclass:duration = property(_server.affected_type_duration_get, _server.affected_type_duration_set)
    __swig_setmethods__["modifier"] = _server.affected_type_modifier_set
    __swig_getmethods__["modifier"] = _server.affected_type_modifier_get
    if _newclass:modifier = property(_server.affected_type_modifier_get, _server.affected_type_modifier_set)
    __swig_setmethods__["location"] = _server.affected_type_location_set
    __swig_getmethods__["location"] = _server.affected_type_location_get
    if _newclass:location = property(_server.affected_type_location_get, _server.affected_type_location_set)
    __swig_setmethods__["bitvector"] = _server.affected_type_bitvector_set
    __swig_getmethods__["bitvector"] = _server.affected_type_bitvector_get
    if _newclass:bitvector = property(_server.affected_type_bitvector_get, _server.affected_type_bitvector_set)
    __swig_setmethods__["next"] = _server.affected_type_next_set
    __swig_getmethods__["next"] = _server.affected_type_next_get
    if _newclass:next = property(_server.affected_type_next_get, _server.affected_type_next_set)
    def __init__(self, *args):
        _swig_setattr(self, affected_type, 'this', _server.new_affected_type(*args))
        _swig_setattr(self, affected_type, 'thisown', 1)
    def __del__(self, destroy=_server.delete_affected_type):
        try:
            if self.thisown: destroy(self)
        except: pass

class affected_typePtr(affected_type):
    def __init__(self, this):
        _swig_setattr(self, affected_type, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, affected_type, 'thisown', 0)
        _swig_setattr(self, affected_type,self.__class__,affected_type)
_server.affected_type_swigregister(affected_typePtr)

class follow_type(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, follow_type, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, follow_type, name)
    def __repr__(self):
        return "<C follow_type instance at %s>" % (self.this,)
    __swig_setmethods__["follower"] = _server.follow_type_follower_set
    __swig_getmethods__["follower"] = _server.follow_type_follower_get
    if _newclass:follower = property(_server.follow_type_follower_get, _server.follow_type_follower_set)
    __swig_setmethods__["next"] = _server.follow_type_next_set
    __swig_getmethods__["next"] = _server.follow_type_next_get
    if _newclass:next = property(_server.follow_type_next_get, _server.follow_type_next_set)
    def __init__(self, *args):
        _swig_setattr(self, follow_type, 'this', _server.new_follow_type(*args))
        _swig_setattr(self, follow_type, 'thisown', 1)
    def __del__(self, destroy=_server.delete_follow_type):
        try:
            if self.thisown: destroy(self)
        except: pass

class follow_typePtr(follow_type):
    def __init__(self, this):
        _swig_setattr(self, follow_type, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, follow_type, 'thisown', 0)
        _swig_setattr(self, follow_type,self.__class__,follow_type)
_server.follow_type_swigregister(follow_typePtr)

class char_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, char_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, char_data, name)
    def __repr__(self):
        return "<C char_data instance at %s>" % (self.this,)
    __swig_setmethods__["pfilepos"] = _server.char_data_pfilepos_set
    __swig_getmethods__["pfilepos"] = _server.char_data_pfilepos_get
    if _newclass:pfilepos = property(_server.char_data_pfilepos_get, _server.char_data_pfilepos_set)
    __swig_setmethods__["nr"] = _server.char_data_nr_set
    __swig_getmethods__["nr"] = _server.char_data_nr_get
    if _newclass:nr = property(_server.char_data_nr_get, _server.char_data_nr_set)
    __swig_setmethods__["in_room"] = _server.char_data_in_room_set
    __swig_getmethods__["in_room"] = _server.char_data_in_room_get
    if _newclass:in_room = property(_server.char_data_in_room_get, _server.char_data_in_room_set)
    __swig_setmethods__["was_in_room"] = _server.char_data_was_in_room_set
    __swig_getmethods__["was_in_room"] = _server.char_data_was_in_room_get
    if _newclass:was_in_room = property(_server.char_data_was_in_room_get, _server.char_data_was_in_room_set)
    __swig_setmethods__["wait"] = _server.char_data_wait_set
    __swig_getmethods__["wait"] = _server.char_data_wait_get
    if _newclass:wait = property(_server.char_data_wait_get, _server.char_data_wait_set)
    __swig_setmethods__["player"] = _server.char_data_player_set
    __swig_getmethods__["player"] = _server.char_data_player_get
    if _newclass:player = property(_server.char_data_player_get, _server.char_data_player_set)
    __swig_setmethods__["real_abils"] = _server.char_data_real_abils_set
    __swig_getmethods__["real_abils"] = _server.char_data_real_abils_get
    if _newclass:real_abils = property(_server.char_data_real_abils_get, _server.char_data_real_abils_set)
    __swig_setmethods__["aff_abils"] = _server.char_data_aff_abils_set
    __swig_getmethods__["aff_abils"] = _server.char_data_aff_abils_get
    if _newclass:aff_abils = property(_server.char_data_aff_abils_get, _server.char_data_aff_abils_set)
    __swig_setmethods__["points"] = _server.char_data_points_set
    __swig_getmethods__["points"] = _server.char_data_points_get
    if _newclass:points = property(_server.char_data_points_get, _server.char_data_points_set)
    __swig_setmethods__["char_specials"] = _server.char_data_char_specials_set
    __swig_getmethods__["char_specials"] = _server.char_data_char_specials_get
    if _newclass:char_specials = property(_server.char_data_char_specials_get, _server.char_data_char_specials_set)
    __swig_setmethods__["player_specials"] = _server.char_data_player_specials_set
    __swig_getmethods__["player_specials"] = _server.char_data_player_specials_get
    if _newclass:player_specials = property(_server.char_data_player_specials_get, _server.char_data_player_specials_set)
    __swig_setmethods__["mob_specials"] = _server.char_data_mob_specials_set
    __swig_getmethods__["mob_specials"] = _server.char_data_mob_specials_get
    if _newclass:mob_specials = property(_server.char_data_mob_specials_get, _server.char_data_mob_specials_set)
    __swig_setmethods__["affected"] = _server.char_data_affected_set
    __swig_getmethods__["affected"] = _server.char_data_affected_get
    if _newclass:affected = property(_server.char_data_affected_get, _server.char_data_affected_set)
    __swig_setmethods__["equipment"] = _server.char_data_equipment_set
    __swig_getmethods__["equipment"] = _server.char_data_equipment_get
    if _newclass:equipment = property(_server.char_data_equipment_get, _server.char_data_equipment_set)
    __swig_setmethods__["carrying"] = _server.char_data_carrying_set
    __swig_getmethods__["carrying"] = _server.char_data_carrying_get
    if _newclass:carrying = property(_server.char_data_carrying_get, _server.char_data_carrying_set)
    __swig_setmethods__["desc"] = _server.char_data_desc_set
    __swig_getmethods__["desc"] = _server.char_data_desc_get
    if _newclass:desc = property(_server.char_data_desc_get, _server.char_data_desc_set)
    __swig_setmethods__["id"] = _server.char_data_id_set
    __swig_getmethods__["id"] = _server.char_data_id_get
    if _newclass:id = property(_server.char_data_id_get, _server.char_data_id_set)
    __swig_setmethods__["proto_script"] = _server.char_data_proto_script_set
    __swig_getmethods__["proto_script"] = _server.char_data_proto_script_get
    if _newclass:proto_script = property(_server.char_data_proto_script_get, _server.char_data_proto_script_set)
    __swig_setmethods__["script"] = _server.char_data_script_set
    __swig_getmethods__["script"] = _server.char_data_script_get
    if _newclass:script = property(_server.char_data_script_get, _server.char_data_script_set)
    __swig_setmethods__["memory"] = _server.char_data_memory_set
    __swig_getmethods__["memory"] = _server.char_data_memory_get
    if _newclass:memory = property(_server.char_data_memory_get, _server.char_data_memory_set)
    __swig_setmethods__["next_in_room"] = _server.char_data_next_in_room_set
    __swig_getmethods__["next_in_room"] = _server.char_data_next_in_room_get
    if _newclass:next_in_room = property(_server.char_data_next_in_room_get, _server.char_data_next_in_room_set)
    __swig_setmethods__["next"] = _server.char_data_next_set
    __swig_getmethods__["next"] = _server.char_data_next_get
    if _newclass:next = property(_server.char_data_next_get, _server.char_data_next_set)
    __swig_setmethods__["next_fighting"] = _server.char_data_next_fighting_set
    __swig_getmethods__["next_fighting"] = _server.char_data_next_fighting_get
    if _newclass:next_fighting = property(_server.char_data_next_fighting_get, _server.char_data_next_fighting_set)
    __swig_setmethods__["followers"] = _server.char_data_followers_set
    __swig_getmethods__["followers"] = _server.char_data_followers_get
    if _newclass:followers = property(_server.char_data_followers_get, _server.char_data_followers_set)
    __swig_setmethods__["master"] = _server.char_data_master_set
    __swig_getmethods__["master"] = _server.char_data_master_get
    if _newclass:master = property(_server.char_data_master_get, _server.char_data_master_set)
    __swig_setmethods__["script_listeners"] = _server.char_data_script_listeners_set
    __swig_getmethods__["script_listeners"] = _server.char_data_script_listeners_get
    if _newclass:script_listeners = property(_server.char_data_script_listeners_get, _server.char_data_script_listeners_set)
    __swig_setmethods__["proto_script_listeners"] = _server.char_data_proto_script_listeners_set
    __swig_getmethods__["proto_script_listeners"] = _server.char_data_proto_script_listeners_get
    if _newclass:proto_script_listeners = property(_server.char_data_proto_script_listeners_get, _server.char_data_proto_script_listeners_set)
    def __init__(self, *args):
        _swig_setattr(self, char_data, 'this', _server.new_char_data(*args))
        _swig_setattr(self, char_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_char_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class char_dataPtr(char_data):
    def __init__(self, this):
        _swig_setattr(self, char_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, char_data, 'thisown', 0)
        _swig_setattr(self, char_data,self.__class__,char_data)
_server.char_data_swigregister(char_dataPtr)

class char_file_u(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, char_file_u, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, char_file_u, name)
    def __repr__(self):
        return "<C char_file_u instance at %s>" % (self.this,)
    __swig_setmethods__["name"] = _server.char_file_u_name_set
    __swig_getmethods__["name"] = _server.char_file_u_name_get
    if _newclass:name = property(_server.char_file_u_name_get, _server.char_file_u_name_set)
    __swig_setmethods__["description"] = _server.char_file_u_description_set
    __swig_getmethods__["description"] = _server.char_file_u_description_get
    if _newclass:description = property(_server.char_file_u_description_get, _server.char_file_u_description_set)
    __swig_setmethods__["title"] = _server.char_file_u_title_set
    __swig_getmethods__["title"] = _server.char_file_u_title_get
    if _newclass:title = property(_server.char_file_u_title_get, _server.char_file_u_title_set)
    __swig_setmethods__["sex"] = _server.char_file_u_sex_set
    __swig_getmethods__["sex"] = _server.char_file_u_sex_get
    if _newclass:sex = property(_server.char_file_u_sex_get, _server.char_file_u_sex_set)
    __swig_setmethods__["chclass"] = _server.char_file_u_chclass_set
    __swig_getmethods__["chclass"] = _server.char_file_u_chclass_get
    if _newclass:chclass = property(_server.char_file_u_chclass_get, _server.char_file_u_chclass_set)
    __swig_setmethods__["level"] = _server.char_file_u_level_set
    __swig_getmethods__["level"] = _server.char_file_u_level_get
    if _newclass:level = property(_server.char_file_u_level_get, _server.char_file_u_level_set)
    __swig_setmethods__["hometown"] = _server.char_file_u_hometown_set
    __swig_getmethods__["hometown"] = _server.char_file_u_hometown_get
    if _newclass:hometown = property(_server.char_file_u_hometown_get, _server.char_file_u_hometown_set)
    __swig_setmethods__["birth"] = _server.char_file_u_birth_set
    __swig_getmethods__["birth"] = _server.char_file_u_birth_get
    if _newclass:birth = property(_server.char_file_u_birth_get, _server.char_file_u_birth_set)
    __swig_setmethods__["played"] = _server.char_file_u_played_set
    __swig_getmethods__["played"] = _server.char_file_u_played_get
    if _newclass:played = property(_server.char_file_u_played_get, _server.char_file_u_played_set)
    __swig_setmethods__["weight"] = _server.char_file_u_weight_set
    __swig_getmethods__["weight"] = _server.char_file_u_weight_get
    if _newclass:weight = property(_server.char_file_u_weight_get, _server.char_file_u_weight_set)
    __swig_setmethods__["height"] = _server.char_file_u_height_set
    __swig_getmethods__["height"] = _server.char_file_u_height_get
    if _newclass:height = property(_server.char_file_u_height_get, _server.char_file_u_height_set)
    __swig_setmethods__["pwd"] = _server.char_file_u_pwd_set
    __swig_getmethods__["pwd"] = _server.char_file_u_pwd_get
    if _newclass:pwd = property(_server.char_file_u_pwd_get, _server.char_file_u_pwd_set)
    __swig_setmethods__["char_specials_saved"] = _server.char_file_u_char_specials_saved_set
    __swig_getmethods__["char_specials_saved"] = _server.char_file_u_char_specials_saved_get
    if _newclass:char_specials_saved = property(_server.char_file_u_char_specials_saved_get, _server.char_file_u_char_specials_saved_set)
    __swig_setmethods__["player_specials_saved"] = _server.char_file_u_player_specials_saved_set
    __swig_getmethods__["player_specials_saved"] = _server.char_file_u_player_specials_saved_get
    if _newclass:player_specials_saved = property(_server.char_file_u_player_specials_saved_get, _server.char_file_u_player_specials_saved_set)
    __swig_setmethods__["abilities"] = _server.char_file_u_abilities_set
    __swig_getmethods__["abilities"] = _server.char_file_u_abilities_get
    if _newclass:abilities = property(_server.char_file_u_abilities_get, _server.char_file_u_abilities_set)
    __swig_setmethods__["points"] = _server.char_file_u_points_set
    __swig_getmethods__["points"] = _server.char_file_u_points_get
    if _newclass:points = property(_server.char_file_u_points_get, _server.char_file_u_points_set)
    __swig_setmethods__["affected"] = _server.char_file_u_affected_set
    __swig_getmethods__["affected"] = _server.char_file_u_affected_get
    if _newclass:affected = property(_server.char_file_u_affected_get, _server.char_file_u_affected_set)
    __swig_setmethods__["last_logon"] = _server.char_file_u_last_logon_set
    __swig_getmethods__["last_logon"] = _server.char_file_u_last_logon_get
    if _newclass:last_logon = property(_server.char_file_u_last_logon_get, _server.char_file_u_last_logon_set)
    __swig_setmethods__["host"] = _server.char_file_u_host_set
    __swig_getmethods__["host"] = _server.char_file_u_host_get
    if _newclass:host = property(_server.char_file_u_host_get, _server.char_file_u_host_set)
    def __init__(self, *args):
        _swig_setattr(self, char_file_u, 'this', _server.new_char_file_u(*args))
        _swig_setattr(self, char_file_u, 'thisown', 1)
    def __del__(self, destroy=_server.delete_char_file_u):
        try:
            if self.thisown: destroy(self)
        except: pass

class char_file_uPtr(char_file_u):
    def __init__(self, this):
        _swig_setattr(self, char_file_u, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, char_file_u, 'thisown', 0)
        _swig_setattr(self, char_file_u,self.__class__,char_file_u)
_server.char_file_u_swigregister(char_file_uPtr)

class txt_block(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, txt_block, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, txt_block, name)
    def __repr__(self):
        return "<C txt_block instance at %s>" % (self.this,)
    __swig_setmethods__["text"] = _server.txt_block_text_set
    __swig_getmethods__["text"] = _server.txt_block_text_get
    if _newclass:text = property(_server.txt_block_text_get, _server.txt_block_text_set)
    __swig_setmethods__["aliased"] = _server.txt_block_aliased_set
    __swig_getmethods__["aliased"] = _server.txt_block_aliased_get
    if _newclass:aliased = property(_server.txt_block_aliased_get, _server.txt_block_aliased_set)
    __swig_setmethods__["next"] = _server.txt_block_next_set
    __swig_getmethods__["next"] = _server.txt_block_next_get
    if _newclass:next = property(_server.txt_block_next_get, _server.txt_block_next_set)
    def __init__(self, *args):
        _swig_setattr(self, txt_block, 'this', _server.new_txt_block(*args))
        _swig_setattr(self, txt_block, 'thisown', 1)
    def __del__(self, destroy=_server.delete_txt_block):
        try:
            if self.thisown: destroy(self)
        except: pass

class txt_blockPtr(txt_block):
    def __init__(self, this):
        _swig_setattr(self, txt_block, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, txt_block, 'thisown', 0)
        _swig_setattr(self, txt_block,self.__class__,txt_block)
_server.txt_block_swigregister(txt_blockPtr)

class txt_q(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, txt_q, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, txt_q, name)
    def __repr__(self):
        return "<C txt_q instance at %s>" % (self.this,)
    __swig_setmethods__["head"] = _server.txt_q_head_set
    __swig_getmethods__["head"] = _server.txt_q_head_get
    if _newclass:head = property(_server.txt_q_head_get, _server.txt_q_head_set)
    __swig_setmethods__["tail"] = _server.txt_q_tail_set
    __swig_getmethods__["tail"] = _server.txt_q_tail_get
    if _newclass:tail = property(_server.txt_q_tail_get, _server.txt_q_tail_set)
    def __init__(self, *args):
        _swig_setattr(self, txt_q, 'this', _server.new_txt_q(*args))
        _swig_setattr(self, txt_q, 'thisown', 1)
    def __del__(self, destroy=_server.delete_txt_q):
        try:
            if self.thisown: destroy(self)
        except: pass

class txt_qPtr(txt_q):
    def __init__(self, this):
        _swig_setattr(self, txt_q, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, txt_q, 'thisown', 0)
        _swig_setattr(self, txt_q,self.__class__,txt_q)
_server.txt_q_swigregister(txt_qPtr)

class descriptor_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, descriptor_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, descriptor_data, name)
    def __repr__(self):
        return "<C descriptor_data instance at %s>" % (self.this,)
    __swig_setmethods__["descriptor"] = _server.descriptor_data_descriptor_set
    __swig_getmethods__["descriptor"] = _server.descriptor_data_descriptor_get
    if _newclass:descriptor = property(_server.descriptor_data_descriptor_get, _server.descriptor_data_descriptor_set)
    __swig_setmethods__["host"] = _server.descriptor_data_host_set
    __swig_getmethods__["host"] = _server.descriptor_data_host_get
    if _newclass:host = property(_server.descriptor_data_host_get, _server.descriptor_data_host_set)
    __swig_setmethods__["bad_pws"] = _server.descriptor_data_bad_pws_set
    __swig_getmethods__["bad_pws"] = _server.descriptor_data_bad_pws_get
    if _newclass:bad_pws = property(_server.descriptor_data_bad_pws_get, _server.descriptor_data_bad_pws_set)
    __swig_setmethods__["idle_tics"] = _server.descriptor_data_idle_tics_set
    __swig_getmethods__["idle_tics"] = _server.descriptor_data_idle_tics_get
    if _newclass:idle_tics = property(_server.descriptor_data_idle_tics_get, _server.descriptor_data_idle_tics_set)
    __swig_setmethods__["connected"] = _server.descriptor_data_connected_set
    __swig_getmethods__["connected"] = _server.descriptor_data_connected_get
    if _newclass:connected = property(_server.descriptor_data_connected_get, _server.descriptor_data_connected_set)
    __swig_setmethods__["desc_num"] = _server.descriptor_data_desc_num_set
    __swig_getmethods__["desc_num"] = _server.descriptor_data_desc_num_get
    if _newclass:desc_num = property(_server.descriptor_data_desc_num_get, _server.descriptor_data_desc_num_set)
    __swig_setmethods__["login_time"] = _server.descriptor_data_login_time_set
    __swig_getmethods__["login_time"] = _server.descriptor_data_login_time_get
    if _newclass:login_time = property(_server.descriptor_data_login_time_get, _server.descriptor_data_login_time_set)
    __swig_setmethods__["showstr_head"] = _server.descriptor_data_showstr_head_set
    __swig_getmethods__["showstr_head"] = _server.descriptor_data_showstr_head_get
    if _newclass:showstr_head = property(_server.descriptor_data_showstr_head_get, _server.descriptor_data_showstr_head_set)
    __swig_setmethods__["showstr_vector"] = _server.descriptor_data_showstr_vector_set
    __swig_getmethods__["showstr_vector"] = _server.descriptor_data_showstr_vector_get
    if _newclass:showstr_vector = property(_server.descriptor_data_showstr_vector_get, _server.descriptor_data_showstr_vector_set)
    __swig_setmethods__["showstr_count"] = _server.descriptor_data_showstr_count_set
    __swig_getmethods__["showstr_count"] = _server.descriptor_data_showstr_count_get
    if _newclass:showstr_count = property(_server.descriptor_data_showstr_count_get, _server.descriptor_data_showstr_count_set)
    __swig_setmethods__["showstr_page"] = _server.descriptor_data_showstr_page_set
    __swig_getmethods__["showstr_page"] = _server.descriptor_data_showstr_page_get
    if _newclass:showstr_page = property(_server.descriptor_data_showstr_page_get, _server.descriptor_data_showstr_page_set)
    __swig_setmethods__["str"] = _server.descriptor_data_str_set
    __swig_getmethods__["str"] = _server.descriptor_data_str_get
    if _newclass:str = property(_server.descriptor_data_str_get, _server.descriptor_data_str_set)
    __swig_setmethods__["backstr"] = _server.descriptor_data_backstr_set
    __swig_getmethods__["backstr"] = _server.descriptor_data_backstr_get
    if _newclass:backstr = property(_server.descriptor_data_backstr_get, _server.descriptor_data_backstr_set)
    __swig_setmethods__["max_str"] = _server.descriptor_data_max_str_set
    __swig_getmethods__["max_str"] = _server.descriptor_data_max_str_get
    if _newclass:max_str = property(_server.descriptor_data_max_str_get, _server.descriptor_data_max_str_set)
    __swig_setmethods__["mail_to"] = _server.descriptor_data_mail_to_set
    __swig_getmethods__["mail_to"] = _server.descriptor_data_mail_to_get
    if _newclass:mail_to = property(_server.descriptor_data_mail_to_get, _server.descriptor_data_mail_to_set)
    __swig_setmethods__["has_prompt"] = _server.descriptor_data_has_prompt_set
    __swig_getmethods__["has_prompt"] = _server.descriptor_data_has_prompt_get
    if _newclass:has_prompt = property(_server.descriptor_data_has_prompt_get, _server.descriptor_data_has_prompt_set)
    __swig_setmethods__["inbuf"] = _server.descriptor_data_inbuf_set
    __swig_getmethods__["inbuf"] = _server.descriptor_data_inbuf_get
    if _newclass:inbuf = property(_server.descriptor_data_inbuf_get, _server.descriptor_data_inbuf_set)
    __swig_setmethods__["last_input"] = _server.descriptor_data_last_input_set
    __swig_getmethods__["last_input"] = _server.descriptor_data_last_input_get
    if _newclass:last_input = property(_server.descriptor_data_last_input_get, _server.descriptor_data_last_input_set)
    __swig_setmethods__["small_outbuf"] = _server.descriptor_data_small_outbuf_set
    __swig_getmethods__["small_outbuf"] = _server.descriptor_data_small_outbuf_get
    if _newclass:small_outbuf = property(_server.descriptor_data_small_outbuf_get, _server.descriptor_data_small_outbuf_set)
    __swig_setmethods__["output"] = _server.descriptor_data_output_set
    __swig_getmethods__["output"] = _server.descriptor_data_output_get
    if _newclass:output = property(_server.descriptor_data_output_get, _server.descriptor_data_output_set)
    __swig_setmethods__["history"] = _server.descriptor_data_history_set
    __swig_getmethods__["history"] = _server.descriptor_data_history_get
    if _newclass:history = property(_server.descriptor_data_history_get, _server.descriptor_data_history_set)
    __swig_setmethods__["history_pos"] = _server.descriptor_data_history_pos_set
    __swig_getmethods__["history_pos"] = _server.descriptor_data_history_pos_get
    if _newclass:history_pos = property(_server.descriptor_data_history_pos_get, _server.descriptor_data_history_pos_set)
    __swig_setmethods__["bufptr"] = _server.descriptor_data_bufptr_set
    __swig_getmethods__["bufptr"] = _server.descriptor_data_bufptr_get
    if _newclass:bufptr = property(_server.descriptor_data_bufptr_get, _server.descriptor_data_bufptr_set)
    __swig_setmethods__["bufspace"] = _server.descriptor_data_bufspace_set
    __swig_getmethods__["bufspace"] = _server.descriptor_data_bufspace_get
    if _newclass:bufspace = property(_server.descriptor_data_bufspace_get, _server.descriptor_data_bufspace_set)
    __swig_setmethods__["large_outbuf"] = _server.descriptor_data_large_outbuf_set
    __swig_getmethods__["large_outbuf"] = _server.descriptor_data_large_outbuf_get
    if _newclass:large_outbuf = property(_server.descriptor_data_large_outbuf_get, _server.descriptor_data_large_outbuf_set)
    __swig_setmethods__["input"] = _server.descriptor_data_input_set
    __swig_getmethods__["input"] = _server.descriptor_data_input_get
    if _newclass:input = property(_server.descriptor_data_input_get, _server.descriptor_data_input_set)
    __swig_setmethods__["character"] = _server.descriptor_data_character_set
    __swig_getmethods__["character"] = _server.descriptor_data_character_get
    if _newclass:character = property(_server.descriptor_data_character_get, _server.descriptor_data_character_set)
    __swig_setmethods__["original"] = _server.descriptor_data_original_set
    __swig_getmethods__["original"] = _server.descriptor_data_original_get
    if _newclass:original = property(_server.descriptor_data_original_get, _server.descriptor_data_original_set)
    __swig_setmethods__["snooping"] = _server.descriptor_data_snooping_set
    __swig_getmethods__["snooping"] = _server.descriptor_data_snooping_get
    if _newclass:snooping = property(_server.descriptor_data_snooping_get, _server.descriptor_data_snooping_set)
    __swig_setmethods__["snoop_by"] = _server.descriptor_data_snoop_by_set
    __swig_getmethods__["snoop_by"] = _server.descriptor_data_snoop_by_get
    if _newclass:snoop_by = property(_server.descriptor_data_snoop_by_get, _server.descriptor_data_snoop_by_set)
    __swig_setmethods__["next"] = _server.descriptor_data_next_set
    __swig_getmethods__["next"] = _server.descriptor_data_next_get
    if _newclass:next = property(_server.descriptor_data_next_get, _server.descriptor_data_next_set)
    __swig_setmethods__["olc"] = _server.descriptor_data_olc_set
    __swig_getmethods__["olc"] = _server.descriptor_data_olc_get
    if _newclass:olc = property(_server.descriptor_data_olc_get, _server.descriptor_data_olc_set)
    def __init__(self, *args):
        _swig_setattr(self, descriptor_data, 'this', _server.new_descriptor_data(*args))
        _swig_setattr(self, descriptor_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_descriptor_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class descriptor_dataPtr(descriptor_data):
    def __init__(self, this):
        _swig_setattr(self, descriptor_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, descriptor_data, 'thisown', 0)
        _swig_setattr(self, descriptor_data,self.__class__,descriptor_data)
_server.descriptor_data_swigregister(descriptor_dataPtr)

class msg_type(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, msg_type, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, msg_type, name)
    def __repr__(self):
        return "<C msg_type instance at %s>" % (self.this,)
    __swig_setmethods__["attacker_msg"] = _server.msg_type_attacker_msg_set
    __swig_getmethods__["attacker_msg"] = _server.msg_type_attacker_msg_get
    if _newclass:attacker_msg = property(_server.msg_type_attacker_msg_get, _server.msg_type_attacker_msg_set)
    __swig_setmethods__["victim_msg"] = _server.msg_type_victim_msg_set
    __swig_getmethods__["victim_msg"] = _server.msg_type_victim_msg_get
    if _newclass:victim_msg = property(_server.msg_type_victim_msg_get, _server.msg_type_victim_msg_set)
    __swig_setmethods__["room_msg"] = _server.msg_type_room_msg_set
    __swig_getmethods__["room_msg"] = _server.msg_type_room_msg_get
    if _newclass:room_msg = property(_server.msg_type_room_msg_get, _server.msg_type_room_msg_set)
    def __init__(self, *args):
        _swig_setattr(self, msg_type, 'this', _server.new_msg_type(*args))
        _swig_setattr(self, msg_type, 'thisown', 1)
    def __del__(self, destroy=_server.delete_msg_type):
        try:
            if self.thisown: destroy(self)
        except: pass

class msg_typePtr(msg_type):
    def __init__(self, this):
        _swig_setattr(self, msg_type, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, msg_type, 'thisown', 0)
        _swig_setattr(self, msg_type,self.__class__,msg_type)
_server.msg_type_swigregister(msg_typePtr)

class message_type(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, message_type, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, message_type, name)
    def __repr__(self):
        return "<C message_type instance at %s>" % (self.this,)
    __swig_setmethods__["die_msg"] = _server.message_type_die_msg_set
    __swig_getmethods__["die_msg"] = _server.message_type_die_msg_get
    if _newclass:die_msg = property(_server.message_type_die_msg_get, _server.message_type_die_msg_set)
    __swig_setmethods__["miss_msg"] = _server.message_type_miss_msg_set
    __swig_getmethods__["miss_msg"] = _server.message_type_miss_msg_get
    if _newclass:miss_msg = property(_server.message_type_miss_msg_get, _server.message_type_miss_msg_set)
    __swig_setmethods__["hit_msg"] = _server.message_type_hit_msg_set
    __swig_getmethods__["hit_msg"] = _server.message_type_hit_msg_get
    if _newclass:hit_msg = property(_server.message_type_hit_msg_get, _server.message_type_hit_msg_set)
    __swig_setmethods__["god_msg"] = _server.message_type_god_msg_set
    __swig_getmethods__["god_msg"] = _server.message_type_god_msg_get
    if _newclass:god_msg = property(_server.message_type_god_msg_get, _server.message_type_god_msg_set)
    __swig_setmethods__["next"] = _server.message_type_next_set
    __swig_getmethods__["next"] = _server.message_type_next_get
    if _newclass:next = property(_server.message_type_next_get, _server.message_type_next_set)
    def __init__(self, *args):
        _swig_setattr(self, message_type, 'this', _server.new_message_type(*args))
        _swig_setattr(self, message_type, 'thisown', 1)
    def __del__(self, destroy=_server.delete_message_type):
        try:
            if self.thisown: destroy(self)
        except: pass

class message_typePtr(message_type):
    def __init__(self, this):
        _swig_setattr(self, message_type, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, message_type, 'thisown', 0)
        _swig_setattr(self, message_type,self.__class__,message_type)
_server.message_type_swigregister(message_typePtr)

class message_list(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, message_list, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, message_list, name)
    def __repr__(self):
        return "<C message_list instance at %s>" % (self.this,)
    __swig_setmethods__["a_type"] = _server.message_list_a_type_set
    __swig_getmethods__["a_type"] = _server.message_list_a_type_get
    if _newclass:a_type = property(_server.message_list_a_type_get, _server.message_list_a_type_set)
    __swig_setmethods__["number_of_attacks"] = _server.message_list_number_of_attacks_set
    __swig_getmethods__["number_of_attacks"] = _server.message_list_number_of_attacks_get
    if _newclass:number_of_attacks = property(_server.message_list_number_of_attacks_get, _server.message_list_number_of_attacks_set)
    __swig_setmethods__["msg"] = _server.message_list_msg_set
    __swig_getmethods__["msg"] = _server.message_list_msg_get
    if _newclass:msg = property(_server.message_list_msg_get, _server.message_list_msg_set)
    def __init__(self, *args):
        _swig_setattr(self, message_list, 'this', _server.new_message_list(*args))
        _swig_setattr(self, message_list, 'thisown', 1)
    def __del__(self, destroy=_server.delete_message_list):
        try:
            if self.thisown: destroy(self)
        except: pass

class message_listPtr(message_list):
    def __init__(self, this):
        _swig_setattr(self, message_list, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, message_list, 'thisown', 0)
        _swig_setattr(self, message_list,self.__class__,message_list)
_server.message_list_swigregister(message_listPtr)

class dex_skill_type(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dex_skill_type, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dex_skill_type, name)
    def __repr__(self):
        return "<C dex_skill_type instance at %s>" % (self.this,)
    __swig_setmethods__["p_pocket"] = _server.dex_skill_type_p_pocket_set
    __swig_getmethods__["p_pocket"] = _server.dex_skill_type_p_pocket_get
    if _newclass:p_pocket = property(_server.dex_skill_type_p_pocket_get, _server.dex_skill_type_p_pocket_set)
    __swig_setmethods__["p_locks"] = _server.dex_skill_type_p_locks_set
    __swig_getmethods__["p_locks"] = _server.dex_skill_type_p_locks_get
    if _newclass:p_locks = property(_server.dex_skill_type_p_locks_get, _server.dex_skill_type_p_locks_set)
    __swig_setmethods__["traps"] = _server.dex_skill_type_traps_set
    __swig_getmethods__["traps"] = _server.dex_skill_type_traps_get
    if _newclass:traps = property(_server.dex_skill_type_traps_get, _server.dex_skill_type_traps_set)
    __swig_setmethods__["sneak"] = _server.dex_skill_type_sneak_set
    __swig_getmethods__["sneak"] = _server.dex_skill_type_sneak_get
    if _newclass:sneak = property(_server.dex_skill_type_sneak_get, _server.dex_skill_type_sneak_set)
    __swig_setmethods__["hide"] = _server.dex_skill_type_hide_set
    __swig_getmethods__["hide"] = _server.dex_skill_type_hide_get
    if _newclass:hide = property(_server.dex_skill_type_hide_get, _server.dex_skill_type_hide_set)
    def __init__(self, *args):
        _swig_setattr(self, dex_skill_type, 'this', _server.new_dex_skill_type(*args))
        _swig_setattr(self, dex_skill_type, 'thisown', 1)
    def __del__(self, destroy=_server.delete_dex_skill_type):
        try:
            if self.thisown: destroy(self)
        except: pass

class dex_skill_typePtr(dex_skill_type):
    def __init__(self, this):
        _swig_setattr(self, dex_skill_type, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, dex_skill_type, 'thisown', 0)
        _swig_setattr(self, dex_skill_type,self.__class__,dex_skill_type)
_server.dex_skill_type_swigregister(dex_skill_typePtr)

class dex_app_type(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dex_app_type, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dex_app_type, name)
    def __repr__(self):
        return "<C dex_app_type instance at %s>" % (self.this,)
    __swig_setmethods__["reaction"] = _server.dex_app_type_reaction_set
    __swig_getmethods__["reaction"] = _server.dex_app_type_reaction_get
    if _newclass:reaction = property(_server.dex_app_type_reaction_get, _server.dex_app_type_reaction_set)
    __swig_setmethods__["miss_att"] = _server.dex_app_type_miss_att_set
    __swig_getmethods__["miss_att"] = _server.dex_app_type_miss_att_get
    if _newclass:miss_att = property(_server.dex_app_type_miss_att_get, _server.dex_app_type_miss_att_set)
    __swig_setmethods__["defensive"] = _server.dex_app_type_defensive_set
    __swig_getmethods__["defensive"] = _server.dex_app_type_defensive_get
    if _newclass:defensive = property(_server.dex_app_type_defensive_get, _server.dex_app_type_defensive_set)
    def __init__(self, *args):
        _swig_setattr(self, dex_app_type, 'this', _server.new_dex_app_type(*args))
        _swig_setattr(self, dex_app_type, 'thisown', 1)
    def __del__(self, destroy=_server.delete_dex_app_type):
        try:
            if self.thisown: destroy(self)
        except: pass

class dex_app_typePtr(dex_app_type):
    def __init__(self, this):
        _swig_setattr(self, dex_app_type, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, dex_app_type, 'thisown', 0)
        _swig_setattr(self, dex_app_type,self.__class__,dex_app_type)
_server.dex_app_type_swigregister(dex_app_typePtr)

class str_app_type(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, str_app_type, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, str_app_type, name)
    def __repr__(self):
        return "<C str_app_type instance at %s>" % (self.this,)
    __swig_setmethods__["tohit"] = _server.str_app_type_tohit_set
    __swig_getmethods__["tohit"] = _server.str_app_type_tohit_get
    if _newclass:tohit = property(_server.str_app_type_tohit_get, _server.str_app_type_tohit_set)
    __swig_setmethods__["todam"] = _server.str_app_type_todam_set
    __swig_getmethods__["todam"] = _server.str_app_type_todam_get
    if _newclass:todam = property(_server.str_app_type_todam_get, _server.str_app_type_todam_set)
    __swig_setmethods__["carry_w"] = _server.str_app_type_carry_w_set
    __swig_getmethods__["carry_w"] = _server.str_app_type_carry_w_get
    if _newclass:carry_w = property(_server.str_app_type_carry_w_get, _server.str_app_type_carry_w_set)
    __swig_setmethods__["wield_w"] = _server.str_app_type_wield_w_set
    __swig_getmethods__["wield_w"] = _server.str_app_type_wield_w_get
    if _newclass:wield_w = property(_server.str_app_type_wield_w_get, _server.str_app_type_wield_w_set)
    def __init__(self, *args):
        _swig_setattr(self, str_app_type, 'this', _server.new_str_app_type(*args))
        _swig_setattr(self, str_app_type, 'thisown', 1)
    def __del__(self, destroy=_server.delete_str_app_type):
        try:
            if self.thisown: destroy(self)
        except: pass

class str_app_typePtr(str_app_type):
    def __init__(self, this):
        _swig_setattr(self, str_app_type, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, str_app_type, 'thisown', 0)
        _swig_setattr(self, str_app_type,self.__class__,str_app_type)
_server.str_app_type_swigregister(str_app_typePtr)

class wis_app_type(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, wis_app_type, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, wis_app_type, name)
    def __repr__(self):
        return "<C wis_app_type instance at %s>" % (self.this,)
    __swig_setmethods__["bonus"] = _server.wis_app_type_bonus_set
    __swig_getmethods__["bonus"] = _server.wis_app_type_bonus_get
    if _newclass:bonus = property(_server.wis_app_type_bonus_get, _server.wis_app_type_bonus_set)
    def __init__(self, *args):
        _swig_setattr(self, wis_app_type, 'this', _server.new_wis_app_type(*args))
        _swig_setattr(self, wis_app_type, 'thisown', 1)
    def __del__(self, destroy=_server.delete_wis_app_type):
        try:
            if self.thisown: destroy(self)
        except: pass

class wis_app_typePtr(wis_app_type):
    def __init__(self, this):
        _swig_setattr(self, wis_app_type, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, wis_app_type, 'thisown', 0)
        _swig_setattr(self, wis_app_type,self.__class__,wis_app_type)
_server.wis_app_type_swigregister(wis_app_typePtr)

class int_app_type(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, int_app_type, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, int_app_type, name)
    def __repr__(self):
        return "<C int_app_type instance at %s>" % (self.this,)
    __swig_setmethods__["learn"] = _server.int_app_type_learn_set
    __swig_getmethods__["learn"] = _server.int_app_type_learn_get
    if _newclass:learn = property(_server.int_app_type_learn_get, _server.int_app_type_learn_set)
    def __init__(self, *args):
        _swig_setattr(self, int_app_type, 'this', _server.new_int_app_type(*args))
        _swig_setattr(self, int_app_type, 'thisown', 1)
    def __del__(self, destroy=_server.delete_int_app_type):
        try:
            if self.thisown: destroy(self)
        except: pass

class int_app_typePtr(int_app_type):
    def __init__(self, this):
        _swig_setattr(self, int_app_type, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, int_app_type, 'thisown', 0)
        _swig_setattr(self, int_app_type,self.__class__,int_app_type)
_server.int_app_type_swigregister(int_app_typePtr)

class con_app_type(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, con_app_type, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, con_app_type, name)
    def __repr__(self):
        return "<C con_app_type instance at %s>" % (self.this,)
    __swig_setmethods__["hitp"] = _server.con_app_type_hitp_set
    __swig_getmethods__["hitp"] = _server.con_app_type_hitp_get
    if _newclass:hitp = property(_server.con_app_type_hitp_get, _server.con_app_type_hitp_set)
    __swig_setmethods__["shock"] = _server.con_app_type_shock_set
    __swig_getmethods__["shock"] = _server.con_app_type_shock_get
    if _newclass:shock = property(_server.con_app_type_shock_get, _server.con_app_type_shock_set)
    def __init__(self, *args):
        _swig_setattr(self, con_app_type, 'this', _server.new_con_app_type(*args))
        _swig_setattr(self, con_app_type, 'thisown', 1)
    def __del__(self, destroy=_server.delete_con_app_type):
        try:
            if self.thisown: destroy(self)
        except: pass

class con_app_typePtr(con_app_type):
    def __init__(self, this):
        _swig_setattr(self, con_app_type, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, con_app_type, 'thisown', 0)
        _swig_setattr(self, con_app_type,self.__class__,con_app_type)
_server.con_app_type_swigregister(con_app_typePtr)

class weather_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, weather_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, weather_data, name)
    def __repr__(self):
        return "<C weather_data instance at %s>" % (self.this,)
    __swig_setmethods__["pressure"] = _server.weather_data_pressure_set
    __swig_getmethods__["pressure"] = _server.weather_data_pressure_get
    if _newclass:pressure = property(_server.weather_data_pressure_get, _server.weather_data_pressure_set)
    __swig_setmethods__["change"] = _server.weather_data_change_set
    __swig_getmethods__["change"] = _server.weather_data_change_get
    if _newclass:change = property(_server.weather_data_change_get, _server.weather_data_change_set)
    __swig_setmethods__["sky"] = _server.weather_data_sky_set
    __swig_getmethods__["sky"] = _server.weather_data_sky_get
    if _newclass:sky = property(_server.weather_data_sky_get, _server.weather_data_sky_set)
    __swig_setmethods__["sunlight"] = _server.weather_data_sunlight_set
    __swig_getmethods__["sunlight"] = _server.weather_data_sunlight_get
    if _newclass:sunlight = property(_server.weather_data_sunlight_get, _server.weather_data_sunlight_set)
    def __init__(self, *args):
        _swig_setattr(self, weather_data, 'this', _server.new_weather_data(*args))
        _swig_setattr(self, weather_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_weather_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class weather_dataPtr(weather_data):
    def __init__(self, this):
        _swig_setattr(self, weather_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, weather_data, 'thisown', 0)
        _swig_setattr(self, weather_data,self.__class__,weather_data)
_server.weather_data_swigregister(weather_dataPtr)

class index_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, index_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, index_data, name)
    def __repr__(self):
        return "<C index_data instance at %s>" % (self.this,)
    __swig_setmethods__["vnum"] = _server.index_data_vnum_set
    __swig_getmethods__["vnum"] = _server.index_data_vnum_get
    if _newclass:vnum = property(_server.index_data_vnum_get, _server.index_data_vnum_set)
    __swig_setmethods__["number"] = _server.index_data_number_set
    __swig_getmethods__["number"] = _server.index_data_number_get
    if _newclass:number = property(_server.index_data_number_get, _server.index_data_number_set)
    __swig_setmethods__["func"] = _server.index_data_func_set
    __swig_getmethods__["func"] = _server.index_data_func_get
    if _newclass:func = property(_server.index_data_func_get, _server.index_data_func_set)
    __swig_setmethods__["farg"] = _server.index_data_farg_set
    __swig_getmethods__["farg"] = _server.index_data_farg_get
    if _newclass:farg = property(_server.index_data_farg_get, _server.index_data_farg_set)
    __swig_setmethods__["proto"] = _server.index_data_proto_set
    __swig_getmethods__["proto"] = _server.index_data_proto_get
    if _newclass:proto = property(_server.index_data_proto_get, _server.index_data_proto_set)
    def __init__(self, *args):
        _swig_setattr(self, index_data, 'this', _server.new_index_data(*args))
        _swig_setattr(self, index_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_index_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class index_dataPtr(index_data):
    def __init__(self, this):
        _swig_setattr(self, index_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, index_data, 'thisown', 0)
        _swig_setattr(self, index_data,self.__class__,index_data)
_server.index_data_swigregister(index_dataPtr)

class trig_proto_list(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, trig_proto_list, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, trig_proto_list, name)
    def __repr__(self):
        return "<C trig_proto_list instance at %s>" % (self.this,)
    __swig_setmethods__["vnum"] = _server.trig_proto_list_vnum_set
    __swig_getmethods__["vnum"] = _server.trig_proto_list_vnum_get
    if _newclass:vnum = property(_server.trig_proto_list_vnum_get, _server.trig_proto_list_vnum_set)
    __swig_setmethods__["next"] = _server.trig_proto_list_next_set
    __swig_getmethods__["next"] = _server.trig_proto_list_next_get
    if _newclass:next = property(_server.trig_proto_list_next_get, _server.trig_proto_list_next_set)
    def __init__(self, *args):
        _swig_setattr(self, trig_proto_list, 'this', _server.new_trig_proto_list(*args))
        _swig_setattr(self, trig_proto_list, 'thisown', 1)
    def __del__(self, destroy=_server.delete_trig_proto_list):
        try:
            if self.thisown: destroy(self)
        except: pass

class trig_proto_listPtr(trig_proto_list):
    def __init__(self, this):
        _swig_setattr(self, trig_proto_list, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, trig_proto_list, 'thisown', 0)
        _swig_setattr(self, trig_proto_list,self.__class__,trig_proto_list)
_server.trig_proto_list_swigregister(trig_proto_listPtr)

class guild_info_type(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, guild_info_type, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, guild_info_type, name)
    def __repr__(self):
        return "<C guild_info_type instance at %s>" % (self.this,)
    __swig_setmethods__["pc_class"] = _server.guild_info_type_pc_class_set
    __swig_getmethods__["pc_class"] = _server.guild_info_type_pc_class_get
    if _newclass:pc_class = property(_server.guild_info_type_pc_class_get, _server.guild_info_type_pc_class_set)
    __swig_setmethods__["guild_room"] = _server.guild_info_type_guild_room_set
    __swig_getmethods__["guild_room"] = _server.guild_info_type_guild_room_get
    if _newclass:guild_room = property(_server.guild_info_type_guild_room_get, _server.guild_info_type_guild_room_set)
    __swig_setmethods__["direction"] = _server.guild_info_type_direction_set
    __swig_getmethods__["direction"] = _server.guild_info_type_direction_get
    if _newclass:direction = property(_server.guild_info_type_direction_get, _server.guild_info_type_direction_set)
    def __init__(self, *args):
        _swig_setattr(self, guild_info_type, 'this', _server.new_guild_info_type(*args))
        _swig_setattr(self, guild_info_type, 'thisown', 1)
    def __del__(self, destroy=_server.delete_guild_info_type):
        try:
            if self.thisown: destroy(self)
        except: pass

class guild_info_typePtr(guild_info_type):
    def __init__(self, this):
        _swig_setattr(self, guild_info_type, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, guild_info_type, 'thisown', 0)
        _swig_setattr(self, guild_info_type,self.__class__,guild_info_type)
_server.guild_info_type_swigregister(guild_info_typePtr)

class game_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, game_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, game_data, name)
    def __repr__(self):
        return "<C game_data instance at %s>" % (self.this,)
    __swig_setmethods__["pk_allowed"] = _server.game_data_pk_allowed_set
    __swig_getmethods__["pk_allowed"] = _server.game_data_pk_allowed_get
    if _newclass:pk_allowed = property(_server.game_data_pk_allowed_get, _server.game_data_pk_allowed_set)
    __swig_setmethods__["pt_allowed"] = _server.game_data_pt_allowed_set
    __swig_getmethods__["pt_allowed"] = _server.game_data_pt_allowed_get
    if _newclass:pt_allowed = property(_server.game_data_pt_allowed_get, _server.game_data_pt_allowed_set)
    __swig_setmethods__["level_can_shout"] = _server.game_data_level_can_shout_set
    __swig_getmethods__["level_can_shout"] = _server.game_data_level_can_shout_get
    if _newclass:level_can_shout = property(_server.game_data_level_can_shout_get, _server.game_data_level_can_shout_set)
    __swig_setmethods__["holler_move_cost"] = _server.game_data_holler_move_cost_set
    __swig_getmethods__["holler_move_cost"] = _server.game_data_holler_move_cost_get
    if _newclass:holler_move_cost = property(_server.game_data_holler_move_cost_get, _server.game_data_holler_move_cost_set)
    __swig_setmethods__["tunnel_size"] = _server.game_data_tunnel_size_set
    __swig_getmethods__["tunnel_size"] = _server.game_data_tunnel_size_get
    if _newclass:tunnel_size = property(_server.game_data_tunnel_size_get, _server.game_data_tunnel_size_set)
    __swig_setmethods__["max_exp_gain"] = _server.game_data_max_exp_gain_set
    __swig_getmethods__["max_exp_gain"] = _server.game_data_max_exp_gain_get
    if _newclass:max_exp_gain = property(_server.game_data_max_exp_gain_get, _server.game_data_max_exp_gain_set)
    __swig_setmethods__["max_exp_loss"] = _server.game_data_max_exp_loss_set
    __swig_getmethods__["max_exp_loss"] = _server.game_data_max_exp_loss_get
    if _newclass:max_exp_loss = property(_server.game_data_max_exp_loss_get, _server.game_data_max_exp_loss_set)
    __swig_setmethods__["max_npc_corpse_time"] = _server.game_data_max_npc_corpse_time_set
    __swig_getmethods__["max_npc_corpse_time"] = _server.game_data_max_npc_corpse_time_get
    if _newclass:max_npc_corpse_time = property(_server.game_data_max_npc_corpse_time_get, _server.game_data_max_npc_corpse_time_set)
    __swig_setmethods__["max_pc_corpse_time"] = _server.game_data_max_pc_corpse_time_set
    __swig_getmethods__["max_pc_corpse_time"] = _server.game_data_max_pc_corpse_time_get
    if _newclass:max_pc_corpse_time = property(_server.game_data_max_pc_corpse_time_get, _server.game_data_max_pc_corpse_time_set)
    __swig_setmethods__["idle_void"] = _server.game_data_idle_void_set
    __swig_getmethods__["idle_void"] = _server.game_data_idle_void_get
    if _newclass:idle_void = property(_server.game_data_idle_void_get, _server.game_data_idle_void_set)
    __swig_setmethods__["idle_rent_time"] = _server.game_data_idle_rent_time_set
    __swig_getmethods__["idle_rent_time"] = _server.game_data_idle_rent_time_get
    if _newclass:idle_rent_time = property(_server.game_data_idle_rent_time_get, _server.game_data_idle_rent_time_set)
    __swig_setmethods__["idle_max_level"] = _server.game_data_idle_max_level_set
    __swig_getmethods__["idle_max_level"] = _server.game_data_idle_max_level_get
    if _newclass:idle_max_level = property(_server.game_data_idle_max_level_get, _server.game_data_idle_max_level_set)
    __swig_setmethods__["dts_are_dumps"] = _server.game_data_dts_are_dumps_set
    __swig_getmethods__["dts_are_dumps"] = _server.game_data_dts_are_dumps_get
    if _newclass:dts_are_dumps = property(_server.game_data_dts_are_dumps_get, _server.game_data_dts_are_dumps_set)
    __swig_setmethods__["load_into_inventory"] = _server.game_data_load_into_inventory_set
    __swig_getmethods__["load_into_inventory"] = _server.game_data_load_into_inventory_get
    if _newclass:load_into_inventory = property(_server.game_data_load_into_inventory_get, _server.game_data_load_into_inventory_set)
    __swig_setmethods__["track_through_doors"] = _server.game_data_track_through_doors_set
    __swig_getmethods__["track_through_doors"] = _server.game_data_track_through_doors_get
    if _newclass:track_through_doors = property(_server.game_data_track_through_doors_get, _server.game_data_track_through_doors_set)
    __swig_setmethods__["immort_level_ok"] = _server.game_data_immort_level_ok_set
    __swig_getmethods__["immort_level_ok"] = _server.game_data_immort_level_ok_get
    if _newclass:immort_level_ok = property(_server.game_data_immort_level_ok_get, _server.game_data_immort_level_ok_set)
    __swig_setmethods__["OK"] = _server.game_data_OK_set
    __swig_getmethods__["OK"] = _server.game_data_OK_get
    if _newclass:OK = property(_server.game_data_OK_get, _server.game_data_OK_set)
    __swig_setmethods__["NOPERSON"] = _server.game_data_NOPERSON_set
    __swig_getmethods__["NOPERSON"] = _server.game_data_NOPERSON_get
    if _newclass:NOPERSON = property(_server.game_data_NOPERSON_get, _server.game_data_NOPERSON_set)
    __swig_setmethods__["NOEFFECT"] = _server.game_data_NOEFFECT_set
    __swig_getmethods__["NOEFFECT"] = _server.game_data_NOEFFECT_get
    if _newclass:NOEFFECT = property(_server.game_data_NOEFFECT_get, _server.game_data_NOEFFECT_set)
    def __init__(self, *args):
        _swig_setattr(self, game_data, 'this', _server.new_game_data(*args))
        _swig_setattr(self, game_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_game_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class game_dataPtr(game_data):
    def __init__(self, this):
        _swig_setattr(self, game_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, game_data, 'thisown', 0)
        _swig_setattr(self, game_data,self.__class__,game_data)
_server.game_data_swigregister(game_dataPtr)

class crash_save_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, crash_save_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, crash_save_data, name)
    def __repr__(self):
        return "<C crash_save_data instance at %s>" % (self.this,)
    __swig_setmethods__["free_rent"] = _server.crash_save_data_free_rent_set
    __swig_getmethods__["free_rent"] = _server.crash_save_data_free_rent_get
    if _newclass:free_rent = property(_server.crash_save_data_free_rent_get, _server.crash_save_data_free_rent_set)
    __swig_setmethods__["max_obj_save"] = _server.crash_save_data_max_obj_save_set
    __swig_getmethods__["max_obj_save"] = _server.crash_save_data_max_obj_save_get
    if _newclass:max_obj_save = property(_server.crash_save_data_max_obj_save_get, _server.crash_save_data_max_obj_save_set)
    __swig_setmethods__["min_rent_cost"] = _server.crash_save_data_min_rent_cost_set
    __swig_getmethods__["min_rent_cost"] = _server.crash_save_data_min_rent_cost_get
    if _newclass:min_rent_cost = property(_server.crash_save_data_min_rent_cost_get, _server.crash_save_data_min_rent_cost_set)
    __swig_setmethods__["auto_save"] = _server.crash_save_data_auto_save_set
    __swig_getmethods__["auto_save"] = _server.crash_save_data_auto_save_get
    if _newclass:auto_save = property(_server.crash_save_data_auto_save_get, _server.crash_save_data_auto_save_set)
    __swig_setmethods__["autosave_time"] = _server.crash_save_data_autosave_time_set
    __swig_getmethods__["autosave_time"] = _server.crash_save_data_autosave_time_get
    if _newclass:autosave_time = property(_server.crash_save_data_autosave_time_get, _server.crash_save_data_autosave_time_set)
    __swig_setmethods__["crash_file_timeout"] = _server.crash_save_data_crash_file_timeout_set
    __swig_getmethods__["crash_file_timeout"] = _server.crash_save_data_crash_file_timeout_get
    if _newclass:crash_file_timeout = property(_server.crash_save_data_crash_file_timeout_get, _server.crash_save_data_crash_file_timeout_set)
    __swig_setmethods__["rent_file_timeout"] = _server.crash_save_data_rent_file_timeout_set
    __swig_getmethods__["rent_file_timeout"] = _server.crash_save_data_rent_file_timeout_get
    if _newclass:rent_file_timeout = property(_server.crash_save_data_rent_file_timeout_get, _server.crash_save_data_rent_file_timeout_set)
    def __init__(self, *args):
        _swig_setattr(self, crash_save_data, 'this', _server.new_crash_save_data(*args))
        _swig_setattr(self, crash_save_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_crash_save_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class crash_save_dataPtr(crash_save_data):
    def __init__(self, this):
        _swig_setattr(self, crash_save_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, crash_save_data, 'thisown', 0)
        _swig_setattr(self, crash_save_data,self.__class__,crash_save_data)
_server.crash_save_data_swigregister(crash_save_dataPtr)

class room_numbers(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, room_numbers, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, room_numbers, name)
    def __repr__(self):
        return "<C room_numbers instance at %s>" % (self.this,)
    __swig_setmethods__["mortal_start_room"] = _server.room_numbers_mortal_start_room_set
    __swig_getmethods__["mortal_start_room"] = _server.room_numbers_mortal_start_room_get
    if _newclass:mortal_start_room = property(_server.room_numbers_mortal_start_room_get, _server.room_numbers_mortal_start_room_set)
    __swig_setmethods__["immort_start_room"] = _server.room_numbers_immort_start_room_set
    __swig_getmethods__["immort_start_room"] = _server.room_numbers_immort_start_room_get
    if _newclass:immort_start_room = property(_server.room_numbers_immort_start_room_get, _server.room_numbers_immort_start_room_set)
    __swig_setmethods__["frozen_start_room"] = _server.room_numbers_frozen_start_room_set
    __swig_getmethods__["frozen_start_room"] = _server.room_numbers_frozen_start_room_get
    if _newclass:frozen_start_room = property(_server.room_numbers_frozen_start_room_get, _server.room_numbers_frozen_start_room_set)
    __swig_setmethods__["donation_room_1"] = _server.room_numbers_donation_room_1_set
    __swig_getmethods__["donation_room_1"] = _server.room_numbers_donation_room_1_get
    if _newclass:donation_room_1 = property(_server.room_numbers_donation_room_1_get, _server.room_numbers_donation_room_1_set)
    __swig_setmethods__["donation_room_2"] = _server.room_numbers_donation_room_2_set
    __swig_getmethods__["donation_room_2"] = _server.room_numbers_donation_room_2_get
    if _newclass:donation_room_2 = property(_server.room_numbers_donation_room_2_get, _server.room_numbers_donation_room_2_set)
    __swig_setmethods__["donation_room_3"] = _server.room_numbers_donation_room_3_set
    __swig_getmethods__["donation_room_3"] = _server.room_numbers_donation_room_3_get
    if _newclass:donation_room_3 = property(_server.room_numbers_donation_room_3_get, _server.room_numbers_donation_room_3_set)
    def __init__(self, *args):
        _swig_setattr(self, room_numbers, 'this', _server.new_room_numbers(*args))
        _swig_setattr(self, room_numbers, 'thisown', 1)
    def __del__(self, destroy=_server.delete_room_numbers):
        try:
            if self.thisown: destroy(self)
        except: pass

class room_numbersPtr(room_numbers):
    def __init__(self, this):
        _swig_setattr(self, room_numbers, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, room_numbers, 'thisown', 0)
        _swig_setattr(self, room_numbers,self.__class__,room_numbers)
_server.room_numbers_swigregister(room_numbersPtr)

class game_operation(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, game_operation, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, game_operation, name)
    def __repr__(self):
        return "<C game_operation instance at %s>" % (self.this,)
    __swig_setmethods__["DFLT_PORT"] = _server.game_operation_DFLT_PORT_set
    __swig_getmethods__["DFLT_PORT"] = _server.game_operation_DFLT_PORT_get
    if _newclass:DFLT_PORT = property(_server.game_operation_DFLT_PORT_get, _server.game_operation_DFLT_PORT_set)
    __swig_setmethods__["DFLT_IP"] = _server.game_operation_DFLT_IP_set
    __swig_getmethods__["DFLT_IP"] = _server.game_operation_DFLT_IP_get
    if _newclass:DFLT_IP = property(_server.game_operation_DFLT_IP_get, _server.game_operation_DFLT_IP_set)
    __swig_setmethods__["DFLT_DIR"] = _server.game_operation_DFLT_DIR_set
    __swig_getmethods__["DFLT_DIR"] = _server.game_operation_DFLT_DIR_get
    if _newclass:DFLT_DIR = property(_server.game_operation_DFLT_DIR_get, _server.game_operation_DFLT_DIR_set)
    __swig_setmethods__["LOGNAME"] = _server.game_operation_LOGNAME_set
    __swig_getmethods__["LOGNAME"] = _server.game_operation_LOGNAME_get
    if _newclass:LOGNAME = property(_server.game_operation_LOGNAME_get, _server.game_operation_LOGNAME_set)
    __swig_setmethods__["max_playing"] = _server.game_operation_max_playing_set
    __swig_getmethods__["max_playing"] = _server.game_operation_max_playing_get
    if _newclass:max_playing = property(_server.game_operation_max_playing_get, _server.game_operation_max_playing_set)
    __swig_setmethods__["max_filesize"] = _server.game_operation_max_filesize_set
    __swig_getmethods__["max_filesize"] = _server.game_operation_max_filesize_get
    if _newclass:max_filesize = property(_server.game_operation_max_filesize_get, _server.game_operation_max_filesize_set)
    __swig_setmethods__["max_bad_pws"] = _server.game_operation_max_bad_pws_set
    __swig_getmethods__["max_bad_pws"] = _server.game_operation_max_bad_pws_get
    if _newclass:max_bad_pws = property(_server.game_operation_max_bad_pws_get, _server.game_operation_max_bad_pws_set)
    __swig_setmethods__["siteok_everyone"] = _server.game_operation_siteok_everyone_set
    __swig_getmethods__["siteok_everyone"] = _server.game_operation_siteok_everyone_get
    if _newclass:siteok_everyone = property(_server.game_operation_siteok_everyone_get, _server.game_operation_siteok_everyone_set)
    __swig_setmethods__["nameserver_is_slow"] = _server.game_operation_nameserver_is_slow_set
    __swig_getmethods__["nameserver_is_slow"] = _server.game_operation_nameserver_is_slow_get
    if _newclass:nameserver_is_slow = property(_server.game_operation_nameserver_is_slow_get, _server.game_operation_nameserver_is_slow_set)
    __swig_setmethods__["MENU"] = _server.game_operation_MENU_set
    __swig_getmethods__["MENU"] = _server.game_operation_MENU_get
    if _newclass:MENU = property(_server.game_operation_MENU_get, _server.game_operation_MENU_set)
    __swig_setmethods__["WELC_MESSG"] = _server.game_operation_WELC_MESSG_set
    __swig_getmethods__["WELC_MESSG"] = _server.game_operation_WELC_MESSG_get
    if _newclass:WELC_MESSG = property(_server.game_operation_WELC_MESSG_get, _server.game_operation_WELC_MESSG_set)
    __swig_setmethods__["START_MESSG"] = _server.game_operation_START_MESSG_set
    __swig_getmethods__["START_MESSG"] = _server.game_operation_START_MESSG_get
    if _newclass:START_MESSG = property(_server.game_operation_START_MESSG_get, _server.game_operation_START_MESSG_set)
    def __init__(self, *args):
        _swig_setattr(self, game_operation, 'this', _server.new_game_operation(*args))
        _swig_setattr(self, game_operation, 'thisown', 1)
    def __del__(self, destroy=_server.delete_game_operation):
        try:
            if self.thisown: destroy(self)
        except: pass

class game_operationPtr(game_operation):
    def __init__(self, this):
        _swig_setattr(self, game_operation, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, game_operation, 'thisown', 0)
        _swig_setattr(self, game_operation,self.__class__,game_operation)
_server.game_operation_swigregister(game_operationPtr)

class autowiz_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, autowiz_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, autowiz_data, name)
    def __repr__(self):
        return "<C autowiz_data instance at %s>" % (self.this,)
    __swig_setmethods__["use_autowiz"] = _server.autowiz_data_use_autowiz_set
    __swig_getmethods__["use_autowiz"] = _server.autowiz_data_use_autowiz_get
    if _newclass:use_autowiz = property(_server.autowiz_data_use_autowiz_get, _server.autowiz_data_use_autowiz_set)
    __swig_setmethods__["min_wizlist_lev"] = _server.autowiz_data_min_wizlist_lev_set
    __swig_getmethods__["min_wizlist_lev"] = _server.autowiz_data_min_wizlist_lev_get
    if _newclass:min_wizlist_lev = property(_server.autowiz_data_min_wizlist_lev_get, _server.autowiz_data_min_wizlist_lev_set)
    def __init__(self, *args):
        _swig_setattr(self, autowiz_data, 'this', _server.new_autowiz_data(*args))
        _swig_setattr(self, autowiz_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_autowiz_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class autowiz_dataPtr(autowiz_data):
    def __init__(self, this):
        _swig_setattr(self, autowiz_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, autowiz_data, 'thisown', 0)
        _swig_setattr(self, autowiz_data,self.__class__,autowiz_data)
_server.autowiz_data_swigregister(autowiz_dataPtr)

class config_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, config_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, config_data, name)
    def __repr__(self):
        return "<C config_data instance at %s>" % (self.this,)
    __swig_setmethods__["play"] = _server.config_data_play_set
    __swig_getmethods__["play"] = _server.config_data_play_get
    if _newclass:play = property(_server.config_data_play_get, _server.config_data_play_set)
    __swig_setmethods__["csd"] = _server.config_data_csd_set
    __swig_getmethods__["csd"] = _server.config_data_csd_get
    if _newclass:csd = property(_server.config_data_csd_get, _server.config_data_csd_set)
    __swig_setmethods__["room_nums"] = _server.config_data_room_nums_set
    __swig_getmethods__["room_nums"] = _server.config_data_room_nums_get
    if _newclass:room_nums = property(_server.config_data_room_nums_get, _server.config_data_room_nums_set)
    __swig_setmethods__["operation"] = _server.config_data_operation_set
    __swig_getmethods__["operation"] = _server.config_data_operation_get
    if _newclass:operation = property(_server.config_data_operation_get, _server.config_data_operation_set)
    __swig_setmethods__["autowiz"] = _server.config_data_autowiz_set
    __swig_getmethods__["autowiz"] = _server.config_data_autowiz_get
    if _newclass:autowiz = property(_server.config_data_autowiz_get, _server.config_data_autowiz_set)
    def __init__(self, *args):
        _swig_setattr(self, config_data, 'this', _server.new_config_data(*args))
        _swig_setattr(self, config_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_config_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class config_dataPtr(config_data):
    def __init__(self, this):
        _swig_setattr(self, config_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, config_data, 'thisown', 0)
        _swig_setattr(self, config_data,self.__class__,config_data)
_server.config_data_swigregister(config_dataPtr)


affect_total = _server.affect_total

affect_modify = _server.affect_modify

affect_to_char = _server.affect_to_char

affect_remove = _server.affect_remove

affect_from_char = _server.affect_from_char

affected_by_spell = _server.affected_by_spell

affect_join = _server.affect_join

money_desc = _server.money_desc

create_money = _server.create_money

isname = _server.isname

is_name = _server.is_name

fname = _server.fname

get_number = _server.get_number

obj_to_char = _server.obj_to_char

obj_from_char = _server.obj_from_char

equip_char = _server.equip_char

unequip_char = _server.unequip_char

invalid_align = _server.invalid_align

obj_to_room = _server.obj_to_room

obj_from_room = _server.obj_from_room

obj_to_obj = _server.obj_to_obj

obj_from_obj = _server.obj_from_obj

object_list_new_owner = _server.object_list_new_owner

extract_obj = _server.extract_obj

get_char_room = _server.get_char_room

get_char_num = _server.get_char_num

char_from_room = _server.char_from_room

char_to_room = _server.char_to_room

extract_char = _server.extract_char

extract_char_final = _server.extract_char_final

extract_pending_chars = _server.extract_pending_chars

get_player_vis = _server.get_player_vis

get_char_vis = _server.get_char_vis

get_char_room_vis = _server.get_char_room_vis

get_char_world_vis = _server.get_char_world_vis

get_obj_in_list_num = _server.get_obj_in_list_num

get_obj_num = _server.get_obj_num

get_obj_in_list_vis = _server.get_obj_in_list_vis

get_obj_vis = _server.get_obj_vis

get_obj_in_equip_vis = _server.get_obj_in_equip_vis

get_obj_pos_in_equip_vis = _server.get_obj_pos_in_equip_vis

find_all_dots = _server.find_all_dots
FIND_INDIV = _server.FIND_INDIV
FIND_ALL = _server.FIND_ALL
FIND_ALLDOT = _server.FIND_ALLDOT

generic_find = _server.generic_find
FIND_CHAR_ROOM = _server.FIND_CHAR_ROOM
FIND_CHAR_WORLD = _server.FIND_CHAR_WORLD
FIND_OBJ_INV = _server.FIND_OBJ_INV
FIND_OBJ_ROOM = _server.FIND_OBJ_ROOM
FIND_OBJ_WORLD = _server.FIND_OBJ_WORLD
FIND_OBJ_EQUIP = _server.FIND_OBJ_EQUIP

Crash_delete_file = _server.Crash_delete_file

Crash_delete_crashfile = _server.Crash_delete_crashfile

Crash_clean_file = _server.Crash_clean_file

Crash_listrent = _server.Crash_listrent

Crash_load = _server.Crash_load

Crash_crashsave = _server.Crash_crashsave

Crash_idlesave = _server.Crash_idlesave

Crash_save_all = _server.Crash_save_all

set_fighting = _server.set_fighting

stop_fighting = _server.stop_fighting

hit = _server.hit

forget = _server.forget

remember = _server.remember

damage = _server.damage

skill_message = _server.skill_message
READ_SIZE = _server.READ_SIZE

touch = _server.touch

log_death_trap = _server.log_death_trap

rand_number = _server.rand_number

dice = _server.dice

sprintbit = _server.sprintbit

sprinttype = _server.sprinttype

get_line = _server.get_line

get_filename = _server.get_filename

mud_time_to_secs = _server.mud_time_to_secs

age = _server.age

num_pc_in_room = _server.num_pc_in_room

core_dump_real = _server.core_dump_real

room_is_dark = _server.room_is_dark

str_cmp = _server.str_cmp

strn_cmp = _server.strn_cmp

circle_srandom = _server.circle_srandom

circle_random = _server.circle_random

MAX = _server.MAX

MIN = _server.MIN

CAP = _server.CAP

num_followers_charmed = _server.num_followers_charmed

die_follower = _server.die_follower

add_follower = _server.add_follower

stop_follower = _server.stop_follower

circle_follow = _server.circle_follow

look_at_room = _server.look_at_room

do_simple_move = _server.do_simple_move

perform_move = _server.perform_move

mana_gain = _server.mana_gain

hit_gain = _server.hit_gain

move_gain = _server.move_gain

advance_level = _server.advance_level

set_title = _server.set_title

gain_exp = _server.gain_exp

gain_exp_regardless = _server.gain_exp_regardless

gain_condition = _server.gain_condition

check_idling = _server.check_idling

point_update = _server.point_update

update_pos = _server.update_pos
OFF = _server.OFF
BRF = _server.BRF
NRM = _server.NRM
CMP = _server.CMP
CRASH_FILE = _server.CRASH_FILE
ETEXT_FILE = _server.ETEXT_FILE
ALIAS_FILE = _server.ALIAS_FILE
SCRIPT_VARS_FILE = _server.SCRIPT_VARS_FILE
BFS_ERROR = _server.BFS_ERROR
BFS_ALREADY_THERE = _server.BFS_ALREADY_THERE
BFS_NO_PATH = _server.BFS_NO_PATH
SECS_PER_MUD_HOUR = _server.SECS_PER_MUD_HOUR
SECS_PER_MUD_DAY = _server.SECS_PER_MUD_DAY
SECS_PER_MUD_MONTH = _server.SECS_PER_MUD_MONTH
SECS_PER_MUD_YEAR = _server.SECS_PER_MUD_YEAR
SECS_PER_REAL_MIN = _server.SECS_PER_REAL_MIN
SECS_PER_REAL_HOUR = _server.SECS_PER_REAL_HOUR
SECS_PER_REAL_DAY = _server.SECS_PER_REAL_DAY
SECS_PER_REAL_YEAR = _server.SECS_PER_REAL_YEAR
FALSE = _server.FALSE
TRUE = _server.TRUE
YES = _server.YES
NO = _server.NO
SEEK_SET = _server.SEEK_SET
SEEK_CUR = _server.SEEK_CUR
SEEK_END = _server.SEEK_END
DB_BOOT_WLD = _server.DB_BOOT_WLD
DB_BOOT_MOB = _server.DB_BOOT_MOB
DB_BOOT_OBJ = _server.DB_BOOT_OBJ
DB_BOOT_ZON = _server.DB_BOOT_ZON
DB_BOOT_SHP = _server.DB_BOOT_SHP
DB_BOOT_HLP = _server.DB_BOOT_HLP
DB_BOOT_TRG = _server.DB_BOOT_TRG
SUF_OBJS = _server.SUF_OBJS
SUF_TEXT = _server.SUF_TEXT
SUF_ALIAS = _server.SUF_ALIAS
SUF_MEM = _server.SUF_MEM
FASTBOOT_FILE = _server.FASTBOOT_FILE
KILLSCRIPT_FILE = _server.KILLSCRIPT_FILE
PAUSE_FILE = _server.PAUSE_FILE
INDEX_FILE = _server.INDEX_FILE
MINDEX_FILE = _server.MINDEX_FILE

boot_db = _server.boot_db

destroy_db = _server.destroy_db

create_entry = _server.create_entry

zone_update = _server.zone_update

fread_string = _server.fread_string

get_id_by_name = _server.get_id_by_name

get_name_by_id = _server.get_name_by_id

save_mud_time = _server.save_mud_time

free_extra_descriptions = _server.free_extra_descriptions

free_text_files = _server.free_text_files

free_player_index = _server.free_player_index

free_help = _server.free_help

real_zone = _server.real_zone

real_room = _server.real_room

real_mobile = _server.real_mobile

real_object = _server.real_object

char_to_store = _server.char_to_store

store_to_char = _server.store_to_char

load_char = _server.load_char

save_char = _server.save_char

init_char = _server.init_char

create_char = _server.create_char

read_mobile = _server.read_mobile

vnum_mobile = _server.vnum_mobile

clear_char = _server.clear_char

reset_char = _server.reset_char

free_char = _server.free_char

create_obj = _server.create_obj

clear_object = _server.clear_object

free_obj = _server.free_obj

read_object = _server.read_object

vnum_object = _server.vnum_object
REAL = _server.REAL
VIRTUAL = _server.VIRTUAL
class reset_com(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, reset_com, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, reset_com, name)
    def __repr__(self):
        return "<C reset_com instance at %s>" % (self.this,)
    __swig_setmethods__["command"] = _server.reset_com_command_set
    __swig_getmethods__["command"] = _server.reset_com_command_get
    if _newclass:command = property(_server.reset_com_command_get, _server.reset_com_command_set)
    __swig_setmethods__["if_flag"] = _server.reset_com_if_flag_set
    __swig_getmethods__["if_flag"] = _server.reset_com_if_flag_get
    if _newclass:if_flag = property(_server.reset_com_if_flag_get, _server.reset_com_if_flag_set)
    __swig_setmethods__["arg1"] = _server.reset_com_arg1_set
    __swig_getmethods__["arg1"] = _server.reset_com_arg1_get
    if _newclass:arg1 = property(_server.reset_com_arg1_get, _server.reset_com_arg1_set)
    __swig_setmethods__["arg2"] = _server.reset_com_arg2_set
    __swig_getmethods__["arg2"] = _server.reset_com_arg2_get
    if _newclass:arg2 = property(_server.reset_com_arg2_get, _server.reset_com_arg2_set)
    __swig_setmethods__["arg3"] = _server.reset_com_arg3_set
    __swig_getmethods__["arg3"] = _server.reset_com_arg3_get
    if _newclass:arg3 = property(_server.reset_com_arg3_get, _server.reset_com_arg3_set)
    __swig_setmethods__["line"] = _server.reset_com_line_set
    __swig_getmethods__["line"] = _server.reset_com_line_get
    if _newclass:line = property(_server.reset_com_line_get, _server.reset_com_line_set)
    __swig_setmethods__["sarg1"] = _server.reset_com_sarg1_set
    __swig_getmethods__["sarg1"] = _server.reset_com_sarg1_get
    if _newclass:sarg1 = property(_server.reset_com_sarg1_get, _server.reset_com_sarg1_set)
    __swig_setmethods__["sarg2"] = _server.reset_com_sarg2_set
    __swig_getmethods__["sarg2"] = _server.reset_com_sarg2_get
    if _newclass:sarg2 = property(_server.reset_com_sarg2_get, _server.reset_com_sarg2_set)
    def __init__(self, *args):
        _swig_setattr(self, reset_com, 'this', _server.new_reset_com(*args))
        _swig_setattr(self, reset_com, 'thisown', 1)
    def __del__(self, destroy=_server.delete_reset_com):
        try:
            if self.thisown: destroy(self)
        except: pass

class reset_comPtr(reset_com):
    def __init__(self, this):
        _swig_setattr(self, reset_com, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, reset_com, 'thisown', 0)
        _swig_setattr(self, reset_com,self.__class__,reset_com)
_server.reset_com_swigregister(reset_comPtr)
cvar = _server.cvar

class zone_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, zone_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, zone_data, name)
    def __repr__(self):
        return "<C zone_data instance at %s>" % (self.this,)
    __swig_setmethods__["name"] = _server.zone_data_name_set
    __swig_getmethods__["name"] = _server.zone_data_name_get
    if _newclass:name = property(_server.zone_data_name_get, _server.zone_data_name_set)
    __swig_setmethods__["builders"] = _server.zone_data_builders_set
    __swig_getmethods__["builders"] = _server.zone_data_builders_get
    if _newclass:builders = property(_server.zone_data_builders_get, _server.zone_data_builders_set)
    __swig_setmethods__["lifespan"] = _server.zone_data_lifespan_set
    __swig_getmethods__["lifespan"] = _server.zone_data_lifespan_get
    if _newclass:lifespan = property(_server.zone_data_lifespan_get, _server.zone_data_lifespan_set)
    __swig_setmethods__["age"] = _server.zone_data_age_set
    __swig_getmethods__["age"] = _server.zone_data_age_get
    if _newclass:age = property(_server.zone_data_age_get, _server.zone_data_age_set)
    __swig_setmethods__["bot"] = _server.zone_data_bot_set
    __swig_getmethods__["bot"] = _server.zone_data_bot_get
    if _newclass:bot = property(_server.zone_data_bot_get, _server.zone_data_bot_set)
    __swig_setmethods__["top"] = _server.zone_data_top_set
    __swig_getmethods__["top"] = _server.zone_data_top_get
    if _newclass:top = property(_server.zone_data_top_get, _server.zone_data_top_set)
    __swig_setmethods__["reset_mode"] = _server.zone_data_reset_mode_set
    __swig_getmethods__["reset_mode"] = _server.zone_data_reset_mode_get
    if _newclass:reset_mode = property(_server.zone_data_reset_mode_get, _server.zone_data_reset_mode_set)
    __swig_setmethods__["number"] = _server.zone_data_number_set
    __swig_getmethods__["number"] = _server.zone_data_number_get
    if _newclass:number = property(_server.zone_data_number_get, _server.zone_data_number_set)
    __swig_setmethods__["cmd"] = _server.zone_data_cmd_set
    __swig_getmethods__["cmd"] = _server.zone_data_cmd_get
    if _newclass:cmd = property(_server.zone_data_cmd_get, _server.zone_data_cmd_set)
    def __init__(self, *args):
        _swig_setattr(self, zone_data, 'this', _server.new_zone_data(*args))
        _swig_setattr(self, zone_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_zone_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class zone_dataPtr(zone_data):
    def __init__(self, this):
        _swig_setattr(self, zone_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, zone_data, 'thisown', 0)
        _swig_setattr(self, zone_data,self.__class__,zone_data)
_server.zone_data_swigregister(zone_dataPtr)

class reset_q_element(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, reset_q_element, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, reset_q_element, name)
    def __repr__(self):
        return "<C reset_q_element instance at %s>" % (self.this,)
    __swig_setmethods__["zone_to_reset"] = _server.reset_q_element_zone_to_reset_set
    __swig_getmethods__["zone_to_reset"] = _server.reset_q_element_zone_to_reset_get
    if _newclass:zone_to_reset = property(_server.reset_q_element_zone_to_reset_get, _server.reset_q_element_zone_to_reset_set)
    __swig_setmethods__["next"] = _server.reset_q_element_next_set
    __swig_getmethods__["next"] = _server.reset_q_element_next_get
    if _newclass:next = property(_server.reset_q_element_next_get, _server.reset_q_element_next_set)
    def __init__(self, *args):
        _swig_setattr(self, reset_q_element, 'this', _server.new_reset_q_element(*args))
        _swig_setattr(self, reset_q_element, 'thisown', 1)
    def __del__(self, destroy=_server.delete_reset_q_element):
        try:
            if self.thisown: destroy(self)
        except: pass

class reset_q_elementPtr(reset_q_element):
    def __init__(self, this):
        _swig_setattr(self, reset_q_element, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, reset_q_element, 'thisown', 0)
        _swig_setattr(self, reset_q_element,self.__class__,reset_q_element)
_server.reset_q_element_swigregister(reset_q_elementPtr)

class reset_q_type(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, reset_q_type, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, reset_q_type, name)
    def __repr__(self):
        return "<C reset_q_type instance at %s>" % (self.this,)
    __swig_setmethods__["head"] = _server.reset_q_type_head_set
    __swig_getmethods__["head"] = _server.reset_q_type_head_get
    if _newclass:head = property(_server.reset_q_type_head_get, _server.reset_q_type_head_set)
    __swig_setmethods__["tail"] = _server.reset_q_type_tail_set
    __swig_getmethods__["tail"] = _server.reset_q_type_tail_get
    if _newclass:tail = property(_server.reset_q_type_tail_get, _server.reset_q_type_tail_set)
    def __init__(self, *args):
        _swig_setattr(self, reset_q_type, 'this', _server.new_reset_q_type(*args))
        _swig_setattr(self, reset_q_type, 'thisown', 1)
    def __del__(self, destroy=_server.delete_reset_q_type):
        try:
            if self.thisown: destroy(self)
        except: pass

class reset_q_typePtr(reset_q_type):
    def __init__(self, this):
        _swig_setattr(self, reset_q_type, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, reset_q_type, 'thisown', 0)
        _swig_setattr(self, reset_q_type,self.__class__,reset_q_type)
_server.reset_q_type_swigregister(reset_q_typePtr)

class player_index_element(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, player_index_element, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, player_index_element, name)
    def __repr__(self):
        return "<C player_index_element instance at %s>" % (self.this,)
    __swig_setmethods__["name"] = _server.player_index_element_name_set
    __swig_getmethods__["name"] = _server.player_index_element_name_get
    if _newclass:name = property(_server.player_index_element_name_get, _server.player_index_element_name_set)
    __swig_setmethods__["id"] = _server.player_index_element_id_set
    __swig_getmethods__["id"] = _server.player_index_element_id_get
    if _newclass:id = property(_server.player_index_element_id_get, _server.player_index_element_id_set)
    def __init__(self, *args):
        _swig_setattr(self, player_index_element, 'this', _server.new_player_index_element(*args))
        _swig_setattr(self, player_index_element, 'thisown', 1)
    def __del__(self, destroy=_server.delete_player_index_element):
        try:
            if self.thisown: destroy(self)
        except: pass

class player_index_elementPtr(player_index_element):
    def __init__(self, this):
        _swig_setattr(self, player_index_element, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, player_index_element, 'thisown', 0)
        _swig_setattr(self, player_index_element,self.__class__,player_index_element)
_server.player_index_element_swigregister(player_index_elementPtr)

class help_index_element(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, help_index_element, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, help_index_element, name)
    def __repr__(self):
        return "<C help_index_element instance at %s>" % (self.this,)
    __swig_setmethods__["keyword"] = _server.help_index_element_keyword_set
    __swig_getmethods__["keyword"] = _server.help_index_element_keyword_get
    if _newclass:keyword = property(_server.help_index_element_keyword_get, _server.help_index_element_keyword_set)
    __swig_setmethods__["entry"] = _server.help_index_element_entry_set
    __swig_getmethods__["entry"] = _server.help_index_element_entry_get
    if _newclass:entry = property(_server.help_index_element_entry_get, _server.help_index_element_entry_set)
    __swig_setmethods__["duplicate"] = _server.help_index_element_duplicate_set
    __swig_getmethods__["duplicate"] = _server.help_index_element_duplicate_get
    if _newclass:duplicate = property(_server.help_index_element_duplicate_get, _server.help_index_element_duplicate_set)
    def __init__(self, *args):
        _swig_setattr(self, help_index_element, 'this', _server.new_help_index_element(*args))
        _swig_setattr(self, help_index_element, 'thisown', 1)
    def __del__(self, destroy=_server.delete_help_index_element):
        try:
            if self.thisown: destroy(self)
        except: pass

class help_index_elementPtr(help_index_element):
    def __init__(self, this):
        _swig_setattr(self, help_index_element, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, help_index_element, 'thisown', 0)
        _swig_setattr(self, help_index_element,self.__class__,help_index_element)
_server.help_index_element_swigregister(help_index_elementPtr)

BAN_NOT = _server.BAN_NOT
BAN_NEW = _server.BAN_NEW
BAN_SELECT = _server.BAN_SELECT
BAN_ALL = _server.BAN_ALL
BANNED_SITE_LENGTH = _server.BANNED_SITE_LENGTH
class ban_list_element(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ban_list_element, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ban_list_element, name)
    def __repr__(self):
        return "<C ban_list_element instance at %s>" % (self.this,)
    __swig_setmethods__["site"] = _server.ban_list_element_site_set
    __swig_getmethods__["site"] = _server.ban_list_element_site_get
    if _newclass:site = property(_server.ban_list_element_site_get, _server.ban_list_element_site_set)
    __swig_setmethods__["type"] = _server.ban_list_element_type_set
    __swig_getmethods__["type"] = _server.ban_list_element_type_get
    if _newclass:type = property(_server.ban_list_element_type_get, _server.ban_list_element_type_set)
    __swig_setmethods__["date"] = _server.ban_list_element_date_set
    __swig_getmethods__["date"] = _server.ban_list_element_date_get
    if _newclass:date = property(_server.ban_list_element_date_get, _server.ban_list_element_date_set)
    __swig_setmethods__["name"] = _server.ban_list_element_name_set
    __swig_getmethods__["name"] = _server.ban_list_element_name_get
    if _newclass:name = property(_server.ban_list_element_name_get, _server.ban_list_element_name_set)
    __swig_setmethods__["next"] = _server.ban_list_element_next_set
    __swig_getmethods__["next"] = _server.ban_list_element_next_get
    if _newclass:next = property(_server.ban_list_element_next_get, _server.ban_list_element_next_set)
    def __init__(self, *args):
        _swig_setattr(self, ban_list_element, 'this', _server.new_ban_list_element(*args))
        _swig_setattr(self, ban_list_element, 'thisown', 1)
    def __del__(self, destroy=_server.delete_ban_list_element):
        try:
            if self.thisown: destroy(self)
        except: pass

class ban_list_elementPtr(ban_list_element):
    def __init__(self, this):
        _swig_setattr(self, ban_list_element, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, ban_list_element, 'thisown', 0)
        _swig_setattr(self, ban_list_element,self.__class__,ban_list_element)
_server.ban_list_element_swigregister(ban_list_elementPtr)

CMDPASS_ORDER_INDIV = _server.CMDPASS_ORDER_INDIV
CMDPASS_ORDER_FOLLOWERS = _server.CMDPASS_ORDER_FOLLOWERS
CMDPASS_FORCE_INDIV = _server.CMDPASS_FORCE_INDIV
CMDPASS_FORCE_ROOM = _server.CMDPASS_FORCE_ROOM
CMDPASS_FORCE_ALL = _server.CMDPASS_FORCE_ALL
CMDPASS_IMPFORCE = _server.CMDPASS_IMPFORCE
CMDPASS_SCRIPTFORCE = _server.CMDPASS_SCRIPTFORCE
CMDPASS_COMM = _server.CMDPASS_COMM
CMDPASS_INALIAS = _server.CMDPASS_INALIAS
CMDPASS_AT = _server.CMDPASS_AT
CMDPASS_FORCE = _server.CMDPASS_FORCE
CMDPASS_ORDER = _server.CMDPASS_ORDER
CMD_NOABBREV = _server.CMD_NOABBREV
CMD_FIXED = _server.CMD_FIXED

command_interpreter = _server.command_interpreter

search_block = _server.search_block

lower = _server.lower

one_argument = _server.one_argument

one_word = _server.one_word

any_one_arg = _server.any_one_arg

two_arguments = _server.two_arguments

fill_word = _server.fill_word

half_chop = _server.half_chop

nanny = _server.nanny

is_abbrev = _server.is_abbrev

is_number = _server.is_number

find_command = _server.find_command

skip_spaces = _server.skip_spaces

delete_doubledollar = _server.delete_doubledollar

insert_command = _server.insert_command

clear_commands = _server.clear_commands

deregister_command_predicate = _server.deregister_command_predicate

deregister_command_byname = _server.deregister_command_byname
class command_info(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, command_info, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, command_info, name)
    def __repr__(self):
        return "<C command_info instance at %s>" % (self.this,)
    __swig_setmethods__["hashcode"] = _server.command_info_hashcode_set
    __swig_getmethods__["hashcode"] = _server.command_info_hashcode_get
    if _newclass:hashcode = property(_server.command_info_hashcode_get, _server.command_info_hashcode_set)
    __swig_setmethods__["number"] = _server.command_info_number_set
    __swig_getmethods__["number"] = _server.command_info_number_get
    if _newclass:number = property(_server.command_info_number_get, _server.command_info_number_set)
    __swig_setmethods__["name"] = _server.command_info_name_set
    __swig_getmethods__["name"] = _server.command_info_name_get
    if _newclass:name = property(_server.command_info_name_get, _server.command_info_name_set)
    __swig_setmethods__["minimum_position"] = _server.command_info_minimum_position_set
    __swig_getmethods__["minimum_position"] = _server.command_info_minimum_position_get
    if _newclass:minimum_position = property(_server.command_info_minimum_position_get, _server.command_info_minimum_position_set)
    __swig_setmethods__["native_callfun"] = _server.command_info_native_callfun_set
    __swig_getmethods__["native_callfun"] = _server.command_info_native_callfun_get
    if _newclass:native_callfun = property(_server.command_info_native_callfun_get, _server.command_info_native_callfun_set)
    __swig_setmethods__["minimum_level"] = _server.command_info_minimum_level_set
    __swig_getmethods__["minimum_level"] = _server.command_info_minimum_level_get
    if _newclass:minimum_level = property(_server.command_info_minimum_level_get, _server.command_info_minimum_level_set)
    __swig_setmethods__["subcmd"] = _server.command_info_subcmd_set
    __swig_getmethods__["subcmd"] = _server.command_info_subcmd_get
    if _newclass:subcmd = property(_server.command_info_subcmd_get, _server.command_info_subcmd_set)
    __swig_setmethods__["flags"] = _server.command_info_flags_set
    __swig_getmethods__["flags"] = _server.command_info_flags_get
    if _newclass:flags = property(_server.command_info_flags_get, _server.command_info_flags_set)
    __swig_setmethods__["priority"] = _server.command_info_priority_set
    __swig_getmethods__["priority"] = _server.command_info_priority_get
    if _newclass:priority = property(_server.command_info_priority_get, _server.command_info_priority_set)
    __swig_setmethods__["override"] = _server.command_info_override_set
    __swig_getmethods__["override"] = _server.command_info_override_get
    if _newclass:override = property(_server.command_info_override_get, _server.command_info_override_set)
    __swig_setmethods__["language"] = _server.command_info_language_set
    __swig_getmethods__["language"] = _server.command_info_language_get
    if _newclass:language = property(_server.command_info_language_get, _server.command_info_language_set)
    def __init__(self, *args):
        _swig_setattr(self, command_info, 'this', _server.new_command_info(*args))
        _swig_setattr(self, command_info, 'thisown', 1)
    def __del__(self, destroy=_server.delete_command_info):
        try:
            if self.thisown: destroy(self)
        except: pass

class command_infoPtr(command_info):
    def __init__(self, this):
        _swig_setattr(self, command_info, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, command_info, 'thisown', 0)
        _swig_setattr(self, command_info,self.__class__,command_info)
_server.command_info_swigregister(command_infoPtr)


hash_command = _server.hash_command
class alias_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, alias_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, alias_data, name)
    def __repr__(self):
        return "<C alias_data instance at %s>" % (self.this,)
    __swig_setmethods__["alias"] = _server.alias_data_alias_set
    __swig_getmethods__["alias"] = _server.alias_data_alias_get
    if _newclass:alias = property(_server.alias_data_alias_get, _server.alias_data_alias_set)
    __swig_setmethods__["replacement"] = _server.alias_data_replacement_set
    __swig_getmethods__["replacement"] = _server.alias_data_replacement_get
    if _newclass:replacement = property(_server.alias_data_replacement_get, _server.alias_data_replacement_set)
    __swig_setmethods__["type"] = _server.alias_data_type_set
    __swig_getmethods__["type"] = _server.alias_data_type_get
    if _newclass:type = property(_server.alias_data_type_get, _server.alias_data_type_set)
    __swig_setmethods__["next"] = _server.alias_data_next_set
    __swig_getmethods__["next"] = _server.alias_data_next_get
    if _newclass:next = property(_server.alias_data_next_get, _server.alias_data_next_set)
    def __init__(self, *args):
        _swig_setattr(self, alias_data, 'this', _server.new_alias_data(*args))
        _swig_setattr(self, alias_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_alias_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class alias_dataPtr(alias_data):
    def __init__(self, this):
        _swig_setattr(self, alias_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, alias_data, 'thisown', 0)
        _swig_setattr(self, alias_data,self.__class__,alias_data)
_server.alias_data_swigregister(alias_dataPtr)

ALIAS_SIMPLE = _server.ALIAS_SIMPLE
ALIAS_COMPLEX = _server.ALIAS_COMPLEX
ALIAS_SEP_CHAR = _server.ALIAS_SEP_CHAR
ALIAS_VAR_CHAR = _server.ALIAS_VAR_CHAR
ALIAS_GLOB_CHAR = _server.ALIAS_GLOB_CHAR
SCMD_NORTH = _server.SCMD_NORTH
SCMD_EAST = _server.SCMD_EAST
SCMD_SOUTH = _server.SCMD_SOUTH
SCMD_WEST = _server.SCMD_WEST
SCMD_UP = _server.SCMD_UP
SCMD_DOWN = _server.SCMD_DOWN
SCMD_INFO = _server.SCMD_INFO
SCMD_HANDBOOK = _server.SCMD_HANDBOOK
SCMD_CREDITS = _server.SCMD_CREDITS
SCMD_NEWS = _server.SCMD_NEWS
SCMD_WIZLIST = _server.SCMD_WIZLIST
SCMD_POLICIES = _server.SCMD_POLICIES
SCMD_VERSION = _server.SCMD_VERSION
SCMD_IMMLIST = _server.SCMD_IMMLIST
SCMD_MOTD = _server.SCMD_MOTD
SCMD_IMOTD = _server.SCMD_IMOTD
SCMD_CLEAR = _server.SCMD_CLEAR
SCMD_WHOAMI = _server.SCMD_WHOAMI
SCMD_NOSUMMON = _server.SCMD_NOSUMMON
SCMD_NOHASSLE = _server.SCMD_NOHASSLE
SCMD_BRIEF = _server.SCMD_BRIEF
SCMD_COMPACT = _server.SCMD_COMPACT
SCMD_NOTELL = _server.SCMD_NOTELL
SCMD_NOAUCTION = _server.SCMD_NOAUCTION
SCMD_DEAF = _server.SCMD_DEAF
SCMD_NOGOSSIP = _server.SCMD_NOGOSSIP
SCMD_NOGRATZ = _server.SCMD_NOGRATZ
SCMD_NOWIZ = _server.SCMD_NOWIZ
SCMD_QUEST = _server.SCMD_QUEST
SCMD_ROOMFLAGS = _server.SCMD_ROOMFLAGS
SCMD_NOREPEAT = _server.SCMD_NOREPEAT
SCMD_HOLYLIGHT = _server.SCMD_HOLYLIGHT
SCMD_SLOWNS = _server.SCMD_SLOWNS
SCMD_AUTOEXIT = _server.SCMD_AUTOEXIT
SCMD_TRACK = _server.SCMD_TRACK
SCMD_CLS = _server.SCMD_CLS
SCMD_REROLL = _server.SCMD_REROLL
SCMD_PARDON = _server.SCMD_PARDON
SCMD_NOTITLE = _server.SCMD_NOTITLE
SCMD_SQUELCH = _server.SCMD_SQUELCH
SCMD_FREEZE = _server.SCMD_FREEZE
SCMD_THAW = _server.SCMD_THAW
SCMD_UNAFFECT = _server.SCMD_UNAFFECT
SCMD_WHISPER = _server.SCMD_WHISPER
SCMD_ASK = _server.SCMD_ASK
SCMD_HOLLER = _server.SCMD_HOLLER
SCMD_SHOUT = _server.SCMD_SHOUT
SCMD_GOSSIP = _server.SCMD_GOSSIP
SCMD_AUCTION = _server.SCMD_AUCTION
SCMD_GRATZ = _server.SCMD_GRATZ
SCMD_SHUTDOW = _server.SCMD_SHUTDOW
SCMD_SHUTDOWN = _server.SCMD_SHUTDOWN
SCMD_QUI = _server.SCMD_QUI
SCMD_QUIT = _server.SCMD_QUIT
SCMD_DATE = _server.SCMD_DATE
SCMD_UPTIME = _server.SCMD_UPTIME
SCMD_COMMANDS = _server.SCMD_COMMANDS
SCMD_SOCIALS = _server.SCMD_SOCIALS
SCMD_WIZHELP = _server.SCMD_WIZHELP
SCMD_DROP = _server.SCMD_DROP
SCMD_JUNK = _server.SCMD_JUNK
SCMD_DONATE = _server.SCMD_DONATE
SCMD_BUG = _server.SCMD_BUG
SCMD_TYPO = _server.SCMD_TYPO
SCMD_IDEA = _server.SCMD_IDEA
SCMD_LOOK = _server.SCMD_LOOK
SCMD_READ = _server.SCMD_READ
SCMD_QSAY = _server.SCMD_QSAY
SCMD_QECHO = _server.SCMD_QECHO
SCMD_POUR = _server.SCMD_POUR
SCMD_FILL = _server.SCMD_FILL
SCMD_POOFIN = _server.SCMD_POOFIN
SCMD_POOFOUT = _server.SCMD_POOFOUT
SCMD_HIT = _server.SCMD_HIT
SCMD_MURDER = _server.SCMD_MURDER
SCMD_EAT = _server.SCMD_EAT
SCMD_TASTE = _server.SCMD_TASTE
SCMD_DRINK = _server.SCMD_DRINK
SCMD_SIP = _server.SCMD_SIP
SCMD_USE = _server.SCMD_USE
SCMD_QUAFF = _server.SCMD_QUAFF
SCMD_RECITE = _server.SCMD_RECITE
SCMD_ECHO = _server.SCMD_ECHO
SCMD_EMOTE = _server.SCMD_EMOTE
SCMD_OPEN = _server.SCMD_OPEN
SCMD_CLOSE = _server.SCMD_CLOSE
SCMD_UNLOCK = _server.SCMD_UNLOCK
SCMD_LOCK = _server.SCMD_LOCK
SCMD_PICK = _server.SCMD_PICK
SCMD_OASIS_REDIT = _server.SCMD_OASIS_REDIT
SCMD_OASIS_OEDIT = _server.SCMD_OASIS_OEDIT
SCMD_OASIS_ZEDIT = _server.SCMD_OASIS_ZEDIT
SCMD_OASIS_MEDIT = _server.SCMD_OASIS_MEDIT
SCMD_OASIS_SEDIT = _server.SCMD_OASIS_SEDIT
SCMD_OASIS_CEDIT = _server.SCMD_OASIS_CEDIT
SCMD_OLC_SAVEINFO = _server.SCMD_OLC_SAVEINFO
SCMD_OASIS_RLIST = _server.SCMD_OASIS_RLIST
SCMD_OASIS_MLIST = _server.SCMD_OASIS_MLIST
SCMD_OASIS_OLIST = _server.SCMD_OASIS_OLIST
SCMD_OASIS_SLIST = _server.SCMD_OASIS_SLIST
SCMD_OASIS_ZLIST = _server.SCMD_OASIS_ZLIST
SCMD_OASIS_TRIGEDIT = _server.SCMD_OASIS_TRIGEDIT
SCMD_OASIS_TLIST = _server.SCMD_OASIS_TLIST
DEFAULT_STAFF_LVL = _server.DEFAULT_STAFF_LVL
DEFAULT_WAND_LVL = _server.DEFAULT_WAND_LVL
CAST_UNDEFINED = _server.CAST_UNDEFINED
CAST_SPELL = _server.CAST_SPELL
CAST_POTION = _server.CAST_POTION
CAST_WAND = _server.CAST_WAND
CAST_STAFF = _server.CAST_STAFF
CAST_SCROLL = _server.CAST_SCROLL
MAG_DAMAGE = _server.MAG_DAMAGE
MAG_AFFECTS = _server.MAG_AFFECTS
MAG_UNAFFECTS = _server.MAG_UNAFFECTS
MAG_POINTS = _server.MAG_POINTS
MAG_ALTER_OBJS = _server.MAG_ALTER_OBJS
MAG_GROUPS = _server.MAG_GROUPS
MAG_MASSES = _server.MAG_MASSES
MAG_AREAS = _server.MAG_AREAS
MAG_SUMMONS = _server.MAG_SUMMONS
MAG_CREATIONS = _server.MAG_CREATIONS
MAG_MANUAL = _server.MAG_MANUAL
TYPE_UNDEFINED = _server.TYPE_UNDEFINED
SPELL_RESERVED_DBC = _server.SPELL_RESERVED_DBC
SPELL_ARMOR = _server.SPELL_ARMOR
SPELL_TELEPORT = _server.SPELL_TELEPORT
SPELL_BLESS = _server.SPELL_BLESS
SPELL_BLINDNESS = _server.SPELL_BLINDNESS
SPELL_BURNING_HANDS = _server.SPELL_BURNING_HANDS
SPELL_CALL_LIGHTNING = _server.SPELL_CALL_LIGHTNING
SPELL_CHARM = _server.SPELL_CHARM
SPELL_CHILL_TOUCH = _server.SPELL_CHILL_TOUCH
SPELL_CLONE = _server.SPELL_CLONE
SPELL_COLOR_SPRAY = _server.SPELL_COLOR_SPRAY
SPELL_CONTROL_WEATHER = _server.SPELL_CONTROL_WEATHER
SPELL_CREATE_FOOD = _server.SPELL_CREATE_FOOD
SPELL_CREATE_WATER = _server.SPELL_CREATE_WATER
SPELL_CURE_BLIND = _server.SPELL_CURE_BLIND
SPELL_CURE_CRITIC = _server.SPELL_CURE_CRITIC
SPELL_CURE_LIGHT = _server.SPELL_CURE_LIGHT
SPELL_CURSE = _server.SPELL_CURSE
SPELL_DETECT_ALIGN = _server.SPELL_DETECT_ALIGN
SPELL_DETECT_INVIS = _server.SPELL_DETECT_INVIS
SPELL_DETECT_MAGIC = _server.SPELL_DETECT_MAGIC
SPELL_DETECT_POISON = _server.SPELL_DETECT_POISON
SPELL_DISPEL_EVIL = _server.SPELL_DISPEL_EVIL
SPELL_EARTHQUAKE = _server.SPELL_EARTHQUAKE
SPELL_ENCHANT_WEAPON = _server.SPELL_ENCHANT_WEAPON
SPELL_ENERGY_DRAIN = _server.SPELL_ENERGY_DRAIN
SPELL_FIREBALL = _server.SPELL_FIREBALL
SPELL_HARM = _server.SPELL_HARM
SPELL_HEAL = _server.SPELL_HEAL
SPELL_INVISIBLE = _server.SPELL_INVISIBLE
SPELL_LIGHTNING_BOLT = _server.SPELL_LIGHTNING_BOLT
SPELL_LOCATE_OBJECT = _server.SPELL_LOCATE_OBJECT
SPELL_MAGIC_MISSILE = _server.SPELL_MAGIC_MISSILE
SPELL_POISON = _server.SPELL_POISON
SPELL_PROT_FROM_EVIL = _server.SPELL_PROT_FROM_EVIL
SPELL_REMOVE_CURSE = _server.SPELL_REMOVE_CURSE
SPELL_SANCTUARY = _server.SPELL_SANCTUARY
SPELL_SHOCKING_GRASP = _server.SPELL_SHOCKING_GRASP
SPELL_SLEEP = _server.SPELL_SLEEP
SPELL_STRENGTH = _server.SPELL_STRENGTH
SPELL_SUMMON = _server.SPELL_SUMMON
SPELL_VENTRILOQUATE = _server.SPELL_VENTRILOQUATE
SPELL_WORD_OF_RECALL = _server.SPELL_WORD_OF_RECALL
SPELL_REMOVE_POISON = _server.SPELL_REMOVE_POISON
SPELL_SENSE_LIFE = _server.SPELL_SENSE_LIFE
SPELL_ANIMATE_DEAD = _server.SPELL_ANIMATE_DEAD
SPELL_DISPEL_GOOD = _server.SPELL_DISPEL_GOOD
SPELL_GROUP_ARMOR = _server.SPELL_GROUP_ARMOR
SPELL_GROUP_HEAL = _server.SPELL_GROUP_HEAL
SPELL_GROUP_RECALL = _server.SPELL_GROUP_RECALL
SPELL_INFRAVISION = _server.SPELL_INFRAVISION
SPELL_WATERWALK = _server.SPELL_WATERWALK
MAX_SPELLS = _server.MAX_SPELLS
SKILL_BACKSTAB = _server.SKILL_BACKSTAB
SKILL_BASH = _server.SKILL_BASH
SKILL_HIDE = _server.SKILL_HIDE
SKILL_KICK = _server.SKILL_KICK
SKILL_PICK_LOCK = _server.SKILL_PICK_LOCK
SKILL_RESCUE = _server.SKILL_RESCUE
SKILL_SNEAK = _server.SKILL_SNEAK
SKILL_STEAL = _server.SKILL_STEAL
SKILL_TRACK = _server.SKILL_TRACK
SPELL_IDENTIFY = _server.SPELL_IDENTIFY
SPELL_FIRE_BREATH = _server.SPELL_FIRE_BREATH
SPELL_GAS_BREATH = _server.SPELL_GAS_BREATH
SPELL_FROST_BREATH = _server.SPELL_FROST_BREATH
SPELL_ACID_BREATH = _server.SPELL_ACID_BREATH
SPELL_LIGHTNING_BREATH = _server.SPELL_LIGHTNING_BREATH
SPELL_DG_AFFECT = _server.SPELL_DG_AFFECT
TOP_SPELL_DEFINE = _server.TOP_SPELL_DEFINE
TYPE_HIT = _server.TYPE_HIT
TYPE_STING = _server.TYPE_STING
TYPE_WHIP = _server.TYPE_WHIP
TYPE_SLASH = _server.TYPE_SLASH
TYPE_BITE = _server.TYPE_BITE
TYPE_BLUDGEON = _server.TYPE_BLUDGEON
TYPE_CRUSH = _server.TYPE_CRUSH
TYPE_POUND = _server.TYPE_POUND
TYPE_CLAW = _server.TYPE_CLAW
TYPE_MAUL = _server.TYPE_MAUL
TYPE_THRASH = _server.TYPE_THRASH
TYPE_PIERCE = _server.TYPE_PIERCE
TYPE_BLAST = _server.TYPE_BLAST
TYPE_PUNCH = _server.TYPE_PUNCH
TYPE_STAB = _server.TYPE_STAB
TYPE_SUFFERING = _server.TYPE_SUFFERING
SAVING_PARA = _server.SAVING_PARA
SAVING_ROD = _server.SAVING_ROD
SAVING_PETRI = _server.SAVING_PETRI
SAVING_BREATH = _server.SAVING_BREATH
SAVING_SPELL = _server.SAVING_SPELL
TAR_IGNORE = _server.TAR_IGNORE
TAR_CHAR_ROOM = _server.TAR_CHAR_ROOM
TAR_CHAR_WORLD = _server.TAR_CHAR_WORLD
TAR_FIGHT_SELF = _server.TAR_FIGHT_SELF
TAR_FIGHT_VICT = _server.TAR_FIGHT_VICT
TAR_SELF_ONLY = _server.TAR_SELF_ONLY
TAR_NOT_SELF = _server.TAR_NOT_SELF
TAR_OBJ_INV = _server.TAR_OBJ_INV
TAR_OBJ_ROOM = _server.TAR_OBJ_ROOM
TAR_OBJ_WORLD = _server.TAR_OBJ_WORLD
TAR_OBJ_EQUIP = _server.TAR_OBJ_EQUIP
class spell_info_type(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, spell_info_type, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, spell_info_type, name)
    def __repr__(self):
        return "<C spell_info_type instance at %s>" % (self.this,)
    __swig_setmethods__["min_position"] = _server.spell_info_type_min_position_set
    __swig_getmethods__["min_position"] = _server.spell_info_type_min_position_get
    if _newclass:min_position = property(_server.spell_info_type_min_position_get, _server.spell_info_type_min_position_set)
    __swig_setmethods__["mana_min"] = _server.spell_info_type_mana_min_set
    __swig_getmethods__["mana_min"] = _server.spell_info_type_mana_min_get
    if _newclass:mana_min = property(_server.spell_info_type_mana_min_get, _server.spell_info_type_mana_min_set)
    __swig_setmethods__["mana_max"] = _server.spell_info_type_mana_max_set
    __swig_getmethods__["mana_max"] = _server.spell_info_type_mana_max_get
    if _newclass:mana_max = property(_server.spell_info_type_mana_max_get, _server.spell_info_type_mana_max_set)
    __swig_setmethods__["mana_change"] = _server.spell_info_type_mana_change_set
    __swig_getmethods__["mana_change"] = _server.spell_info_type_mana_change_get
    if _newclass:mana_change = property(_server.spell_info_type_mana_change_get, _server.spell_info_type_mana_change_set)
    __swig_setmethods__["min_level"] = _server.spell_info_type_min_level_set
    __swig_getmethods__["min_level"] = _server.spell_info_type_min_level_get
    if _newclass:min_level = property(_server.spell_info_type_min_level_get, _server.spell_info_type_min_level_set)
    __swig_setmethods__["routines"] = _server.spell_info_type_routines_set
    __swig_getmethods__["routines"] = _server.spell_info_type_routines_get
    if _newclass:routines = property(_server.spell_info_type_routines_get, _server.spell_info_type_routines_set)
    __swig_setmethods__["violent"] = _server.spell_info_type_violent_set
    __swig_getmethods__["violent"] = _server.spell_info_type_violent_get
    if _newclass:violent = property(_server.spell_info_type_violent_get, _server.spell_info_type_violent_set)
    __swig_setmethods__["targets"] = _server.spell_info_type_targets_set
    __swig_getmethods__["targets"] = _server.spell_info_type_targets_get
    if _newclass:targets = property(_server.spell_info_type_targets_get, _server.spell_info_type_targets_set)
    __swig_setmethods__["name"] = _server.spell_info_type_name_set
    __swig_getmethods__["name"] = _server.spell_info_type_name_get
    if _newclass:name = property(_server.spell_info_type_name_get, _server.spell_info_type_name_set)
    __swig_setmethods__["wear_off_msg"] = _server.spell_info_type_wear_off_msg_set
    __swig_getmethods__["wear_off_msg"] = _server.spell_info_type_wear_off_msg_get
    if _newclass:wear_off_msg = property(_server.spell_info_type_wear_off_msg_get, _server.spell_info_type_wear_off_msg_set)
    def __init__(self, *args):
        _swig_setattr(self, spell_info_type, 'this', _server.new_spell_info_type(*args))
        _swig_setattr(self, spell_info_type, 'thisown', 1)
    def __del__(self, destroy=_server.delete_spell_info_type):
        try:
            if self.thisown: destroy(self)
        except: pass

class spell_info_typePtr(spell_info_type):
    def __init__(self, this):
        _swig_setattr(self, spell_info_type, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, spell_info_type, 'thisown', 0)
        _swig_setattr(self, spell_info_type,self.__class__,spell_info_type)
_server.spell_info_type_swigregister(spell_info_typePtr)

SPELL_TYPE_SPELL = _server.SPELL_TYPE_SPELL
SPELL_TYPE_POTION = _server.SPELL_TYPE_POTION
SPELL_TYPE_WAND = _server.SPELL_TYPE_WAND
SPELL_TYPE_STAFF = _server.SPELL_TYPE_STAFF
SPELL_TYPE_SCROLL = _server.SPELL_TYPE_SCROLL
class attack_hit_type(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, attack_hit_type, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, attack_hit_type, name)
    def __repr__(self):
        return "<C attack_hit_type instance at %s>" % (self.this,)
    __swig_setmethods__["singular"] = _server.attack_hit_type_singular_set
    __swig_getmethods__["singular"] = _server.attack_hit_type_singular_get
    if _newclass:singular = property(_server.attack_hit_type_singular_get, _server.attack_hit_type_singular_set)
    __swig_setmethods__["plural"] = _server.attack_hit_type_plural_set
    __swig_getmethods__["plural"] = _server.attack_hit_type_plural_get
    if _newclass:plural = property(_server.attack_hit_type_plural_get, _server.attack_hit_type_plural_set)
    def __init__(self, *args):
        _swig_setattr(self, attack_hit_type, 'this', _server.new_attack_hit_type(*args))
        _swig_setattr(self, attack_hit_type, 'thisown', 1)
    def __del__(self, destroy=_server.delete_attack_hit_type):
        try:
            if self.thisown: destroy(self)
        except: pass

class attack_hit_typePtr(attack_hit_type):
    def __init__(self, this):
        _swig_setattr(self, attack_hit_type, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, attack_hit_type, 'thisown', 0)
        _swig_setattr(self, attack_hit_type,self.__class__,attack_hit_type)
_server.attack_hit_type_swigregister(attack_hit_typePtr)


find_skill_num = _server.find_skill_num

mag_damage = _server.mag_damage

mag_affects = _server.mag_affects

mag_groups = _server.mag_groups

mag_masses = _server.mag_masses

mag_areas = _server.mag_areas

mag_summons = _server.mag_summons

mag_points = _server.mag_points

mag_unaffects = _server.mag_unaffects

mag_alter_objs = _server.mag_alter_objs

mag_creations = _server.mag_creations

call_magic = _server.call_magic

mag_objectmagic = _server.mag_objectmagic

cast_spell = _server.cast_spell

spell_level = _server.spell_level

init_spell_levels = _server.init_spell_levels

skill_name = _server.skill_name
SCRIPT_RET_CANCEL = _server.SCRIPT_RET_CANCEL
SCRIPT_RET_INTERCEPT = _server.SCRIPT_RET_INTERCEPT
SCRIPT_RET_ACTOR_DEAD = _server.SCRIPT_RET_ACTOR_DEAD
SCRIPT_RET_SUBJECT_DEAD = _server.SCRIPT_RET_SUBJECT_DEAD
SCRIPT_RET_VICT_DEAD = _server.SCRIPT_RET_VICT_DEAD
SCRIPT_RET_OBJ_DEAD = _server.SCRIPT_RET_OBJ_DEAD
SCRIPT_RET_OK = _server.SCRIPT_RET_OK
SCRIPT_RET_UPDATED = _server.SCRIPT_RET_UPDATED
SCRIPT_RET_OBJECT_DEAD = _server.SCRIPT_RET_OBJECT_DEAD
SCRIPT_PLAYER = _server.SCRIPT_PLAYER
SCRIPT_MOBILE = _server.SCRIPT_MOBILE
SCRIPT_OBJECT = _server.SCRIPT_OBJECT
SCRIPT_ROOM = _server.SCRIPT_ROOM
SCRIPT_ZONE = _server.SCRIPT_ZONE
SCRIPT_SPELL = _server.SCRIPT_SPELL
SCRIPT_SKILL = _server.SCRIPT_SKILL
SCRIPT_COMMAND = _server.SCRIPT_COMMAND
SCRIPT_NULL = _server.SCRIPT_NULL
MUT_R = _server.MUT_R
MUT_W = _server.MUT_W
MUT_X = _server.MUT_X
class SCRIPT_CONT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SCRIPT_CONT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SCRIPT_CONT, name)
    def __repr__(self):
        return "<C SCRIPT_CONT instance at %s>" % (self.this,)
    __swig_setmethods__["data"] = _server.SCRIPT_CONT_data_set
    __swig_getmethods__["data"] = _server.SCRIPT_CONT_data_get
    if _newclass:data = property(_server.SCRIPT_CONT_data_get, _server.SCRIPT_CONT_data_set)
    __swig_setmethods__["write_level"] = _server.SCRIPT_CONT_write_level_set
    __swig_getmethods__["write_level"] = _server.SCRIPT_CONT_write_level_get
    if _newclass:write_level = property(_server.SCRIPT_CONT_write_level_get, _server.SCRIPT_CONT_write_level_set)
    __swig_setmethods__["cont_type"] = _server.SCRIPT_CONT_cont_type_set
    __swig_getmethods__["cont_type"] = _server.SCRIPT_CONT_cont_type_get
    if _newclass:cont_type = property(_server.SCRIPT_CONT_cont_type_get, _server.SCRIPT_CONT_cont_type_set)
    __swig_setmethods__["cont_id"] = _server.SCRIPT_CONT_cont_id_set
    __swig_getmethods__["cont_id"] = _server.SCRIPT_CONT_cont_id_get
    if _newclass:cont_id = property(_server.SCRIPT_CONT_cont_id_get, _server.SCRIPT_CONT_cont_id_set)
    def __init__(self, *args):
        _swig_setattr(self, SCRIPT_CONT, 'this', _server.new_SCRIPT_CONT(*args))
        _swig_setattr(self, SCRIPT_CONT, 'thisown', 1)
    def __del__(self, destroy=_server.delete_SCRIPT_CONT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SCRIPT_CONTPtr(SCRIPT_CONT):
    def __init__(self, this):
        _swig_setattr(self, SCRIPT_CONT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SCRIPT_CONT, 'thisown', 0)
        _swig_setattr(self, SCRIPT_CONT,self.__class__,SCRIPT_CONT)
_server.SCRIPT_CONT_swigregister(SCRIPT_CONTPtr)

GSP_CHARACTER = _server.GSP_CHARACTER
GSP_INTEGER = _server.GSP_INTEGER
GSP_LONG = _server.GSP_LONG
GSP_LONGLONG = _server.GSP_LONGLONG
GSP_STRING = _server.GSP_STRING
GSP_VOID_DATA = _server.GSP_VOID_DATA
GSP_OBJECT = _server.GSP_OBJECT
GSP_INVALID = _server.GSP_INVALID
class t_script_param(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, t_script_param, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, t_script_param, name)
    def __repr__(self):
        return "<C t_script_param instance at %s>" % (self.this,)
    __swig_setmethods__["type"] = _server.t_script_param_type_set
    __swig_getmethods__["type"] = _server.t_script_param_type_get
    if _newclass:type = property(_server.t_script_param_type_get, _server.t_script_param_type_set)
    __swig_getmethods__["data"] = _server.t_script_param_data_get
    if _newclass:data = property(_server.t_script_param_data_get)
    def __init__(self, *args):
        _swig_setattr(self, t_script_param, 'this', _server.new_t_script_param(*args))
        _swig_setattr(self, t_script_param, 'thisown', 1)
    def __del__(self, destroy=_server.delete_t_script_param):
        try:
            if self.thisown: destroy(self)
        except: pass

class t_script_paramPtr(t_script_param):
    def __init__(self, this):
        _swig_setattr(self, t_script_param, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, t_script_param, 'thisown', 0)
        _swig_setattr(self, t_script_param,self.__class__,t_script_param)
_server.t_script_param_swigregister(t_script_paramPtr)

class t_script_param_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, t_script_param_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, t_script_param_data, name)
    def __repr__(self):
        return "<C t_script_param_data instance at %s>" % (self.this,)
    __swig_setmethods__["l_val"] = _server.t_script_param_data_l_val_set
    __swig_getmethods__["l_val"] = _server.t_script_param_data_l_val_get
    if _newclass:l_val = property(_server.t_script_param_data_l_val_get, _server.t_script_param_data_l_val_set)
    __swig_setmethods__["i_val"] = _server.t_script_param_data_i_val_set
    __swig_getmethods__["i_val"] = _server.t_script_param_data_i_val_get
    if _newclass:i_val = property(_server.t_script_param_data_i_val_get, _server.t_script_param_data_i_val_set)
    __swig_setmethods__["c_val"] = _server.t_script_param_data_c_val_set
    __swig_getmethods__["c_val"] = _server.t_script_param_data_c_val_get
    if _newclass:c_val = property(_server.t_script_param_data_c_val_get, _server.t_script_param_data_c_val_set)
    __swig_setmethods__["ll_val"] = _server.t_script_param_data_ll_val_set
    __swig_getmethods__["ll_val"] = _server.t_script_param_data_ll_val_get
    if _newclass:ll_val = property(_server.t_script_param_data_ll_val_get, _server.t_script_param_data_ll_val_set)
    __swig_setmethods__["str"] = _server.t_script_param_data_str_set
    __swig_getmethods__["str"] = _server.t_script_param_data_str_get
    if _newclass:str = property(_server.t_script_param_data_str_get, _server.t_script_param_data_str_set)
    __swig_setmethods__["ptr"] = _server.t_script_param_data_ptr_set
    __swig_getmethods__["ptr"] = _server.t_script_param_data_ptr_get
    if _newclass:ptr = property(_server.t_script_param_data_ptr_get, _server.t_script_param_data_ptr_set)
    __swig_setmethods__["obj"] = _server.t_script_param_data_obj_set
    __swig_getmethods__["obj"] = _server.t_script_param_data_obj_get
    if _newclass:obj = property(_server.t_script_param_data_obj_get, _server.t_script_param_data_obj_set)
    def __init__(self, *args):
        _swig_setattr(self, t_script_param_data, 'this', _server.new_t_script_param_data(*args))
        _swig_setattr(self, t_script_param_data, 'thisown', 1)
    def __del__(self, destroy=_server.delete_t_script_param_data):
        try:
            if self.thisown: destroy(self)
        except: pass

class t_script_param_dataPtr(t_script_param_data):
    def __init__(self, this):
        _swig_setattr(self, t_script_param_data, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, t_script_param_data, 'thisown', 0)
        _swig_setattr(self, t_script_param_data,self.__class__,t_script_param_data)
_server.t_script_param_data_swigregister(t_script_param_dataPtr)

HOOK_RANDOM_CHANCE = _server.HOOK_RANDOM_CHANCE
HOOK_COMMAND_ENTERED = _server.HOOK_COMMAND_ENTERED
HOOK_COMMAND_OVERRIDE = _server.HOOK_COMMAND_OVERRIDE
HOOK_SPEECH = _server.HOOK_SPEECH
HOOK_ACTION = _server.HOOK_ACTION
HOOK_CONT_DIED = _server.HOOK_CONT_DIED
HOOK_CHAR_ENTERED = _server.HOOK_CHAR_ENTERED
HOOK_CONT_ENTERED = _server.HOOK_CONT_ENTERED
HOOK_RECEIVED_ITEM = _server.HOOK_RECEIVED_ITEM
HOOK_FIGHTING = _server.HOOK_FIGHTING
HOOK_HITPERCENT_LESSTHAN = _server.HOOK_HITPERCENT_LESSTHAN
HOOK_GIVEN_CASH = _server.HOOK_GIVEN_CASH
HOOK_CONT_LOADED = _server.HOOK_CONT_LOADED
HOOK_CONT_ENEMY_SEEN = _server.HOOK_CONT_ENEMY_SEEN
HOOK_CONT_SPELLHIT = _server.HOOK_CONT_SPELLHIT
HOOK_CHAR_LEFT = _server.HOOK_CHAR_LEFT
HOOK_DOOR_CHANGED = _server.HOOK_DOOR_CHANGED
HOOK_DECAYTIMER = _server.HOOK_DECAYTIMER
HOOK_CONT_GET = _server.HOOK_CONT_GET
HOOK_CONT_DROP = _server.HOOK_CONT_DROP
HOOK_CONT_GIVEN = _server.HOOK_CONT_GIVEN
HOOK_CONT_WORN = _server.HOOK_CONT_WORN
HOOK_CONT_REMOVED = _server.HOOK_CONT_REMOVED
HOOK_CONT_RESET = _server.HOOK_CONT_RESET
HOOK_CONT_PUT = _server.HOOK_CONT_PUT
HOOK_CONT_TELEPORTED = _server.HOOK_CONT_TELEPORTED
HOOK_PLAYER_ENTERED_GAME = _server.HOOK_PLAYER_ENTERED_GAME
HOOK_CAST = _server.HOOK_CAST
class ScriptEventArgs(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ScriptEventArgs, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ScriptEventArgs, name)
    def __repr__(self):
        return "<C ScriptEventArgs instance at %s>" % (self.this,)
    __swig_setmethods__["sender"] = _server.ScriptEventArgs_sender_set
    __swig_getmethods__["sender"] = _server.ScriptEventArgs_sender_get
    if _newclass:sender = property(_server.ScriptEventArgs_sender_get, _server.ScriptEventArgs_sender_set)
    __swig_setmethods__["actor"] = _server.ScriptEventArgs_actor_set
    __swig_getmethods__["actor"] = _server.ScriptEventArgs_actor_get
    if _newclass:actor = property(_server.ScriptEventArgs_actor_get, _server.ScriptEventArgs_actor_set)
    __swig_setmethods__["arg1"] = _server.ScriptEventArgs_arg1_set
    __swig_getmethods__["arg1"] = _server.ScriptEventArgs_arg1_get
    if _newclass:arg1 = property(_server.ScriptEventArgs_arg1_get, _server.ScriptEventArgs_arg1_set)
    __swig_setmethods__["arg2"] = _server.ScriptEventArgs_arg2_set
    __swig_getmethods__["arg2"] = _server.ScriptEventArgs_arg2_get
    if _newclass:arg2 = property(_server.ScriptEventArgs_arg2_get, _server.ScriptEventArgs_arg2_set)
    def __init__(self, *args):
        _swig_setattr(self, ScriptEventArgs, 'this', _server.new_ScriptEventArgs(*args))
        _swig_setattr(self, ScriptEventArgs, 'thisown', 1)
    def __del__(self, destroy=_server.delete_ScriptEventArgs):
        try:
            if self.thisown: destroy(self)
        except: pass

class ScriptEventArgsPtr(ScriptEventArgs):
    def __init__(self, this):
        _swig_setattr(self, ScriptEventArgs, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, ScriptEventArgs, 'thisown', 0)
        _swig_setattr(self, ScriptEventArgs,self.__class__,ScriptEventArgs)
_server.ScriptEventArgs_swigregister(ScriptEventArgsPtr)
SNull = cvar.SNull

class ScriptListener(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ScriptListener, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ScriptListener, name)
    def __repr__(self):
        return "<C ScriptListener instance at %s>" % (self.this,)
    __swig_setmethods__["module"] = _server.ScriptListener_module_set
    __swig_getmethods__["module"] = _server.ScriptListener_module_get
    if _newclass:module = property(_server.ScriptListener_module_get, _server.ScriptListener_module_set)
    __swig_setmethods__["language"] = _server.ScriptListener_language_set
    __swig_getmethods__["language"] = _server.ScriptListener_language_get
    if _newclass:language = property(_server.ScriptListener_language_get, _server.ScriptListener_language_set)
    __swig_setmethods__["actionType"] = _server.ScriptListener_actionType_set
    __swig_getmethods__["actionType"] = _server.ScriptListener_actionType_get
    if _newclass:actionType = property(_server.ScriptListener_actionType_get, _server.ScriptListener_actionType_set)
    __swig_setmethods__["handler"] = _server.ScriptListener_handler_set
    __swig_getmethods__["handler"] = _server.ScriptListener_handler_get
    if _newclass:handler = property(_server.ScriptListener_handler_get, _server.ScriptListener_handler_set)
    __swig_setmethods__["next"] = _server.ScriptListener_next_set
    __swig_getmethods__["next"] = _server.ScriptListener_next_get
    if _newclass:next = property(_server.ScriptListener_next_get, _server.ScriptListener_next_set)
    def __init__(self, *args):
        _swig_setattr(self, ScriptListener, 'this', _server.new_ScriptListener(*args))
        _swig_setattr(self, ScriptListener, 'thisown', 1)
    def __del__(self, destroy=_server.delete_ScriptListener):
        try:
            if self.thisown: destroy(self)
        except: pass

class ScriptListenerPtr(ScriptListener):
    def __init__(self, this):
        _swig_setattr(self, ScriptListener, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, ScriptListener, 'thisown', 0)
        _swig_setattr(self, ScriptListener,self.__class__,ScriptListener)
_server.ScriptListener_swigregister(ScriptListenerPtr)


obj_script_cont = _server.obj_script_cont

ch_script_cont = _server.ch_script_cont

check_hooks = _server.check_hooks

check_cast_hooks = _server.check_cast_hooks

script_hook_command = _server.script_hook_command

check_null_hooks = _server.check_null_hooks

check_mob_hooks = _server.check_mob_hooks

str_to_param = _server.str_to_param

int_to_param = _server.int_to_param

obj_to_param = _server.obj_to_param

script_greet_memory = _server.script_greet_memory

script_mob_loaded = _server.script_mob_loaded

script_obj_loaded = _server.script_obj_loaded

script_mob_leave_trigger = _server.script_mob_leave_trigger

script_char_left_room_trigger = _server.script_char_left_room_trigger

script_char_door_trigger = _server.script_char_door_trigger

script_enter_trigger = _server.script_enter_trigger

script_act_trigger = _server.script_act_trigger

script_cast_trigger = _server.script_cast_trigger

script_random_mob_trigger = _server.script_random_mob_trigger

script_char_enter_room_trigger = _server.script_char_enter_room_trigger

script_drop_trigger = _server.script_drop_trigger

script_drop_o_trigger = _server.script_drop_o_trigger

script_get_o_trigger = _server.script_get_o_trigger

script_give_o_trigger = _server.script_give_o_trigger

script_wear_o_trigger = _server.script_wear_o_trigger

script_remove_o_trigger = _server.script_remove_o_trigger

script_random_o_trigger = _server.script_random_o_trigger

script_timer_o_trigger = _server.script_timer_o_trigger

script_random_w_trigger = _server.script_random_w_trigger

script_compute_kill_exp = _server.script_compute_kill_exp

script_char_damage_char = _server.script_char_damage_char

script_char_compute_armor_class = _server.script_char_compute_armor_class

script_char_compute_damroll = _server.script_char_compute_damroll

script_char_compute_hitroll = _server.script_char_compute_hitroll

script_char_compute_thaco = _server.script_char_compute_thaco

script_pulse = _server.script_pulse

script_char_hitmiss_catch = _server.script_char_hitmiss_catch

send_bad_position_message = _server.send_bad_position_message

script_mobread = _server.script_mobread

script_objread = _server.script_objread

script_roomread = _server.script_roomread

script_add_system_listener = _server.script_add_system_listener

script_del_system_listener = _server.script_del_system_listener

script_check_system_listeners = _server.script_check_system_listeners

script_clear_listeners_language = _server.script_clear_listeners_language

script_free_listener = _server.script_free_listener

script_make_listener = _server.script_make_listener

script_check_listeners = _server.script_check_listeners
SCRIPTFLAG_GLOBAL = _server.SCRIPTFLAG_GLOBAL
SCRIPTFLAG_OBJ_EQUIPPED = _server.SCRIPTFLAG_OBJ_EQUIPPED
SCRIPTFLAG_OBJ_INVENTORY = _server.SCRIPTFLAG_OBJ_INVENTORY
SCRIPTFLAG_OBJ_ROOM = _server.SCRIPTFLAG_OBJ_ROOM
PYSCRIPTS_VERSION = _server.PYSCRIPTS_VERSION

py_pulse = _server.py_pulse

shutdown_python = _server.shutdown_python

boot_python = _server.boot_python
class py_command_info(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, py_command_info, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, py_command_info, name)
    def __repr__(self):
        return "<C py_command_info instance at %s>" % (self.this,)
    __swig_setmethods__["hashcode"] = _server.py_command_info_hashcode_set
    __swig_getmethods__["hashcode"] = _server.py_command_info_hashcode_get
    if _newclass:hashcode = property(_server.py_command_info_hashcode_get, _server.py_command_info_hashcode_set)
    __swig_setmethods__["number"] = _server.py_command_info_number_set
    __swig_getmethods__["number"] = _server.py_command_info_number_get
    if _newclass:number = property(_server.py_command_info_number_get, _server.py_command_info_number_set)
    __swig_setmethods__["name"] = _server.py_command_info_name_set
    __swig_getmethods__["name"] = _server.py_command_info_name_get
    if _newclass:name = property(_server.py_command_info_name_get, _server.py_command_info_name_set)
    __swig_setmethods__["minimum_position"] = _server.py_command_info_minimum_position_set
    __swig_getmethods__["minimum_position"] = _server.py_command_info_minimum_position_get
    if _newclass:minimum_position = property(_server.py_command_info_minimum_position_get, _server.py_command_info_minimum_position_set)
    __swig_setmethods__["py_callfun"] = _server.py_command_info_py_callfun_set
    __swig_getmethods__["py_callfun"] = _server.py_command_info_py_callfun_get
    if _newclass:py_callfun = property(_server.py_command_info_py_callfun_get, _server.py_command_info_py_callfun_set)
    __swig_setmethods__["native_callfun"] = _server.py_command_info_native_callfun_set
    __swig_getmethods__["native_callfun"] = _server.py_command_info_native_callfun_get
    if _newclass:native_callfun = property(_server.py_command_info_native_callfun_get, _server.py_command_info_native_callfun_set)
    __swig_setmethods__["minimum_level"] = _server.py_command_info_minimum_level_set
    __swig_getmethods__["minimum_level"] = _server.py_command_info_minimum_level_get
    if _newclass:minimum_level = property(_server.py_command_info_minimum_level_get, _server.py_command_info_minimum_level_set)
    __swig_setmethods__["subcmd"] = _server.py_command_info_subcmd_set
    __swig_getmethods__["subcmd"] = _server.py_command_info_subcmd_get
    if _newclass:subcmd = property(_server.py_command_info_subcmd_get, _server.py_command_info_subcmd_set)
    __swig_setmethods__["priority"] = _server.py_command_info_priority_set
    __swig_getmethods__["priority"] = _server.py_command_info_priority_get
    if _newclass:priority = property(_server.py_command_info_priority_get, _server.py_command_info_priority_set)
    __swig_setmethods__["override"] = _server.py_command_info_override_set
    __swig_getmethods__["override"] = _server.py_command_info_override_get
    if _newclass:override = property(_server.py_command_info_override_get, _server.py_command_info_override_set)
    __swig_setmethods__["next"] = _server.py_command_info_next_set
    __swig_getmethods__["next"] = _server.py_command_info_next_get
    if _newclass:next = property(_server.py_command_info_next_get, _server.py_command_info_next_set)
    def __init__(self, *args):
        _swig_setattr(self, py_command_info, 'this', _server.new_py_command_info(*args))
        _swig_setattr(self, py_command_info, 'thisown', 1)
    def __del__(self, destroy=_server.delete_py_command_info):
        try:
            if self.thisown: destroy(self)
        except: pass

class py_command_infoPtr(py_command_info):
    def __init__(self, this):
        _swig_setattr(self, py_command_info, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, py_command_info, 'thisown', 0)
        _swig_setattr(self, py_command_info,self.__class__,py_command_info)
_server.py_command_info_swigregister(py_command_infoPtr)

class py_MudModule(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, py_MudModule, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, py_MudModule, name)
    def __repr__(self):
        return "<C py_MudModule instance at %s>" % (self.this,)
    __swig_setmethods__["name"] = _server.py_MudModule_name_set
    __swig_getmethods__["name"] = _server.py_MudModule_name_get
    if _newclass:name = property(_server.py_MudModule_name_get, _server.py_MudModule_name_set)
    __swig_setmethods__["obj"] = _server.py_MudModule_obj_set
    __swig_getmethods__["obj"] = _server.py_MudModule_obj_get
    if _newclass:obj = property(_server.py_MudModule_obj_get, _server.py_MudModule_obj_set)
    __swig_setmethods__["next"] = _server.py_MudModule_next_set
    __swig_getmethods__["next"] = _server.py_MudModule_next_get
    if _newclass:next = property(_server.py_MudModule_next_get, _server.py_MudModule_next_set)
    def __init__(self, *args):
        _swig_setattr(self, py_MudModule, 'this', _server.new_py_MudModule(*args))
        _swig_setattr(self, py_MudModule, 'thisown', 1)
    def __del__(self, destroy=_server.delete_py_MudModule):
        try:
            if self.thisown: destroy(self)
        except: pass

class py_MudModulePtr(py_MudModule):
    def __init__(self, this):
        _swig_setattr(self, py_MudModule, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, py_MudModule, 'thisown', 0)
        _swig_setattr(self, py_MudModule,self.__class__,py_MudModule)
_server.py_MudModule_swigregister(py_MudModulePtr)


room_deref = _server.room_deref

descriptor_deref = _server.descriptor_deref

char_deref = _server.char_deref

py_Bottle_Char = _server.py_Bottle_Char

py_Bottle_Room_vnum = _server.py_Bottle_Room_vnum

py_Bottle_Exit = _server.py_Bottle_Exit

py_Bottle_Obj = _server.py_Bottle_Obj

py_char_getname = _server.py_char_getname

python_obj_call = _server.python_obj_call

python_wld_call = _server.python_wld_call

python_mob_call = _server.python_mob_call
class charp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, charp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, charp, name)
    def __repr__(self):
        return "<C charp instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, charp, 'this', _server.new_charp(*args))
        _swig_setattr(self, charp, 'thisown', 1)
    def __del__(self, destroy=_server.delete_charp):
        try:
            if self.thisown: destroy(self)
        except: pass
    def assign(*args): return _server.charp_assign(*args)
    def value(*args): return _server.charp_value(*args)
    def cast(*args): return _server.charp_cast(*args)
    __swig_getmethods__["frompointer"] = lambda x: _server.charp_frompointer
    if _newclass:frompointer = staticmethod(_server.charp_frompointer)

class charpPtr(charp):
    def __init__(self, this):
        _swig_setattr(self, charp, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, charp, 'thisown', 0)
        _swig_setattr(self, charp,self.__class__,charp)
_server.charp_swigregister(charpPtr)

charp_frompointer = _server.charp_frompointer


class_abbreviate = _server.class_abbreviate

double_deref_doublechar = _server.double_deref_doublechar

deref_doublechar = _server.deref_doublechar

deref_char = _server.deref_char

