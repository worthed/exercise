# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/26 下午9:56
IDE：PyCharm
描述：面向对象，实例化一个thread类
"""
from time import sleep,ctime
import threading

loops = [4,2]

class ThreadFunc(object):

    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

    def loop(n_loop, n_sec):
        print('开始第%d个loop方法：' %n_loop,ctime())
        sleep(n_sec)
        print('结束第%d个loop方法：' %n_loop,ctime())

    def main():
        print('程序开始：',ctime())
        threads = []
        n_loops = range(len(loops))

        for i in n_loops:
            t = threading.Thread(target=ThreadFunc(ThreadFunc.loop, (i, loops[i]), ThreadFunc.loop.__name__))
            threads.append(t)

        for i in n_loops:
            threads[i].start()

        for i in  n_loops:
            threads[i].join()

        print('所有结束！',ctime())

if __name__ == '__main__':
    ThreadFunc.main()
