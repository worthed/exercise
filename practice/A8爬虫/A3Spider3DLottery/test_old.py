# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/11 下午6:22
IDE：PyCharm
描述：
"""
from bs4 import BeautifulSoup
import re
from practice.common.MysqlDataToJson import MysqlDataToJSON
from support.common.connect_mysql.connect_mysql_and_query import localhost_query,localhost_insert_or_update
from support.common.others.dict_to_mysql import dict_to_mysql,replace_dict_none

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

sql = 'select COLUMN_NAME from information_schema.columns where table_name=\'lottery\' ' \
      'and COLUMN_NAME not in (\'lottery_id\',\'lottery_return_update_at\');'
query_column_name = localhost_query(sql)
sqldata_to_dict = MysqlDataToJSON(query_result=query_column_name)
sqldata_to_dict.get_json()
items = write()



for item in items:
    new_item = replace_dict_none(item)
    dict_to_mysql(table_name='lottery', column_name_dict=sqldata_to_dict.get_json(), insert_data_dict=new_item)