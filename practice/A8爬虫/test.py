# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/11 下午6:22
IDE：PyCharm
描述：
"""
import requests
from bs4 import BeautifulSoup
import xlwt
import time
import pdb
import re

def write():
    with open('tttt.html','rb') as file_open:
        content = file_open.read().decode('utf-8')
    soup = BeautifulSoup(content,'lxml')
    i = 0
    for item in soup.select('tr')[2:-1]:
        yield  {
            '开奖日期': item.select('td')[i].text,
            '期号': item.select('td')[i + 1].text,
            '中奖号码1': item.select('td em')[0].text,
            '中奖号码2': item.select('td em')[1].text,
            '中奖号码3': item.select('td em')[2].text,
            '中奖注数_单选': item.select('td')[i + 3].text,
            '中奖注数_组选3': item.select('td')[i + 4].text,
            '中奖注数_组选6': item.select('td')[i + 5].text,
            # 销售额，将','去掉
            '销售额(元)': re.sub('[,]','',item.select('td')[i + 6].text.strip('\n')),
            # 去掉%
            '返奖比例': re.sub('[%]','',item.select('td')[i + 7].text),

        }

dict = {'开奖日期': '2018-06-21', '期号': '2018165', '中奖号码1': '9', '中奖号码2': '0', '中奖号码3': '2', '中奖注数_单选': '17513', '中奖注数_组选3': '0', '中奖注数_组选6': '22498', '销售额(元)': '48986916', '返奖比例': ' 45.98'}

def dict_to_mysql(dict,mysql):
    """
    保证dict和mysql表的字段一致
    :param dict: 字典
    :param mysql: mysql表名
    :return:
    """
    dict

items = write()
for item in items:
    print(item)
    lottery_date = item['开奖日期']
    lottery_issue = item['期号']
    lottery_onenum = item['中奖号码1']
    lottery_twonum = item['中奖号码2']
    lottery_threenum = item['中奖号码3']
    lottery_single = item['中奖注数_单选']
    lottery_group_three = item['中奖注数_组选3']
    lottery_group_six = item['中奖注数_组选6']
    lottery_sales = item['销售额(元)']
    lottery_return_rates = item['返奖比例']
