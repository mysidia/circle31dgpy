# $Id: credits.py,v 1.2 2004/03/07 16:16:52 mysidia Exp $
import mud

registered_credit_lines = []

def dispatch(ch) :
	for x in registered_credit_lines :
		try:
			ch.write("%-8s v%-5s  : " % (str(x["module"]), x["version"]) )
			ch.send(str(x["text"]))	
		except:
			pass

def addmod(modname,modptr) :
	if not("__author__" in dir(modptr)) :
		modptr.__author__ = "Unknown"
	if not("__version__" in dir(modptr)) :
		modptr.__version__ = "?"

	y = {"module" : modname, "version" : modptr.__version__}
	content = "%-25s (%-8.8s)" %  (modptr.__author__, modptr.__date__)
	name = ""

	if "__name__" in dir(modptr) :
		name = " : " + modptr.__name__ 

	if "__text__" in dir(modptr) :
		y["text"]  = content + name + "\r\n                 : " + modptr.__text__
	else :
		y["text"] = content + name
	registered_credit_lines.append(y)

def add(module,version,text) :
	y = {"module" : module, "version" : str(version), "text" : str(text)}
	registered_credit_lines.append(y)

def remove(module) :
	for x in registered_credit_lines :
		if module == x["module"] :
			registered_credit_lines.delete(x)
