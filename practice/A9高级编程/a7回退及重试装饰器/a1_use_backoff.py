# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/11 下午2:55
IDE：PyCharm
描述：此模块提供函数装饰器，该函数装饰器可用于包装函数，以便函数重试直到满足某些条件为止。当访问可
能出现间歇性故障的不可靠资源（如网络资源和外部API）时，它应该有用。一般来说，它还可以用于外部生成
内容的动态轮询资源。

装饰器既支持同步代码的常规功能，也支持异步代码的asyncio的协同程序。
"""
import requests
import aiohttp
import backoff

'-1-'
# 当出现任何requests异常时，使用指数退避（即退避时间指数增长）
@backoff.on_exception(backoff.expo,
                      requests.exceptions.RequestException,
                      max_tries=8)
def get_url(url):
    return requests.get(url)

# 对于需要多个异常类型采取相同退避行为的情况，装饰器还将接受异常元组
@backoff.on_exception(backoff.expo,
                      (requests.exceptions.Timeout,
                       requests.exceptions.ConnectionError),
                      max_tries=8)
def get_url(url):
    return requests.get(url)


'-2-'
# 放弃机制 max_tries max_time giveup
def fatal_code(e):
    return 400 <= e.response.status_code < 500

@backoff.on_exception(backoff.expo,
                      requests.exceptions.RequestException,
                      max_tries=8,
                      max_time=60,
                      giveup=fatal_code)
def get_url(url):
    return requests.get(url)


'-3-'
# 当目标函数返回值符合某个特定条件时，on_predicate装饰器会安排重试。
# 例子：当目标函数的返回值为空列表时，使用斐波那契序列退避（退避时间满足）
@backoff.on_predicate(backoff.fibo, lambda x: x == [], max_value=13)
def poll_for_messages(queue):
    return queue.get()
# 简写:当未指定断言函数时，默认做返回值的假值测试
@backoff.on_predicate(backoff.fibo, max_value=13)
def poll_for_message(queue):
    return queue.get()
#  or 一个继续每秒钟轮询直到得到非假结果的函数
@backoff.on_predicate(backoff.constant, interval=1)
def poll_for_message(queue):
    return queue.get()


'-4-'
#  组合backoff使用
@backoff.on_predicate(backoff.fibo, max_value=13)
@backoff.on_exception(backoff.expo,
                      requests.exceptions.HTTPError,
                      max_tries=4)
@backoff.on_exception(backoff.expo,
                      requests.exceptions.TimeoutError,
                      max_tries=8)
def poll_for_message(queue):
    return queue.get()


'-5-'
# 运行时配置：装饰函数可以通过在运行时执行函数来获得参数值

def lookup_max_tries():
    # pretend we have a global reference to 'app' here
    # and that it has a dictionary-like 'config' property
    # 当关键字参数作为常量值传递时，这很好，
    # 但是假设我们想要查阅带有配置选项的字典，这些配置选项仅在运行时可用。
    return app.config["BACKOFF_MAX_TRIES"]

@backoff.on_exception(backoff.expo,
                      ValueError,
                      max_tries=lookup_max_tries)
def xx(xx):
    return None


'-6-'
# 事件处理
# 例子：打印回退事件的细节的处理程序
def backoff_hdlr(details):
    print ("Backing off {wait:0.1f} seconds afters {tries} tries "
           "calling function {func} with args {args} and kwargs "
           "{kwargs}".format(**details))

@backoff.on_exception(backoff.expo,
                      requests.exceptions.RequestException,
                      on_backoff=backoff_hdlr)
def get_url(url):
    return requests.get(url)

# 每个事件类型的多个处理程序
@backoff.on_exception(backoff.expo,
                      requests.exceptions.RequestException,
                      on_backoff=[backoff_hdlr1, backoff_hdlr2])
def get_url(url):
    return requests.get(url)


'-7-'
# 异步代码：要在基于asyncio的异步代码中使用backoff，
# 您只需要将backoff.on_exception或backoff.on_predicate应用于协同例程
@backoff.on_exception(backoff.expo,
                      aiohttp.ClientError,
                      max_time=60)
async def get_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return requests.get(url)


'-8-'
# 日志配置: 错误和回退和重试尝试被记录到“退避”记录器。默认情况下，此记录器配置为NullHandler，
# 因此除非配置处理程序，否则将没有输出
logging.getLogger('backoff').addHandler(logging.StreamHandler())
logging.getLogger('backoff').setLevel(logging.INFO)