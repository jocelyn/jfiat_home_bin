#!/usr/local/bin/python
#
# alias set_es "python ~/bin/set_es.py \!: none  > /tmp/.__tmp__set_es ; \
#                  source /tmp/.__tmp__set_es; \
#                  \rm /tmp/.__tmp__set_es ;"
#

import sys;
import os;
import re;
import pyjoce.os2;
from pyjoce.conf.config import *;

def bin_path (p):
	if os.environ.has_key('ISE_PLATFORM'):
		isep = os.environ['ISE_PLATFORM']
	else:
		isep = '%ISE_PLATFORM%'
	return "%s/studio/spec/%s/bin" % (p, isep)


es_bin_path = {};
for k in es_path.keys():
	es_bin_path[k] = bin_path (es_path[k])
eiffel_path = {}
if pyjoce.os2.is_current_platform_win32 ():
	for kp in es_bin_path:
		eiffel_path[kp] = pyjoce.os2.make_os_path (es_bin_path[kp])

usage = "Usage: prog {"
es_bin_path_keys = es_bin_path.keys()
for k in es_bin_path_keys:
	usage = "%s|%s" % (usage, k)
usage = "%s}\n" % (usage)

if __name__ == '__main__':
	arg = ""

	if len (sys.argv) > 1:
		arg = sys.argv[1]
	if len (arg) == 0:
		arg = os.getcwd()
#		arg = es_bin_path_default_key
	if not es_bin_path.has_key (arg):
		if not os.path.exists(arg):
			arg = ''

#	sys.stderr.write ("arg=%s\n" %(arg))
#	if len (arg) == 0 and os.environ.has_key ('ISE_EIFFEL'):
#		arg = os.environ['ISE_EIFFEL']

	if es_bin_path.has_key (arg):
		sources = []
		for k in es_bin_path_keys :
			if k != arg:
				sources.append (pyjoce.os2.make_os_path (es_bin_path[k]) )
		target = eiffel_path[arg]
	elif os.path.exists(arg):
		sources = []
		for k in es_bin_path_keys :
			sources.append (pyjoce.os2.make_os_path (es_bin_path[k]) )
		target = pyjoce.os2.make_os_path (bin_path(arg))
	else:
		sources = []
		target = ""

	path_env = os.environ['PATH']
	paths = re.split (pyjoce.os2.path_separator (), path_env)
	
	for s in sources:
		virgin_path = pyjoce.os2.path_removed_by (s)
	new_path = pyjoce.os2.path_added_with (target)

	if (len (target) > 0):
		sys.stderr.write ("Set to %s ..\n" % (target))
	else:
		sys.stderr.write (usage)
		sys.exit ()

	sys.stdout.write (pyjoce.os2.make_set_variable ('PATH', new_path))
	sys.stdout.write ("\n")
