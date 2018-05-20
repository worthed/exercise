# -*- coding:utf-8 -*-
'''
子进程

在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的
'''

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)