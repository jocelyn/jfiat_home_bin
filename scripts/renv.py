#!/usr/local/bin/python

#
# How to use it ?
#
#---------------------------------------------------------------------------
# Win32: create a bat file containing
#
# [renv.bat]
#		@echo off
#		set TMP_BAT=%TMP%\__tmp__rainbow_env.bat
#		python %BINDIR%\renv.py %TMP_BAT% %1 %2 %3
#		call %TMP_BAT%
#		@echo off
#		del %TMP_BAT%
#		@echo on
# --------------------------------------------------------------------------
# Unices: create an alias :
#	alias renv "python ~/bin/renv.py /tmp/.__tmp__renv \!:\ none ; \
#				source /tmp/.__tmp__renv; \rm /tmp/.__tmp__renv ;"
#	
#---------------------------------------------------------------------------

import sys;
import os;
import string;
import pyjoce.os2;

def is_CSH_shell ():
	return os.environ['SHELL'][-3:] == 'csh'

def is_current_platform_win32 ():
	return sys.platform == 'win32'

###############################################
### CONFIGURATION                           ###

if is_current_platform_win32 () :
	source_dir = "d:/users/jfiat/work/rainbow/src/"
	compilation_dir = "d:/compilation/rainbow/"
else:
	source_dir = "/home/jfiat/src/"
	compilation_dir = "/home/jfiat/compile.jfiat/"

lst_os = ['win', 'lin', 'sol']
lst_eiffel = ['ise', 'iss']
lst_version = ['dev', 'prod', 'browse']

# First is default

###############################################
### PLEASE DO NOT CHANGE THE FOLLOWING TEXT ###

def array_contains (a_array, a_item):
	found = 0
	for item in a_array:
		found = found or (item == a_item)
	return found


def make_os_path (path):
	if is_current_platform_win32 ():
		return string.replace(path, "/", "\\")
	else:
		return string.replace(path, "\\", "/")

def make_env (var):
	if is_current_platform_win32 ():
		return "%%%s%%" % (var)
	else:
		return "${%s}" % (var)


def saveConfig (filecontent, filename):
	outputfile = open (filename, 'w');
	outputfile.write (filecontent)
	outputfile.close ()

def usage():
	print ""
	print "Usage: script  file.bat version os eiffel  "
	print "               version  : dev | prod       "
	print "               os       : win | lin | sol  "
	print "               eiffel   : iss | ise        \n\n"

def make_set_variable (varname, varvalue):
	if is_current_platform_win32():
		return "set %s=%s" % (varname, varvalue)
 	else:
		if is_CSH_shell ():
			return "setenv %s %s" % (varname, varvalue)
		else:
			return "%s=%s" % (varname, varvalue)

def main():
	if len(sys.argv) < 2:
		# At least one arg : the filename
		usage ();
	else:
		rainbow_conf = {}
		if os.environ.has_key ('RAINBOW_OS'):
			rainbow_conf['os'] = os.environ['RAINBOW_OS']
		if os.environ.has_key ('RAINBOW_EIFFEL'):
			rainbow_conf['eiffel'] = os.environ['RAINBOW_EIFFEL']
		if os.environ.has_key ('RAINBOW_VERSANT'):
			rainbow_conf['version'] = os.environ['RAINBOW_VERSION']


		outputfilename = sys.argv[1]
		argv = sys.argv[3:]
		argc = len (argv)
		i = 0
		while i < argc :
			arg = argv[i]
			if arg in lst_os:
				rainbow_conf['os'] = arg
			elif arg in lst_eiffel:
				rainbow_conf['eiffel'] = arg
			elif arg in lst_version:
				rainbow_conf['version'] = arg
			i = i + 1


		if not rainbow_conf.has_key ('version'):
			rainbow_conf['version'] = lst_version[0]
		if not rainbow_conf.has_key ('os'):
			rainbow_conf['os'] = lst_os[0]
		if not rainbow_conf.has_key ('eiffel'):
			rainbow_conf['eiffel'] = lst_eiffel[0]

		#print rainbow_conf

		print "VERSION  : %s" % (rainbow_conf['version'])
		print "OS       : %s" % (rainbow_conf['os'])
		print "EIFFEL   : %s" % (rainbow_conf['eiffel'])

		# Configuration

		rainbow_root 						= source_dir + rainbow_conf['version']

		#Env setting
		rainbow_conf['rainbow'] 		= os.path.join (rainbow_root, "rainbow")
		rainbow_conf['third_party'] 	= os.path.join (rainbow_root, "third_party")
		rainbow_conf['versant'] 		= os.path.join (make_env ("RAINBOW_THIRD_PARTY"), "eifversant")
		rainbow_conf['compile'] 		= compilation_dir 

		text = ""
		text = text + "\n"
		text = text + make_set_variable ("RAINBOW_OS", rainbow_conf['os']) + "\n"
		text = text + make_set_variable ("RAINBOW_EIFFEL", rainbow_conf['eiffel']) + "\n"
		text = text + make_set_variable ("RAINBOW_VERSION", rainbow_conf['version']) + "\n"
		text = text + make_set_variable ("RAINBOW", make_os_path (rainbow_conf['rainbow'])) + "\n"
		text = text + make_set_variable ("RAINBOW_THIRD_PARTY", make_os_path (rainbow_conf['third_party'])) + "\n"
		text = text + make_set_variable ("RAINBOW_VERSANT", make_os_path (rainbow_conf['versant'])) + "\n"
		text = text + make_set_variable ("RAINBOW_COMPILE", make_os_path (rainbow_conf['compile'])) + "\n"
		tmp = rainbow_conf['compile']
		tmp = tmp + rainbow_conf['version'] 
		tmp = os.path.join (tmp, rainbow_conf['os'])
		text = text + make_set_variable ("RAINBOW_PROJECT", make_os_path (tmp))
		text = text + "\n"
		text = text + "\n"
		text = text + make_set_variable ("GOBO", os.path.join (make_os_path (rainbow_conf['third_party']), 'gobo' ) ) + "\n"
		text = text + make_set_variable ("PATH", pyjoce.os2.path_added_with (os.path.join (make_env ("GOBO"), 'bin' ) )) + "\n"
		text = text + "\n"

		if is_current_platform_win32 ():
			text = text + "SET NAGCL05_32=d:\\opt\\nag\n"
			text = text + "SET LIB=%LIB%;%NAGCL05_32%\\lib\n"
			text = text + "SET INCLUDE=%INCLUDE%;%NAGCL05_32%\\include\n"
			text = text + "\n"

		#text = text + "@echo on\n"
		print text
		saveConfig (text, outputfilename)

# MAIN PROGRAM ...
main ();

