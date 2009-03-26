#!/usr/local/bin/python

import sys;
import pyjoce;

def title():
	return "dev on trunk 63"

def params():
	val = {}
	val['eiffel_src'] = 'trunk'
	val['ise_eiffel'] = 'es63'
	val['eweasel'] = 'off'
	val['ms_env'] = '20'
	val['gobo'] = 'ise'
	val['colors'] = '1f'
	return val

