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
from time import sleep
from random import randint
import re
from lxml import etree
from practice.A8爬虫.lagou.get_lagou_positions_to_mysql import get_lagou_headers
from support.common.connect.connect_db.ConnectDB import localhost_insert_or_update,localhost_query


headers = get_lagou_headers()

def get_position_info_to_mysql(position_id):
    position_url = "https://www.lagou.com/jobs/{0}.html".format(position_id)
    work_duty = ''
    work_requirement = ''
    response00 = requests.get(position_url,headers=headers).text
    html = etree.HTML(response00)
    content = html.xpath('//*[@id="job_detail"]/dd[2]/div/p/text()')

    # 岗位职责
    j = 0
    for i in range(len(content)):
        content[i] = content[i].replace('\xa0',' ')
        if content[i][0].isdigit():
            if j == 0:
                content[i] = content[i][2:].replace('、',' ')
                content[i] = re.sub('[；;.0-9。]','', content[i])
                work_duty = work_duty+content[i] + '/'
                j = j + 1
            elif content[i][0] == '1' and not content[i][1].isdigit():
                break
            else:
                content[i] = content[i][2:].replace('、', ' ')
                content[i] = re.sub('[、；;.0-9。]','',content[i])
                work_duty = work_duty + content[i] + '/'
        m = i

    # 岗位要求
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
                break
            else:
                content[i] = content[i][2:].replace('、', ' ')
                content[i] = re.sub('[、；;.0-9。]', '', content[i])
                work_requirement = work_requirement + content[i] + '/'

    print(work_duty)
    print(work_requirement)

    sql = "INSERT INTO `jobs_lagou_info` (`jobs_lagou_info_positionId`, " \
          "`jobs_lagou_info_work_duty`, `jobs_lagou_info_work_requirement`) VALUES " \
          "(\"{0}\",\"{1}\",\"{2}\");".format(position_id,work_duty,work_requirement)
    localhost_insert_or_update(sql)
    print(position_url,"存储成功")

    sleep(randint(5, 10))


if __name__ == '__main__':
    get_all_position_id_sql = "select jobs_lagou_position_positionId from jobs_lagou_position " \
                              "where jobs_lagou_position_id > 467 " \
                              "order by jobs_lagou_position_positionId;"
    all_position_id = localhost_query(get_all_position_id_sql)

    for position_id in all_position_id:
        print(position_id[0],"开始")
        get_position_info_to_mysql(position_id[0])