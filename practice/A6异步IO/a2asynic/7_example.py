# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/11/20 下午4:54
IDE：PyCharm
描述：
"""
import asyncio
import functools


def callback(arg, *, kwarg='default'):
    print('callback invoked with {} and {}'.format(arg, kwarg))


async def main(loop):
    wrapped = functools.partial(callback, kwarg='not default')
    loop.call_soon(wrapped, 2)
    await asyncio.sleep(2)

    tasks = [loop.create_task(callback(t, kwarg='not default')) for t in range(0, 5)]
    # 执行task，也采用await
    await asyncio.wait(tasks)

event_loop = asyncio.get_event_loop()
try:
    print('进入事物循环')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('关闭事物循环')
    event_loop.close()

