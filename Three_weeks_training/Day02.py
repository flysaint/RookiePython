# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 23:58:16 2019

@author: fly_s
题目：寻找班级里面名字最长的人
有一串人名：
names=(' Kunpen Ji, Li XIAO, Caron Li, Donl SHI, Ji ZHAO,Fia YUAN Y, Weue
DING, Xiu XU, Haiying WANG, Hai LIN,Jey JIANG, Joson WANG E, Aiyang ZHANG,Hay
MENG, Jak ZHANG E, Chang Zhang, Coro ZHANG')
希望做到：
问题1 排序。按照名字 A-Z排序
问题2 找出里面姓“ZHANG”有几个
问题3 找出名字里面最长的人
"""

names=(' Kunpen Ji, Li XIAO, Caron Li, Donl SHI, Ji ZHAO,Fia YUAN Y, Weue DING, \
       Xiu XU, Haiying WANG, Hai LIN,Jey JIANG, Joson WANG E, Aiyang ZHANG,Hay \
       MENG, Jak ZHANG E, Chang Zhang, Coro ZHANG')

def sort_name(names):
    return sorted([name.trip(" ") for name in names.split(",")])


def find_name(names,sub = 'ZHANG'):
    for name in names.split(','):
        print('name = {}'.format(name))
        if str('ZHANG') in (name.upper()):
            return name


