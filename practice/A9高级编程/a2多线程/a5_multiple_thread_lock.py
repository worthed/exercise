# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/26 下午10:20
IDE：PyCharm
描述：糖果机和信号量
"""
from atexit import register
from random import randrange
from threading import Thread,Lock,BoundedSemaphore
# 新增信号量BoundedSemaphore
'''
当分配一个单位的资源时，计数器值减1，而当一个单位的资源返回资源池时，计数器值加 1。
BoundedSemaphore 的一个额外功能是这个计数器的值永远不会超过它的初始值，换句话说，
它可以防范其中信号量释放次数多于获得次数的异常用例。
'''
from time import sleep,ctime


lock = Lock() # 一个锁
MAX = 5 # 一个表示库存商品最大值的常量
candytray = BoundedSemaphore(MAX) # 糖果盘


# 补充糖果
def refill():
    lock.acquire()  # 是一个临界区，这就是为什么获取锁是执行所有行的仅有方法
    print('补充糖果中……')
    try:
        candytray.release()
    except ValueError:
        print('糖果盘已满，跳过。')
    else:
        print('补充成功\n')
    lock.release()

# 购买糖果
def buy():
    lock.acquire()
    print('购买糖果中……')
    if candytray.acquire(False): # 检测是否所有资源都已经消费完
        '''
        计数器的值不能小于 0，因此这个调用一般会在计数器再次增加之前被阻塞。
        通过传入非阻塞的标志False，让调用不再阻塞，而在应当阻塞的时候返回一个 False，指明没有更多的资源了。
        '''
        print('购买成功\n')
    else:
        print('糖果盘为空，跳过。')
    lock.release()

# 生产商
def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

# 消费者
def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

def _main():
    print('开始时间：',ctime())
    nloops = randrange(2,6)
    print('糖果机（已经有%d个了，已满）' %MAX)
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()
    Thread(target=producer, args=(nloops,)).start()

@register
def _atexit():
    print('结束时间：',ctime())

if __name__ == '__main__':
    _main()