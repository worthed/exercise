# -*- coding:utf-8 -*-
'''
asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，
然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO
'''
import asyncio

@asyncio.coroutine  # 把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行
def hello():
    print("Hello World!")
    # 异步调用asyncio.sleep()
    r = yield from asyncio.sleep(2)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine 协程
loop.run_until_complete(hello())
loop.close()

'''
1、hello()会首先打印出Hello world!
2、yield from语法可以让我们方便地调用另一个generator。
   由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
3、当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。

把asyncio.sleep(2)看成是一个耗时2秒的IO操作，在此期间，
主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
'''
