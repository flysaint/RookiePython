# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 23:58:10 2019

@author: fly_s
day03
题目 九宫格
九宫格中，有横竖3个格子。在每行的数字不同的情况下，让每行每列，及对对角线上的三数之和等于15
1~9数字，很

思路1
暴力解法
从1~9挑出3个数字，共有9*8*7 = 504种
然后从504种中抽取，让行列对角线都等于15

创建数组，先保证数组之和等于15
"""
arr_out = []
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            arr_inner = []
            arr_inner.append(i)
            arr_inner.append(j)
            arr_inner.append(k)
            if sum(arr_inner) == 15:
                arr_out.append(arr_inner)
                
nine_glax_out = []
for arr1 in arr_out:
    for arr2 in arr_out:
        for arr3 in arr_out:
            if (arr1[0] + arr2[0] + arr3[0] == 15 and arr1[1] + arr2[1] + arr3[1] == 15 \
            and arr1[2] + arr2[2] + arr3[2] == 15 and arr1[0] + arr2[1] + arr3[2] == 15 \
            and arr1[2] + arr2[1] + arr3[0] == 15):
                nine_glax = []
                nine_glax.append(arr1)
                nine_glax.append(arr2)
                nine_glax.append(arr3)
                nine_glax_out.append(nine_glax)
    


'''
高手
Step1 获取1~9的全排列
Python 标准库有一个赫赫有名的模块叫做 itertools
里面提供了很多迭代函数
比如permutations，可以方便的全排列序列中的数字，每一个组合都是3个数字，
比如 S1(1,2,3),S2(1,5,8)，这样我们得到一个长的列表 [S1,S2..Sn]

Step2 列出3*3的矩阵
每一行都是48个中选1个，那么3行

Step3 计算行列斜对角线都是15

Step4
过滤重复矩阵
1 9 5
9 5 1
5 1 9
我们希望过滤掉
保证他们没有交集
if(len(set(row1)&set(row2)) == 0)
'''

import itertools
def jiuGongge():
#step1
#琼剧
nums=[x for x in range(1,10)]
seq_3nums=[p for p in itertools.permutations(nums,3)]
#􁬦􁄁􀚊􀞾􁒵􀔭15
seq_3nums=[p for p in itertools.permutations(nums,3) if sum(p)==15]
# print (seq_3nums)
#step2:􀵤􁔱􁤈􀒅􀚜􀒅􀩒􁥯􀒅􀷑􀩒􁥯􀒅􀓾􁕚􀣐􀔅15
matrix=[]
for row1_1,row1_2,row1_3 in seq_3nums:






























