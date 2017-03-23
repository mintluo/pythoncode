#!/usr/bin/python2.7
# -*- coding: utf-8 -*- 
# author: milletluo
# 自动登录邮箱，下载包含关键字和指定日期后的邮件附件
import poplib
import email
import datetime
import time
import os
import xlrd
import xlwt
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

#获取编码方式
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

#邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

#提取文件名，去掉后缀
def GetFileName(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    return shotname

#下载邮件附件
def GetmailAttachment(emailhost,emailuser,emailpass,datestr,keywords,searchnum):
    host = emailhost
    username = emailuser
    password = emailpass
    keywords = keywords   #查询的邮件的主题
    datestr = datestr     #查询的邮件日期

    currentpath=os.getcwd()#获取当前目录
    foldername = datestr+keywords#文件夹名和最后输出文件名
    new_path = os.path.join(currentpath, foldername)#文件存储路径
    if os.path.exists(new_path) == False:#如果文件夹不存在，创建文件夹
        os.makedirs(new_path)

    #for 163mail，user POP3
    # pop_conn = poplib.POP3(host)
    #需要验证的邮件服务
    pop_conn = poplib.POP3_SSL(host)
    # 可选:打印POP3服务器的欢迎文字:
    print(pop_conn.getwelcome())
    # 可以打开或关闭调试信息:
    #pop_conn.set_debuglevel(1)
    pop_conn.user(username)
    pop_conn.pass_(password)
	# stat()返回邮件数量和占用空间:
    print('Messages: %s. Size: %s' % pop_conn.stat())

    num = len(pop_conn.list()[1])  #邮件总数
    if num < int(searchnum):  #当总邮件数目小于searchnum的时候读取所有邮件
        num2 = 0
    else:
        num2 = num-int(searchnum)
    getfilesucess = 0
    #遍历倒数emailnum封邮件
    for i in range(num,num2,-1):
        #poplib.rert('邮件号码')方法返回一个元组:(状态信息,邮件,邮件尺寸)
		#hdr,message,octet=server.retr(1) 读去第一个邮件信息.
		#hdr的内容就是响应信息和邮件大小比如'+OK 12498 octets'
		#message 是包含邮件所有行的列表.
		#octet 是这个邮件的内容.
        resp, lines, octets = pop_conn.retr(i)
        # lines存储了邮件的原始文本的每一行,
        # 可以获得整个邮件的原始文本:
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        # 稍后解析出邮件:
        msg = Parser().parsestr(msg_content)

        subject = msg.get("Subject")
        date1 = time.strptime(msg.get("Date")[0:24],'%a, %d %b %Y %H:%M:%S') #格式化收件时间
        date2 = time.strftime("%Y%m%d", date1)
        #中文邮件的标题和内容都是base64编码的.解码可以使用email.Header 里的decode_header()方法
        subjectnew = decode_str(subject)
        print('MESSAGE%d: %s' % (i,subjectnew))
        print( "=======================================")
        if (date2>=datestr) and (keywords in subjectnew):
            for part in msg.walk():
                filename = part.get_filename()
                contentType = part.get_content_type()
                mycode=part.get_content_charset();
                #不知为何xlsx附件格式为application/octet-stream?
                if filename: #and (contentType == 'application/vnd.ms-excel' or contentType == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
                    data = part.get_payload(decode=True)
                    h = email.Header.Header(filename)
                    dh = email.Header.decode_header(h)
                    fname = dh[0][0]
                    encodeStr = dh[0][1]
                    #保存附件
                    if encodeStr != None:
                        try:
                            fname = fname.decode(encodeStr, mycode)
                            os.chdir(new_path)
                            fEx = open("%s%s"%(date2,fname), 'wb')
                            fEx.write(data)
                            fEx.close()
                            print('MATCHED, DOWNLOAD FILE OK\n')
                            getfilesucess += 1
                        except:
                            print('DECODE FAILED!\n')
                else:
                    print('MATCHED, BUT NO FILE!\n')
                    pass
        else:
            print('NOT MATCH!\n')
    if getfilesucess == 0:
        print('JOB DONE, NO MATCH FILE!')
    else:
        if getfilesucess==1:
            print('THERE ARE ONLY 1 FILE,NOTHING COMBINED!')
        else:
            os.chdir(new_path)
            # 返回一个列表，其中包含在目录条目的名称
            files = os.listdir(new_path)
            outfile = xlwt.Workbook()
            for fname in files:
                sourcefile=GetFileName(fname)
                print(sourcefile)
                print(type(sourcefile))
                data = xlrd.open_workbook(os.path.join(new_path, fname))#打开源表格
                table = data.sheet_by_index(0)#打开源表格sheet
                nrows = table.nrows#源表格数据数目
                newsheet = outfile.add_sheet(sourcefile)#目的表格新增sheet
                #遍历源表格中数据，写入目的表格新增sheet
                for i in range(nrows):
                    for j in range(len(table.row(i))):
                        newsheet.write(i, j,table.row(i)[j].value)
            outname='000'+foldername+'.xls'
            outfile.save(outname)
            print('JOB DONE,%d FILES COMBINED TO %s!' % (getfilesucess,outname))

    pop_conn.quit()

if __name__ == '__main__':
    #emailhost = raw_input('请输入邮箱服务器地址: ')
    emailhost='pop-mail.outlook.com'
    #emailuser = raw_input('请输入邮箱地址: ')
    emailuser='lm409@hotmail.com'
    #emailpass = raw_input('请输入邮箱密码: ')
    emailpass='07156517162lm'
    datestr = raw_input('Please input the STARTDATE(eg:20170401): ')
    keywords = raw_input('Please input the KEYWORD: ').decode('gbk')
    searchnum = raw_input('Please input the SEARCHNUM: ')
    GetmailAttachment(emailhost,emailuser,emailpass,datestr,keywords,searchnum)
