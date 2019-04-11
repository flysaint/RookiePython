# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:09:46 2019
@author: fly_s

Day09
1. 创建一个电话号码
编写一个接受10个整数(0到9之间)数组的函数，它以电话号码的形式返回这些数字的字符串。
TestCase:
Test.describe("Basic tests")
Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123)456-7890")
Test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111)111-1111")
Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123)456-7890")
Test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023)056-0890")
Test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000)000-0000")

"""
# 解法2 {} 配合 format
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# 解法3 % 的用法
def create_phone_number(n):
    n = ''.join(map(str,n))
    #return '(%s)%s-%s'%(n[:3], n[3:6], n[6:])
    return '({}){}-{}'.format(n[:3], n[3:6], n[6:])

'''
2. 人性化的可读性时间
编写以一个函数，它以非负整数(秒)作为输入，并以人类可读的格式返回时间(HH:MM:SS)
HH = 小时，填充到2位数，范围:00 - 99
MM = 分钟， 填充到2位数，范围：00 - 59
SS = 秒， 填充到2位数，范围：00 - 59
最长时间永远不会超过 359999(99:59:59)
Test.assert_equals(make_readable(0), "00:00:00")
Test.assert_equals(make_readable(5), "00:00:05")
Test.assert_equals(make_readable(60), "00:01:00")
Test.assert_equals(make_readable(86399), "23:59:59")
Test.assert_equals(make_readable(359999), "99:59:59")
'''
import numpy as np

# 高手1 {:02} format 保留两位
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(int(s / 3600), int(s / 60 % 60), s % 60)

# 高手2   %02d: 保留两位
def make_readable(seconds):
    h= seconds/3600
    m= (seconds/60 % 60)
    s= (seconds%60)
    return "%02d:%02d:%02d" % (h, m, s)












