# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/20 下午9:09
IDE：PyCharm
描述：自定义一个上下文管理器
"""

class ContextManager(object):
    def __enter__(self):
        print("[in __enter__] acquiring resources")

    def __exit__(self, exception_type, exception_value, traceback):
        print("[in __exit__] releasing resources")
        if exception_type is None:
            print("[in __exit__] Exited without exception")
        else:
            print("[in __exit__] Exited with exception: %s" % exception_value)
            return False

with ContextManager():
    print("[in with-body] Testing")
    # raise (Exception("something wrong"))
    #  在with语句体中人为地抛出一个异常如我们所期待，with语句体中抛出异常，
    # __exit__方法中exception_type不为None，__exit__方法返回False，异常被重新抛出




