# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 22:22:00 2019
@author: fly_s
Day04
1. 未使用的最小id
需要管理大量数据，使用以零为基础和非负ID来使每个数据项都是唯一的！
因此，需要一个方法来计算下一个新数据返回最小的使用ID
注意：给定已使用的ID数组可能未排序。出于测试原因，可能存在重复的ID，但你无需查找或删除它们！
TestCase:
assert (next_id([0,1,2,3,4,5,6,7,8,9,10]) == 11)
assert (next_id([5,4,3,2,1]) == 0)
assert (next_id([0,1,2,3,5]) == 4)
assert (next_id([0,0,0,0,0,0]) == 1)
assert (next_id([]) == 0)
"""
testNums = [0,1,2,3,4,5,6,7,8,9,10]

def next_id(testNums):
    if  not testNums or len(testNums) == 0:
        return 0
    nextId = [i for i in range(0,max(testNums) + 2) if i not in testNums]
    return nextId[0]
# 高手1 累加遍历  
def next_id(arr):
    t = 0
    while t in arr:
        t +=1
    return t
# 高手2 
from functools import reduce
def next_id(arr):
    '''
    reduce 函数用法  reduce(function, iterable[, initializer]) 
    function -- 函数，有两个参数
    iterable -- 可迭代对象
    initializer -- 可选，初始参数
    案例：reduce(lambda x, y: x+y, [1,2,3,4,5])  # 累加
    '''
    return reduce(lambda acc, x: acc + 1 if x == acc else acc, sorted(arr), 0)

'''
2. 获得中间字符
你会得到一个字符串，你需要写一个函数返回单词的中间字符。如果单词的长度为奇数，则返回中间字符。如果单词的长度是偶数，则返回中间2个字符
assert(get_middle("test") == "es")
assert(get_middle("testing")== "t")
assert(get_middle("middle")== "dd")
assert(get_middle("A") == "A")
assert(get_middle("of") == "of")
'''
import pandas as pd
import numpy as np

def get_middle(s):
#your code here
    slen = len(s)
    if np.mod(slen,2) == 0:
        return s[int(slen/2 - 1):int(slen/2 + 1)]
    else:
        return s[int(slen/2)]
    
# 高手解法
def get_middle(s):
    return s[(len(s)-1)/2:len(s)/2+1]        







































