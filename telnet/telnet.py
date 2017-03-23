# -*- coding: utf-8 -*-
# author: caohp
# 自动登录telnet，同时收集装置相关信息

import time
import telnetlib

def my_telnet(Host,Commands,Filepath):

    f=open(Filepath,'a+')
    tn=telnetlib.Telnet(Host,port=23,timeout=10)

    tn.read_until(b'ogin:',timeout=2)
    tn.write(b'sznari'+b'\n')
    tn.read_until(b'assword:',timeout=2)
    tn.write(b'a'+b'\n')
    tn.read_until(b'->',timeout=2)

    print('信息收集中，请等待......')
    for x in range(3):
        for command in Commands:
            byte_command=command.encode(encoding="utf-8")
            tn.write(b'%s\n' %byte_command)
            #f.write(str(tn.read_until(b'->',timeout=5)+b'\n'))
            receiveword=(tn.read_until(b'->',timeout=5)).decode('utf-8')
            print(receiveword)

    tn.write(b'exit'+b'\n')
    f.close()


if __name__=='__main__':
    #Host=input('请输入装置IP（如192.168.253.3）：')
    Host=b'222.111.112.122'
    #filename=input('请为需要保存的文件命名（如001.txt）：')
    filename='test.txt'
    Filepath='D:/'+filename
    Commands=['version','netstat']
    print('装置连接中，请等待......')
    my_telnet(Host,Commands,Filepath)
    print('信息收集完成，文件保存路径为：%s' %Filepath)
    print('10s后窗口将自动关闭！')
    time.sleep(10)
