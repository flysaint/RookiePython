# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 23:38:14 2019

@author: fly_s

Day01
字符串趣味实战
1-1 替换 1-20内的数字，3的倍数和5的倍数用不同的数字替代
列出1~20的数字，若是3的倍数就用apple代替，若是5的倍数就用orange替代，
若既是3的倍数又是5的倍数，就用appleorange代替。

思考
利用
testStr[len(testStr)::] 返回testStr本身
因此
testStr[i%num*len(testStr)::] 在i是num整数时，就输出原字符串
"""

for i in range(1,21):
    print('apple'[i%3*len('apple')::]+'orange'[i%5*len('orange')::]or i)
    
    
