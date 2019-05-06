# -*- coding: utf-8 -*-
"""
Created on Tue May  7 00:46:01 2019

@author: fly_s
Day08 
时间处理
写一个生日提醒小程序
1. 计算你的生日比如，近20年来(1990-2019)，每年的生日是星期几，统计下星期几出现的次数比较多
2. 生日提醒。距离生日还有几天
3. 计算你和你老婆或者女朋友的生日差多少天

关键是用好 time,datetime,calendar三个库
"""

def get_birthday_weekday(birthday_str):
    weekday=datetime.strptime(birthday_str,'%Y-%m-%d').weekday()
    weekdays=['Mon','Tue','Wes','Thur','Fri','Sat','Sun']
    return weekdays[weekday]

def internal_days(name,your_birthday):
    try:
        birthday=datetime.strptime(your_birthday, '%Y-%m-%d')
        delta_days=(birthday-datetime.today()).days
        if delta_days>0:
            return (f'{name} {delta_days}')
        elif delta_days<0:
            return (f'􁪗{name} {abs(delta_days)}')
        else:
            return (f'{name}!')
    except ValueError as e:
        print ('Please input the birthday format as :1991-2-3')
        
def statist_birthday():
    birthday_list=[str(y)+'-1-1' for y in range(1990,2020)]
    res=[]
    for b in birthday_list:
        res.append(get_birthday_weekday(b))
    print (Counter(res))