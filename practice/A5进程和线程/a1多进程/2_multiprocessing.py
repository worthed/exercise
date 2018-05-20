# -*- coding:utf-8 -*-
'''
multiprocessing模块就是跨平台版本的多进程模块,可避免fork()只能在unix系统使用的情况
'''
import os
from multiprocessing import Process

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',)) # 创建一个Process实例
    print('Child process will start.')
    p.start()  # 用start()方法启动实例
    p.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')