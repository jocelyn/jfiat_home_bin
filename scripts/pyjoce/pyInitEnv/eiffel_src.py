#!/usr/local/bin/python

import sys;
import os;
import pyjoce;
from pyjoce.conf import config;

def id():
	return "2: eiffel_src"

def title():
	return "Eiffel Src"

def arg():
	return "--src"

def choices():
	arr = []
	res = config.eiffel_src_path;
	res_keys = res.keys ()
	res_keys.sort()
	for k in res_keys:
		arr.append ([k, res[k]])
	arr.append (["_cwd", "Current directory"])
	arr.append (["_none", "none"])
	arr.append (["_skip", "skip"])
	arr.append (["_default", config.eiffel_src_path_default_key])
	return arr;

def datas():
	return [id(), title(), arg(), choices(), True]

def output_init(home_bin,choice,out=sys.stdout):
	out.write ("@echo off\n")
	if choice == '_skip':
		out.write ("@echo Skipping: %s settings\n" % (title()))
	else:
		#sys.stderr.write ("\n## %s ##\n" % (choice))
		#out.write ("@echo ## %s ##\n" % (choice))
		if choice == '_none':
			out.write ("@echo Unset EIFFEL_SRC\n")
			out.write (pyjoce.os2.make_set_variable ('EIFFEL_SRC', ''))
			out.write ("\n")
		else:
			if choice == '_cwd':
				out.write (pyjoce.os2.make_set_variable ('EIFFEL_SRC', os.getcwd()));
			elif os.path.exists(choice):
				out.write (pyjoce.os2.make_set_variable ('EIFFEL_SRC', choice));
			else:
				out.write (pyjoce.os2.make_set_variable ('EIFFEL_SRC', pyjoce.os2.make_os_path ("%s\\%s" % (config.eiffel_src_path[choice], "Src"))))
			out.write ("\n")

		out.write ("\n")

			# add Src\C\shell\bin to PATH #
		out.write (pyjoce.os2.make_set_variable ('PATH', '%PATH%;%EIFFEL_SRC%\\C\\shell\\bin'))
		out.write ("\n")
		out.write ("@echo Set EIFFEL_SRC=%EIFFEL_SRC%\n")


def output(home_bin,choice,out=sys.stdout):
	#out.write ("@echo ## Setting:%s ##\n" % (title()))
	if choice == '_skip':
		out.write ("@echo Skipping: %s settings\n" % (title()))
	else:
		#sys.stderr.write ("\n## %s ##\n" % (choice))
		#out.write ("@echo ## %s ##\n" % (choice))
		if choice == '_none':
			out.write (pyjoce.os2.make_set_variable ('ISE_LIBRARY', '%ISE_EIFFEL%'))
		else:
			try:
				lib_mode = os.environ['initenv_var_library'];
			except:
				lib_mode = ''
			if lib_mode == 'src':
				out.write (pyjoce.os2.make_set_variable ('ISE_LIBRARY', '%EIFFEL_SRC%'))
			else:
				out.write (pyjoce.os2.make_set_variable ('ISE_LIBRARY', '%ISE_EIFFEL%'))
		out.write ("\n")

