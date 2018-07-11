# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/10 下午2:18
IDE：PyCharm
描述：
"""

import re
comment = 'q银行维护中'
regex = '(.*)银行(.*)维护(.*)'

print(re.match(regex,comment).group())