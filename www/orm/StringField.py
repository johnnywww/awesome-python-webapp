#!/usr/bin/env python
#-*- coding: utf-8 -*-

from orm.Field import *

class StringField(Field):
	def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
		super(StringField, self).__init__(name, ddl, primary_key, default)
