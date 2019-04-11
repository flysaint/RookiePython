# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:44:57 2019

@author: DELL
Day08
1. 计算重复字母出现的次数
编写一个函数，该函数将返回在输入字符串中出现多次(不同的不区分大小写的)字母字符和
数字的级数。可以假定输入字符串仅包含字母(大写和小写)和数字。

assert(duplicate_count("abcde"), 0)
assert(duplicate_count("abcdea"), 1)
assert(duplicate_count("indivisibility"), 1)
"""
def duplicate_count(text):
    # Your code goes here


'''
2 把0挪到队尾
编写一个算法，该算法采用数组并将所有零移动到最后，保留其他元素的顺序
assert(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,
[],0,1,9,0,0,{},0,0,9]) == ["a","b",None,"c","d",1,False,1,3,[],1,9,
{},9,0,0,0,0,0,0,0,0,0,0])
assert(move_zeros([0,1,None,2,False,1,0]) == [1,None,2,False,1,0,0])
assert(move_zeros(["a","b"]) == ["a","b"])
assert(move_zeros(["a"]) == ["a"])
assert(move_zeros([0,0]) == [0,0])
assert(move_zeros([0]) == [0])
assert(move_zeros([False]) == [False])
assert(move_zeros([]) == [])
'''
# 注意的点 False == 0，因此要注意 len(str(n)) < 5 的判断
def move_zeros(array):
    head=[]
    tail=[]
    for n in chars:
        if n==0 and len(str(n))<5:
            tail.append(n)
            else:
                head.append(n)
                head.extend(tail)
    return head
# sorted排序，关键字是0
def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)

# 高手2 将0移除，在直接依据相差的长度，拼接
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))













