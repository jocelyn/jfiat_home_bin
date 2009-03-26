#!/usr/local/bin/python

import sys;
import pyjoce;

def title():
	return "eweasel";

def parent():
	return "trunk63d";

def params():
	val = {}
	val['ise_eiffel'] = 'es_weasel'
	val['eweasel'] = 'on'
	val['colors'] = '2f'
	return val

def post_actions():
	val = []
	val.append ("cd /d %EWEASEL%")
	val.append ("cd bin")
	return val;

