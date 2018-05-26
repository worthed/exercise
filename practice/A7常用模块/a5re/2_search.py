# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/26 下午8:07
IDE：PyCharm
描述：匹配字符串的起始和结尾以及单词边界
"""
import re

def is_not_None(data,eg_name):
    if data is not None:
        print(eg_name + " : " + data.group())

'eg1-匹配字符串的起始和结尾以及单词边界------'
'-1-'
is_not_None(re.search('^The', 'The end.'),'eg1-1')  # 匹配
'-2-'
is_not_None(re.search('^The', 'end. The'),'eg1-2')  # 不作为起始,匹配失败
'-3-'
is_not_None(re.search(r'\bthe', 'bite the dog'),'eg1-3') # 在边界，匹配成功
'-4-'
is_not_None(re.search(r'\bthe', 'bitethe dog'),'eg1-4') # 有边界，匹配失败
'-5-'
is_not_None(re.search(r'\Bthe', 'bitethe dog'),'eg1-5') # 没有边界，匹配成功

