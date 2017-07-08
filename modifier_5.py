# -*- coding:utf-8 -*-
import time


def timeit(func):
    def wrapper(args):
        start = time.clock()
        func(args)
        end = time.clock()
        print "used:", end - start
    return wrapper


@timeit
def foo(arg):
    print "in foo(), arg is" + arg


foo("aaaaa")
