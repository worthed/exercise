# -*- coding:utf-8 -*-
'''
用Task封装两个coroutine
'''

import threading
import asyncio

@asyncio.coroutine
def hello():
    print("Hello World! (%s)" % threading.currentThread())
    r = yield from asyncio.sleep(2)
    print("Hello again! (%s)" % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 两个coroutine是由同一个线程并发执行的
# 如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行