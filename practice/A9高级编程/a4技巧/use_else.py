# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/27 下午9:52
IDE：PyCharm
描述：
"""
'''
for: 仅当 for 循环运行完毕时（即 for 循环没有被 break 语句中止）才运行 else 块。

while: 仅当 while 循环因为条件为假值(False)而退出时（即 while 循环没有被break语句中止）才运行else块。

try: 仅当 try 块中没有异常抛出时才运行 else 块。

即，如果异常或者 return、break 或 continue 语句导致控制权跳到了复合语句的主块之外，那么else 子句也会被跳过。
'''

# for else
my_list = ['apple', 'pear', 'orange']
for item in my_list:
    if item == 'banana':
        print('Founded!')
        break
else:
    raise ValueError('No banana flavor found!')


# while else
a = 'apple'

while a == 'banana':
    pass
else:
    raise ValueError('No banana flavor found!')


# try else
''''''
try:
    first_func()
except OSError:
    log('OSerror')
else:
    second_func()