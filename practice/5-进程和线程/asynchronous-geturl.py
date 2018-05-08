# -*- coding:utf-8 -*-
import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    # 返回值是一对IO，分别代表读写，当执行获取header时，3个程序协同工作，互不影响，也因此不分先后，无需等待
    # yield from就是挂起执行,这个reader和writer都是connect的返回值,也就是说,挂着去执行connet这个方法(即连接上面的网址),
    # 这边等待中,然后去执行其他的逻辑了,等这里connet成功会返回reader和writer继续执行
    reader, writer = yield from connect
    # 对于r = yield from cor，这里的r其实是生成器cor发生StopIteration时的返回值,无return语句时返回None
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
