# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 11:13
# @Author  : Inkky
# @Email   : yingyang_chen@163.com
'''
弥补GIL
和thread用法类似
'''
import multiprocessing as mp
import threading as td
import time


def t_job(a, d):
    print('aaa %s'%td.current_thread())

def p_job(a, d):
    print('bbb %s'%mp.current_process())

#一定要添加main函数语句
if __name__ == '__main__':
    t1 = td.Thread(target=t_job, args=(1, 2),name='thread')
    p1 = mp.Process(target=p_job, args=(1, 2),name='process')
    t1.start()
    p1.start()
    t1.join()
    p1.join()

'''
存储进程输出 Queue
multiprocessing 应该是会在核中间用 queue 互换信息,
但是 list 却不能完成这种任务
'''
def job(q):
    res=0
    for i in range(100):
        res=res+i+i**2
    q.put(res)

if __name__ == '__main__':
    q=mp.Queue()
    p2=mp.Process(target=job,args=(q,))
    p3=mp.Process(target=job,args=(q,))
    p2.start()
    p3.start()
    p2.join()
    p3.join()
    res1=q.get()
    res2=q.get()
    print('p2',res1)
    print('p3',res2)
    print(res1+res2)