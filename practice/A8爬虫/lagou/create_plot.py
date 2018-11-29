# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/11/29 上午10:28
IDE：PyCharm
描述：制作图标
"""
from support.common.connect.connect_db.ConnectDB import DBinfo
import pymysql
import pandas as pd
from pyecharts import Bar, Line

sql = "select jobs_lagou_position_positionType as 'positionType',jobs_lagou_position_companySize as 'companySize',jobs_lagou_position_education as 'education',count(1) as 'count' from jobs_lagou_info inner join jobs_lagou_position on jobs_lagou_position_positionId = jobs_lagou_info_positionId and jobs_lagou_position_positionName  not regexp '开发|性能|实习|主管|总监|经理|组长|挖掘|算法|DBA' group by jobs_lagou_position_positionType,jobs_lagou_position_companySize,jobs_lagou_position_education;"
DBdict = DBinfo.DBDict
lagou_position_datas = pd.read_sql(sql,con=pymysql.connect(**DBdict['local']))

analy_position = lagou_position_datas.loc[(lagou_position_datas['positionType']=='数据分析')].sort_values(by="companySize")
test_position = lagou_position_datas.loc[(lagou_position_datas['positionType']=='测试')].sort_values(by="companySize")

analy_line = Line("公司规模与学历-数据分析")
analy_line.add("本科", x_axis=analy_position.loc[(analy_position['education']=='本科')]["companySize"], y_axis=analy_position.loc[(analy_position['education']=='本科')]["count"],mark_line=["average"])
#analy_line.add("大专", x_axis=analy_position.loc[(analy_position['education']=='大专')]["companySize"], y_axis=analy_position.loc[(analy_position['education']=='大专')]["count"],mark_line=["average"])
#analy_line.add("不限", x_axis=analy_position.loc[(analy_position['education']=='不限')]["companySize"], y_axis=analy_position.loc[(analy_position['education']=='不限')]["count"],mark_line=["average"])
analy_line

'''
analy_test = Line("公司规模与学历-测试")
analy_test.add("本科", x_axis=test_position.loc[(test_position['education']=='本科')]["companySize"], y_axis=test_position.loc[(test_position['education']=='本科')]["count"],mark_line=["average"])
analy_test.add("大专", x_axis=test_position.loc[(test_position['education']=='大专')]["companySize"], y_axis=test_position.loc[(test_position['education']=='大专')]["count"],mark_line=["average"])
analy_test.add("不限", x_axis=test_position.loc[(test_position['education']=='不限')]["companySize"], y_axis=test_position.loc[(test_position['education']=='不限')]["count"],mark_line=["average"])
analy_test
'''

