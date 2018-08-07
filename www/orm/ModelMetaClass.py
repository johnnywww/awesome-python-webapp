#!/usr/bin/env python
#-*- coding: utf-8 -*-
import logging; logging.basicConfig(level=logging.INFO)
from orm.Field import *

def create_args_string(num):
	L = []
	for n in range(num):
		L.append('?')
	return ', '.join(L)

class ModelMetaClass(type):
	def __new__(cls, name, bases, attrs):
		if 'Model' == name:
			return super(ModelMetaClass, cls).__new__(cls, name, bases, attrs)
		tablename = attrs.get('__table__', None) or name
		logging.info('found model: %s (table: %s)' % (name, tablename))
		mappings = dict()
		fields = []
		primaryKey = None
		for k, v in attrs.items():
			if isinstance(v, Field):
				logging.info('  found mapping: %s ==> %s' % (k, v))
				mappings[k] = v
				if v.get_primary_key():
					if primaryKey:
						raise RuntimeError('Duplicate primary key for field: %s' % k)
					primaryKey = k
				else:
					fields.append(k)
		if not primaryKey:
			raise RuntimeError('Primary key not exist')
		for k in mappings.keys():
			attrs.pop(k)
		escaped_fields = list(map(lambda f: '`%s`' % f, fields))
		attrs['__mappings__'] = mappings # 保存属性和列的映射关系
		attrs['__table__'] = tablename
		attrs['__primary_key__'] = primaryKey
		attrs['__fields__'] = fields
		attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tablename)
		attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values(%s)' % (tablename, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
		attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tablename, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).get_name() or f), fields)), primaryKey)
		attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tablename, primaryKey)
		return super(ModelMetaClass, cls).__new__(cls, name, bases, attrs)

			
