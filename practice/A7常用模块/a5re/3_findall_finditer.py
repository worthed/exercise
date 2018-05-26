# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/26 下午8:13
IDE：PyCharm
描述：使用 findall()和 finditer()查找每一次出现的位置
"""
import re
def is_not_None(data,eg_name):
    print(eg_name + " : " , data)

'eg1-findall()总是返回一个列表----------'
'-1-'
is_not_None(re.findall('car', 'car'),'eg1-1')
'-2-'
is_not_None(re.findall('car', 'scary'),'eg1-2')
'-3-'
is_not_None(re.findall('car', 'carry the barcardi to the car'),'eg1-3')



'eg2-与findall()函数类似但是更节省内存的变体，finditer()在匹配对象中迭代----------'
'-1-'
s = 'This and that.'
is_not_None(re.findall(r'(th\w+) and (th\w+)', s, re.I),'eg2-1')
'-2-'
is_not_None([g.groups() for g in re.finditer(r'(th\w+) and (th\w+)',s, re.I)],'eg2-2')


'eg3-在单个字符串中执行单个分组的匹配----------'
'-1-'
is_not_None( re.findall(r'(th\w+)', s, re.I),'eg3-1')
'-2-'
is_not_None(re.finditer(r'(th\w+)', s, re.I),'eg3-2')
