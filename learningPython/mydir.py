# -*- coding: utf-8 -*-
#能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件
#并打印出相对路径
import os

def findfile(name):
    for root,dirs,files in os.walk('.'):
        for f in files:
            x=os.path.split(f)[1]
            if name in x:
                print(os.path.join(root,f))

if __name__=='__main__':
    str_search = input('输入要查找的字符串:')
    findfile(str_search)

            
