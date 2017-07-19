# -*- coding: utf-8 -*-

import os
import shutil
import xlrd
import string

### 创建多层目录
def mkdirs(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 创建目录操作函数
        os.makedirs(path)
        # 如果不存在则创建目录
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False

def search_file(path, filename, newpath):
    queue = []
    queue.append(path);
    while len(queue) > 0:
        tmp = queue.pop(0)
        if (os.path.isdir(tmp)):
            for item in os.listdir(tmp):
                queue.append(os.path.join(tmp, item))
        elif (os.path.isfile(tmp)):
            name = os.path.basename(tmp)  # 获取文件名
            dirname = os.path.dirname(tmp)  # 获取文件目录
            full_path = os.path.join(dirname, name)  # 将文件名与文件目录连接起来，形成完整路径
            des_path = newpath+'/'+path+'_'+name  #目标路径
            print(name+':::'+filename)
            #if filename in name:
            if(name.find(filename)!=-1):
                shutil.move(full_path, des_path)

if __name__ == '__main__':
    #打开excel文件
    data=xlrd.open_workbook('名单.xlsx')
    #获取第一张工作表（通过索引的方式）
    table=data.sheet_by_index(0)
    #datalist用来存放数据
    datalist_UNIQID=[]
    datalist_NAME=[]
    #将table中第一行的数据读取并添加到data_list中
    datalist_UNIQID.extend(table.col_values(0))
    datalist_NAME.extend(table.col_values(2))
    #foldname = [a+'_'+b for a, b in zip(datalist_UNIQID,datalist_NAME)]
    dir_tjbg='体检报告'
    dir_fsgz='放射工作人员证'
    dir_hbpx='环保系统培训证书'
    dir_ykfs='牙科放射培训'
    #打印出第一行的全部数据
    for index, name in zip(datalist_UNIQID, datalist_NAME):
        foldername=index+'_'+name.strip()
        print(foldername)
        mkdirs(foldername)
        search_file(dir_tjbg,name.strip(),foldername)
        search_file(dir_fsgz,name.strip(),foldername)
        search_file(dir_hbpx,name.strip(),foldername)
        search_file(dir_ykfs,name.strip(),foldername)