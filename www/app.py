#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
@author:MrSprint
@file:app.py
@time:2016 16-12-6 下午3:29
'''

import logging;logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time,uuid
from datetime import datetime
from aiohttp import web
from orm import Model, StringField, BooleanField, FloatField, TextField
def index(request):
    return web.Response(body=b'<h1>Sprint</h1>',content_type='text/html',charset='UTF-8')
#如果不加后面的content_type='text/html',charset='UTF-8'会因编码问题导致显示的为下载文件

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('sever started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

