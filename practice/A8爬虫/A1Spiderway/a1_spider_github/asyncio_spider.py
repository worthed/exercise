# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/5 下午4:36
IDE：PyCharm
描述：异步任务爬虫
"""
import requests
import time

URL = 'https://morvanzhou.github.io/'


def normal():
    for i in range(2):
        r = requests.get(URL)
        url = r.url
        print(url)

t1 = time.time()
normal()
print("Normal total time:", time.time()-t1)


# 网络异步
import aiohttp
import asyncio

async def job(session):
    response = await session.get(URL)       # 等待返回，切换到执行其他程序
    return str(response.url)


async def main(loop):
    async with aiohttp.ClientSession() as session:      # 官网推荐建立 Session 的形式
        tasks = [loop.create_task(job(session)) for _ in range(2)]
        # 等待所有task完成
        finished, unfinished = await asyncio.wait(tasks)
        all_results = [r.result() for r in finished]    # 获取所有结果
        print(all_results)

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
print("Async total time:", time.time() - t1)
