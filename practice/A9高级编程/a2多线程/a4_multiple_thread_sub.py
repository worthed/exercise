# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/26 下午10:08
IDE：PyCharm
描述：派生 Thread 的子类，并创建子类的实例
"""
from time import sleep,ctime
import threading

loops = [4,2]

class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
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
            t = MyThread(MyThread.loop, (i, loops[i]), MyThread.loop.__name__)
            threads.append(t)

        for i in n_loops:
            threads[i].start()

        for i in  n_loops:
            threads[i].join()

        print('所有结束！',ctime())

if __name__ == '__main__':
    MyThread.main()


