# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 23:31:57 2019

@author: fly_s

Day05
融合多个技巧的文件练习

5-1 搜索文件夹，并统计里面的文件
假设我们有一个目录里面包含若干个文件和子目录：
问题1: 我们要统计该目录下有多少个文件并显示出来(包含子目录)
问题2: 该目录总共的大小可以按M，可以按k显示
问题3：该目录下最大的文件和最小的文件，以及对应的大小
"""


import os
def get_file_size(file):
#判断文件是否存在，存在则取文件大小
    if os.path.exists(file):
        return os.path.getsize(file)
    else:
        return 0
    
def statist_files(path):
    files=[]
    #遍历路径下所有文件，包括子目录 os.walk可以帮助直接递归
    for dirpath,dirnames,filenames in os.walk(path):
        for file_name in filenames:
            files.append(os.path.join(dirpath,file_name))
    #用推到列表，获取每个文件和文件大小
    return [{'name':f,\'size':get_file_size(f)} for f in files]


def count_files_size(files_info,size_display_mode='M'):
    # 计算文件大小，按照K,M,G,Byte分别计算
    sizes=[file_info.get('size',0) for file_info in files_info]
    if size_display_mode=='K' or size_display_mode=='k':
        return str(round(sum(sizes)/1024,3))+'K'
    elif size_display_mode=='M' or size_display_mode=='m':
        return str(round(sum(sizes) / (1024*1024), 3)) + 'M'
    elif size_display_mode=='G' or size_display_mode=='g':
        return str(round(sum(sizes) / (1024 * 1024 *1024), 3)) + 'G'
    else:
        return str(round(sum(sizes)))+'Byte'
    
def get_sorted_files(files):
    #按照文件和大小排序
    sorted_files=sorted(files,key=lambda x:x['size'],reverse=True)
    return sorted_files






