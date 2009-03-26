#!/usr/local/bin/python

import sys;
import tracer;
import string;

class Questionner:

	def __init__(self, a_tracer):
		self.tracer = a_tracer

	def trace (self, t):
		self.tracer.put(t)

	def process_question(self, title, values, values_keys):
		self.trace ("\n*** %s ***\n" % (title))

		dft_key = values["_default"];
		dft_answer = "?"
		selection={}
		i = 0
		m = 0
		for e in values_keys:
			if len(e) > m:
				m = len(e)
		for e in values_keys:
			if e[0] != '_':
				i = i + 1
				pref = ' '
				if (e == dft_key):
					dft_answer = "%d" % i
					pref = '.'
				selection["%d" % (i)] = e
				self.trace ("%s%3d:%s - %s\n" % (pref, i, e + " "*(m - len(e)), values[e]))
		for e in values_keys:
			if e[0] == '_' and e != "_default":
				i = i + 1
				if (e == dft_key):
					dft_answer = "%d" % i
				selection["%d" % (i)] = e
				self.trace (" %3d:%s - %s\n" % (i, e + " "*(m - len(e)), values[e]))

		self.trace (" %3s - %s\n" % ("q", "Quit"))

		self.trace ("-> your selection ? [%s] : " % (dft_answer))
		my_selection = ""
		my_input = sys.stdin.readline()
		my_input = string.lower (my_input[:-1])
		if my_input == "":
			my_input = dft_answer
		if my_input == "q":
			self.trace ("Bye bye ...\n")
			sys.exit()
		elif selection.has_key (my_input):
			my_selection = selection[my_input]
			self.trace ("\nYour selection = [%s] -> [%s]\n" % (my_input, values[my_selection]))
		else:
			self.trace ("\n-> Invalid selection [%s] \n\n" % (my_input))
			my_selection = process_question(title, values, values_keys)
		return my_selection
		

