#
# Command to Restart the Python Interpreter
#

from mud import *

__name__ = "py.restart Command"
__author__ = "jh"
__date__ = "Feb 2004"
__version__ = "1.0"
__deps__ = []


def do_restart_python(ch, cmd, args, subcmd, rawtext) :
	log("(GC) %s restarting python" % (ch.get_name()), NRM, LVL_IMMORT, TRUE);
	ch.send("Restarting python...");
	py_clear_commands();
	py_restart();
