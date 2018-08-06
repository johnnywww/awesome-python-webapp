#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Field import Field

class TextField(Field):
	def __init__(self, name=None, primary_key=False, default=None, ddl='mediumtext'):
		super(TextField, self).__init__(name, ddl, primary_key, default)
