# coding=utf-8
import poplib
import cStringIO
import email
import base64
import datetime
import time
#import xlrd
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from email import parser
import sys
reload(sys)
sys.setdefaultencoding('gbk')

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value
#########下载邮件附件
def GetmailAttachment(emailhost,emailuser,emailpass,datestr,keywords):
    host = emailhost
    username = emailuser
    password = emailpass
    keywords = keywords   #查询的邮件的主题
    datestr = datestr     #查询的邮件日期


    #for 163mail，user POP3 ########
    # pop_conn = poplib.POP3(host)
    #需要验证的邮件服务
    pop_conn = poplib.POP3_SSL(host)
    pop_conn.set_debuglevel(1)


    pop_conn.user(username)
    pop_conn.pass_(password)

    num = len(pop_conn.list()[1])  #邮件总数
    if num < 10:  #当总邮件数目小于50的时候读取所有邮件
        num2 = 0
    else:
        num2 = num-10

    getfilesuss = 0
    for i in range(num,num2,-1):
        m = pop_conn.retr(i)
        buf = cStringIO.StringIO()
        #print(m)
        #将j存入buf
        for j in m[1]:
            print >> buf,j
        #从文件开头开始算起
        buf.seek(0)
        msg = email.message_from_file(buf)
        #print(msg)
        subject = msg.get("Subject")
        date1 = time.strptime(msg.get("Date")[0:24],'%a, %d %b %Y %H:%M:%S') #格式化收件时间
        date2 = time.strftime("%Y%m%d", date1)
        #print(float(time.mktime(date2)))
        print(date2)
        #     print date2,subject
        subjectnew = decode_str(subject)
        #subjectnew = subject.split('?gb2312?B?')  #gb2312编码邮件的解码
        print(subjectnew)
        print(keywords)
        print( "=======================================")
        if (date2>=datestr) and (keywords in subjectnew):
            for part in msg.walk():
                filename = part.get_filename()
                contentType = part.get_content_type()
                mycode=part.get_content_charset();
                print(filename)
                print(contentType)
                print( "---------------------------------------")
                #不知为何附件格式为application/octet-stream
                if filename: #and (contentType == 'application/vnd.ms-excel' or contentType == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
                    data = part.get_payload(decode=True)
                    h = email.Header.Header(filename)
                    dh = email.Header.decode_header(h)
                    fname = dh[0][0]
                    encodeStr = dh[0][1]
                    if encodeStr != None:
                        fname = fname.decode(encodeStr, mycode)
                    #end if
                    fEx = open("%s"%(fname), 'wb')
                    fEx.write(data)
                    fEx.close()
                    print '文件下载成功'
                    getfilesuss += 1
                    #return fEx.name
                else:
                    pass
            #break
    if getfilesuss == 0:
        print '未找到符合条件的邮件'

    pop_conn.quit()

mail=GetmailAttachment('pop-mail.outlook.com','lm409@hotmail.com','07156517162lm','20170319','test')
