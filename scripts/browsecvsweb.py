#!/usr/local/bin/python

import os;
import sys;
import string;
import re;
cvsroot="/home/cvs"
cvsurl="http://cvs.ise/cgi-bin/viewcvs.cgi"

fn = sys.argv[1]
dn = os.path.dirname(fn)
bn = os.path.basename(fn)
#os.system ("echo " + fn + " >> e:\\toto")
os.chdir (dn)
r = os.popen ('cvs status ' + bn, 'r').read ()

regexp = "\n\s+Repository revision:\s+([a-zA-Z0-9\.]+)\s+%s([^\s|^,]+).*\n" % (cvsroot)
#regexp = "\n\s+Repository revision:.*\n"
p = re.compile (regexp);
result = p.search (r,0)
if result:
	rev = result.group (1)
	path = result.group (2)
	url = "%s%s#rev%s" % (cvsurl, path, rev)
else:
	url = cvsurl

cmd = "start %s" % (url)
os.system (cmd)


