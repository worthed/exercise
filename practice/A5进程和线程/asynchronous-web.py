# -*- coding:utf-8 -*-
import asyncio
from aiohttp import web

async def index(request):
    await asyncio.sleep(1)
    return web.Response(body='<h1>index</h1>'.encode('utf-8'), content_type='text/html')

async def hello(request):
    await asyncio.sleep(1)
    text = '<h1>hello, %s!</h1>' % request.match_info['wangyuxiang']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{wangyuxiang}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9001)
    print('Server started at http://127.0.0.1:9001...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

@asyncio.coroutine
def create_pool(loop, **kw):
