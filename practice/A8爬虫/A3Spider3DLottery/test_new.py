# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/12 下午12:20
IDE：PyCharm
描述：
retry装饰器有个坑：装饰的函数必须为最上层函数write_to_excel，
如果装饰的是出错的函数parse_one_page，则retry无法使用

写excel有个坑：
如果创建file和加sheet，如果在函数内，外部循环时，每次都会重新生成文件和sheet，
最终只能得到最后依次循环的结果而保存
"""
import requests
from bs4 import BeautifulSoup
import re
import time
from retrying import retry
from support.common.others.my_wrapper import retry_if_type_error
from support.common.others.dict_to_mysql import dict_to_mysql,replace_dict_none_to_null
from support.common.others.MysqlDataToDict import MysqlDataToDict
from support.common.connect_mysql.connect_mysql_and_query import localhost_query

class SpiderLottery(object):

    def __init__(self,page,per_page_count,sheet):
        """
        参数值，page，per_page_count作为参数传入
        :param page: 第几页
        :param per_page_count: 每页的数据条数
        :param file: 添加的file，在外部添加，避免在函数内添加，
                     在循环每次会重新生成文件，只能得到最后依次循环的结果
        :param sheet: sheet
        """
        self.page = page
        self.per_page_count = per_page_count
        self.sheet1 = sheet

    def get_one_page(self,url):
        """
        获取一页的响应内容
        :param url: url地址
        :return: 响应的text
        """
        headers = {
            'Host': 'kaijiang.zhcw.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None


    def parse_one_page(html):
        """
        解析每一页的内容
        :param html: 传入响应的text
        :return:
        """
        soup = BeautifulSoup(html, 'lxml')
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
                '销售额(元)': re.sub('[,]', '', item.select('td')[i + 6].text.strip('\n')),
                # 去掉%
                '返奖比例': re.sub('[%]', '', item.select('td')[i + 7].text),
            }


    @retry(retry_on_exception=retry_if_type_error)
    def write_to_sql(self):
        """
        写入到excel
        :return:
        """
        # 依次爬取每一页内容的每一期信息，并将其依次写入excel
        url = 'http://kaijiang.zhcw.com/zhcw/html/3d/list_{}.html'.format(str(self.page))
        html = SpiderLottery.get_one_page(self,url)
        print('正在保存第%d页……'% self.page)
        # 写入每一期的信息
        items = SpiderLottery.parse_one_page(html)

        sql = 'select COLUMN_NAME from information_schema.columns where table_name=\'lottery\' ' \
              'and COLUMN_NAME not in (\'lottery_id\',\'lottery_return_update_at\');'
        query_column_name = localhost_query(sql)
        sqldata_to_dict = MysqlDataToDict(query_result=query_column_name)
        sqldata_to_dict.get_dict()

        for item in items:
            new_item = MysqlDataToDict(item)
            dict_to_mysql(table_name='lottery', column_name_dict=sqldata_to_dict.get_dict(), insert_data_dict=new_item)


def main():
    # 一共246页
    for k in range(1, 247):
        spider = SpiderLottery(page=k, per_page_count=20, sheet='')
        spider.write_to_sql()
        time.sleep(2)

if __name__ == '__main__':
    main()