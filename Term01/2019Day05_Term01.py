# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 22:57:54 2019
@author: fly_s
Day05
1. 统计元音字母
给定一个字符串，统计里面的元音字母！我们给定的元音列表是 :[a,e,i,o,u]，输入的字符串只会是小写字母或者含有空格
TestCase
assert(getCount("abracadabra") ==  5)
"""
# 解1
def getCount(chars):
    return len([ c for c in chars if c in ['a', 'e', 'i', 'o', 'u' ]])
# 高手法1 巧妙利用sum和生成器的结合。
'''
注意 (1 for let in inputStr if let in "aeiouAEIOU") 其实是一个生成器
什么是生成器？ 一种迭代器
什么是迭代器？ 任何实现了_next_ 的对象 都可以叫做迭代器
迭代器。就是用于迭代操作（for 循环）的对象，它像列表一样可以迭代获取其中的每一个元素，

生成器。用关键字 yield 来返回值，这种函数叫生成器函数，函数被调用时会返回一个生成器对象，生成器本质上还是一个迭代器。

生成器表达式和列表对象
生成器表达式 generator： g = (x*2 for x in range(10))
列表对象 list：l = [x*2 for x in range(10)]
'''
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
# 高手法2
def getCount(s):
    return sum(c in 'aeiou' for c in s)
# 高手法3 正则表达式 findall函数
import re
def getCount(str):
    return len(re.findall('[aeiou]', str, re.IGNORECASE))

'''
2 反转字符串
编写一个函数，它接受一个或多个单词的字符串，其中里面含五个或更多字母单词必须要反转。
传入的字符串只包含字母和空格 。仅当存在多个单词时才会包含空格
TestCase:
assert(spin_words("Welcome") == "emocleW")
assert(spin_words("Hey fellow warriors") == "Hey wollef sroirraw")
assert(spin_words("This is another test") == "This is rehtona test")
'''

# 高手法1
def spin_words(inputStr):
    return ' '.join([s[::-1] if len(s) > 5 else s for s in inputStr.split()])

# 高手法2
import re
def spin_words(sentence):
    return re.sub(r"\w{5,}", lambda w: w.group(0)[::-1], sentence)















