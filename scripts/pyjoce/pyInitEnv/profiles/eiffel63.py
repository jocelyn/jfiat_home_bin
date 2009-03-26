#!/usr/local/bin/python

import sys;
import pyjoce;

def title():
	return "Standard Eiffel63"

def params():
	val = {}
	val['eiffel_src'] = '_none'
	val['ise_eiffel'] = 'es63r'
	val['eweasel'] = 'off'
	val['ms_env'] = '20'
	val['gobo'] = 'ise'
	val['colors'] = '2f'
	return val

