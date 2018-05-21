# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/21 下午3:26
IDE：PyCharm
描述：
"""
from practice.A8爬虫.jianshu.jianshu_get_notes_no import get_notes_no,open_file
import requests

pages = open_file('get_notes_no_pages')
cookie = open_file('get_notes_no_cookie')
ifnonematch = open_file('get_notes_no_ifnonematch')
notes_no = get_notes_no(pages, cookie, ifnonematch)
csrftoken = open_file('post_like_csrftoken')
post_like_cookie = open_file('post_like_cookie')

url = 'https://www.jianshu.com/notes/{param1}/like'.format(param1=notes_no)
headers = {
    'Host': 'www.jianshu.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json',
    'Origin': 'https://www.jianshu.com',
    'X-CSRF-Token': '{param2}'.format(param2=csrftoken),
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Referer': 'https://www.jianshu.com/p/{param3}'.format(param3=pages),
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cookie': '{param4}'.format(param4=post_like_cookie),
    'Content-Length': '0'
}

execute = requests.post(url,headers=headers)


