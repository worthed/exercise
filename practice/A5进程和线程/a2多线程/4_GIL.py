# -*- coding:utf-8 -*-
'''
启动该死循环，启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核
但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%，为什么Python不行呢？

因为GIL锁：Global Interpreter Lock
任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。

GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，
也只能用到1个核

所以，在Python中，可以使用多线程，但不要指望能有效利用多核。



原因就在于 GIL ，在 Cpython 解释器（Python语言的主流解释器）中，有一把全局解释锁（Global Interpreter Lock），
在解释器解释执行 Python 代码时，先要得到这把锁，意味着，任何时候只可能有一个线程在执行代码，其它线程要想获得 CPU
执行代码指令，就必须先获得这把锁，如果锁被其它线程占用了，那么该线程就只能等待，直到占有该锁的线程释放锁才有执行代码
指令的可能。
'''

# python死循环
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()