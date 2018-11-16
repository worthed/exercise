# -*- coding:utf-8 -*-
'''
Python list和dict生成
'''

ls = [1, 2, 3, 4]
list1 = [i for i in ls if i > 2]
print(list1)
list2 = [i * 2 for i in ls if i > 2]
print(list2)

dic1 = {x: x ** 2 for x in (2, 4, 6)}
print(dic1)

dic2 = {x: 'item' + str(x ** 2) for x in (2, 4, 6)}
print(dic2)

set1 = {x for x in 'hello world' if x not in 'low level'}
print(set1)


# 列表，可以不用使用first_name = l[0]，last_name = l[1]
lst = ['David', 'Pythonista', '+1-514-555-1234']
first_name, last_name, phone_number = lst
# Python 3 Only
first, *middle, last = lst


# 循环嵌套
# 不推荐
x_list, y_list, z_list = [], [], []
for x in x_list:
    for y in y_list:
        for z in z_list:
            None
##推荐
from itertools import product
for x, y, z in product(x_list, y_list, z_list):
    None


# 把元组转换成一个字典
l = (('Knights', 'Ni'), ('Monty', 'Python'), ('SPAM', 'SPAAAM'))
d = dict(l)
print(d)