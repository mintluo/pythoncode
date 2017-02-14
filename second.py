from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox,QInputDialog,QLineEdit
from main import Ui_Form
import sys,time

class mynewShow(QtWidgets.QWidget,Ui_Form):
    _signal=QtCore.pyqtSignal(str)
    def __init__(self):
        super(mynewShow,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.prn)
        self._signal.connect(self.mynewslot)
    def prn(self):
        print("print test!")
        time.sleep(1)
        print("delay 1s")
        self._signal.emit("This is slot!")
    def mynewslot(self,parameter):
        self.msg()
    #def msg(self):
     #   OK=QMessageBox.warning(self,("title"),("""message"""),QMessageBox.StandardButtons(QMessageBox.Yes|QMessageBox.No))
    def msg(self):
        result,ok=QInputDialog.getText(self,("title"),("message"),QLineEdit.Normal,("默认文字"))
        print(result,ok)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = mynewShow()
    ui.show()
    sys.exit(app.exec_())