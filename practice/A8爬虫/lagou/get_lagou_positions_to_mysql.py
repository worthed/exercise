# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/11/23 下午9:50
IDE：PyCharm
描述：爬取拉钩数据并存入mysql
"""
import json
import requests
from time import sleep
from random import randint
from retrying import retry
from urllib3.exceptions import InsecureRequestWarning
# 使用requests库请求HTTPS时,因为忽略证书验证,导致每次运行时都会报错
requests.urllib3.disable_warnings(InsecureRequestWarning)
# 自己集成的数据处理框架
from support.common.connect.connect_db.ConnectDB import localhost_insert_or_update
from support.common.support_utils.WrapperUtils import retry_if_type_error
from practice.A8爬虫.scrawl_proxy_and_save import select_from_IPpool
from urllib.request import quote
from fake_useragent import UserAgent


with open("../lagou/lagou_cookies", "rb") as openfile:
    lagou_cookies = openfile.readlines()[0]


def get_lagou_headers(city,position,header_type='info'):
    # 转化为url编码
    city_url_code = quote(city)
    position_url_code = quote(position)
    referer = "https://www.lagou.com/jobs/list_{0}?city={1}&cl=false&fromSearch=true&labelWords=&suginput="\
            .format(position_url_code, city_url_code)
    position_headers = {
        'User-Agent': str(UserAgent().random),
        'Host':'www.lagou.com',
        'Referer': referer,
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Cookie': lagou_cookies
    }

    info_headers = {
        'User-Agent': str(UserAgent().random),
        'Host':'www.lagou.com',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Cookie': lagou_cookies
    }

    if header_type == "position":
        return position_headers
    else:
        return info_headers


@retry(retry_on_exception=retry_if_type_error)
def get_lagou_first_page_to_mysql(city,position,page_num=1):
    """
    获取第一页的职位并记录到mysql
    :param city: 城市
    :param position: 职业
    :param page_num: 页码。默认传1，获取第一页
    :return: 总的职位数，用于get_pagenum_and_insert_others函数遍历剩下的页面
    """

    url = "https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false"

    headers = get_lagou_headers(city,position,header_type='position')

    form_data = {
        'first': 'true',
        'pn': page_num,
        'kd': position,
        'city': city
    }

    # 随机获得一个ip
    proxies = select_from_IPpool()

    response = requests.post(url, headers=headers,data=form_data,proxies=proxies,
                             cookies=lagou_cookies)
    response.raise_for_status()
    response.encoding = 'utf-8'
    pages = response.json()
    # print(json.dumps(pages))  # 转化为json，方便阅读

    # 定位到工作的具体信息
    job_info = pages['content']['positionResult']['result']
    job_count = pages['content']['positionResult']['totalCount']

    # 遍历岗位
    for job in job_info:
        # 岗位相关
        positionId = job['positionId']
        positionName = job['positionName']
        firstType = job['firstType']
        positionLables = ','.join(job['positionLables'])
        salary = job['salary']
        workYear = job['workYear']
        education = job['education']
        jobNature = job['jobNature']
        positionAdvantage = job['positionAdvantage']
        # 公司相关
        companyId=job['companyId']
        companyFullName = job['companyFullName']
        companyShortName = job['companyShortName']
        companySize = job['companySize']
        financeStage = job['financeStage']
        industryField = job['industryField']
        companyLabelList = ','.join(job['companyLabelList'])
        city = job['city']
        district = job['district']
        createTime = job['createTime']

        sql = "INSERT INTO jobs_lagou_position " \
              "(jobs_lagou_position_positionType,jobs_lagou_position_positionId, " \
              "jobs_lagou_position_positionName, jobs_lagou_position_firstType, " \
              "jobs_lagou_position_positionLables, jobs_lagou_position_salary, " \
              "jobs_lagou_position_workYear, jobs_lagou_position_education, " \
              "jobs_lagou_position_jobNature, jobs_lagou_position_positionAdvantage, " \
              "jobs_lagou_position_companyId, jobs_lagou_position_companyFullName, " \
              "jobs_lagou_position_companyShortName, jobs_lagou_position_companySize, " \
              "jobs_lagou_position_financeStage, jobs_lagou_position_industryField, " \
              "jobs_lagou_position_companyLabelList, jobs_lagou_position_city, " \
              "jobs_lagou_position_district, jobs_lagou_position_createTime) " \
              "VALUES " \
              "('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}'," \
              "'{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}');"\
            .format(position,positionId,positionName,firstType,positionLables,salary,
                    workYear,education,jobNature,positionAdvantage,companyId,
                    companyFullName,companyShortName,companySize,financeStage,
                    industryField,companyLabelList,city,district,createTime)

        localhost_insert_or_update(sql)

    print("第{0}页已完成爬取！".format(page_num))
    return job_count


@retry(retry_on_exception=retry_if_type_error)
def get_lagou_positions_to_mysql(city,position):
    """
    爬取拉勾网职位信息
    :param city: 爬取的城市
    :param position: 爬取的职位
    :return: 无返回
    """
    # 职位总数
    job_count = get_lagou_first_page_to_mysql(city,position,page_num=1)
    # 获得页面总数，因拉钩只会显示前30页，如果取余大于30，则只遍历至第30页，如果下于30，则遍历至当前页
    page_count = job_count//15
    if page_count >= 30:
        page_count = 30
    else:
        page_count = page_count
    for page in range(2,page_count+1):
        get_lagou_first_page_to_mysql(city,position,page_num=page)
        sleep(randint(15,20))


if __name__ == '__main__':

    city = '成都'
    position = '测试'
    get_lagou_positions_to_mysql(city,position)
