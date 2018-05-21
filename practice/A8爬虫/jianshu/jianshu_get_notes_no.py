# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/21 下午2:44
IDE：PyCharm
描述：
"""
import requests
import re

def open_file(filename):
    with open('/Users/wangyuxiang/PycharmProjects/exercise/practice/A8爬虫/jianshu/'
              'config/{param}.txt'.format(param=filename), 'rb') as open_file:
        return open_file.read().decode('utf-8')


def get_notes_no(pages, cookie, ifnonematch):
    url = 'https://www.jianshu.com/p/{param1}'.format(param1=pages)
    headers = {
        'Host': 'www.jianshu.com',
        'Connection': 'keep-alive',
        'Cache-Control':'max-age=0',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie':'{param2}'.format(param2=cookie),
        'If-None-Match':'{param3}'.format(param3=ifnonematch)
    }

    response = requests.get(url, headers=headers).text
    notes_no = (re.findall(r"app-argument=jianshu://notes/(.+?)\">", response))
    return notes_no[0]



