# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/1 下午9:46
IDE：PyCharm
描述：爬百度百科
"""
from bs4 import BeautifulSoup
import requests
import re
import random
import time


base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(20):
    url = base_url + his[-1]
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    }

    html = requests.get(url,headers=headers)
    html.encoding = 'utf8'

    soup = BeautifulSoup(html.text, features='lxml')
    # 获取h1的内容
    print(soup.find('h1').get_text(), '    url: ', his[-1])

    # 找到所有'网络爬虫'词条中的链接，a里，属性为target = _blank，href中的链接
    sub_urls = soup.find_all("a", {
                                   "target": "_blank",
                                   "href": re.compile("/item/(%.{2})+$")
                                  }
                             )


    if len(sub_urls) != 0:
        # 随机抽取一个链接
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # 如果没有爬取到，则返回上一个链接继续爬
        his.pop()
        print(his)
    time.sleep(1)


