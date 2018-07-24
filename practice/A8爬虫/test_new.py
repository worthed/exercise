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
from support.common.others.MysqlDataToDict import MysqlDataToDict
from support.common.connect_mysql.connect_mysql_and_query import localhost_query,localhost_insert_or_update
from practice.A8爬虫.Spider3DLottery import SpiderLottery
from support.common.others.my_wrapper import retry_if_type_error
from retrying import retry
from support.common.others.dict_to_mysql import dict_to_mysql


class SpiderLotteryToMysql(SpiderLottery):

    def __init__(self, column_name_dict, page, per_page_count, sheet):
        """
        :param insert_data_dict: 待插入的数据的dict
        :param column_name_dict: 插入的表的字段名dict
        :param page: 继承父类
        :param per_page_count: 继承父类
        :param sheet: 继承父类
        """
        super(SpiderLotteryToMysql,self).__init__(page, per_page_count, sheet)
        #self.insert_data_dict = insert_data_dict
        self.column_name_dict = column_name_dict


    def dict_to_mysql(self,insert_data_dict):
        """
        字典，json插入mysql
        :return:
        """
        column_name = ''
        for i in self.column_name_dict:
            if column_name != '':
                column_name = column_name + ',' + column_name.join(i.values())
            else:
                column_name = column_name + column_name.join(i.values())

        cols = ', '.join(insert_data_dict.values())
        sql = "INSERT INTO %s (%s) VALUES (%s)" % ('lottery', column_name, cols)
        localhost_insert_or_update(sql)

    @retry(retry_on_exception=retry_if_type_error)
    def get_page_res(self):
        """
        写入到mysql
        :return:
        """
        # 依次爬取每一页内容的每一期信息，并将其依次写入excel
        url = 'http://kaijiang.zhcw.com/zhcw/html/3d/list_{}.html'.format(str(self.page))
        html = SpiderLotteryToMysql.get_one_page(self, url)
        print('正在保存第%d页……' % self.page)
        # 写入每一期的信息
        return SpiderLotteryToMysql.parse_one_page(html)

    def write_to_mysql(self):
        items = SpiderLotteryToMysql.get_page_res(self)
        for item in items:
            SpiderLotteryToMysql.dict_to_mysql(self,insert_data_dict=item)

'''
sql = 'select COLUMN_NAME from information_schema.columns where table_name=\'lottery\' ' \
      'and COLUMN_NAME not in (\'lottery_id\',\'lottery_return_update_at\');'
query_result = localhost_query(sql)
sqldata_to_dict = MysqlDataToJSON(query_result=query_result)
column_name_dict = sqldata_to_dict.get_json()

for k in range(1, 247):
    sp = SpiderLotteryToMysql(column_name_dict=sqldata_to_dict.get_json(),
                          page=k,
                          per_page_count='',
                          sheet=''
                          )
    sp.write_to_mysql()
'''

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
query_result = localhost_query(sql)
sqldata_to_dict = MysqlDataToDict(query_result=query_result)
column_name_dict = sqldata_to_dict.get_dict()

kk = SpiderLotteryToMysql(column_name_dict='',page='',per_page_count='',sheet='')
items = kk.get_page_res()
print(items)
for item in items:
    print(item)
    dict_to_mysql(table_name='lottery',column_name_dict=column_name_dict,insert_data_dict=item)