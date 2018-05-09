# -*- coding:utf-8 -*-
'''
爬取知乎日报的内容
'''
import requests
proxies = {
  "http": "http://117.95.200.151:40628",
  "https": "http://110.209.250.202:8118",
}

# 知乎禁止爬虫，需要加上headers头伪装
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

url = 'http://daily.zhihu.com/'
res = requests.get(url, headers=headers, proxies=proxies).text
print(len(res))