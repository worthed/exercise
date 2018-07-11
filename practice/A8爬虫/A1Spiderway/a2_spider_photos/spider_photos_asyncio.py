# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/11 下午12:42
IDE：PyCharm
描述：
"""
import uuid
import asyncio
import aiohttp
from practice.common.my_wrapper import out_wrapper
from practice.A8爬虫.A1Spiderway.a2_spider_photos.spider_photos_normal import save_flag,user_conf


async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            save_flag(await response.read(), ''.join([str(uuid.uuid4()),'.jpg']))

@out_wrapper
def download_many():
    urls = user_conf()
    loop = asyncio.get_event_loop()
    to_do = [download_one(url) for url in urls]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)

if __name__ == '__main__':
    download_many()