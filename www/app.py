#!/usr/bin/env python
#-*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web
from orm import Model, IntegerField, StringField

class DeviceType(Model):
	__table__ = 'devicetype'
	devicetype_id = IntegerField(primary_key = True)
	parent_devicetype_id = IntegerField()
	name = StringField()
	remark = StringField

def index(request):
	return web.Response(body=b'<h1>Aswesome</h1>', content_type='text/html')

@asyncio.coroutine
def init(loop):
	app = web.Application(loop = loop)
	app.router.add_route('GET', '/', index)
	port = 9100
	srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', port)
	logging.info('server started at http://127.0.0.1:%s...' % (port, ))
	return srv

@asyncio.coroutine
def create_db_pool(loop, **kw):
	logging.info("create database connection pool...")
	global __dbpool
	__dbpool = yield from aiomysql.create_pool(
		host = kw.get('host', 'localhost'),
		port = kw.get('port', 3306),
		user=kw['user'],
		password=kw['password'],
		db=kw['db'],
		charset=kw.get('charset', 'utf8'),
		autocommit=kw.get('autocommit', True),
		maxsize=kw.get('maxsize', 10),
		minsize=kw.get('minsize', 1),
		loop=loop
	)

@asyncio.coroutine
def select(sql, *args, size=None):
	logging.info(sql, args)
	global __dbpool
	with (yield from __dbpool) as conn:
		cur = yield from conn.cursor(aiomysql.DictCursor)
		yield from cur.execute(.replace('?', '%s'), args or () )
		if size:
			rs = yield.from cur.fetchmany(size)
		else:
			rs = yield.from cur.fetchall()
		yield from cur.close()
		logging.info('rows returned: %s' % len(rs))
		return rs

@aysncio.coroutine
def execute_ddl(loop, *args):
	global __dbpool
	with (yield from __dbpool) as conn:
		try:
			cur = yield.from conn.cursor()
			yield from cur.execute(sql.replace('?', '%s'), args or ())
			affected = cur.rowcount
			yield from cur.close()
		except BaseException as e:
			raise
		return affected	

if '__main__' == __name__:
	loop = asyncio.get_event_loop()
	loop.run_until_complete((init(loop), create_db_pool(loop, host='192.168.5.99', user='www-data', password='sysware', db='testblog')))
	loop.run_forever()


