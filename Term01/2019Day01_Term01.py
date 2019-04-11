# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 23:04:54 2019
@author: fly_s
1. 有序字符数
计算每个字符串的出现次数，并按照出现的顺序将其作为元组列表返回。
例如给你一个字符串"abracadabra"，统计里面的字符按照下面的格式输出：
TestCase:
ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d',1)]
ordered_count("Code Wars") == [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1),
('a', 1), ('r', 1), ('s', 1)]
"""
# 高手解题法1
import re
from collections import OrderedDict

def ordered_count(input):
    counts = OrderedDict()
    for char in input:
        counts[char] = counts.get(char, 0) + 1
    return list(counts.items())


from collections import Counter
def ordered_count(input):
    return list(Counter(input).items())

'''
2. 缩写双字名称
编写一个函数将名称转化为首字母。这个kata严格地用两个词，它们之间有一个空格。
输出应该是两个大写字母，并用点分隔它们。
它应该如下所示：
Sam Harris` => `S.H
Patrick Feeney` => `P.F
TestCase:
    
def abbrevName(name):
#your code
    Test.assert_equals(abbrevName("Sam Harris"), "S.H");
    Test.assert_equals(abbrevName("Patrick Feenan"), "P.F");
    Test.assert_equals(abbrevName("Evan Cole"), "E.C");
    Test.assert_equals(abbrevName("P Favuzzi"), "P.F");
    Test.assert_equals(abbrevName("David Mendieta"), "D.M");
'''
# 菜鸟法
def abbrevName(testStr):
    '.'.join([word[0].upper() for word in testStr.split()])

# 高手法a
abbrevName = lambda name: ".".join(e[0].upper() for e in name.split())
