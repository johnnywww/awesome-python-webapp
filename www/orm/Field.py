#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Field(object):
	def __init__(self, name, column_type, primary_key, default):
		self._name = name
		self._column_type = column_type
		self._primary_key = primary_key
		self._default = default

	def get_primary_key(self):
		return self._primary_key

	def get_name(self):
		return self._name
		
	def __str__(self):
		return '<%s, %s:%s>' %(self.__class__.__name__, self._column_type, self._name)
