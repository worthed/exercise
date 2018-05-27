# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/26 下午9:37
IDE：PyCharm
描述：
"""
from time import sleep,ctime
import threading

loops = [4,2]

def loop(n_loop, n_sec):
    print('开始第%d个loop方法：' %n_loop,ctime())
    sleep(n_sec)
    print('结束第%d个loop方法：' %n_loop,ctime())

def main():
    print('程序开始：',ctime())
    threads = []
    n_loops = range(len(loops))

    for i in n_loops:
        t = threading.Thread(target=loop,args=(i, loops[i]))
        threads.append(t)

    for i in n_loops:
        threads[i].start()

    for i in  n_loops:
        threads[i].join()

    print('所有结束！',ctime())


'''
对于 join()方法而言，其另一个重要方面是其实它根本不需要调用。
一旦线程启动，它们 就会一直执行，直到给定的函数完成后退出。
如果主线程还有其他事情要去做，而不是等待 这些线程完成(例如其他处理或者等待新的客户端请求)，
就可以不调用 join()。join()方法只 有在你需要等待线程完成的时候才是有用的
'''

if __name__ == '__main__':
    main()

