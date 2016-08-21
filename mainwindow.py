# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Aug 20 16:09:32 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from WebClient import WebClient

class Ui_MainWindow(object):

    #Slots

    def refresh(self):
        wc = WebClient("")

        orders = wc.getOrders()

        print(orders)

        self.orderCounter.setText("ok")

    ######

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 442)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralWidget)
        self.treeWidget.setObjectName("treeWidget")
        self.horizontalLayout.addWidget(self.treeWidget)
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.orderCounter = QtWidgets.QLabel(self.groupBox)
        self.orderCounter.setObjectName("orderCounter")
        self.gridLayout.addWidget(self.orderCounter, 0, 1, 1, 1)
        self.refreshButton = QtWidgets.QPushButton(self.groupBox)
        self.refreshButton.setObjectName("refreshButton")
        self.refreshButton.clicked.connect(self.refresh)             #Refresh Slot
        self.gridLayout.addWidget(self.refreshButton, 1, 0, 1, 2)
        self.printButton = QtWidgets.QPushButton(self.groupBox)
        self.printButton.setObjectName("printButton")
        self.gridLayout.addWidget(self.printButton, 2, 0, 1, 2)
        self.horizontalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 726, 19))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Заказы"))
        self.groupBox.setTitle(_translate("MainWindow", "Панель управления  "))
        self.label.setText(_translate("MainWindow", "Кол-во заказов:"))
        self.orderCounter.setText(_translate("MainWindow", "0"))
        self.refreshButton.setText(_translate("MainWindow", "Обновить"))
        self.printButton.setText(_translate("MainWindow", "Распечатать"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
