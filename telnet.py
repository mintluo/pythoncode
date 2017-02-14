__author__ = 'admin'

import sys
import telnetlib
import time

HOST = b"222.111.112.9"
USER = b"sznari"
PASS = b"a"
cmd = b"ll"  #
tn = telnetlib.Telnet(HOST)
tn.set_debuglevel(2)
print("begin test")
#
tn.read_until(b"VxWorks login: ")
#
tn.write(USER + b"\n")
# print("login success");
#
tn.read_until(b"Password: ")
tn.write(PASS + b"\n")
# print("password success");
# �ж��Ƿ�ɹ���½����
#tn.read_until(b"Microsoft Telnet Server")
# ������������Ӧ��DOS������
tn.read_until(b"-> ")
tn.write(cmd + b"\n")
tn.read_until(b"-> ")
tn.write(b"i\n")

# print("cmd success");
tn.read_until(b"-> ")
tn.write(b"exit\n")
time.sleep(3)
# ��ȡ��ƥ�䵽������
print("print tn")
#print(tn.read_all().decode('ascii'))
receiveword = str(tn.read_all().decode('ascii'))
print(receiveword)
#time.sleep(3)
#receiveword = str(tn.read_all().decode('ascii'))
#print(receiveword)
tn.close()
print("end test")