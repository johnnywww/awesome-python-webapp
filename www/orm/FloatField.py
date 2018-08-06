#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Field import *

class FloatField(Field):
	def __init__(self, name=None, primary_key=False, default=None, ddl='real'):
		super(FloatField, self).__init__(name, ddl, primary_key, default)
