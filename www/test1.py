#!/usr/bin/env python
#-*- coding: utf-8 -*-

import asyncio
from orm.AppModel import User

from orm.Model import create_db_pool

def test(loop):
    yield from create_db_pool(loop, host='192.168.5.99', user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    yield from u.save()

if '__main__' == __name__:
	loop = asyncio.get_event_loop()
	for x in test(loop):
		pass
	loop.close()
