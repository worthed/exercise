# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/4 下午6:15
IDE：PyCharm
描述：
"""
'-1-'
# 字符串中本身的双引号需要转义
string1 = "hello，my，\"god\" "
# 字符串本身的双引号不需要转义
string2 = 'hello, my "god" '
sql1 = 'select * from asset where asset_create_at >= "2018-08-01" '


a = ('select * '
     'from asset '
     'where asset_id = "123456";'
    )

b = u"Hi"  # 转成unicode格式

assert 'Hello World！'.istitle() == True  # 判定字符串是否每个单词有且只有第一个字母是大写
print('Hello world！'.title())  # 将每一个单词的首字母大写

# 两种不同的split
print('  hello  world!  '.split())
print('  hello  world!  '.split(' '))


