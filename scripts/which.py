"""
which.py is the Win32 equivalent of the which command of the Unix platform.
It understands the PATH and PATHEXT environment variables.

It's an imporved version of the Ned Batchelder (http://www.nedbatchelder.com) script.
Vivian De Smedt (http://www.vdesmedt.com/~vds2212).
"""

import os, os.path, sys, getopt, string, re


def which(args, options):
	path = ["."]  + filter(None, os.environ["PATH"].split(";"))
	pathext = map(string.lower, filter(None, os.environ["PATHEXT"].split(";")))

	# The command name we are looking for
	prog_name = args[0]

	# Is the command name really a file name?
	if prog_name.find('.') >= 0:
		# Fake it by making pathext a list of one empty string.
		pathext = ['']

	# Loop over the directories on the path, looking for the file.
	if options.regexp:
		prog_pattern = prog_name
		prog_pattern = re.sub("\\\\", "\\\\", prog_pattern)
		prog_pattern = re.sub("\\.", "\\.", prog_pattern)
		prog_pattern = re.sub("\\*", ".*", prog_pattern)
		prog_pattern = re.sub("\\?", ".", prog_pattern)

	for d in path:
		if options.skip_dot and d and d[0] == ".":
			continue

		if options.regexp:
			if not os.path.isdir(d):
				continue
			files = os.listdir(d)
			for file in files:
				if re.match(prog_pattern, file, re.I):
					file_path = os.path.join(d, file)
					print file_path
					if not options.all:
						return 0
			continue

		for e in pathext:
			file_path = os.path.join(d, prog_name + e)
			if os.path.exists(file_path):
				if not options.show_dot and d and d[0] == ".":
					file_path = os.path.abspath(file_path)
				print file_path
				if not options.all:
					return 0


def printUsage():
	"""Print the help string that should printed by which.py -h"""
	print "usage: which.py [options] programname"
	print """
 -a,   --all         Print all matching executables in PATH, not just the first.
       --skip-dot    Skip directories in PATH that start with a dot.
       --show-dot    Don't expand a dot to current directory in output.
       --regexp      Consider the programname as a regular expression.
 -v -V --version     Print version and exit successfully.
 -h,   --help        Print this help and exit successfully.

See http://www.vdesmedt.com/~vds2212/which.html for informations and updates.
Send an email to vivian@vdesmedt.com for comments and bug reports."""


def printVersion():
	print "which.py version 0.5.0"


class Options:
	def __init__(self):
		self.all = 0
		self.skip_dot = 0
		self.show_dot = 0
		self.regexp = 0


def main(argv):
	options = Options()

	opts, args = getopt.getopt(argv, "havV", ["help", "all", "version", "skip-dot", "show-dot", "regexp"])
	for o, v in opts:
		if o in ["-a", "--all"]:
			options.all = 1
		elif o == "--skip-dot":
			options.show_dot = 1
		elif o == "--show-dot":
			options.show_dot = 1
		elif o == "--regexp":
			options.regexp = 1
		elif o in ["-v", "--version"]:
			printVersion()
			return 0
		elif o in ["-h", "--help"]:
			printUsage()
			return 0

	if len(args) <= 0:
		printUsage()
		return 1

	return which(args, options)


if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
	