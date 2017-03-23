import getpass
import time
import telnetlib

HOST = "222.111.112.9"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)
#tn.set_debuglevel(2)
tn.read_until(b"VxWorks login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
tn.read_until(b"-> ")
tn.write(b"ll\n")
tn.read_until(b"-> ")
tn.write(b"i\n")
#tn.read_until(b"-> ")
tn.write(b"exit\n")
time.sleep(3)
print("begin print")
print(tn.read_some().decode('ascii'))
print("end test")