# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/20 下午9:05
IDE：PyCharm
描述：简单的读写文件的上下文管理器（一个实现了__enter__和__exit__方法的对象就称之为上下文管理器）

__enter__一般用于资源分配，如打开文件、连接数据库、获取线程锁；
__exit__一般用于资源释放，如关闭文件、关闭数据库连接、释放线程锁

"""

with open('output.txt', 'w') as f:
    f.write('Hello world')


"""
1、首先执行open('output', 'w')，返回一个文件对象
2、调用这个文件对象的__enter__方法，
3、并将__enter__方法的返回值赋值给变量f执行with语句体，即with语句包裹起来的代码块
4、不管执行过程中是否发生了异常，执行文件对象的__exit__方法，在__exit__方法中关闭文件

# 无论写文件的操作成功与否，是否有异常抛出，with语句都会保证文件被关闭
"""



'''
如果不使用with

try:
    f = open("output", "w")
    f.write("Hello world")
finally:
    f.close()
'''



