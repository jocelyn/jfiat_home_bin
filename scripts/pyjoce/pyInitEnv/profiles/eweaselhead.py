#!/usr/local/bin/python

import sys;
import pyjoce;

def title():
	return "eweasel (head)";

def parent():
	return "eweasel63d";

def params():
	val = {}
	val['ise_eiffel'] = 'D:\\Eiffel\\delivhead\\EiffelXX_eweasel'
	val['eiffel_src'] = 'trunk_head'
	val['colors'] = '70'
	return val

def post_actions():
	val = []
	val.append ("cd /d %EWEASEL%")
	val.append ("cd bin")
	return val;

