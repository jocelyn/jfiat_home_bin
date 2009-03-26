#!/usr/local/bin/python


import sys
import os
import string
import re


def is_CSH_shell ():
	return os.environ['SHELL'][-3:] == 'csh'

def is_current_platform_win64 ():
	return sys.platform == 'win32' and "64 bit (AMD64)" in sys.version
def is_current_platform_win32 ():
	return sys.platform == 'win32'
def is_current_platform_windows ():
	return sys.platform == 'win32'
def is_current_platform_sunos ():
	return sys.platform[:5] == 'sunos'
def is_current_platform_linux ():
	return sys.platform[:5] == 'linux'

def dir_separator ():
	return os.sep

def path_separator ():
	return os.pathsep      

def make_os_path (path):
	if is_current_platform_windows ():
		result = string.replace(path, '/', '\\')
		result = string.replace(result, '\\\\', '\\')
	else:
		result = string.replace(path, '\\', '/')
		result = string.replace(result, '//', '/')
	return result

def make_env (var):
	if is_current_platform_windows ():
		return "%%%s%%" % (var)
	else:
		return "${%s}" % (var)

def make_set_variable (varname, varvalue):
	if is_current_platform_windows():
		return "set %s=%s" % (varname, varvalue)
	else:
		if is_CSH_shell ():
			return "setenv %s %s" % (varname, varvalue)
		else:
			return "%s=%s" % (varname, varvalue)

def make_source_file (filename):
	if is_current_platform_windows():
		return "Not Available"
 	else:
		return "source %s" % (filename)

def path_added_with (var):
	path_env = path_cleaned ()
	path_env = "%s%s%s" % (path_env, path_separator() ,var)
	os.environ['PATH'] = path_env
	return os.environ['PATH']

def path_removed_by (var):
	path_env = path_cleaned ()
	paths = re.split (path_separator (), path_env)
	result = ""
	lower_var = "%s" % var
	lower_var = lower_var.lower()
	for path in paths:
		lower_path = "%s" % path
		lower_path = lower_path.lower()
		if lower_path != lower_var:
			result = "%s%s%s" % (result,path, path_separator())
	os.environ['PATH'] = result[:-1]
	return os.environ['PATH']

def path_cleaned (delpath=""):
	var = 'PATH'
	arr = env_var_cleaned_array (var, delpath)
	res = []
	for p in arr:
#		sys.stderr.write ("%s\n" % (p))
		if os.path.exists (p):
			res.append (p)
	os.environ[var] = array_to_value(res, path_separator())
	return os.environ [var]

def env_var_cleaned_array (var, delvar=""):
	var_env = os.environ[var]
#	sys.stderr.write ("env_var_cleaned_array (var=%s, delvar=%s)\n" % (var, delvar))

	values = re.split (path_separator(), var_env)
	new_values = []
	new_lower_values = []
	lower_delvar = "%s" % (delvar)
	lower_delvar = lower_delvar.lower()
	for v in values:
		lower_value = "%s" % v
		lower_value = lower_value.lower()
#		sys.stderr.write ("env_var_cleaned_array -> %s\n" % (lower_value))
		if lower_delvar != lower_value:
			if (not lower_value in new_lower_values) and ( len (lower_value) > 0):
				new_lower_values.append (lower_value)
				new_values.append (v)
#		else:
#			sys.stderr.write ("env_var_cleaned_array -> FOUND\n")
	return new_values

def array_to_value (new_values, var_separator):
	result = ""
	for v in new_values:
		result = "%s%s%s" % (result, v, var_separator)
	return result[:-1]

def env_var_cleaned (var):
	new_values = env_var_cleaned_array (var)
	return array_to_value(new_values, path_separator())

