#!/usr/local/bin/python
#

import sys;
import os;
import re;
import pyjoce.os2;

if __name__ == '__main__':
	delpath = ""
	if len(sys.argv) > 1 :
		delpath = sys.argv[1]

	new_path = pyjoce.os2.path_cleaned (delpath)
	os.environ['PATH'] = new_path

	sys.stdout.write (pyjoce.os2.make_set_variable ('PATH', new_path))
	sys.stdout.write ("\n")

