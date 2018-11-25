# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/11/24 下午8:10
IDE：PyCharm
描述：
"""
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.urllib3.disable_warnings(InsecureRequestWarning)
# 使用requests库请求HTTPS时,因为忽略证书验证,导致每次运行时都会报错
import json
from urllib.request import quote
from support.common.connect.connect_db.ConnectDB import localhost_insert_or_update
from fake_useragent import UserAgent
import re
from lxml import etree
from bs4 import BeautifulSoup
from practice.A8爬虫.lagou.get_lagou_positions_to_mysql import get_lagou_headers,lagou_cookies

city = '成都'
position = '测试'
headers = get_lagou_headers(city,position)

position_url = "https://www.lagou.com/jobs/2891727.html"
work_duty = ''
work_requirement = ''
response00 = requests.post(position_url,headers=headers).text
html = etree.HTML(response00)
content = html.xpath('//*[@id="job_detail"]/dd[2]/div/p/text()')
# 数据清理
j = 0
for i in range(len(content)):
    content[i] = content[i].replace('\xa0',' ')
    if content[i][0].isdigit():
        if j == 0:
            content[i] = content[i][2:].replace('、',' ')
            content[i] = re.sub('[；;.0-9。]','', content[i])
            work_duty = work_duty+content[i]+ '/'
            j = j + 1
        elif content[i][0] == '1' and not content[i][1].isdigit():
            break
        else:
            content[i] = content[i][2:].replace('、', ' ')
            content[i] = re.sub('[、；;.0-9。]','',content[i])
            work_duty = work_duty + content[i]+ '/'
    m = i
# 岗位职责
print(work_duty)
# 数据清理
j = 0
for i in range(len(content)):
    content[i] = content[i].replace('\xa0',' ')
    if content[i][0].isdigit():
        if j == 0:
            content[i] = content[i][2:].replace('、', ' ')
            content[i] = re.sub('[、；;.0-9。]', '', content[i])
            work_requirement = work_requirement + content[i] + '/'
            j = j + 1
        elif content[i][0] == '1' and not content[i][1].isdigit():
            # 控制范围
            break
        else:
            content[i] = content[i][2:].replace('、', ' ')
            content[i] = re.sub('[、；;.0-9。]', '', content[i])
            work_requirement = work_requirement + content[i] + '/'
# 岗位要求
print(work_requirement)
print("-----------------------------")
