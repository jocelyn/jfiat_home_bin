#!/usr/local/bin/python

import sys;
import pyjoce;
import os;
from pyjoce.conf import config;

def id():
	return "eweasel"

def title():
	return "eWeasel"

def arg():
	return "--eweasel"

def choices():
	arr = []
	arr.append (["on", "Enabled"])
	arr.append (["off", "Disabled"])
	arr.append (["_default", "off"])
	return arr;

def datas():
	return [id(), title(), arg(), choices(), True]

def output_init(home_bin,choice,out=sys.stdout):
	out.write ("Rem ## Init:%s ##\n" % (title()))

def output(home_bin,choice,out=sys.stdout):
	if choice == '_skip':
		out.write ("@echo Skipping: %s settings\n" % (title()))
	else:
		ch = choice
		if choice == "on":
			out.write (pyjoce.os2.make_set_variable ('EWEASEL', '%EIFFEL_SRC%\\..\\eweasel'))
			out.write ("\n")
			out.write (pyjoce.os2.make_set_variable ('EWEASEL_OUTPUT', '%EWEASEL%\\test_output'))
			out.write ("\n")

			out.write (pyjoce.os2.make_set_variable ('ISE_LIBRARY', '%ISE_EIFFEL%'))
			out.write ("\n")

				# Add eweasel to PATH
			out.write (pyjoce.os2.make_set_variable ('PATH', '%PATH%;%EWEASEL%\\spec\\%ISE_PLATFORM%\\bin'))
			out.write ("\n")

		else:
			out.write (pyjoce.os2.make_set_variable ('EWEASEL', ''))
			out.write ("\n")
			out.write (pyjoce.os2.make_set_variable ('EWEASEL_OUTPUT', ''))
			out.write ("\n")
		out.write ("@echo off\n")

