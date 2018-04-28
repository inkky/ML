# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 9:25
# @Author  : Inkky
# @Email   : yingyang_chen@163.com
'''
GIL最大的问题就是Python的多线程程序并不能利用多核CPU的优势
（比如一个使用了多个线程的计算密集型程序只会在一个单CPU上面运行）。

在讨论普通的GIL之前，有一点要强调的是
GIL只会影响到那些严重依赖CPU的程序（比如计算型的）。
如果你的程序大部分只会涉及到I/O，比如网络交互，那么使用多线程就很合适，
因为它们大部分时间都在等待。
'''

import threading
import time
from queue import Queue

threading.active_count()  # 获取已激活的线程数
threading.enumerate()  # 查看所有线程信息
threading.current_thread()  # 查看现在正在运行的线程


# 添加线程
def thread_job1():
    # print('this is a thread of %s'%threading.current_thread())
    print('t1 start\n')
    for i in range(10):
        time.sleep(0.1)  # 任务间隔0.1s
    print('t1 finish')


def thread_job2():
    print('t2 start\n')
    print('t2 finish\n')


thread1 = threading.Thread(target=thread_job1, name='t1')
thread2 = threading.Thread(target=thread_job2)
thread1.start()
thread2.start()
thread1.join()  # 使用join加以控制
thread2.join()
print('all done')

'''
将数据列表中的数据传入，使用四个线程处理，
将结果保存在Queue中，
线程执行完后，从Queue中获取存储的结果
l:list
q:queue
'''


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)  # 多线程调用的函数不能用return返回值


def multitreading():
    q = Queue()  # q中存放返回值，代替return的返回值
    threads = []
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]
    for i in range(4):  # 定义四个线程
        # Thread首字母要大写，被调用的job函数没有括号，只是一个索引，参数在后面
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)  # 把每个线程append到线程列表中
    for thread in threads:  # join四个线程到主线程
        thread.join()
    results = []
    for i in range(4):
        results.append(q.get())  # q.get()按顺序从q中拿出一个值
    print(results)

multitreading()

'''
lock在不同线程使用同一共享内存时，能够确保线程之间互不影响
'''
def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=1
        print('job1:%d'%A)
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=10
        print('job2:%d'%A)
    lock.release()

lock=threading.Lock()
A=0
t1=threading.Thread(target=job1)
t2=threading.Thread(target=job2)
t1.start()
t2.start()
t1.join()
t2.join()