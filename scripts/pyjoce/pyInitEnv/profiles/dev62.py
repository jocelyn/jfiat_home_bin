#!/usr/local/bin/python

import sys;
import pyjoce;

def title():
	return "es62 on trunk"

def params():
	val = {}
	val['eiffel_src'] = 'trunk'
	val['ise_eiffel'] = 'es62'
	val['eweasel'] = 'off'
	val['ms_env'] = '20'
	val['gobo'] = 'ise'
	val['colors'] = '3f'
	return val

