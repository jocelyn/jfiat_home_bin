#!/usr/local/bin/python

from _winreg import *
import os, sys

def show_env (root_key, test_key_name, remote_name=None):

	if remote_name is not None:
		print "!"*140
		try:
			remote_key = ConnectRegistry(remote_name, HKEY_CURRENT_USER)
		except EnvironmentError, exc:
			print "Could not connect to the remote machine -", exc.strerror
			remote_key = None
		if remote_key is not None:
			root_key = remote_key

	
	print "#"*72
	print "### %s " % (test_key_name)
	print "#"*72
	print ""
	val = QueryValue (root_key, test_key_name)
	key = OpenKey(root_key, test_key_name)

	index = 0
	while 1:
		try:
			data = EnumValue(key, index)
			(value_name, value_data, value_type) = data
			print "<%s>  %-20s = %s " % (value_type, value_name, value_data)
		except EnvironmentError:
			break
		index = index + 1

	key.Close()

try:
    remote_name = sys.argv[sys.argv.index("--remote")+1]
except (IndexError, ValueError):
    remote_name = None

show_env (HKEY_CURRENT_USER, "Environment", remote_name)
show_env (HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Control\\Session Manager\\Environment", remote_name)

