# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/13 下午6:02
IDE：PyCharm
描述：
"""
import asyncio
import time

async def task(t):
    print('任务开始', t)
    await asyncio.sleep(1)
    print('任务耗时1秒钟')

async def main(loop):
    tasks = [loop.create_task(task(t)) for t in range(0, 5)]
    await asyncio.wait(tasks)

t1 = time.time()
loop = asyncio.get_event_loop()  # 建立 loop
loop.run_until_complete(main(loop))  # 执行 loop
loop.close()  # 关闭 loop
print("总共耗时: ", time.time() - t1)


