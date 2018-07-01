# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/1 下午8:44
IDE：PyCharm
描述：
"""
from bs4 import BeautifulSoup
import requests


url = "https://morvanzhou.github.io/static/scraping/basic-structure.html"
html = requests.get(url).text
soup = BeautifulSoup(html, features='lxml')
print(soup.h1)  # h1里面的内容
print('\n', soup.p)  # p里面的内容

# 获取链接
all_href = soup.find_all('a')
# 真正的 link 不是在 <a> 中间 </a>, 而是在 <a href="link"> 里面
# 可用像 Python 字典的形式, 用 key 来读取 l["href"].
all_href = [l['href'] for l in all_href]
print('\n', all_href)
