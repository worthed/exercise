# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/13 下午6:02
IDE：PyCharm
描述：
task1执行时，不管结果，开始执行task2
task2执行时，不管结果，开始执行task3
"""
import asyncio
import time
def taskhh(t):
    print('12321312')
    time.sleep(2)


async def task(t):
    print('任务开始', t)
    # await，执行，但不管结果
    await asyncio.coroutine(taskhh(1))
    print('任务耗时1秒钟')

async def main(loop):
    tasks = [loop.create_task(task(t)) for t in range(0, 5)]
    # 执行task，也采用await
    await asyncio.wait(tasks)

t1 = time.time()
loop = asyncio.get_event_loop()  # 把要做得事情用循环写进去
loop.run_until_complete(main(loop))  # 执行 loop,等待所有await内容返回
loop.close()  # 关闭 loop
print("总共耗时: ", time.time() - t1)  # 时间取决于最长的loop所需要的时间


