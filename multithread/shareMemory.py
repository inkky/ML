# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 17:00
# @Author  : Inkky
# @Email   : yingyang_chen@163.com
'''

'''
import multiprocessing as mp
import time

# 其中d和i参数用来设置数据类型的，
# d表示一个双精浮点类型，i表示一个带符号的整型。
value1 = mp.Value('i', 0)
value2 = mp.Value('d', 3.14)
array = mp.Array('i', [1, 2, 3, 4])  # 这里的Array和numpy中的不同，它只能是一维的，不能是多维的。


def job(v, num,l):
    l.acquire()
    for _ in range(5):
        time.sleep(0.2)
        v.value += num  # v.value获取共享变量值
        print('\n',v.value, end="")
    l.release()

def multicore():
    l=mp.Lock()
    v = mp.Value('i', 0)  # 定义共享变量
    p1 = mp.Process(target=job, args=(v, 1,l))
    p2 = mp.Process(target=job, args=(v, 3,l))  # 设定不同的number看如何抢夺内存
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    multicore()