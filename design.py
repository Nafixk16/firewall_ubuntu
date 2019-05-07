# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addList.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import re
from firewallrule import firewall
from PyQt5 import Qt

class Ui_MainWindow(object):

    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 607)
        # self.fobj = firewall()

        

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 256, 581))
        self.listWidget.setObjectName("listWidget")

        # self.widgetLayout = QtWidgets.QWidget(self.centralwidget)
        # self.widgetLayout.setGeometry(QtCore.QRect(260, -10, 551, 591))
        # self.widgetLayout.setObjectName("widget")
        # self.ip_block_handler()
        
        

        # self.ip_block_handler()
        # self.gproxy = QGraphicsProxyWidget()
        

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.addItemInList()
        # self.ip_block_handler()
        self.listWidget.itemSelectionChanged.connect(self.itemChange)
        
       

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def addItemInList(self):

        item1  = QtWidgets.QListWidgetItem("IP Block")
        item1.setIcon(QtGui.QIcon("image/ipblock.png"))

        item2  = QtWidgets.QListWidgetItem("Packet Trace")
        item2.setIcon(QtGui.QIcon("image/packet.png"))

        item3 = QtWidgets.QListWidgetItem("Port Configuration")
        item3.setIcon(QtGui.QIcon("image/port.jpg"))

        self.listWidget.setStyleSheet(" font: 15.5pt ")
                # self.listWidget("nafix")
        # self.listWidget.addItem(item)
        self.listWidget.addItem(item1)
        self.listWidget.addItem(item2)
        self.listWidget.addItem(item3)

        

    def itemChange(self):
        
        currentItem = self.listWidget.currentItem().text()
        print(type(currentItem))
        if currentItem == "IP Block":
            self.ip_block_handler()

        if currentItem == "Port Configuration":
            print("in cure item")
            self.portConfigureHandler()

            
          

# ********************************************** Port Configuration ***************************************
    def portConfigureHandler(self):
     
        
        self.widgetLayout = QtWidgets.QGraphicsView(self.centralwidget)
        self.widgetLayout.setGeometry(QtCore.QRect(260, -10, 551, 591))
        self.widgetLayout.setObjectName("graphicsView")
        self.widgetLayout.show()

        comb = QComboBox(self.widgetLayout)
        comb.setGeometry(150,50,251,41)
        comb.addItem("TCP source port")
        comb.addItem("UDP source port")
        comb.addItem("Any incoming port")
        comb.show()
    
        


         #label
        l2 = QLabel(self.widgetLayout)
        l2.setGeometry(50,300,500,70)
        l2.setText("The block port or domain name will add in black list you can remove \n it from black list menu")
        l2.show()

        #label
        l1 = QLabel(self.widgetLayout)
        l1.setGeometry(60,233,400,17)
        l1.setText("Enter the TCP Port")
        l1.show()

        #input field
        inp1 =  QLineEdit(self.widgetLayout)
        inp1.setGeometry(191,228,222,32)
        inp1.show()


        #btn
        pushBtn =  QPushButton(self.widgetLayout)
        pushBtn.setObjectName("click me")
        pushBtn.setText("OK")
        pushBtn.setGeometry(QtCore.QRect(370,490,115,32))
        pushBtn.show()

        pushBtn.clicked.connect(lambda: self.onPortBtnClick(inp1,comb))
        comb.currentTextChanged.connect(lambda: self.onPortConfugureCombochnage(comb,l1,inp1))
        # inp1.textChanged.connect(lambda: self.onBlocklistInpChange(inp1)) 


    
    def onPortConfugureCombochnage(self,comb,l1,inp1):

        if comb.currentText() == "TCP source port":
            l1.clear()
            l1.setText("Enter the TCP port")


        if comb.currentText() == "UDP source port":
            l1.clear()
            l1.setText("Enter the UDP port")
        
            
        
        if comb.currentText() == "Any incoming port":
            l1.clear()
            l1.setText("Enter port")
                    

    def onPortBtnClick(self,inp1,comb):
        text = inp1.text()
        current_text = comb.currentText()
        msgbox = QMessageBox()
        if text:
            r1 = re.match(r"(^[1-9]*$)",text)
            if r1:
                text = int(text)
                if text > 65536:
                    print("invalid")
                    
                    msgbox.information(self.centralwidget,"warning","Invalid port")
                else:
                    

                    print("valid")
                    #here function call
            else:
                print("invlaide")
                msgbox.information(self.centralwidget,"warning","string error!")
        else:
            msgbox.information(self.centralwidget,"warning","Empty Field")



        
       




# ************************************************  ip block list item **************************************
    def ip_block_handler(self):

      
        # combo box
        print("in block handler")

        
        self.widgetLayout = QtWidgets.QGraphicsView(self.centralwidget)
        self.widgetLayout.setGeometry(QtCore.QRect(260, -10, 551, 591))
        self.widgetLayout.setObjectName("graphicsView")
        self.widgetLayout.show()

        comb = QComboBox(self.widgetLayout)
        comb.setGeometry(150,50,251,41)
        comb.addItem("Block By IP")
        comb.addItem("Block By Domain")
        comb.show()
    
        


         #label
        l2 = QLabel(self.widgetLayout)
        l2.setGeometry(50,300,500,70)
        l2.setText("The block IP or domain name will add in black list you can remove \n it from black list menu")
        l2.show()

        #label
        l1 = QLabel(self.widgetLayout)
        l1.setGeometry(60,233,400,17)
        l1.setText("Enter the IP")
        l1.show()

        #input field
        inp1 =  QLineEdit(self.widgetLayout)
        inp1.setGeometry(181,230,222,30)
        inp1.setPlaceholderText("192.168.1.0")
        inp1.show()


        #btn
        pushBtn =  QPushButton(self.widgetLayout)
        pushBtn.setObjectName("click me")
        pushBtn.setText("OK")
        pushBtn.setGeometry(QtCore.QRect(370,490,115,32))
        pushBtn.show()

        # signal slot
        pushBtn.clicked.connect(lambda: self.onBlocklistBtnClick(inp1,comb))
        comb.currentTextChanged.connect(lambda: self.onBlockListCombochnage(comb,l1,inp1))
        inp1.textChanged.connect(lambda: self.onBlocklistInpChange(inp1)) 

    def onBlocklistInpChange(self, inp1):
        inp1.setStyleSheet("color: black")
    
    def onBlocklistBtnClick(self,inp1,comb):
        
        text = inp1.text()
        combtext = comb.currentText()
        if text:
            if combtext == "Block By IP":
                r1= re.match(r"^(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\.(?!$)|$)){4}$",text)
                if not r1:
                    inp1.setStyleSheet("color: red")
                else:
                    print("s")
                    # self.fobj.blockIP(text)
                    
            if combtext == "Block By Domain":
                r1= re.match(r"^(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\.(?!$)|$)){4}$",text)
                if r1:
                    inp1.setStyleSheet("color: red")
        else:
            inp1.setStyleSheet("color: red")



    def onBlockListCombochnage(self,comb,l1,inp1):

        if comb.currentText() == "Block By IP":
            l1.clear()
            l1.setText("Enter the IP")
            inp1.setPlaceholderText("192.168.1.0")


        if comb.currentText() == "Block By Domain":
            l1.clear()
            l1.setText("Enter the Domain Name")
            inp1.setPlaceholderText("www.google.com")

           
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
   
    MainWindow.show()
    sys.exit(app.exec_())

