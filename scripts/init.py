#!/usr/local/bin/python

import os;
import sys;
import string;


def process_question(title, values):
	sys.stderr.write ("\n*** %s ***\n" % (title))
	values_keys = values.keys ()
	selection={}
	i = 0
	for e in values_keys:
		i = i + 1
		selection["%d" % (i)] = e
		sys.stderr.write (" %3d - %s\n" % (i, values[e]))

	sys.stderr.write (" %3s - %s\n" % ("q", "Quit"))

	sys.stderr.write ("-> your selection ? : ")
	my_input = sys.stdin.readline()
	my_input = string.lower (my_input[:-1])
	if my_input == "q":
		sys.stderr.write ("Bye bye ...\n")
		sys.exit()
	elif selection.has_key (my_input):
		my_selection = selection[my_input]
		sys.stderr.write ("\nYour selection = [%s] -> [%s]\n" % (my_input, values[my_selection]))
	else:
		sys.stderr.write ("\n-> Invalid selection [%s] \n\n" % (my_input))
		process_question()
	return my_selection

#h = os.environ['HOME']
#u = os.environ['USERNAME']
d = os.path.expanduser ("~/bin")
list_files = os.listdir (d)
choices={}
n = 0
for f in list_files:
	if len(f) > 4 and (string.lower (f[:5]) == 'init_'):
		n = n + 1
		choices[n] = f

answer = process_question("Script to launch", choices)
answer = choices[answer]

sys.stdout.write (answer + "\n")
