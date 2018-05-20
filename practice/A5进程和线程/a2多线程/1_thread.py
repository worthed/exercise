# -*- coding:utf-8 -*-
'''
多任务可以由多进程完成，也可以由一个进程内的多线程完成，进程是由若干线程组成的，一个进程至少有一个线程。

Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，
threading是高级模块，对_thread进行了封装
'''

# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
import time, threading

# 新线程执行的代码
def loop():
    # 由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
    # Python的threading模块有个current_thread()函数，它永远返回当前线程的实例
    print('thread %s is running...' % threading.current_thread().name)
    n = 0

    # 主线程实例的名字叫MainThread,子线程的名字在创建时指定，我们用LoopThread命名子线程，在打印输出的时候显示名字

    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

