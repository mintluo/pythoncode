#!/usr/bin/python2
# -*- coding: utf-8 -*-
# author: milletluo
# 自动登录邮箱，下载包含关键字和指定日期后的邮件附件

import os
import xlrd
import xlwt

def combinxls():
    new_path='C:\\autotelnet1'
    foldername='test.xls'
    os.chdir(new_path)
    # 返回一个列表，其中包含在目录条目的名称
    files = os.listdir(new_path)
    outfile = xlwt.Workbook()
    for fname in files:
        data = xlrd.open_workbook(os.path.join(new_path, fname))#打开源表格
        table = data.sheet_by_index(0)#打开源表格sheet
        nrows = table.nrows#源表格数据数目
        newsheet = outfile.add_sheet(fname)#目的表格新增sheet
        for i in range(nrows):
            for j in range(len(table.row(i))):
                newsheet.write(i, j,table.row(i)[j].value)
    outfile.save(foldername)
    print('JOB DONE, FILES COMBINED!' )

if __name__ == '__main__':
    combinxls()
    #foldername='test.xls'
    #outfile = xlwt.Workbook()
    #newsheet = outfile.add_sheet('fname')
    #outfile.save(foldername)
