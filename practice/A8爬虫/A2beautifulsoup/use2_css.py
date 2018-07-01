# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/1 下午9:04
IDE：PyCharm
描述：爬取css
"""
from bs4 import BeautifulSoup
import requests


url = "https://morvanzhou.github.io/static/scraping/list.html"
html = requests.get(url).text
soup = BeautifulSoup(html, features='lxml')

# 获取含month的class
month = soup.find_all('li', {"class": "month"})
for m in month:
    # get_text 只显示text，不显示标签信息
    print(m.get_text())

# 选择ul里面class=jan的信息
jan = soup.find('ul', {"class": 'jan'})
d_jan = jan.find_all('li')
for d in d_jan:
    print(d.get_text())
