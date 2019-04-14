# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:52:05 2019
@author: DELL
Day10 翻转一个数字
给定一个数字，写一个函数来输出其反向的数字。例如，给出123答案是321
数字应该保留他们的标志；即翻转时，负数应该仍为负数。
Test.assert_equals(reverse_number(123), 321)
Test.assert_equals(reverse_number(-123), -321)
Test.assert_equals(reverse_number(1000), 1)
Test.assert_equals(reverse_number(4321234), 4321234)
Test.assert_equals(reverse_number(5), 5)
Test.assert_equals(reverse_number(0), 0)
Test.assert_equals(reverse_number(98989898), 89898989)
"""
# 高手1 正数的情况；直接翻转，取整数；负数的情况，把他变成正数，翻转，再加上负号。
def reverse_number(n):
    if n < 0: return -reverse_number(-n)
    return int(str(n)[::-1])
# 高手2 变成正数后翻转，再加上符号
def reverseNumber(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)

'''
2. 检查ip
编写一种算法，以十进制格式识别有效的ipv4地址。如果ip由四个八位字节组成，其值在0和255之间，
则视为有效。该函数的输入保证是单个字符串。
如 
有效:
1.2.3.4
123.45.67.89
无效:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Test.assert_equals(is_valid_IP(''), False)
Test.assert_equals(is_valid_IP('abc.def.ghi.jkl'), False)
Test.assert_equals(is_valid_IP('123.456.789.0'), False)
Test.assert_equals(is_valid_IP('12.34.56'), False)
Test.assert_equals(is_valid_IP('12.34.56 .1'), False)
Test.assert_equals(is_valid_IP('12.34.56.-1'), False)
Test.assert_equals(is_valid_IP('123.045.067.089'), False)
Test.assert_equals(is_valid_IP('127.1.1.0'), True)
Test.assert_equals(is_valid_IP('0.0.0.0'), True)
Test.assert_equals(is_valid_IP('0.34.82.53'), True)
Test.assert_equals(is_valid_IP('192.168.1.300'), False)
'''
ips = '192.168.1.300'
# 高手法 1
def is_valid_IP(ipStr):
    ipList = ipStr.split('.')
    ipsum = sum([1 if ip.isdigit() and 0<= int(ip) <=255 else 0 for ip in ipList])
    return ipsum == 4 
import re
# 高手法2 正则表达式
def is_valid_IP(strng):
    return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?
                         =$)',strng))
# 高手3 使用 socket 模块里面的inet_pton 来检测字符串能否转换成ip地址，然后用异常进行捕获
import socket
def is_valid_IP(addr):
try:
    socket.inet_pton(socket.AF_INET, addr)
    return True
except socket.error:
    return False











