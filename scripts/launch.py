#!/usr/local/bin/python

import os;
import sys;
import string;

cmd = sys.argv [1];
if len (sys.argv) > 1:
	nb = string.atoi (sys.argv [2]);
else :
	nb = 0;

i = 1;
print "Launch %i times : %s" %(nb, cmd)
while (i < nb) or (nb == 0) :
	print "\n--------------------------------------------------------------"
	print "\nExecute [%i] : %s" %(i, cmd)
	print "\n--------------------------------------------------------------"
	os.system (cmd)
	i =  i + 1

