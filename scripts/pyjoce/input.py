#!/usr/local/python

import sys;
import re;
import string;

def do_pause ():
	sys.stderr.write ("Press Enter to continue ...")
	input = sys.stdin.readline ()

def answer_is_yes (msg):
	sys.stderr.write ("[?] %s ? [Y/N] " % (msg))
	input = sys.stdin.readline ()
	input = input[0]
	return ((input == 'Y') or (input == 'y'))

def read_string ():
	input = sys.stdin.readline ()
	#input = input[0]
	return input[:]

def read_integer (default=0):
	reg_integer = "^\s*([0-9][0-9]*)\s*"
	p_integer = re.compile (reg_integer)
	input = sys.stdin.readline ()
	#sys.stderr.write ( "[%s]\n\n" % (input))
	result = p_integer.search (input)
	if result:
		return string.atoi (result.group (1))
	return default

