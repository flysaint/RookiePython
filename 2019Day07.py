# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 23:47:43 2019

@author: fly_s

Day07
1. 来排个序
对给定字符串排序。字符串中每个单词都包含一个数字。此数字是单词在在结果中应该具有位置。
注意：数字可以是1到9，因此1将是第一个单词(不是0).
example:
"is2 Thi1s T4est 3a" --> "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2" --> "Fo1r the2 g3ood 4of th5e pe6ople"
testcase:
assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est", "Oops! it don't like right."
assert order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople", "Oops! it don't like right."
assert order("") == "","Oops! it don't like right."
"""
import re
# 菜鸟法
def order(text):
    if len(text)==0:return ""
    # 先将text截取成字符串组
    str_list = text.split()
    # 将个字符串组中的数值找出来。
    num_list = [re.sub('[^\d+]','',num)  for num in str_list]
    # 组成 dict键值对，然后使用数值作为key，进行sort排序
    sort_list = sorted(zip(num_list,str_list),key = lambda x:x[0])
    # 利用字符串组和字符串数值，
    new_list = [t[1] for t in  sort_list]
    return (' '.join(new_list))
'''
# 高手法1 这个非常巧妙，利用数字和字母组合的字符串，又一个技巧，数字总是排序在字母前面
s='1ad9'
print (sorted(s))
>>['1', '9', 'a', 'd']
为啥数字排序在字母前面，因为1和字母的ascii的码，数字的小，字母的大
print ({c:ord(c) for c in s})
>>{'1': 49, 'a': 97, 'd': 100, '9': 57}
'''
def order(words):
    return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

# 高手法2 这个通俗点，把key里面原来用lambda 写的改成了 extract_number函数 
def extract_number(word):
    for l in word:
        if l.isdigit(): return int(l)
    return None
def order(sentence):
    return ' '.join(sorted(sentence.split(), key=extract_number))


























