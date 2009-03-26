#!/usr/local/bin/python

########################################
str_from = "";
str_to = "";

########################################




import sys;
import re;
import os;
from string import split;


if (len (str_from) == 0) or (len (str_to) == 0):
	sys.exit ()

substitutions = []
substitutions.append (Replacor ("cvs", str_from, str_to))

class Replacor:
	def __init__ (self, name, str_from, str_to):
		self.name = name
		self.str_from = str_from
		self.str_to = str_to
		self.p_from = re.compile (str_from);
		self.count = 0

def process (z_src, subs):
	total_subs = 0
	keep_processing = 1;
	try:
		myfile = open (src, 'r');
		mystring = myfile.read ();
		myfile.close ();
	except:
		print ("ERROR: unable to read %s" %(src))
		keep_processing = 0

	if keep_processing > 0:
		counts = {}
		for s_replicator in subs:
			counts[s_replicator.str_from] = 0

		total_subs = 0
		for s_replicator in subs:
			str_from = s_replicator.str_from
			str_to = s_replicator.str_to
			p_from = s_replicator.p_from
			(mystring, counts[str_from]) = p_from.subn (str_to, mystring)
			s_replicator.count = s_replicator.count + counts[str_from]
			total_subs = total_subs + counts[str_from]

		if total_subs > 0:
			for s_replicator in subs:
				sys.stdout.write (" %s:%-3d " % (s_replicator.name, counts[s_replicator.str_from])) #, s_replicator.count))
			try:
				if simulating != 1 :
					### Backup
					if do_backup == 1:
						myfile = open (src, 'r');
						myoldstring = myfile.read ();
						myfile.close ();

						myfile = open (src + ".bak", 'w');
						myfile.write (myoldstring);
						myfile.close ();

					### Save New
					myfile = open (src, 'w');
					myfile.write (mystring);
					myfile.close ();
					sys.stdout.write (" [Saved] ")

			except:
				print ("ERROR: unable to write %s" %(src))
		#else:
			#sys.stdout.write (" \t\t no substitution")
	return total_subs


def entries_from (fn):
	myfile = open (fn, 'r');
	lines = re.split ("\n", myfile.read())
	myfile.close ();
	return lines

#################################################################
###                                                           ###
#################################################################


simulating = 1
verbose = 0
do_backup = 1
args = sys.argv[1:]
argc = len (sys.argv) ;
files = []
list_filename = ""
i = 1;
while i < argc and not files:
	arg = sys.argv[i];
	i = i + 1;
	if arg[0] == '-' :
		if arg == '-s': # Simulation
			simulating = 1
		if arg == '-x': # No Simulation
			simulating = 0
		if arg == '-v':
			verbose = 1
		if arg == '-l':
			list_filename = sys.argv[i]
			i = i + 1
		if arg == '-backup':
			do_backup = 1
		if arg == '-nobackup':
			do_backup = 0
	else:
		files = sys.argv[i-1:]

if len (list_filename) > 0:
	files = entries_from (list_filename)

if simulating == 1:
	print "### Simulation : ON  (default) ###"
else :
	print "### Simulation : OFF           ###"
if verbose:
	print "### Verbose    : ON            ###"
else: 
	print "### Verbose    : OFF (default) ###"
if do_backup:
	print "### Backup     : ON  (default) ###"
else: 
	print "### Backup     : OFF           ###"


#keep_going = sys.stdin.read ("Continue (y/n) ?")
#print keep_going

index = 0;
if not files:
	print "No argument !!!"
	print "Usage: script {-s} {-x} {-v} files ..."
	print "       -s: simulation"
	print "       -x: no simulation "
	print "       -v: verbose"
	print "       -backup: create *.bak file"
	print "       -nobackup: do not backup as *.bak file"
	print "       -l: file containing list of files to process"
	print ""
	print "       Default: simulation on"
	print "                verbose    off"
	
	sys.exit ()
	files = os.popen ('find . -name "*.htm*" -print').readlines ()


for src in files:
	index = index + 1;
	src = split (src , '\n')[0];
	if len (src) > 0: # not empty
		total_substitutions = process (src, substitutions);
		if total_substitutions > 0 :
			sys.stdout.write ("> %-3i %s" % (index, src))
			sys.stdout.write ("\n")
		else:
			if verbose:
				print " no change                                  >     %s" % (src)

print "Finished..."
	
