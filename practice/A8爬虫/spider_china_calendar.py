# -*- coding:utf-8 -*-
'''

'''

import os
import requests
from lxml import etree

inputcalendar = input("{'Please input date(eg:2018-3-21):'}")
calendartype = input("{'Please input calendartype(eg:入宅):'}")
url = 'https://nongli.911cha.com/{}.html'.format(inputcalendar)

suit = []
aviod = []

def get_url_response(url):
    response = requests.get(url)
    return response

def response_parse(url):
    response = get_url_response(url)
    page = response.content
    html = etree.HTML(page)

    days = inputcalendar
    # 宜
    global suit
    suit = html.xpath('//*[@class="green"]/td/a/text()')
    # 忌
    global aviod
    aviod = html.xpath('//*[@class="pink"]/td/a/text()')

    for i in suit:
        if i == '入宅':
            print(days, "is a GooddDay!")
        else:
            continue

response_parse(url)