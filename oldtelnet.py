import telnetlib , socket


class TELNET(object):

    def __init__(self):
        self.tn = None
        self.username = "sznari"
        self.password = "a"
        self.host = "222.111.112.9"
        self.port = 23
        self.timeout = 5
        self.login_prompt = b"VxWorks login: "
        self.password_prompt = b"Password: "

    def connect(self):
        try :
            self.tn = telnetlib.Telnet(self.host,self.port,self.timeout)
            self.tn.set_debuglevel(2)
        except socket.timeout :
            print("TELNET.connect() socket.timeout")

        self.tn.read_until(self.login_prompt, self.timeout) 
        self.tn.write(self.username.encode('ascii') + b"\n")

        if self.password :
            self.tn.read_until(self.password_prompt,self.timeout)
            self.tn.write(self.password.encode('ascii') + b"\n")

    def write(self,msg):
        self.tn.write(msg.encode('ascii') + b"\n")
        return True


    def read_until(self,value):
        return self.tn.read_until(value)


    def read_all(self):
        try :
            return self.tn.read_all().decode('ascii')
        except socket.timeout :
            print("read_all socket.timeout")
            return False

    def close(self):
        self.tn.close()
        return True


    def request(self,msg):
        self.__init__()
        self.connect()
        if self.write(msg) == True :
            self.close()
            resp = self.read_all()
            return resp
        else :
            return False
print("begin test")
telnet = TELNET()
#call request function 

resp = telnet.request('ll\n') # it will be return ps output
print(resp)
print("end test")