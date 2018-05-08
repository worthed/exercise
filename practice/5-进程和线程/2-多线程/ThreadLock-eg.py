# -*- coding:utf-8 -*-
'''
要确保一个线程在修改balance的时候，别的线程一定不能改，就要给change_it()上一把锁
当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改

锁的坏处：
1、首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
2、由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止
'''
import time, threading

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        # 先要获取锁
        lock.acquire()
        try:
            # 放心地改
            change_it(n)
        finally:
            # 改完了释放锁,否则那些苦苦等待锁的线程将永远等待下去，成为死线程
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)