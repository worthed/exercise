# -*- coding:utf-8 -*-
'''
协程相比于多进程和多线程的优点
（多进程和多线程除了创建的开销大之外还有一个难以根治的缺陷，就是处理进程之间或线程之间的协作问题，
因为是依赖多进程和多线程的程序在不加锁的情况下通常是不可控的，而协程则可以完美地解决协作问题，由用户来决定协程之间的调度。）

特点是允许用户的主动调用和主动退出，挂起当前的例程然后返回值或去执行其他任务，接着返回原来停下的点继续执行。
'''
from lxml import etree
from time import time
import asyncio
import aiohttp

url = 'https://movie.douban.com/top250'

async def fetch_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def parse(url):
    page = await fetch_content(url)
    html = etree.HTML(page)

    xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
    xpath_title = './/span[@class="title"]'
    xpath_pages = '//*[@id="content"]/div/div[1]/div[2]/a'

    pages = html.xpath(xpath_pages)
    fetch_list = []
    result = []

    for element_movie in html.xpath(xpath_movie):
        result.append(element_movie)

    for p in pages:
        fetch_list.append(url + p.get('href'))

    tasks = [fetch_content(url) for url in fetch_list]
    pages = await asyncio.gather(*tasks)

    for page in pages:
        html = etree.HTML(page)
        for element_movie in html.xpath(xpath_movie):
            result.append(element_movie)

    for i, movie in enumerate(result, 1):
        title = movie.find(xpath_title).text
        print(i, title)


def main():
    loop = asyncio.get_event_loop()
    start = time()
    for i in range(5):
        loop.run_until_complete(parse(url))
    end = time()
    print ('Cost {} seconds'.format((end - start) / 5))
    loop.close()

