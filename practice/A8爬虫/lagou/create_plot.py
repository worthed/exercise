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
from pyecharts import Bar,Line,Pie,Style,Scatter,Boxplot

# 经验和薪资水平二维分析
info_from_excel = pd.read_excel("/Users/wangyuxiang/Desktop/lagoudata.xlsx",header=0)
years_sala = info_from_excel[['jobs_lagou_position_positionType','low','jobs_lagou_position_workYear']]
years_sala.columns = ['positionType','low','workYear']

def assort_salary(str_01):
    reg_str01 = "(\d+)"
    res_01 = re.findall(reg_str01, str_01)
    if len(res_01) == 2:
        a0 = int(res_01[0])
        b0 = int(res_01[1])
    else :
        a0 = int(res_01[0])
        b0 = int(res_01[0])
    return (a0+b0)/2

test_datas = years_sala.loc[years_sala['positionType']=='测试']
analy_datas = years_sala.loc[years_sala['positionType']=='数据分析']


# group by 职位类别、公司规模、薪资下限


Years = ['应届毕业生','不限','1-3年','3-5年','5-10年']
print(analy_datas.loc[analy_datas['workYear']=='3-5年'])


y_analy = []
for j in Years:
    analy_data = analy_datas.loc[analy_datas['workYear']==j]
    if analy_data.empty == 1:
        y_analy.append(pd.Series([1,2,3,4]))
    else:
        y_analy.append(analy_data['low'])

boxplot = Boxplot("箱形图")
#boxplot.add("测试", Years,boxplot.prepare_data(y_test))
boxplot.add("数据分析", Years,boxplot.prepare_data(y_analy))
boxplot.render()