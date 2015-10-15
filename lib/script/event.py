import mud
import server

null_event_handlers = []

def clear_system_listeners() :
	null_event_handlers = []

def add_null_system_listener(mod_name, eventType, func) :
	null_event_handlers.append({ "module" : mod_name, "type" : eventType, "handler" : func})

def remove_null_system_listener(mod_name, eventType = None) :
	for i in null_event_handlers :
		if i["module"] == mod_name :
			if eventType == None or eventType == i["type"] :
				null_event_handlers.remove(i)

def event_driver(eventType,args) :
	if args.sender.cont_type == server.SCRIPT_NULL :
		for x in null_event_handlers :
			if x["type"] != eventType :
				continue
			result = x["handler"](eventType, args)
#
#  INCOMPLETE: there's not yet passing back of info about if char/vict/object
#              was extracted
#
	return 0


#
# INCOMPLETE: No functions to unwrap the EVENT arguments or the 
#
# Script container (for NON-NULL sender, i.e. Non-Global Triggers) yet.
#
def arg_isvalid(x) :
	if x.type == GSP_INVALID :
		return 0
	return 1

def arg_ischar(x) :
	if x.type == GSP_CHARACTER :
		return 1
	return 0

def arg_isint(x) :
	if x.type == GSP_INTEGER :
		return 1
	return 0

def arg_islong(x) :
	if x.type == GSP_LONG :
		return 1
	return 0

def arg_islonglong(x) :
	if x.type == GSP_LONGLONG :
		return 1
	return 0

def arg_isstring(x) : 
	if x.type == GSP_STRING :
		return 1
	return 0

def arg_isvoid(x) :
	if x.type == GSP_VOID_DATA :
		return 1
	return 0

def arg_isobj(x) :
	if x.type == GSP_OBJECT :
		return 1
	return 0

def arg_char(x) :
	if x.type == GSP_CHARACTER :
		return x.data.c_val

	
