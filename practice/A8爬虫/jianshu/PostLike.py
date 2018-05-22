# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/21 下午4:55
IDE：PyCharm
描述：简书点赞机器人
"""
import requests
import re
import time

class PostLike(object):
    def __init__(self, get_no_page, get_no_cookie, #get_no_ifnonematch,
                 post_like_cookie, post_like_csrftoken):

        self.get_no_page = get_no_page
        self.get_no_cookie = get_no_cookie
        #self.get_no_ifnonematch = get_no_ifnonematch
        self.post_like_cookie = post_like_cookie
        self.post_like_csrftoken = post_like_csrftoken

    # 根据页面，获取notes_no
    def get_notes_no(self):
        url = 'https://www.jianshu.com/p/{param1}'.format(param1=self.get_no_page)
        headers = {
            'Host': 'www.jianshu.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': '{param2}'.format(param2=self.get_no_cookie),
            #'If-None-Match': '{param3}'.format(param3=self.get_no_ifnonematch)
        }

        response = requests.get(url, headers=headers,verify=False).text
        notes_no = (re.findall(r"app-argument=jianshu://notes/(.+?)\">", response))
        return notes_no[0]

    # 发送点赞的请求
    def post_like(self):
        url = 'https://www.jianshu.com/notes/{param1}/like'.format(param1=PostLike.get_notes_no(self))
        headers = {
            'Host': 'www.jianshu.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'Origin': 'https://www.jianshu.com',
            'X-CSRF-Token': '{param2}'.format(param2=self.post_like_csrftoken),
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'Referer': 'https://www.jianshu.com/p/{param3}'.format(param3=self.get_no_page),
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': '{param4}'.format(param4=self.post_like_cookie),
            'Content-Length': '0'
        }

        requests.post(url, headers=headers,verify=False)


if __name__ == '__main__':
    def open_file(filename):
        with open('/Users/wangyuxiang/PycharmProjects/exercise/practice/A8爬虫/jianshu/'
                  'config/{param}.txt'.format(param=filename), 'rb') as open_file:
            return open_file.readlines()
            #.read().decode('utf-8')


    get_no_page = open_file('get_no_page')
    for page in get_no_page:
        for i in range(1, 3):
            time.sleep(i)
        print(str(page)[2:14])


        postlike = PostLike(get_no_page=page,
                            get_no_cookie=open_file('get_no_cookie'),
                            #get_no_ifnonematch=open_file('get_no_ifnonematch'),
                            post_like_cookie=open_file('post_like_cookie'),
                            post_like_csrftoken=open_file('post_like_csrftoken'))
        postlike.post_like()
