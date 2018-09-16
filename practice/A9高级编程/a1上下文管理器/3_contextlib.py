# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/20 下午9:15
IDE：PyCharm
描述：使用contextlib库来自定义上下文管理器
"""

from contextlib import contextmanager
import os

@contextmanager
def func():
    try:
        print("[in __enter__] acquiring resources")
        yield
        # yield之前的代码相当于__enter__方法，在进入with语句体之前执行，
        # yield之后的代码相当于__exit__方法，在退出with语句体的时候执行
    finally:
        print("[in __exit__] releasing resources")

with func():
    print("[in with-body] Testing")
    # raise(Exception("something wrong"))


# 使用 with 处理加锁
##不推荐
import threading
lock = threading.Lock()
lock.acquire()
try:
    None
finally:
    lock.release()

##推荐
import threading
lock = threading.Lock()
with lock:
    None
