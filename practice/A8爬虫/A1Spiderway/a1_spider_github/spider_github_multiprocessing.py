# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/5 下午4:28
IDE：PyCharm
描述：分布式爬虫（基于多进程）
"""
import multiprocessing as mp
import time
from urllib.request import urljoin
from bs4 import BeautifulSoup
import requests
import re

base_url = 'https://morvanzhou.github.io/'

# 爬取网页
def crawl(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    # time.sleep(0.1)
    return response.text

# 解析网页
def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find_all('a', {"href": re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    page_urls = set([urljoin(base_url, url['href']) for url in urls])   # 去重
    url = soup.find('meta', {'property': "og:url"})['content']
    return title, page_urls, url

# 没爬过的网页
unseen = set([base_url,])
# 爬取过的网页
seen = set()

# 判断是否为内外网
if base_url != "http://127.0.0.1:4000/":
    restricted_crawl = True
else:
    restricted_crawl = False


pool = mp.Pool(4)
count, t1 = 1, time.time()


while len(unseen) != 0:
    if restricted_crawl and len(seen) > 20:
            break
    print('\nDistributed Crawling...')
    crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
    htmls = [j.get() for j in crawl_jobs]

    print('\nDistributed Parsing...')
    parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
    results = [j.get() for j in parse_jobs]

    print('\nAnalysing...')
    seen.update(unseen)         # seen the crawled
    unseen.clear()              # nothing unseen

    for title, page_urls, url in results:
        print(count, title, url)
        count += 1
        unseen.update(page_urls - seen)     # get new url to crawl

print('Total time: %.1f s' % (time.time()-t1, ))


