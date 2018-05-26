# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/26 上午10:17
IDE：PyCharm
描述：re的match
1、匹配单个字符串
2、匹配多个字符串
3、匹配任意单个字符串
4、匹配字符集：对于 r2d2|c3po的限制将比[cr][23][dp][o2]更为严格
5、重复、特殊字符以及分组
"""
import re

def is_not_None(data,eg_name):
    if data is not None:
        print(eg_name + " : " + data.group())


'eg1-匹配单个字符串------'
'-1-'
is_not_None(re.match('foo', 'foo'),'eg1-1')  # 匹配成功，输出匹配内容
'-2-'
is_not_None(re.match('foo', 'bar'),'eg1-2') # 匹配失败，赋值为 None
'-3-'
re.match('foo', 'food on the table').group()  # 可以直接将方法带在后面
'-4-'
#single_str_4 = re.match('foo', 'seafood').group()  # 不能匹配，会报错，用serch()方法替代则会成功


'eg2-匹配多个字符串------'
'-1-'
is_not_None(re.match('bat|bet|bit', 'bat'),'eg2-1')  # 匹配成功
'-2-'
# re.match('bat|bet|bit', 'He bit me!').group() # 不能匹配字符串，用serch()方法替代则会成功


'eg3-匹配任意单个字符串------'
'-1-'
is_not_None(re.match('.end', 'bend'),'eg3-1')  # 匹配成功
'-2-'
is_not_None(re.match('.end', 'end'),'eg3-2')  # 不匹配任何字符
'-3-'
is_not_None(re.match('.end', '\nend'),'eg3-3') # 除了 \n 之外的任何字符，都可以匹配
'-4-'
is_not_None(re.search('.end', 'The end.'),'eg3-4')  # 在搜索中匹配 ' ' ，输出为' end'
'-5-搜索一个真正的句点(小数点)，需要通过使用一个反斜线 对句点的功能进行转义'
patt314 = '3.14'  # 表示正则表达式的点号
pi_patt = '3\.14' # 表示字面量的点号 (dec. point)
is_not_None(re.match('3\.14', '3.14'),'eg3-5-1') # 精确匹配
is_not_None(re.match('3.14', '3014'),'eg3-5-2') # 点号匹配'0'
is_not_None(re.match('3.14', '3.14'),'eg3-5-3') # 点号匹配 '.'


'eg4-匹配字符集：对于 r2d2|c3po的限制将比[cr][23][dp][o2]更为严格------'
'-1-'
is_not_None(re.match('[cr][23][dp][o2]', 'c3po'),'eg4-1')  # 匹配成功
'-2-'
is_not_None(re.match('[cr][23][dp][o2]', 'c2do'),'eg4-2')  # 匹配成功
'-3-'
is_not_None(re.match('r2d2|c3po', 'c2do'),'eg4-3')  # 匹配失败
'-4-'
is_not_None(re.match('r2d2|c3po', 'r2d2'),'eg4-4')  # 匹配成功


'eg5-重复、特殊字符以及分组------'
'-1-'
is_not_None(re.match('\w\w\w-\d\d\d', 'abc-123'),'eg5-1') # 由连字符号分隔的字母数字字符串和数字组成,匹配成功
'-2-'
is_not_None(re.match('\w\w\w-\d\d\d', 'abc-xyz'),'eg5-2') # 匹配失败
'-3-'
is_not_None(re.match('(\w\w\w)-(\d\d\d)', 'abc-123'),'eg5-3') # 匹配成功
print(re.match('(\w\w\w)-(\d\d\d)', 'abc-123').group(1))
print(re.match('(\w\w\w)-(\d\d\d)', 'abc-123').group(2))
print(re.match('(\w\w\w)-(\d\d\d)', 'abc-123').groups())


