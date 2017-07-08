# -*- coding:utf-8 -*-
import time
"""修饰符无参数，原函数无参数"""


def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print "used:", end - start
    return wrapper


@timeit
def foo():
    print "in foo()"

foo()
# 用下面2行代码代替上面，会输出None，？？？？为啥
# a = timeit(foo)
# print a()
