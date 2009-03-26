#!/usr/local/bin/python

import os;
import sys;
import string;
import pyjoce.os2;
from pyjoce.conf import config;
import pyjoce
from pyjoce import pyInitEnv;

from framework.tracer import Tracer;
from framework.questionner import Questionner;

#sys.path.append(pyjoce.__path__[0])
#sys.stderr.write ("%s\n" % (sys.path))
#sys.exit()

tracer = Tracer();
quest = Questionner(tracer);

def trace (msg):
	tracer.put(msg)

### Start ... ###


configs = pyjoce.pyInitEnv.configs();
entries=[]
custom_modes={}
the_profile = ''

for c in configs:
	#trace("conf=%s\n" % (c))
	entries.append (pyjoce.pyInitEnv.datas_from(c))

entries.sort (lambda x, y: cmp(x[1],y[1]))


try:
	custom_modes['debug'] = sys.argv[sys.argv.index("--debug")+1]
except (IndexError, ValueError):
	custom_modes['debug'] = ''

try:
	custom_modes['platform'] = sys.argv[sys.argv.index("--platform")+1]
except (IndexError, ValueError):
	if pyjoce.os2.is_current_platform_win64:
		custom_modes['platform'] = "win64"
	elif pyjoce.os2.is_current_platform_win32:
		custom_modes['platform'] = "windows"
	else:
		custom_modes['platform'] = ''

try:
	custom_modes['library'] = sys.argv[sys.argv.index("--library")+1]
except (IndexError, ValueError):
	custom_modes['library'] = 'src'

try:
	custom_modes['colors'] = sys.argv[sys.argv.index("--colors")+1]
except (IndexError, ValueError):
	custom_modes['colors'] = ''

try:
	name = sys.argv[sys.argv.index("--name")+1]
except (IndexError, ValueError):
	name = ''

profiles = pyjoce.pyInitEnv.profiles();
try:
	the_profile = sys.argv[sys.argv.index("--profile")+1]
except (IndexError, ValueError):
	the_profile = ''

### Get Args ###
versions = {}
nb_versions = 0
if len(entries) == 0:
	trace("No config !!\n")
else:
	for e in entries:
		if e == None:
			trace ("None object !!!!\n")
		else:
			k = e[0]
			p = e[3]
			#trace ("Getting args %-10s " % (p))
			the_version = ''
			try:
				the_version = sys.argv[sys.argv.index(p) + 1]
				nb_versions = nb_versions + 1
			except (IndexError, ValueError):
				the_version = ''
			#trace (" -> %s=%s \n" % (k, the_version))
			versions[k] = the_version

dft_prof = "-select-"
if nb_versions == 0 and len(the_profile) == 0:
	if len(profiles) > 0:
		values = {}
		values_keys = []
		dft = dft_prof

		for p in profiles:
			if p == "default":
				dft = p
			values_keys.append(p)
			pstr = pyjoce.pyInitEnv.profile_params_to_string(p);
			values[p] = pstr
			#trace(" - profile: %s=%s\n" % (p, pstr))

		values_keys.append(dft_prof)
		values[dft_prof] = 'Select each parameter'

		k = "_default"
		values_keys.append(k)
		values[k] = dft

		the_profile = quest.process_question("Profile", values, values_keys)

if len(the_profile) > 0 and the_profile != dft_prof:
	trace("Load profile %s\n" % (the_profile))
	vv = pyjoce.pyInitEnv.profile_params(the_profile);
	for v in vv:
		if versions.has_key (v):
			if len(versions[v]) == 0:
				versions[v] = vv[v]
			else:
				trace(" - Profile value [%s=%s] overwritten by [%s]\n" %(v, vv[v], versions[v]));
		else:
			custom_modes[v] = vv[v]

for cm in custom_modes:
	if len(custom_modes[cm]) > 0:
		#trace("set initenv_var_%s=%s\n" %(cm, custom_modes[cm]))
		os.environ["initenv_var_%s" % (cm)] = custom_modes[cm]

if True:
	if False:
		for v in versions:
			trace(" :: %s=%s\n" % (v, versions[v]))

### Check params ###
for e in entries:
	the_version = versions[e[0]]
#	trace ("the_version=%s\n" % (the_version))
	values = {}
	values_keys = []
	for val in e[4]:
		values [val[0]] = val[1]
		values_keys.append (val[0])

	if not values.has_key (the_version): 
		if e[5] and os.path.exists (the_version):
			the_version = the_version
		else:
			the_version = quest.process_question(e[2], values, values_keys)
	versions[e[0]] = the_version

### Display config ###
trace ( "Set environment :\n\n")
cmd = ""
title = ""
for e in entries:
	k = e[0]
	v = versions[k]
	trace (" - %-10s = %-6s \n" % (k, v))
	if v != "_none" and v != "_skip":
		title = "%s%s:" % (title, v)
	cmd = "%s %s %s" % (cmd, e[3], v)

if len(custom_modes) > 0:
	cmd = "%s \n\t\t" % (cmd)
	for cm in custom_modes:
		if len(custom_modes[cm]) > 0:
			cmd = "%s %s %s" % (cmd, "--" + cm, custom_modes[cm])
trace (" => initenv %s \n" % (cmd))
trace ("\n")

### Build config ###
home_bin ="%HOME%\\bin"
sys.stdout.write ("@call %s\\initenv_common.bat\n" % (home_bin))

# First loop to init essential settings
for e in entries:
	k = e[0]
	t = e[2]
	v = versions[k]
	trace (" + %-10s = %-6s (init)" % (t, v))
	pyjoce.pyInitEnv.process_output_init (k,t,home_bin, v)
	trace ("\n")

# Second loop to complete settings
for e in entries:
	k = e[0]
	t = e[2]
	v = versions[k]
	trace (" + %-10s = %-6s " % (t, v))
	pyjoce.pyInitEnv.process_output (k,t,home_bin, v)
	trace ("\n")

if len(custom_modes['colors']) > 0:
	sys.stdout.write ("\n@color %s\n" % (custom_modes['colors']))

if len(name) > 0:
	sys.stdout.write ("\n@title %s\n" % (name))
else:
	sys.stdout.write ("\n@title %s\n" % (title))

	# clean Env variables PATH, LIB, INCLUDE #
sys.stdout.write ("@echo off\n")
sys.stdout.write ("@call %s\\clean_env_var.bat %s\n" % (home_bin, 'PATH'))
sys.stdout.write ("@call %s\\clean_env_var.bat %s\n" % (home_bin, 'LIB'))
sys.stdout.write ("@call %s\\clean_env_var.bat %s\n" % (home_bin, 'INCLUDE'))

if len(the_profile) >0:
	sys.stdout.write ("@echo ### Using profile %s ###\n" %( the_profile))

	the_post_actions = pyjoce.pyInitEnv.profile_post_actions(the_profile);
	if the_post_actions != None:
		for a in the_post_actions:
			trace("%s\n" %(a))
			sys.stdout.write ("%s\n" %(a))
# End #
