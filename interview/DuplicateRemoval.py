# -*- coding:utf-8 -*-
'''
对一个数组进行去重
'''

# 去重数组
list_a = ['a','b','a','c','e','f','c','b','j','c','h']

# 方法一
new_list_a = set(list_a)
print(new_list_a)

# 方法二
list_b = []
for i in list_a:
    if i not in list_b:
        list_b.append(i)

print(list_b)