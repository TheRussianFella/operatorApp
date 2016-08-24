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
    #Slots

    def refresh(self):
        wc = WebClient("http://localhost:8000")

        jsonOrders = wc.getOrders()

        self.treeWidget.clear()


        elementCount = 0

        for order in jsonOrders['orders']:

            orderId = str(order['id'])
            self.orders[orderId] = Order(orderId)

            treeOrder = QtWidgets.QTreeWidgetItem()

            mes = "Заказ №" + orderId
            treeOrder.setText(0, mes)
            self.treeWidget.addTopLevelItem(treeOrder)

            for bundle in order['bundles']:

                bundleId = str(bundle['id'])
                name = bundle['name']
                quantity = bundle['quantity']

                self.orders[orderId].add( Bundle(bundleId, name, quantity) )

                elementCount = 0

                treeBundle = QtWidgets.QTreeWidgetItem()

                tempMes1 = "Набор " + name
                tempMes2 = " №" + self.orders[orderId][bundleId].id
                tempMes3 = " X" + str(self.orders[orderId][bundleId].quantity)
                mes = tempMes1 + tempMes2 + tempMes3
                treeBundle.setText(0, mes)

                treeOrder.addChild(treeBundle)
                for element in bundle['elements']:
                    id = str(element['id'])
                    name = element['name']
                    quantity = element['quantity']

                    self.orders[orderId][bundleId].add(Element(id, name, quantity))

                    treeElement = QtWidgets.QTreeWidgetItem()

                    name = self.orders[orderId][bundleId][elementCount].name
                    quantity = str(self.orders[orderId][bundleId][elementCount].quantity)

                    elementCount += 1

                    mes = name + " X" + quantity

                    treeElement.setText(0, mes)

                    treeBundle.addChild(treeElement)

        #for order in self.orders.values():
            #print(order.id)
            #for bundle in order.bundles.values():
                #print(bundle.id)
                #print(bundle.elements)


    def startWork(self):

        d = QtWidgets.QDialog()
        d.setWindowTitle("helpDialog")

        startButton = QtWidgets.QPushButton("Start",d)
        cancelButton = QtWidgets.QPushButton("Cancel",d)

        layout = QtWidgets.QVBoxLayout(d)

        #if :
        #    curItem = self.treeWidget.topLevelItem(0)

        curItem = self.treeWidget.selectedItems()[0]

        if curItem.child(0).childCount() != 0:
            curItem = curItem.child(0)

        bundlePos = curItem.text(0).index('№') + 1
        lastPos = curItem.text(0).index('X') - 1
        bundleId = curItem.text(0)[bundlePos:lastPos]

        order = curItem.parent().text(0)
        orderPos = order.index('№') + 1

        orderId = order[orderPos:]

        table = QtWidgets.QTableWidget()
        table.setRowCount(self.orders[orderId][bundleId].length())
        table.setColumnCount(3)
        table.columnSpan(0, 1)

        index = 0

        for element in self.orders[orderId][bundleId].elements:

            pic = QtWidgets.QLabel()
            pm = QtGui.QPixmap(50, 50)
            pm.load("test.jpg")
            pic.setPixmap(pm)

            table.setCellWidget(index, 0, pic)
            table.setItem(index, 1, QtWidgets.QTableWidgetItem(element.name))
            table.setItem(index, 2, QtWidgets.QTableWidgetItem(str(element.quantity)))
            index += 1


        #pic = QtWidgets.QLabel(d)
        #pic.setFixedSize(50, 50)
        #pm = QtGui.QPixmap(50, 50)
        #pic.setPixmap(pm)

        layout.addWidget(table)
        layout.addWidget(startButton)
        layout.addWidget(cancelButton)

        d.exec_()

    ##########

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
