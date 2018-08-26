# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/8/20 下午3:06
IDE：PyCharm
描述：
"""
'-1-'
# 字符串中本身的双引号需要转义
string1 = "hello，my，\"god\" "
# 字符串本身的双引号不需要转义
string2 = 'hello, my "god" '
sql1 = 'select * from asset where asset_create_at >= "2018-08-01" '

'-2-三元操作符 C?X:Y'
X,Y = 0,-2
print(X if X<Y else Y)

'-3-if else'
# if else
n = 1
if n == 0:
    print('is zero\n')
elif n == 1:
    print('is one\n')
elif n == 2:
    print('is two\n')
else:
    print('no no no\n')

def f(x):
    return {0:"is zero\n",
            1:"is one\n",
            2:"is two\n",}.get(x, 'no no no\n')

print(f(1))

age = 7
print(type(age))

age_2 = '7'
print(type(age_2))