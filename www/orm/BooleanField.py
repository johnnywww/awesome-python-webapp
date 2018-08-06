#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Field import Field

class BooleanField(Field):
	def __init__(self, name=None, primary_key=False, default=None, ddl='bool'):
		super(BooleanField, self).__init__(name, ddl, primary_key, default)
