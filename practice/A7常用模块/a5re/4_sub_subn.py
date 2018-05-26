# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/26 下午8:40
IDE：PyCharm
描述：
使用 sub()和 subn()搜索与替换
用来替换的部分通常是一个字符串， 但它也可能是一个函数，该函数返回一个用来替换的字符串
subn() 还返回一个表示替换的总数，替换后的字符串和表示替换总数的数字一起作为一个拥有两个元素的元组返回
"""
import re
def is_not_None(data,eg_name):
    print(eg_name + " : " , data)

'eg1-替换功能，及替换的总数----------'
'-1-'
is_not_None(re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n'),'eg1-1')  # 将X替换为Mr. Smith
'-2-'
is_not_None(re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X,\n'),'eg1-2')  # 返回元祖格式
'-3-'
is_not_None(re.sub('[ae]', 'X', 'abcdef'),'eg1-3') # 将a和e替换为X
'-4-'
is_not_None(re.subn('[ae]', 'X', 'abcdef'),'eg1-4') # 将a和e替换为X,返回替换的总数


'eg2-使用反斜线N， 其中 N 是在替换字符串中使用的分组编号----------'
'-1-'
# 将美式的日期表示法 MM/DD/YY{,YY}格式转换为其他国家常用的格式 DD/MM/YY{,YY}
is_not_None(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',r'\2/\1/\3', '2/20/91'),'eg2-1')
'-2-'
is_not_None(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',r'\2/\1/\3', '2/20/1991'),'eg2-2')