# -*- coding:utf-8 -*-
"""函数修饰符，含不同参数"""
import sys
import traceback


def de(f):
    def _call_(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            print "param type error"
    return _call_


@de
def func1(lst1, lst2):
    for item in lst1 + lst2:
        print item


@de
def func2(dic):
    for k, v in dic.items():
        print k, v


if __name__ == "__main__":
    func1([1, 2], [3, 4])
    func2([1, 2])  # param type error
