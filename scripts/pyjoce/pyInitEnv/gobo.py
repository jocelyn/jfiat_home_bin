#!/usr/local/bin/python

import sys;
import pyjoce;
import os;

def id():
	return "gobo";

def title():
	return "GOBO Env"

def arg():
	return "--gobo"

def choices():
	arr =[]
	arr.append (["dev", "from SVN"])
	arr.append (["ise", "from ISE_EIFFEL"])
	arr.append (["_skip", "skip"])
	arr.append (["_default", "ise"])
	return arr;

def datas():
	return [id(), title(), arg(), choices(), True]

def output_init(home_bin,choice,out=sys.stdout):
	out.write ("Rem ## Init:%s ##\n" % (title()))
	out.write ("@echo off\n")

def output(home_bin, choice,out=sys.stdout):
#	out.write ("@echo ## %s ##\n" % (title()))
	if choice == '_skip':
		out.write ("@echo Skipping: %s settings\n" % (title()))
	else:
		out.write ("@echo off\n")
		out.write ("@call %s\\clean_path.bat %s\n" % (home_bin, "D:\\eiffel\\third_party\\gobo\\bin"))
		out.write ("@call %s\\clean_path.bat %s\n" % (home_bin, "%ISE_EIFFEL%\\library\\gobo\\svn\\bin"))
		out.write ("@call %s\\clean_path.bat %s\n" % (home_bin, "%ISE_EIFFEL%\\library\\gobo\\spec\\%ISE_PLATFORM%\\bin"))
#		for v in range(57,63):
#			out.write ("@call %s\\clean_path.bat %s\n" % (home_bin, "F:\\eiffel\\%i\\library\\gobo\\svn\\bin" % (v)))
#			out.write ("@call %s\\clean_path.bat %s\n" % (home_bin, "F:\\eiffel\\%i\\library\\gobo\\spec\\%ISE_PLATFORM%\\bin" % (v)))

		out.write ("@echo off\n")
		if choice == "dev":
			out.write (pyjoce.os2.make_set_variable ('GOBO', pyjoce.os2.make_os_path ("D:\\eiffel\\third_party\\gobo")))
			out.write ("\n")
			out.write (pyjoce.os2.make_set_variable ('PATH', '%PATH%;%GOBO%\\bin'))
		elif choice == "ise":
			out.write (pyjoce.os2.make_set_variable ('GOBO', pyjoce.os2.make_os_path ("%ISE_EIFFEL%\\library\\gobo\\svn")))
			out.write ("\n")
			out.write (pyjoce.os2.make_set_variable ('PATH', '%PATH%;%ISE_EIFFEL%\\library\\gobo\\spec\\%ISE_PLATFORM%\\bin'))
		elif os.path.exists(choice):
			out.write (pyjoce.os2.make_set_variable ('GOBO', choice))
			out.write ("\n")
			out.write (pyjoce.os2.make_set_variable ('PATH', '%PATH%;%GOBO%\\bin'))
		else:
			out.write ("@echo Ignore GOBO environment settings\n")
			return;

		out.write ("\n")
		out.write (pyjoce.os2.make_set_variable ('PATH', '%PATH%;%GOBO%\\bin'))
		out.write ("\n")

