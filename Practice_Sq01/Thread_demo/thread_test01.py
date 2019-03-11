# -*- coding: utf-8 -*-

# @Time    : 2019/3/12 0012 0:42
# @Author  : Administrator
# @Comment : 多线程，线程池水示例


import time
import threading


# 新线程执行的代码:
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 10000:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        # time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name


def loop01(n):
    # print 'thread %s >>> %s' % (threading.current_thread().name, n)
    # time.sleep(5)
    print n
    f0()


def f0():
    pass



if __name__ == '__main__':
    # test
    # start_time = time.time()
    # print 'time: %s' % (time.strftime("%Y-%m-%d %H:%M:%S"))
    # t = threading.Thread(target=loop, name='LoopThread')
    # t.start()
    # t.join()
    # end_time = time.time()
    # print 'time: %s' % (time.strftime("%Y-%m-%d %H:%M:%S"))
    # print 'time cost: %s' % ('%.2f' % (end_time - start_time))

    # test01
    start_time = time.time()
    print 'time: %s' % (time.strftime("%Y-%m-%d %H:%M:%S"))
    print 'thread %s is running...' % threading.current_thread().name
    # li = []
    for n in range(10000):
        t = threading.Thread(target=loop01, args=(n,), name='LoopThread')
        # li.append(t)
        t.start()
    # for i in li:
    #     i.join()        # 等待子线程全部执行完

    # t = threading.Thread(target=loop01, args=(1,), name='LoopThread')
    # # t.setDaemon(True)  # 设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
    # t.start()
    # t = threading.Thread(target=loop01, args=(2,), name='LoopThread')
    # t.start()
    # t = threading.Thread(target=loop01, args=(3,), name='LoopThread')
    # t.start()
    print 'thread %s ended.' % threading.current_thread().name
    end_time = time.time()
    print 'time: %s' % (time.strftime("%Y-%m-%d %H:%M:%S"))
    print 'time cost: %s' % ('%.2f' % (end_time - start_time))


    # start_time = time.time()
    # print 'time: %s' % (time.strftime("%Y-%m-%d %H:%M:%S"))
    # print '%s is running...' % threading.current_thread().name
    # n = 0
    # # while n < 10000:
    # #     n += 1
    # #     loop01(n)
    # for i in range(10000):
    #     loop01(i)
    # print '%s ended.' % threading.current_thread().name
    # end_time = time.time()
    # print 'time: %s' % (time.strftime("%Y-%m-%d %H:%M:%S"))
    # print 'time cost: %s' % ('%.2f' % (end_time - start_time))


