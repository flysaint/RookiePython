# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 23:46:26 2019

@author: fly_s

Day06 异常处理
在python程序中，分别使用未定义变量，访问列表不存在的索引、访问字典不存在的关键字观察系统提示的错误信息
"""

# 6-1 通过Py't'hon程序产生 IndexError，并用try捕获异常
try:
    b = ['a', 'b', 'c']
    b[3]
except IndexError:
    print('列表不存在索引')

# 6-2 模拟计算机
import re
def verify_num(n):
    #用正则判断几种数字，正数，负数，小数点数字
    patt=re.compile(r'^(-?\d+)(\.\d+)?$')
    return True if re.match(patt,n) else False

def verify_opt(opt):
    # 判断运算符号
    return opt in ['+','-','*','/']

def mini_calculator():
    #用户输入数据
    my_input=input('Please two nums and operation,such as 1,2,+:\n')
    try:
        args=my_input.split(',')
        if len(args)==3:
            a,b,opt=args
            if not verify_num(str(a)) or not verify_num(str(b)) or not \
            verify_opt(opt):
                print ('Input format is incorrect!')
                return
    #拼接表达式，然后用eval进行求解表达式值
            res=eval('{}{}{}'.format(a,opt,b))
            print ('{}{}{}={}'.format(a,opt,b,res))
        else:
            print ('Args len should be 3!')
    except ValueError as e:
        print ('Value error',e)
    except Exception as e:
        print (e)
        
        
        
        
        
        
        
        
        
        
        
        