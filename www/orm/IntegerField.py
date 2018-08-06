#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Field import *

class IntegerField(Field):
	def __init__(self, name=None, primary_key=False, default=None, ddl='bigint'):
		super(IntegerField, self).__init__(name, ddl, primary_key, default)
