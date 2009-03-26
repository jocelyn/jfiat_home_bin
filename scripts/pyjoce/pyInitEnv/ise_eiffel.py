#!/usr/local/bin/python

import sys;
import pyjoce;
import os;
from pyjoce.conf import config;

def id():
	return "1: ise_eiffel"

def title():
	return "ISE Eiffel"

def arg():
	return "--eiffel"

def choices():
	arr = []
	res = config.es_path;
	res_keys = res.keys ()
	res_keys.sort()
	for k in res_keys:
		arr.append ([k, res[k]])
			
	arr.append (["_cwd", "Current directory"])
	arr.append (["_skip", "skip"])
	arr.append (["_default", config.es_bin_path_default_key])
	return arr;

def datas():
	return [id(), title(), arg(), choices(), True]

def output_init(home_bin,choice,out=sys.stdout):
#	out.write ("Rem ## Init:%s ##\n" % (title()))
	if choice == '_skip':
		out.write ("@echo Skipping: %s settings\n" % (title()))
	else:
		ch = choice
		if ch == "_cwd":
			ch = os.getcwd()

		if config.es_path.has_key(ch):
			eiffel_version = ch
			out.write (pyjoce.os2.make_set_variable ('ISE_EIFFEL', pyjoce.os2.make_os_path (config.es_path[eiffel_version])))
			out.write ("\n")
		else:
			eiffel_version = pyjoce.os2.make_os_path (ch)
			out.write (pyjoce.os2.make_set_variable ('ISE_EIFFEL', eiffel_version))
			out.write ("\n")

		out.write ("@echo Set ISE_EIFFEL=%s\n" % ('%ISE_EIFFEL%'))

		out.write (pyjoce.os2.make_set_variable ('ISE_LIBRARY', '%ISE_EIFFEL%')) # Default
		out.write ("\n")


			# ISE_PLATFORM #
		try:
			platf = os.environ['initenv_var_platform'];
		except:
			platf = ''
		if len(platf) > 0:
			out.write (pyjoce.os2.make_set_variable ('ISE_PLATFORM', platf))
			out.write ("\n")

			# ISE_C_COMPILER #
		if platf == 'windows' or platf == 'win64':
			out.write (pyjoce.os2.make_set_variable ('ISE_C_COMPILER', "msc"))
			out.write ("\n")

			# ISE_CFLAGS #
		try:
			debug_mode = os.environ['initenv_var_debug'];
		except:
			debug_mode = 'off'
		#debug_mode = 'no'
		if debug_mode == 'yes' or debug_mode == 'on':
			out.write (pyjoce.os2.make_set_variable ('ISE_CFLAGS', " -Zi -Zm200 -W3 "))
		else:
			out.write (pyjoce.os2.make_set_variable ('ISE_CFLAGS', " -Zm200 -W3 "))
		out.write ("\n")

			# add Estudio to PATH #
		if eiffel_version != "":
			out.write ("@call %s\\set_es.bat %s\n" % (home_bin, eiffel_version))
			out.write ("\n")

def output(home_bin,choice,out=sys.stdout):
#	out.write ("@echo ## %s ##\n" % (title()))
	if choice == '_skip':
		out.write ("@echo Skipping: %s settings\n" % (title()))
	else:
		ch = choice
		if ch == "_cwd":
			ch = os.getcwd()

		if config.es_path.has_key(ch):
			eiffel_version = ch
		else:
			eiffel_version = pyjoce.os2.make_os_path (ch)

		out.write ("@echo off\n")

			# DOCUMENT_DIR #
		out.write (pyjoce.os2.make_set_variable ('DOCUMENT_DIR', '%EIFFEL_SRC%\\..\\Documentation'))
		out.write ("\n")

			# add Build to PATH #
		out.write (pyjoce.os2.make_set_variable ('PATH', '%PATH%;%ISE_EIFFEL%\\esbuilder\\spec\\%ISE_PLATFORM%\\bin'))
		out.write ("\n")

			# add Gobo bin to PATH #
		out.write (pyjoce.os2.make_set_variable ('PATH', '%PATH%;%ISE_EIFFEL%\\library\\gobo\\spec\\%ISE_PLATFORM%\\bin'))
		out.write ("\n")

			# add Estudio to PATH #
		if eiffel_version != "":
			out.write ("@call %s\\set_es.bat %s\n" % (home_bin, eiffel_version))
			out.write ("\n")
		out.write ("@echo off\n")
