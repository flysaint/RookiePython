# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:26:35 2019
@author: DELL
Day11
1.用函数计算
这次我们想用函数编写计算并得到结果。我们来看一些例子
Test.describe('Basic Tests')
Test.assert_equals(seven(times(five())), 35)
Test.assert_equals(four(plus(nine())), 13)
Test.assert_equals(eight(minus(three())), 5)
Test.assert_equals(six(divided_by(two())), 3)
"""
testStr = 'seven(times(five())'
# 高手1 匿名函数 None的用法。
def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)
def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda x: x*y
def divided_by(y): return lambda x: x/y

# 高手2 先构造表达式，然后利用 eval来求治，很简洁。eval执行字符串表达式
def zero(arg=""): return eval("0" + arg)
def one(arg=""): return eval("1" + arg)
def two(arg=""): return "2" + arg
def three(arg=""): return eval("3" + arg)
def four(arg=""): return eval("4" + arg)
def five(arg=""): return eval("5" + arg)
def six(arg=""): return eval("6" + arg)
def seven(arg=""): return eval("7" + arg)
def eight(arg=""): return eval("8" + arg)
def nine(arg=""): return eval("9" + arg)
def plus(n): return "+%s" % n
def minus(n): return "-%s" % n
def times(n): return "*%s" % n
def divided_by(n): return "/%s" % n
