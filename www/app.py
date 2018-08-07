#!/usr/bin/env python
#-*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web
from orm.Model import Model
from orm.StringField import *
from orm.IntegerField import *

'''
App
'''

__author__ = 'Johnnywww'

__version__ = '1.0'

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



if '__main__' == __name__:
	loop = asyncio.get_event_loop()
	loop.run_until_complete((init(loop), create_db_pool(loop, host='192.168.5.99', user='www-data', password='sysware', db='testblog')))
	loop.run_forever()


