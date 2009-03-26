"""pyInitEnv

"""

__revision__ = "$Id: __init__.py 160 2008-10-15 09:46:38Z  $"
__version__ = "1.0"

import sys;
from profiles import profiles, profile_params, profile_params_to_string, profile_post_actions;

def trace (msg):
	if True:
		if False:
			sys.stderr.write (msg)

def has_sub_module (cfg_name):
#	trace ("has [%s] ? \n" % (cfg_name))
	try:
		__import__("%s.%s" % (__name__, cfg_name))
		return 1
	except:
		trace ("Error importing [%s] ? \n" % (cfg_name))
		return 0

def configs():
	import os;
	import re;
	
	trace ("Loading configs\n")
	dirname = os.path.dirname(__file__)
	list_files = os.listdir (dirname)
	cfg = []
	p = re.compile ("^([a-z0-9][a-zA-Z0-9_]+)\.py$")
	for f in list_files:
		mo = p.match (f)
		if mo:
			trace (" - %s\n" %(mo.group(1)))
			cfg.append (mo.group(1))

	res = []
	cfg.sort()
	for c in cfg:
		if has_sub_module(c):
			trace (" -> %s\n" % (c))
			res.append(c)

	return res;

def call_from (cfg_name, featname):
	try:
		__import__("%s.%s" % (__name__, cfg_name))
		cmd = "%s.%s" % (cfg_name, featname)
		#sys.stderr.write("cmd=%s \n" % (cmd))
		return eval (cmd)
	except:
		return None

def process_from (cfg_name, featname, report_error=True):
	modname = cfg_name;
	try:
		__import__("%s.%s" % (__name__, modname))
		cmd = "%s.%s" % (modname, featname)
#		sys.stderr.write("cmd=[%s]\n" % (cmd))
		return eval (cmd)
	except:
		if report_error:
			sys.stderr.write("\n\n-------------\n")
			sys.stderr.write(" -> Cmd failed [%s.%s]" % (modname, featname))
			sys.stderr.write("\n-------------\n")
			sys.stderr.write ("\n\nUnexpected error: %s" % (sys.exc_info()[0]))
#			sys.stderr.write ("\n\nUnexpected error: %s" % (sys.exc_info()[1]))
			sys.stderr.write("\n-------------\n")
		return None

def id_from (cfg_name):
	return call_from (cfg_name, "id()")
def choices_from (cfg_name):
	return call_from (cfg_name, "choices()")
def datas_from (cfg_name):
	arr = [cfg_name]
	arr.extend (call_from (cfg_name, "datas()"))
	return arr

def process_output_init (cfg_name,title,home_bin,choice):
	sys.stdout.write("@echo [Init: %s] \n" % (title))
	process_from (cfg_name, "output_init(\'%s\',\'%s\', sys.stdout)" % (home_bin.replace ('\\', '\\\\'), choice))
	sys.stdout.write("\n")

def process_output (cfg_name,title,home_bin,choice):
	sys.stdout.write("@echo [Setting: %s] \n" % (title))
	process_from (cfg_name, "output(\'%s\',\'%s\', sys.stdout)" % (home_bin.replace ('\\', '\\\\'), choice))
	sys.stdout.write("\n")

