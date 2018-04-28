# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 14:19
# @Author  : Inkky
# @Email   : yingyang_chen@163.com
'''
对比下多进程，多线程和什么都不做时的消耗时间，看看哪种方式更有效率。
'''

import multiprocessing as mp


def job(q):
    res = 0
    for i in range(10000000):
        res = res + i + i ** 2
    q.put(res)


def multicore():
    q = mp.Queue()
    p2 = mp.Process(target=job, args=(q,))
    p3 = mp.Process(target=job, args=(q,))
    p2.start()
    p3.start()
    p2.join()
    p3.join()
    res1 = q.get()
    res2 = q.get()
    # print('p2', res1)
    # print('p3', res2)
    print('mutiprocess', res1 + res2)


import threading as td


def multithread():
    q = mp.Queue()
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    # print('p2', res1)
    # print('p3', res2)
    print('multithread', res1 + res2)


def normal():
    res = 0
    for _ in range(2):
        for i in range(10000000):
            res = res + i + i ** 2
    print('normal', res)


import time

if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time:', st1 - st)
    multicore()
    st2 = time.time()
    print('multiprocess time :', st2 - st1)
    multithread()
    st3 = time.time()
    print('multithread time:', st3 - st2)
