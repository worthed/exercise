# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/26 下午8:57
IDE：PyCharm
描述：拓展功能
"""
import re
def is_not_None(data,eg_name):
    print(eg_name + " : " , data)

'-1-'
is_not_None(re.findall(r'(?i)yes', 'yes? Yes. YES!!'),'eg1-1') # 不区分大小写查找
'-2-'
is_not_None(re.findall(r'(?i)th\w+', 'The quickest way is through this tunnel.'),'eg1-2') # 不区分大小写查找
'-3-'
# 通过使用“多行”，能够 在目标字符串中实现跨行搜索，而不必将整个字符串视为单个实体
# 注意，此时忽略了实例“the”，因为它们并不出现在各自的行首。
is_not_None(re.findall(r'(?im)(^th[\w ]+)',
                       """This line is the first,
                       another line,
                       that line, 
                       it's the best"""),'eg1-3')