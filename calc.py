
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(428, 494)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.values=['']
        self.operators=[]
        self.V_r_n=0
        self.V_r_o=-1
        
        self._0 = QtWidgets.QPushButton(self.centralwidget)
        self._0.setGeometry(QtCore.QRect(100, 380, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._0.setFont(font)
        self._0.setObjectName("_0")
        self._0.clicked.connect(self.b_0)
        # self._0.setStyleSheet("background:red ; color:white")
        
        self._1 = QtWidgets.QPushButton(self.centralwidget)
        self._1.setGeometry(QtCore.QRect(20, 300, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._1.setFont(font)
        self._1.setObjectName("_1")
        # self._1.clicked.connect(self.button_number)
        self._1.clicked.connect(self.b_1)

        self._2 = QtWidgets.QPushButton(self.centralwidget)
        self._2.setGeometry(QtCore.QRect(100, 300, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._2.setFont(font)
        self._2.setObjectName("_2")
        self._2.clicked.connect(self.b_2)
        
        self._3 = QtWidgets.QPushButton(self.centralwidget)
        self._3.setGeometry(QtCore.QRect(180, 300, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._3.setFont(font)
        self._3.setObjectName("_3")
        self._3.clicked.connect(self.b_3)
        
        self._4 = QtWidgets.QPushButton(self.centralwidget)
        self._4.setGeometry(QtCore.QRect(20, 220, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._4.setFont(font)
        self._4.setObjectName("_4")
        self._4.clicked.connect(self.b_4)
        
        self._5 = QtWidgets.QPushButton(self.centralwidget)
        self._5.setGeometry(QtCore.QRect(100, 220, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._5.setFont(font)
        self._5.setObjectName("_5")
        self._5.clicked.connect(self.b_5)
        
        self._6 = QtWidgets.QPushButton(self.centralwidget)
        self._6.setGeometry(QtCore.QRect(180, 220, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._6.setFont(font)
        self._6.setObjectName("_6")
        self._6.clicked.connect(self.b_6)
        
        self._7 = QtWidgets.QPushButton(self.centralwidget)
        self._7.setGeometry(QtCore.QRect(20, 140, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._7.setFont(font)
        self._7.setObjectName("_7")
        self._7.clicked.connect(self.b_7)
        
        self._8 = QtWidgets.QPushButton(self.centralwidget)
        self._8.setGeometry(QtCore.QRect(100, 140, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._8.setFont(font)
        self._8.setObjectName("_8")
        self._8.clicked.connect(self.b_8)
        
        self._9 = QtWidgets.QPushButton(self.centralwidget)
        self._9.setGeometry(QtCore.QRect(180, 140, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._9.setFont(font)
        self._9.setObjectName("_9")
        self._9.clicked.connect(self.b_9)
        
        self._00 = QtWidgets.QPushButton(self.centralwidget)
        self._00.setGeometry(QtCore.QRect(180, 380, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._00.setFont(font)
        self._00.setObjectName("_00")
        self._00.clicked.connect(self.b_00)
        
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 380, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        
        self._on = QtWidgets.QPushButton(self.centralwidget)
        self._on.setGeometry(QtCore.QRect(340, 220, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._on.setFont(font)
        self._on.setObjectName("_on")
        self._on.clicked.connect(self.b_on)
        
        self._x = QtWidgets.QPushButton(self.centralwidget)
        self._x.setGeometry(QtCore.QRect(260, 220, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._x.setFont(font)
        self._x.setObjectName("_x")
        self._x.clicked.connect(self.b_x)
        
        self._minus = QtWidgets.QPushButton(self.centralwidget)
        self._minus.setGeometry(QtCore.QRect(340, 300, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._minus.setFont(font)
        self._minus.setObjectName("_minus")
        self._minus.clicked.connect(self.b_minus)
        
        self._plus = QtWidgets.QPushButton(self.centralwidget)
        self._plus.setGeometry(QtCore.QRect(260, 300, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._plus.setFont(font)
        self._plus.setObjectName("_plus")
        self._plus.clicked.connect(self.b_plus)
        
        self._equall = QtWidgets.QPushButton(self.centralwidget)
        self._equall.setGeometry(QtCore.QRect(260, 380, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._equall.setFont(font)
        self._equall.setObjectName("_equall")
        self._equall.clicked.connect(self.b_equall)
        
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(15, 17, 400, 99))
        self.label2.setStyleSheet("background:balck")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 19, 391, 91))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color:white")
        
        self._ac = QtWidgets.QPushButton(self.centralwidget)
        self._ac.setGeometry(QtCore.QRect(260, 140, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._ac.setFont(font)
        self._ac.setObjectName("_ac")
        self._ac.clicked.connect(self.button_ac)
        self._ac.setStyleSheet("color:red")
        
        
        self._mod = QtWidgets.QPushButton(self.centralwidget)
        self._mod.setGeometry(QtCore.QRect(340, 140, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._mod.setFont(font)
        self._mod.setObjectName("_mod")
        self._mod.clicked.connect(self.b_mod)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 428, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "basil"))
        self._7.setText(_translate("MainWindow", "7"))
        self._8.setText(_translate("MainWindow", "8"))
        self._ac.setText(_translate("MainWindow", "ac"))
        self._9.setText(_translate("MainWindow", "9"))
        self._mod.setText(_translate("MainWindow", "%"))
        self._5.setText(_translate("MainWindow", "5"))
        self._4.setText(_translate("MainWindow", "4"))
        self._on.setText(_translate("MainWindow", "/"))
        self._6.setText(_translate("MainWindow", "6"))
        self._x.setText(_translate("MainWindow", "*"))
        self._2.setText(_translate("MainWindow", "2"))
        self._0.setText(_translate("MainWindow", "0"))
        self._equall.setText(_translate("MainWindow", "="))
        self._1.setText(_translate("MainWindow", "1"))
        self._minus.setText(_translate("MainWindow", "-"))
        self._3.setText(_translate("MainWindow", "3"))
        self._00.setText(_translate("MainWindow", "."))
        self._plus.setText(_translate("MainWindow", "+"))
        # self.label.setText(_translate("MainWindow", "enter"))
    
    def b_0(self):
        return self.button_number(0)
    def b_1(self):
        return self.button_number(1)
    def b_2(self):
        return self.button_number(2)
    def b_3(self):
        return self.button_number(3)
    def b_4(self):
        return self.button_number(4)
    def b_5(self):
        return self.button_number(5)
    def b_6(self):
        return self.button_number(6)
    def b_7(self):
        return self.button_number(6)
    def b_7(self):
        return self.button_number(7)
    def b_8(self):
        return self.button_number(8)
    def b_9(self):
        return self.button_number(9)
    def b_00(self):
        if "." not in self.values[self.V_r_n]:
            return self.button_number('.')
    def button_number(self,b_):        
        button_click=f"{b_}"
        if len(self.values)<self.V_r_n+1:
            self.values.append('') 
        self.values[self.V_r_n]+=f'{button_click}'
        self.updata_label(b_)
        print(self.values)
        print(self.operators)
        print(self.V_r_n)
        print(self.V_r_o)

    def b_on(self):
        return self.operation_b('/')
    def b_x(self):
        return self.operation_b('*')
    def b_plus(self):
        return self.operation_b('+')
    def b_minus(self):
        return self.operation_b('-')
    def b_mod(self):
        return self.operation_b('%')
    def operation_b(self,_b):
        se = ['/','*','-','+','%']
        if(self.label.text()[len(self.label.text())-1] in se ):
            self.operators[self.V_r_o]=_b
            self.label.setText(self.label.text()[:-1]+_b)
        elif self.V_r_n>=self.V_r_o:    
            self.operators.append(_b)
            self.V_r_o+=1
            self.V_r_n+=1
            self.updata_label(_b)
        print(self.values)
        print(self.operators)
        print(self.V_r_n)
        print(self.V_r_o)
    def updata_label(self,_b):
        self.label.setText(self.label.text()+f"{_b}") 
    def b_equall(self):
        while len(self.values)>1:
            if('*' in self.operators):
                f=self.operators.index('*')
                self.operators.pop(f)
                self.values[f]=float(self.values[f])*float(self.values[f+1])
                self.values.pop(f+1)
                self.V_r_n-=1
                self.V_r_o-=1
            elif('/' in self.operators):
                f=self.operators.index('/')
                self.operators.pop(f)
                self.values[f]=float(self.values[f])/float(self.values[f+1])
                self.V_r_n-=1
                self.V_r_o-=1
                self.values.pop(f+1)
            elif('+' in self.operators):
                f=self.operators.index('+')
                self.operators.pop(f)
                self.values[f]=float(self.values[f])+float(self.values[f+1])
                self.V_r_n-=1
                self.V_r_o-=1
                self.values.pop(f+1)
            elif('-' in self.operators):
                f=self.operators.index('-')
                self.operators.pop(f)
                self.values[f]=float(self.values[f])-float(self.values[f+1])
                self.V_r_n-=1
                self.V_r_o-=1
                self.values.pop(f+1)
            elif('%' in self.operators):
                f=self.operators.index('%')
                self.operators.pop(f)
                self.values[f]=float(self.values[f])%float(self.values[f+1])
                self.values.pop(f+1)
                self.V_r_n-=1
                self.V_r_o-=1
            
        self.label.setText(f"{self.values[0]}")



    def button_ac(self):
        self.values=['']
        self.operators=[]
        self.V_r_n=0
        self.V_r_o=-1
        self.label.clear()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
