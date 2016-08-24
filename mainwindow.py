# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Aug 20 16:09:32 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from WebClient import WebClient
from Machine import Machine
from Order import Order
from Bundle import Bundle
from Element import Element

class Ui_MainWindow(object):

    orders = {}
    d = QtWidgets.QDialog

    #Slots

    def refresh(self):
        wc = WebClient("http://localhost:8000")

        jsonOrders = wc.getOrders()

        elementCount = 0

        for order in jsonOrders['orders']:

            orderId = str(order['id'])
            self.orders[orderId] = Order(orderId)

            for bundle in order['bundles']:

                bundleId = str(bundle['id'])
                name = bundle['name']
                quantity = bundle['quantity']

                self.orders[orderId].add( Bundle(bundleId, name, quantity) )

                elementCount = 0

                for element in bundle['elements']:
                    id = str(element['id'])
                    name = element['name']
                    quantity = element['quantity']

                    self.orders[orderId][bundleId].add(Element(id, name, quantity))

                    name = self.orders[orderId][bundleId][elementCount].name
                    quantity = str(self.orders[orderId][bundleId][elementCount].quantity)

                    elementCount += 1

        self.paintTree(self.orders)

    def startWork(self):

        curItem = self.treeWidget.selectedItems()[0]

        if curItem.child(0).childCount() != 0:
            curItem = curItem.child(0)

        bundlePos = curItem.text(0).index('№') + 1
        lastPos = curItem.text(0).index('X') - 1
        bundleId = curItem.text(0)[bundlePos:lastPos]

        order = curItem.parent().text(0)
        orderPos = order.index('№') + 1

        orderId = order[orderPos:]

        if curItem.child() == None:
            name = curItem.name

            index = 0
            for element in self.orders[orderId][bundleId]:
                if element.name == name:
                    break
                index += 1


        self.d = QtWidgets.QDialog()

        self.d.setWindowTitle("helpDialog")

        cancelButton = QtWidgets.QPushButton("Cancel",self.d)
        cancelButton.clicked.connect(self.d.close)

        layout = QtWidgets.QVBoxLayout(self.d)

        hor = QtWidgets.QHBoxLayout()

        pic = QtWidgets.QLabel(self.d)
        pic.setFixedSize(100, 100)
        pm = QtGui.QPixmap(100, 100)
        pm.load("test.jpg")
        pic.setPixmap(pm)

        hor.addWidget(pic)

        element = self.orders[orderId][bundleId][0]

        name = QtWidgets.QLabel(element.name)

        hor.addWidget(name)

        quant = QtWidgets.QLabel("X" + str(element.quantity))

        hor.addWidget(quant)

        layout.addLayout(hor)

        layout.addWidget(cancelButton)

        self.d.exec_()

    def changeElementInDialog(self, orderId, bundleId, element):

        self.d.close()

        self.d = QtWidgets.QDialog()

        self.d.setWindowTitle("helpDialog")

        cancelButton = QtWidgets.QPushButton("Cancel",self.d)
        cancelButton.clicked.connect(self.d.close)

        layout = QtWidgets.QVBoxLayout(self.d)

        hor = QtWidgets.QHBoxLayout()

        pic = QtWidgets.QLabel(self.d)
        pic.setFixedSize(100, 100)
        pm = QtGui.QPixmap(100, 100)
        pm.load("test.jpg")
        pic.setPixmap(pm)

        hor.addWidget(pic)

        element = self.orders[orderId][bundleId][element]

        name = QtWidgets.QLabel(element.name)

        hor.addWidget(name)

        quant = QtWidgets.QLabel("X" + str(element.quantity))

        hor.addWidget(quant)

        layout.addLayout(hor)

        layout.addWidget(cancelButton)

        self.d.exec_()

    ##########

    def paintTree(self, orders):

        self.treeWidget.clear()

        for order in orders.values():

            treeOrder = QtWidgets.QTreeWidgetItem()

            orderId = order.id
            mes = "Заказ №" + orderId
            treeOrder.setText(0, mes)
            self.treeWidget.addTopLevelItem(treeOrder)

            for bundle in order.bundles.values():

                treeBundle = QtWidgets.QTreeWidgetItem()

                bundleId = bundle.id
                tempMes1 = "Набор " + bundle.name
                tempMes2 = " №" + bundle.id
                tempMes3 = " X" + str(bundle.quantity)
                mes = tempMes1 + tempMes2 + tempMes3
                treeBundle.setText(0, mes)

                treeOrder.addChild(treeBundle)

                elementCount = 0

                for element in bundle.elements:

                    treeElement = QtWidgets.QTreeWidgetItem()

                    name = element.name
                    quantity = str(element.quantity)

                    elementCount += 1

                    mes = name + " X" + quantity

                    treeElement.setText(0, mes)

                    treeBundle.addChild(treeElement)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 442)
        MainWindow.setWindowTitle("Панель оператора")
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
        self.printButton.clicked.connect(self.startWork)            #Start work slot
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
        self.refresh()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("operatorPanel", "operatorPanel"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Заказы"))
        self.groupBox.setTitle(_translate("MainWindow", "Панель управления  "))
        self.label.setText(_translate("MainWindow", "Кол-во заказов:"))
        self.orderCounter.setText(_translate("MainWindow", "0"))
        self.refreshButton.setText(_translate("MainWindow", "Обновить"))
        self.printButton.setText(_translate("MainWindow", "Обработать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
