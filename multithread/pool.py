# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 14:30
# @Author  : Inkky
# @Email   : yingyang_chen@163.com
'''
进程池就是我们将所要运行的东西，放到池子里，Python会自行解决多进程的问题
'''

import multiprocessing as mp


def job(x):
    return x * x


# 接下来用map()获取结果，
# 在map()中需要放入函数和需要迭代运算的值，
# 然后它会自动分配给CPU核
def multicore():
    # pool = mp.Pool()
    pool = mp.Pool(processes=3)
    res = pool.map(job, range(10))
    print(res)
    res = pool.apply_async(job, (2,))
    print(res.get())
    # 迭代器，i=0时apply一次，i=1时apply一次等等
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    # 从迭代器中取出
    print([res.get() for res in multi_res])


if __name__ == '__main__':
    multicore()
