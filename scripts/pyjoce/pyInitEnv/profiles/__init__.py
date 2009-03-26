"""pyInitEnv

"""

__revision__ = "$Id: __init__.py 159 2008-10-15 09:38:07Z  $"
__version__ = "1.1"

import sys;

def trace (msg):
	if True:
		if False:
			sys.stderr.write (msg)

def has_sub_module (prof_name):
#	trace ("has [%s] ? \n" % (prof_name))
	try:
		__import__("%s.%s" % (__name__, prof_name))
		return 1
	except:
		trace ("Error importing [%s] ? \n" % (prof_name))
		return 0

def process_from (modname, featname, report_error=True):
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

def profile_params (prof_name):
	arr = {}
	par = profile_parent(prof_name)
	if par != None:
		if len(par) > 0:
			par_arr = profile_params(par)
			for p in par_arr:
				arr[p] = par_arr[p]
	p_arr = process_from(prof_name, "params()", False)
	if p_arr != None:
		for a in p_arr:
			arr[a] = p_arr[a]
	return arr;

def profile_parent (prof_name):
	return process_from(prof_name, "parent()", False)

def profile_title (prof_name):
	return process_from(prof_name, "title()", False)

def profile_params_to_string (prof_name):
	t = profile_title(prof_name);
	if t == None:
		ps = profile_params(prof_name)
		r = "\""
		for p in ps:
			r = "%s--%s %s " %(r,p, ps[p])
		r = "%s\"" %(r);
	else:
		r = t
	par = profile_parent(prof_name)
	if par != None:
		if len(par) > 0:
			r = "%s (based on %s)" % (r, par)
	return r;

def profile_post_actions (prof_name):
	arr = []
	par = profile_parent(prof_name)
	if par != None:
		if len(par) > 0:
			par_arr = profile_post_actions(par)
			for p in par_arr:
				arr.append (p)
	p_arr = process_from(prof_name, "post_actions()", False)
	if p_arr != None:
		for a in p_arr:
			arr.append (a)
	return arr;

def profiles():
	import os;
	import re;
	
	trace ("Loading profiles\n")
	dirname = os.path.dirname(__file__)
	list_files = os.listdir (dirname)
	profs = []
	p = re.compile ("^([a-z0-9][a-zA-Z0-9_]+)\.py$")
	for f in list_files:
		mo = p.match (f)
		if mo:
			profs.append (mo.group(1))

	res = []
	profs.sort()
	for c in profs:
		if has_sub_module(c):
			trace (" -> %s\n" % (c))
			res.append(c)
		else:
			trace (" -> INVALID %s\n" % (c))
	return res;

