# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/27 下午5:28
IDE：PyCharm
描述：使用queen模块来提供线程间通信的机制
"""
from random import randint
from time import sleep
from multiprocessing import Queue
from practice.A9高级编程.a2多线程.a4_multiple_thread_sub import MyThread

# 实现使用queen对象，以及随机生产（消费）的商品的数量，生产者和消费者独立且并发地执行线程

def writeQ(queue):
    print('生产者Q……')
    queue.put('xxx', 1)
    print('size now', queue.qsize())

def readQ(queue):
    val = queue.get(1)
    print('消费Q……size now',queue.qsize())

def writer(queue,loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1,3))

def reader(queue,loops):
    for i in range(loops):
        readQ((queue))
        sleep(randint(2,5))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2,5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q,nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print('结束！')

if __name__ == '__main__':
    main()