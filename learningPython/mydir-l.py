# -*- coding: utf-8 -*-
import os,os.path,stat,string
from datetime import datetime
#利用os模块实现dir -l

def mode_format(mode):
    '''
    获得的st_mode文件权限码其实是linux系统中规定的，
    原来是无符号int类型
    转成八进制，后三位表示文件权限：例如0o400777/0o100666
    第三位上的1表示文件，4表示目录
    :param mode: int
    :return: str
    '''
    trans_dict = {'0': '---', '1': '--x', '2': '-w-', '3': '-wx', '4': 'r--', '5': 'r-x', '6': 'rw-', '7': 'rwx'}
    mode = oct(mode)
    mode_f = ''
    if mode[2] == '4':
        mode_f += 'd'
    else:
        mode_f += '-'
    for i in mode[-3:]:
        mode_f += (trans_dict[i])
    return mode_f

l = [x for x in os.listdir('.')]
#print(l)
for x in l:
    #print(x)
    fileStats = os.stat(x) #返回一个os.stat_result对象
    p=mode_format(fileStats.st_mode)
    #print(oct(fileStats.st_mode))
    #permission = stat.S_IMODE (fileStats.st_mode) # 文件权限
    #p = oct(permission) #返回八进制
    #print(permission)
    iNum = str(fileStats.st_ino) #inode number
    nU = str(fileStats.st_uid)#文件拥有者的用户标识符
    nG = str(fileStats.st_gid) #文件拥有者的组标识符
    fS = str(fileStats.st_size) #文件大小，单位字节
    cT = str(datetime.fromtimestamp(fileStats.st_ctime)) #文件创建时间
    strs = p+' '+iNum +' '+nU +' '+nG+' '+fS+' '+cT+' '+x
    print(strs)

            
