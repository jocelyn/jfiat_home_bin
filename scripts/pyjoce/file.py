#!/usr/local/bin/python

import re;

def saveFile (filecontent, filename):
	outputfile = open (filename, 'w');
	outputfile.write (filecontent)
	outputfile.close ()

def linesFromFile (filename):
	myfile = open (filename, 'r')
	lines = re.split ("\n", myfile.read ())
	myfile.close ()
	return lines

