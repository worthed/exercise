# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/11 下午10:20
IDE：PyCharm
描述：
retry装饰器有个坑：装饰的函数必须为最上层函数write_to_excel，
如果装饰的是出错的函数parse_one_page，则retry无法使用

写excel有个坑：
如果创建file和加sheet，如果在函数内，外部循环时，每次都会重新生成文件和sheet，
最终只能得到最后依次循环的结果而保存

dict_to_mysql有个坑：
1、如果dict的values是None的话，会插入失败，因此需要把None替换为''
2、有的爬出来，dict的values不是None，而是空格，不考虑此情况也会失败，因此需要去除空格
3、数据库字段如果不是char、vchar字段的，会插入失败，后优化把第一点的None替换为''，改为None替换为NULL
4、数据库字段如果是 整型 NOT NULL DEFAULT '0'，会插入失败（目前还没有解决）
"""
import requests
from bs4 import BeautifulSoup
import re
import xlwt
from retrying import retry
from support.common.others.my_wrapper import retry_if_type_error
from support.common.others.dict_to_mysql import dict_to_mysql,replace_dict_none_to_null
from support.common.others.MysqlDataToJson import MysqlDataToJSON
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
    def write_to_excel(self):
        """
        写入到excel
        :return:
        """
        row0 = ['开奖日期','期号','号码1','号码2','号码3',
                '单选','组选3','组选6','销售额(元)','返奖比例']
        # 写入第一行
        for j in range(0,len(row0)):
            self.sheet1.write(0,j,row0[j])

        # 依次爬取每一页内容的每一期信息，并将其依次写入excel
        url = 'http://kaijiang.zhcw.com/zhcw/html/3d/list_{}.html'.format(str(self.page))
        html = SpiderLottery.get_one_page(self,url)
        print('正在保存第%d页……'% self.page)
        # 解析每一页
        # 带插入的行号 = （页数-1）* 每页的条数 + 1
        number = (self.page - 1) * self.per_page_count + 1
        items = SpiderLottery.parse_one_page(html)
        for item in items:
            self.sheet1.write(number, 0, item['开奖日期'])
            self.sheet1.write(number, 1, item['期号'])
            self.sheet1.write(number, 2, item['中奖号码1'])
            self.sheet1.write(number, 3, item['中奖号码2'])
            self.sheet1.write(number, 4, item['中奖号码3'])
            self.sheet1.write(number, 5, item['中奖注数_单选'])
            self.sheet1.write(number, 6, item['中奖注数_组选3'])
            self.sheet1.write(number, 7, item['中奖注数_组选6'])
            self.sheet1.write(number, 8, item['销售额(元)'])
            self.sheet1.write(number, 9, item['返奖比例'])
            number += 1

    @retry(retry_on_exception=retry_if_type_error)
    def write_to_mysql(self):
        """
        写入到mysql
        :return:
        """
        # 依次爬取每一页内容的每一期信息
        url = 'http://kaijiang.zhcw.com/zhcw/html/3d/list_{}.html'.format(str(self.page))
        html = SpiderLottery.get_one_page(self,url)
        print('正在保存第%d页……'% self.page)
        # 解析每一页
        items = SpiderLottery.parse_one_page(html)

        # 获取表名
        sql = 'select COLUMN_NAME from information_schema.columns where table_name=\'lottery\' ' \
              'and COLUMN_NAME not in (\'lottery_id\',\'lottery_return_update_at\');'
        query_result = localhost_query(sql)
        # sql查询结果转化为字典
        sqldata_to_dict = MysqlDataToJSON(query_result=query_result)
        # 获取转化后的dict
        sqldata_to_dict.get_json()

        # 遍历循环插入
        for item in items:
            # 替换None为''，带空格的值去掉空格
            new_item = replace_dict_none_to_null(item)
            dict_to_mysql(table_name='lottery',
                          column_name_dict=sqldata_to_dict.get_json(),
                          insert_data_dict=new_item)


def write_to_mysql_main():
    # 一共246页
    for k in range(1, 247):
        spider = SpiderLottery(page=k, per_page_count=20, sheet='')
        spider.write_to_mysql()
        #time.sleep(2)

def write_to_excel_main():
    file = xlwt.Workbook()
    sheet1 = file.add_sheet('3D', cell_overwrite_ok=True)
    # 一共246页
    for k in range(1, 247):
        spider = SpiderLottery(page=k, per_page_count=20, sheet=sheet1)
        spider.write_to_excel()
        #time.sleep(2)
    file.save('3D.xls')

if __name__ == '__main__':
    write_to_excel_main()