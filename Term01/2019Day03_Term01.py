# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:39:23 2019
@author: fly_s
Day03
1. 判断时奇数还是偶数
创建一个函数，它以整数作为参数，对偶数返回“偶数”，对奇数返回“奇数”
TestCase:
assert(even_or_odd(2) == "Even")
assert(even_or_odd(0) == "Even")
assert(even_or_odd(7) == "Odd")
assert(even_or_odd(1) == "Odd")
assert(even_or_odd(-1) == "Odd")    
"""
import pandas as pd
import numpy as np
# 菜鸟法
def even_or_odd(num):
    if (np.mod(num,2) == 0):a
        return "Even"
    elif (np.mod(num,2) != 0):
        return "Odd"
# 高手法1
def even_or_odd(num):
    return ["Even","Odd"][num % 2]
# 高手法2
def even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

'''
2. 检查信用卡
给定一个信用卡号码，我们可以通过一些基本知识来确定发行人/供应商是谁。
完成get_issuer() 将下面显示的值的功能来确定给卡号的发卡机构。如果数字不匹配，则该函数应该返回字符串 Unknow
Card       | Type Begins With     | Number Length
AMEX       | 34 or 37             |   15
Discover   | 6011                 |   16
Mastercard | 51, 52, 53, 54 or 55 |   16
VISA       | 4                    |   13 or 16
TestCase:
assert(get_issuer(4111111111111111) == "VISA")
get_issuer(4111111111111) == "VISA"
get_issuer(4012888888881881) == "VISA"
get_issuer(378282246310005) == "AMEX"
get_issuer(6011111111111117) == "Discover"
get_issuer(5105105105105100) == "Mastercard"
get_issuer(5105105105105106) == "Mastercard"
get_issuer(9111111111111111) == "Unknown"
'''
mappings=[
    {'name':'AMEX','Begins':[34,37],"Number Length":15},
    {'name': 'Discover', 'Begins': [6011], "Number Length": 16},
    {'name': 'Mastercard', 'Begins': [51, 52, 53, 54 ,55], "Number Length": 16},
    {'name': 'VISA', 'Begins': [4], "Number Length": [13,16]}
]
def get_issuer(num):
    for mapping in mappings:
        flags=[str(num).startswith(str(x)) for x in mapping['Begins']]
        if any(flags):
            return mapping['name']
    return 'Unknown'
# 高手法1
ISSUERS = {
    ((34, 37), (15,)): 'AMEX',
    ((6011,), (16,)): 'Discover',
    ((51, 52, 53, 54, 55), (16,)): 'Mastercard',
    ((4,), (13, 16)): 'VISA',
}
# 直接 map替换 str。再直接整体 看 tuple是否在里面
def get_issuer(number):
    for (starts,lenghs),issuer in ISSUERS.items():
        # startswith(strs) strs可以放入tuple,里面的元素都可以被识别
        if str(number).startswith(tuple(map(str,starts))) and len(str(number)) in lenghs:
            return issuer
    return 'Unknown'








    
