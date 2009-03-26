#!/usr/local/bin/python

import sys;
import pyjoce.os2;

def id():
	return "ms_env";

def title():
	return "MS Env"

def arg():
	return "--msenv"

def choices():
	arr = []
	arr.append (["10",			".NET 1.0"])
	arr.append (["1x",			".NET 1.x"])
	arr.append (["20",			".NET 2.0"])
	arr.append (["0", 			"Without .NET"])
	arr.append (["_none",		"none"])
	arr.append (["_skip", 		"skip"])
	arr.append (["_default",	"1x"])
	return arr;

def datas():
	return [id(), title(), arg(), choices(), False]

def output_init(home_bin,choice,out=sys.stdout):
	#out.write ("@echo ## Init:%s ##\n" % (title()))
	out.write ("@echo off\n")
	if choice == '_skip':
		out.write ("@echo Skipping: %s settings\n" % (title()))
	elif choice == '10':
		out.write ("@call %s\\init_dotnet10.bat\n" % (home_bin))
	elif choice == '20':
		out.write ("@call %s\\init_dotnet20.bat\n" % (home_bin))
	elif choice == '1x':
		out.write ("@call %s\\init_dotnet1x.bat\n"  % (home_bin))
	elif choice == '_':
		out.write ("@call %s\\init_ms.bat\n"  % (home_bin))
	else:
		out.write ("@echo Ignore MS environment settings\n")

def output(home_bin,choice,out=sys.stdout):
#	out.write ("@echo ## %s ##\n" % (title()))
	out.write ("rem %s setting completed\n" % (title()))
		
