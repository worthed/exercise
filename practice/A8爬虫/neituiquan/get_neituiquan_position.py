# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/12/3 下午1:04
IDE：PyCharm
描述：
"""
import requests
import re
from random import randint
from urllib3.exceptions import InsecureRequestWarning
# 使用requests库请求HTTPS时,因为忽略证书验证,导致每次运行时都会报错
requests.urllib3.disable_warnings(InsecureRequestWarning)
# 自己集成的数据处理框架
from support.common.connect.connect_db.ConnectDB import localhost_insert_or_update,localhost_query
from fake_useragent import UserAgent
from time import sleep


# 请求头信息
headers = {
    'User-Agent': str(UserAgent().random),
    'Host':'api.itneituiquan.com',
    'Referer': 'http://www.itneituiquan.com/',
    'Origin': 'http://www.itneituiquan.com',
    'Connection': 'keep-alive'
}


def get_datas_to_mysql(datas):
    """
    写数据到mysql
    :param datas: 捕获到的json返回
    :return:
    """
    for data in datas:
        # 具体取值详情可见表设计
        id = data['id']
        companyName = data['companyName']
        industryTypeName = data['industryTypeName']
        name = data['name']
        numbers = data['numbers']
        state = data['state']
        financeTypeName = data['financeTypeName']
        qualificationsName = data['qualificationsName']
        workExperienceName = data['workExperienceName']
        salaryRangeName = data['salaryRangeName']
        positionTypeName = data['positionTypeName']
        address = data['address']

        sql = "INSERT INTO `jobs_neitui_position` (`jobs_neitui_position_id`, " \
              "`jobs_neitui_position_companyName`, `jobs_neitui_position_industryTypeName`, " \
              "`jobs_neitui_position_name`, `jobs_neitui_position_numbers`, `jobs_neitui_position_state`, " \
              "`jobs_neitui_position_financeTypeName`, `jobs_neitui_position_qualificationsName`, " \
              "`jobs_neitui_position_workExperienceName`, `jobs_neitui_position_salaryRangeName`, " \
              "`jobs_neitui_position_positionTypeName`, `jobs_neitui_position_address`) " \
              "VALUES ('{0}','{1}', '{2}', '{3}', '{4}', '{5}', '{6}','{7}', '{8}', '{9}','{10}', '{11}');" \
            .format(id, companyName, industryTypeName, name, numbers, state,
                    financeTypeName,
                    qualificationsName, workExperienceName, salaryRangeName,
                    positionTypeName, address)
        # 写数据
        localhost_insert_or_update(sql)


def get_position_main():
    """
    爬取数据主运行程序
    :return:
    """
    for i in range(1, 15):
        url = "http://api.itneituiquan.com/portal/position?financingType=&qualifications" \
              "Type=&workExperience=&salaryRange=&specialPerformanceType=&name=&pageSize=4" \
              "&pageIndex={0}&debug=true".format(i)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response.encoding = 'utf-8'
        pages = response.json()

        # 取值
        datas = pages['data']
        #print(json.dumps(pages))  # 转化为json，方便阅读分析

        # 存库
        get_datas_to_mysql(datas)
        print("第{0}页数据已储存！".format(i))

        # 模拟浏览行为
        sleep(randint(5, 10))


def get_position_info_main():
    """
    通过positionid获取页面详情，用于读取工作职责和任职资格
    :return:
    """
    get_position_id_sql = "select jobs_neitui_position_id from jobs_neitui_position " \
                          "where jobs_neitui_position_state = 'active';"

    position_id = localhost_query(get_position_id_sql)
    for id in position_id:
        # 职位详情url
        position_info_url = "http://api.itneituiquan.com/portal/position/{0}?debug=true".format(
            id[0])
        response = requests.get(position_info_url, headers=headers)
        response.raise_for_status()
        response.encoding = 'utf-8'
        pages = response.json()  # page = json.dumps(pages)

        # 详情信息再json中的位置
        datas = pages['data']
        work_duty_original = datas['desc']
        work_requirement_original = datas['requirements']

        # 正则处理，去掉文字中的html标签
        pat = re.compile('<[^>]+>', re.S)
        work_duty = pat.sub('', work_duty_original)
        work_requirement = pat.sub('', work_requirement_original)

        sql = "INSERT INTO `jobs_neitui_info` (`jobs_neitui_info_positionid`, " \
              "`jobs_neitui_info_work_duty`, `jobs_neitui_info_work_requirement`) " \
              "VALUES ('{0}', '{1}', '{2}');".format(id[0], work_duty,work_requirement)

        localhost_insert_or_update(sql)
        print("{0} 已爬取！".format(position_info_url))

        # 模拟浏览行为
        sleep(randint(5, 10))


def deal_salary():
    """
    处理薪水，拆分为上限和下限
    :return:
    """
    get_all_salary_sql = "select jobs_neitui_position_id,jobs_neitui_position_salaryRangeName  " \
                         "from jobs_neitui_position " \
                         "where jobs_neitui_position_salaryRangeName != '面议';"
    all_salary = localhost_query(get_all_salary_sql)

    for salary in all_salary:
        id = salary[0]
        salary_split = re.split("k", salary[1])
        # 需转化为int类型，因为库表设计的格式为int
        low = int(salary_split[0])
        high = int(salary_split[1][1:])

        update_position_sql = "update jobs_neitui_position set " \
                              "jobs_neitui_position_salaryRangeName_low = '{0}'," \
                              "jobs_neitui_position_salaryRangeName_high='{1}' " \
                              "where jobs_neitui_position_id = '{2}' limit 1;".format(low,high,id)
        localhost_insert_or_update(update_position_sql)


if __name__ == '__main__':
    deal_salary()

