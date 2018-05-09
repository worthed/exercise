# -*- coding:utf-8 -*-
'''
如果要启动大量的子进程，可以用进程池的方式批量创建子进程
'''

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(3)  # 因为Pool的默认大小是4,故task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，但最多同时执行4个进程
    # 由于Pool的默认大小是CPU的核数，如果你拥有8核CPU，要提交至少9个子进程才能看到等待效果
    for i in range(5):
        p.apply_async(long_time_task, args = (i,))
    print('Waiting for all subprocesses done...')    # subprocesses 子进程
    p.close()
    # 对Pool对象调用join()方法会等待所有子进程执行完毕
    # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.join()
    print('All subprocesses done.')