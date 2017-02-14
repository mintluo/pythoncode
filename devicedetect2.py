__author__ = 'admin'

import sys
import telnetlib
import time
from PyQt5 import QtWidgets, QtCore

displayword = [0, 0, 0, 0, 0, 0, 0, 0]
host = {}
host['ip'] = b'222.111.112.9'
host['user'] = b'sznari'
host['password'] = b'a'
host['commands'] = [b'i',b'll']
#print(host['ip'])

class DetectUnit(QtWidgets.QWidget):
    def __init__(self):
        super(DetectUnit,self).__init__()
        #QtWidgets.QWidget.__init__(self, parent)
        #QtWidgets.QMainWindow.__init__(self, parent)
        self.initUI()

    def initUI(self):
        startext = QtWidgets.QPushButton('测试开始', self)                #创建一个按钮
        startext.resize(65, 40)                                        #设置按钮大小
        #self.connect(startext, QtCore.SIGNAL('clicked()'), self.do)
        startext.clicked.connect(self.do)

        self.textEdit = QtWidgets.QTextEdit()                                 #创建一个文本框

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(10)                                        #设置一个表格布局，并设置组件间的间隔是20

        grid.addWidget(startext, 1, 0)
        grid.addWidget(self.textEdit, 1, 1, 5, 1)

        self.setLayout(grid)                                       #设置窗体主布局

        self.setWindowTitle('硬件测试')
        self.resize(450, 300)

    def do(self):
    # print(host['ip'])
        tn = telnetlib.Telnet(host['ip'])
        tn.set_debuglevel(2)

        tn.read_until(b"VxWorks login: ")
        tn.write(host['user']+b"\n")

        tn.read_until(b"Password: ")
        tn.write(host['password']+b"\n")
        time.sleep(5)


        for command in host['commands']:
            tn.read_until(b"-> ")
            tn.write(command+b"\n")

        tn.write(b"exit\n")
        #tn.close()
        time.sleep(3)

        receiveword = str(tn.read_all().decode('ascii'))
        print(receiveword)
"""
        if receiveword.find('Device0 Mdin240 is Ok!') != -1:
            displayword[0]='Device0 Mdin240 is Ok!' + '\r\n'
        elif receiveword.find('Device0 Mdin240 is Fail!') != -1:
            displayword[0]='Device0 Mdin240 is Fail!' + '\r\n'
        else:
            displayword[0]='The Mdin240 test is not success!'+ '\r\n'

        if receiveword.find('Device1 Tlv320aic23b is Ok!') != -1:
            displayword[1]='Device1 Tlv320aic23b is Ok!' + '\r\n'
        elif receiveword.find('Device1 Tlv320aic23b is Fail!') != -1:
            displayword[1]='Device1 Tlv320aic23b is Fail!' + '\r\n'
        else:
            displayword[1]='The Tlv320aic23b test is not success!'+ '\r\n'

        if receiveword.find('Device2 Lm75B is Ok!') != -1:
            displayword[2]='Device2 Lm75B is Ok!' + '\r\n'
        elif receiveword.find('Device2 Lm75B is Fail!') != -1:
            displayword[2]='Device2 Lm75B is Fail!' + '\r\n'
        else:
            displayword[2]='The Lm75B test is not success!'+ '\r\n'

        if receiveword.find('Device3 Tw2867 is Ok!') != -1:
            displayword[3]='Device3 Tw2867 is Ok!' + '\r\n'
        elif receiveword.find('Device3 Tw2867 is Fail!') != -1:
            displayword[3]='Device3 Tw2867 is Fail!' + '\r\n'
        else:
            displayword[3]='The Tw2867 test is not success!'+ '\r\n'

        if receiveword.find('Device4 Cri24C256 is Ok!') != -1:
            displayword[4]='Device4 Cri24C256 is Ok!' + '\r\n'
        elif receiveword.find('Device4 Cri24C256 is Fail!') != -1:
            displayword[4]='Device4 Cri24C256 is Fail!' + '\r\n'
        else:
            displayword[4]='The Cri24C256 test is not success!'+ '\r\n'

        if receiveword.find('Device5 Ds1339 is Ok!') != -1:
            displayword[5]='Device5 Ds1339 is Ok!' + '\r\n'
        elif receiveword.find('Device5 Ds1339 is Fail!') != -1:
            displayword[5]='Device5 Ds1339 is Fail!' + '\r\n'
        else:
            displayword[5]='The Ds1339 test is not success!'+ '\r\n'

        if receiveword.find('Device6 Slave Hi3520 is Ok!') != -1:
            displayword[6]='Device6 Slave Hi3520 is Ok!' + '\r\n'
        elif receiveword.find('Device6 Slave Hi3520 is Fail!') != -1:
            displayword[6]='Device6 Slave Hi3520 is Fail!' + '\r\n'
        else:
            displayword[6]='The Slave Hi3520 test is not success!'+ '\r\n'

        if receiveword.find('Device7 Sil3114 is Ok!') != -1:
            displayword[7]='Device7 Sil3114 is Ok!' + '\r\n'
        elif receiveword.find('Device7 Sil3114 is Fail!') != -1:
            displayword[7]='Device7 Sil3114 is Fail!' + '\r\n'
        else:
            displayword[7]='The Sil3114 test is not success!'+ '\r\n'

        self.textEdit.setText(displayword[0] +displayword[1] + displayword[2] + displayword[3] + displayword[4] +
                              displayword[5] + displayword[6] + displayword[7])"""

            #print('finish!')

app = QtWidgets.QApplication(sys.argv)
ex = DetectUnit()
ex.show()
sys.exit(app.exec_())