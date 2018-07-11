# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/11 下午5:50
IDE：PyCharm
描述：计算文件file_open的非空字符个数
"""
with open('/Users/wangyuxiang/PycharmProjects/support/support/analyze/sql/check_repeated_withhold_res.txt','rb') as file_open:
    # 生成器表达式（性能优于列表解析）
    l = sum([len(word) for line in file_open for word in line.split()])

# 列表解析
l = sum(len(word) for line in file_open for word in line.split())