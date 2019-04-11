# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 23:52:11 2019
@author: fly_s
Day02
1. 求表达式中的正数的和

得到一组数字，返回所有正数的和
[1,-4,7,12] => 1 + 7 + 12 = 20
TestCase:

assert (positive_sum([1,2,3,4,5]),15)
assert (positive_sum([1,-2,3,4,5]),13)
assert (positive_sum([-1,2,3,4,-5]),9)    
    
"""
numlist = [1,-2,3,4,5]
def positive_sum(numlist):
    sum([num for num in numlist if num > 0 ])
    
"""
2. 拼接字符
根据下面的表达设计一个函数：
accum("abcd") -> "A-Bb-Ccc-Dddd" 
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"


assert (accum("ZpglnRxqenU"), "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
assert (accum("NyffsGeyylB"), "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
assert (accum("MjtkuBovqrU"), "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
assert (accum("EvidjUnokmM"), "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
assert (accum("HbideVbxncC"), "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")
"""
testStr = "ZpglnRxqenU"
# 高手法1
# enumerate 能够同for 循环 将 下标 和 具体的值一起读取出来
def accum(words):
    res=[c*(index+1) for index,c in enumerate(words)]
    return '-'.join(map(lambda x:x.capitalize(),res))

# 高手法2
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


s = 'ZpglnRxqenU'


for i, c in enumerate(s):
    print('i = {} , c = {}'.format(i,c))





