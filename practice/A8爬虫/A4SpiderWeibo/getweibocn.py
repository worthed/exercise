# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/8/1 下午12:54
IDE：PyCharm
描述：
"""
import requests

user_id = '1606962013'
url = f'https://weibo.cn/{user_id}/info'
headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Host': 'weibo.cn',
'Upgrade-Insecure-Requests': '1',
'Referer':'https://m.weibo.cn/p/index?containerid=2302835650995316_-_INFO&title=%25E5%259F%25BA%25E6%259C%25AC%25E8%25B5%2584%25E6%2596%2599&luicode=10000011&lfid=2302835650995316&featurecode=20000320',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

res = requests.get(url=url,headers=headers)
print(res)
r = res.text

print(r)