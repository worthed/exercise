# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/4 下午6:27
IDE：PyCharm
描述：sort一般作用于列表，sorted作用于任意可迭代的对象
1、实际运用中，如需保留原有列表，使用sorted函数比较合适，否则选择sort函数，因为sort不会复制原有列表，
消耗的内存较少，效率也比较高
2、不论sort和sorted，传入key比传入cmp效率要高
"""
persons = [{'name': 'Jon', 'age': 32},
           {'name': 'Alan', 'age': 50},
           {'name': 'Bob', 'age': 23},]
persons_sort = sorted(persons, key=lambda x: (x['name'], -x['age']))
print(persons_sort)

'-1-对字典进行排序'
phone_book = {'Linda':'7750', 'Bob':'9345', 'Carol':'5834'}
from operator import itemgetter
phone_book_sort = sorted(phone_book.items(),key=itemgetter(1))
print(phone_book_sort)

'-2-多维list排序'
game_result = [['Bob',95.00,'A'],
               ['Alan',86.0,'C'],
               ['Mandy',82.5,'A'],
               ['Rob','86','E']]
game_result_sort = sorted(game_result,key=itemgetter(2,1))
# 当第二个字段成绩相同的时候按照等级高低从低到高排序
print(game_result_sort)

'-3-字典总混合list排序'
mydict = {'Li':['M',7],
          'Zhang':['E',2],
          'Wang':['P',3],
          'Du':['C',2],
          'Ma':['C',9],
          'Zhe':['H',7]
          }
mydict_sort = sorted(mydict.items(), key=lambda v: itemgetter(1)(v))
# 按照list里面的等级和分数排序
print(mydict_sort)


'-4-list中混合字典'
gameresult = [{ "name": "Bob", "wins":10, "losses":3, "rating":75.00 },
              {"name": "David", "wins": 3, "losses":5, "rating":57.00 },
              {"name": "Carol" , "wins":4, "losses":5, "rating":57.00},
              {"name":"Patty", "wins":9, "losses":3, "rating": 71.48}]
gameresult_sort = sorted(gameresult, key=itemgetter("rating","name"))
print(gameresult_sort)