# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/1 下午9:14
IDE：PyCharm
描述：使用正则表达式抓取
"""

from bs4 import BeautifulSoup
import requests
import re


url = "https://morvanzhou.github.io/static/scraping/table.html"
html = requests.get(url).text
soup = BeautifulSoup(html, features='lxml')

# 抓img里，属性为src的jpg格式的链接
img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg')})
for link in img_links:
    print(link['src'])
