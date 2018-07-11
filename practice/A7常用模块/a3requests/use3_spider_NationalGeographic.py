# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/5 下午3:38
IDE：PyCharm
描述：爬取国家地理
找带有 img_list 的这种 <ul>, 然后在 <ul> 里面找 <img>
"""

from bs4 import BeautifulSoup
import requests

URL = "http://www.nationalgeographic.com.cn/animals/"

headers = {
    'Host': 'www.ngchina.com.cn',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': '__cfduid=d7cf675ba18eb84b022fed33b677650b41530776141; cf_clearance=d42a690cb659ae65f0aaa1263716b4a125c5a650-1530776145-57600; PHPSESSID=sqscqunqamu15kjnfv0jrb4ru4; Hm_lvt_ca8fdc4afd8dbaec0d0f29ebf69ff42a=1530776147; Hm_lpvt_ca8fdc4afd8dbaec0d0f29ebf69ff42a=1530776797',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer':'http://www.ngchina.com.cn/animals/',

}


#  找到带有 img_list 的这种 <ul>
html = requests.get(URL,headers).text
soup = BeautifulSoup(html, 'lxml')
img_ul = soup.find_all('ul', {"class": "img_list"})
print(html)

# 循环下载
for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)
