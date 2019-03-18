# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 23:52:51 2019
@author: fly_s
Day06
1.找到大写字母
写一个函数 capitals() 给你一串字符串，找到里面的大写字母，并返回它们的index
TestCase
assert( capitals('CodEWaRs') == [0,3,4,6] )
"""
# 高手1
def capitals(words):
    return [i  for i,word in enumerate(words) if word.isupper()]
# 高手2
def capitals(words):
    return [i for i in range(len(words)) if words[i].isupper() ]
'''
# 2. 递归数字总和
遍历数字从个位数，十位，百位... 以此相加计算总和。则以这种方式继续减少，
直到只剩下一位数字。这仅适用于自然数，比如
digital_root(493193)
'''
def digital_root(num):
    numStr = str(num)
    while len(numStr) > 1:
        numStr = str(sum([int(n) for n in numStr]))   
    return numStr
#高手法1 
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
#高手2
def digital_root(n):
    while n > 9:
        n = sum(map(int,str(n)))
    return n













