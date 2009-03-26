#!/usr/local/bin/python
#

import sys;
import os;
import re;
import pyjoce.os2;

def clean_env_var(arg):
	new_value = pyjoce.os2.env_var_cleaned (arg)
	os.environ[arg] = new_value

if __name__ == '__main__':
	arg = sys.argv[1]
	if os.environ.has_key (arg):
		clean_env_var(arg)
		sys.stdout.write (pyjoce.os2.make_set_variable (arg, os.environ[arg]))
		sys.stdout.write ("\n")
