# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addList.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtGui import QListWidgetItem
# import QListWidgetItem

class Ui_MainWindow(object):
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


      

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 256, 584))
        self.listWidget.setObjectName("listWidget")


        self.addItemInList()


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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

