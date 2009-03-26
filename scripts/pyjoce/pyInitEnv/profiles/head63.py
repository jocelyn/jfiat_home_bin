#!/usr/local/bin/python

import sys;
import pyjoce;

def title():
	return "dev on unmodified trunk@HEAD"

def parent():
	return "default";

def params():
	val = {}
	val['eiffel_src'] = 'trunk_head'
	val['colors'] = '70'
	return val

