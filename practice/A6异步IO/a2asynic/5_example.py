# -*- coding:utf-8 -*-
'''
asyncio是python 3.4中新增的模块，它提供了一种机制，使得你可以用协程（coroutines）、
IO复用（multiplexing I/O）在单线程环境中编写并发模型

事件驱动模型


1、当事件循环开始运行时，它会在Task中寻找coroutine（协程）来执行调度，因为事件循环注册了print_sum()，
因此print_sum()被调用
2、执行result = await compute(x, y)这条语句（等同于result = yield from compute(x, y)），
因为compute()自身就是一个coroutine，
3、因此print_sum()这个协程就会暂时被挂起，compute()被加入到事件循环中，程序流执行compute()中的print语句
，打印”Compute %s + %s …”，
4、然后执行了await asyncio.sleep(1.0)，因为asyncio.sleep()也是一个coroutine，
接着compute()就会被挂起，等待计时器读秒，
5、在这1秒的过程中，事件循环会在队列中查询可以被调度的coroutine，
而因为此前print_sum()与compute()都被挂起了，因此事件循环会停下来等待协程的调度，
6、当计时器读秒结束后，程序流便会返回到compute()中执行return语句，结果会返回到print_sum()中的result中，
最后打印result，
事件队列中没有可以调度的任务了，此时loop.close()把事件队列关闭，程序结束
'''

# 事件驱动模型，事件驱动模型就是异步编程的重中之重
import asyncio

async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()
