# -*- coding:utf-8 -*-
"""函数修饰符"""
# http://www.cnblogs.com/xupeizhi/archive/2013/02/07/2908600.html


def de(f):
    def _call_():
        print "--------------------"
        return f()
    return _call_


@de
def func1():
    print "I am function func1"


@de
def func2():
    print "I am function func2"


if __name__ == '__main__':
    func1()
    func2()
