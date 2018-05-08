# -*- coding:utf-8 -*-
'''
包管理
'''

# 一个包里有三个模块，mod1.py, mod2.py, mod3.py，但使用from demopack import *导入模块时，如何保证只有mod1、mod3被导入了


# 答案:增加__init__.py文件，并在文件中增加：

__all__ = ['mod1','mod3']