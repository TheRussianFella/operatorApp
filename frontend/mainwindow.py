from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal as Signal
import random
import io
from PIL import Image, ImageQt

from WebClient import WebClient
from Machine import Machine
from Order import Order
from Bundle import Bundle
from Element import Element
#import printing

class MainWindow(QtWidgets.QMainWindow):

    #Signals

    orderCompletedSignal = Signal(str, name = "orderCompletedSignal")
    changeSignal = Signal(str, str, int, name = "changeSignal")

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setObjectName("MainWindow")
        self.setGeometry(0, 0, 726, 442)
        self.setWindowTitle("Панель оператора")

        self.orders = dict()

        self.machine = Machine()
        self.machine.goodSignal.connect(self.goodHandler)
        self.machine.badSignal.connect(self.badHandler)
        #self.machine.work()
        #try:
        #    _thread.start_thread(self.machine.work(), ("Thread-1", 1))
        #except:
        #    print("THREAD ERROR")
        #self.changeSignal.connect(self.changeElementInDialog)
        #self.orderCompletedSignal.connect(self.orderCompleted)

        self.setupUi()

        self.refreshButton.clicked.connect(self.refresh)
        self.printButton.clicked.connect(self.startWork)

        self.changeSignal.connect(self.changeElementInDialog)

        QtCore.QMetaObject.connectSlotsByName(self)

        self.refresh()

        self.d = QtWidgets.QDialog()
    #Slots

    def refresh(self):
        self.wc = WebClient("http://139.59.150.2:80")

        jsonOrders = self.wc.getOrders()

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

                    frontPicUrl = element['frontimage']
                    backPicUrl = element['backimage']
                    contentPicUrl = element['content_image']

                    frontPicData = self.wc.getPic(frontPicUrl)
                    backPicData = self.wc.getPic(backPicUrl)
                    contentPicData = self.wc.getPic(contentPicUrl)

                    frontPicIO = io.BytesIO(frontPicData.content)
                    backPicIO = io.BytesIO(backPicData.content)
                    contentPicIO = io.BytesIO(contentPicData.content)

                    frontPic = Image.open(frontPicIO)
                    backPic = Image.open(backPicIO)
                    contentPic = Image.open(contentPicIO)

                    self.orders[orderId][bundleId].add(Element(id, name, quantity,
                                                               frontPic, backPic,
                                                               contentPic))

                    name = self.orders[orderId][bundleId][elementCount].name
                    quantity = str(self.orders[orderId][bundleId][elementCount].quantity)

                    elementCount += 1

        self.paintTree(self.orders)

        self.orderCounter.setText(str(len(self.orders)))
    def startWork(self):

        curItem = self.treeWidget.selectedItems()[0]

        if curItem.child(0) == None:
            bundlePos = curItem.parent().text(0).index('№') + 1
            lastPos = curItem.parent().text(0).index('X') - 1
            self.currBundleId = curItem.parent().text(0)[bundlePos:lastPos]

            order = curItem.parent().parent().text(0)
            orderPos = order.index('№') + 1

            self.currOrderId = order[orderPos:]

            text = curItem.text(0)

            xPos = text.index('X')

            name = text[:xPos - 1]

            index = 0
            for element in self.orders[self.currOrderId][self.currBundleId]:
                if element.name == name:
                    break
                index += 1

            self.changeSignal.emit(self.currOrderId, self.currBundleId, index)

            return

        if curItem.child(0).childCount() != 0:
            curItem = curItem.child(0)

        bundlePos = curItem.text(0).index('№') + 1
        lastPos = curItem.text(0).index('X') - 1
        self.currBundleId = curItem.text(0)[bundlePos:lastPos]

        order = curItem.parent().text(0)
        orderPos = order.index('№') + 1

        self.currOrderId = order[orderPos:]


        #self.d = QtWidgets.QDialog()

        self.d.setWindowTitle("helpDialog")

        cancelButton = QtWidgets.QPushButton("Cancel",self.d)
        cancelButton.clicked.connect(self.goodHandler)
        #cancelButton.clicked.connect(self.d.close)

        layout = QtWidgets.QVBoxLayout(self.d)

        hor = QtWidgets.QHBoxLayout()

        self.currElement = 0
        element = self.orders[self.currOrderId][self.currBundleId][self.currElement]

        pic = QtWidgets.QLabel(self.d)
        pic.setFixedSize(100, 100)
        pm = QtGui.QPixmap(100, 100)
        pm.fromImage(ImageQt.ImageQt(element.contentPic))
        pic.setPixmap(pm)

        hor.addWidget(pic)

        name = QtWidgets.QLabel(element.name)

        hor.addWidget(name)

        quant = QtWidgets.QLabel("X" + str(element.quantity))

        hor.addWidget(quant)

        layout.addLayout(hor)

        layout.addWidget(cancelButton)

        self.d.open()

        #printing.print_images([(element.frontPic, element.backPic)])

    def changeElementInDialog(self, orderId, bundleId, element):

        self.d.close()

        self.d = QtWidgets.QDialog()

        self.d.setWindowTitle("helpDialog")

        cancelButton = QtWidgets.QPushButton("Cancel",self.d)
        cancelButton.clicked.connect(self.goodHandler)

        layout = QtWidgets.QVBoxLayout(self.d)

        hor = QtWidgets.QHBoxLayout()

        #for cnt in reversed(range(self.d.layout.hor.count())):
            #widget = self.dvbox.takeAt(cnt).widget()

            #if widget is not None:
                #widget.deleteLater

        elementObj = self.orders[orderId][bundleId][element]

        pic = QtWidgets.QLabel(self.d)
        pic.setFixedSize(100, 100)
        pm = QtGui.QPixmap(100, 100)
        pm.fromImage(ImageQt.ImageQt(elementObj.contentPic))
        pic.setPixmap(pm)

        hor.addWidget(pic)

        element = self.orders[orderId][bundleId][element]

        name = QtWidgets.QLabel(element.name)

        hor.addWidget(name)

        quant = QtWidgets.QLabel("X" + str(element.quantity))

        hor.addWidget(quant)

        layout.addLayout(hor)

        layout.addWidget(cancelButton)

        self.d.open()

        #printing.print_images([(element.frontPic, element.backPic)])

    def badHandler(self, errorCode):
        self.achtungDialog = QtWidgets.QDialog()
        self.achtungDialog.setWindowTitle("Ошибка")

        self.achtungDialog.setFixedSize(300, 150)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("Проблема со станком"))
        button = QtWidgets.QPushButton("OK")
        layout.addWidget(button)
        button.clicked.connect(self.exitAchtung)
        self.achtungDialog.setLayout(layout)
        self.achtungDialog.show()

    def goodHandler(self):

        #if goodCode == Machine.goodCodes.ACHTUNG_GONE:
        #    self.achtungDialog.close()

        #elif goodCode == Machine.goodCodes.NEW_SLIDE:
        self.orders[self.currOrderId][self.currBundleId].elements.pop(self.currElement)

        if self.orders[self.currOrderId][self.currBundleId].length() == 0:
            del(self.orders[self.currOrderId].bundles[self.currBundleId])
            self.currElement = 0
            if len(self.orders[self.currOrderId].bundles) <= int(self.currBundleId) + 1:
                self.orderCompletedSignal.emit(self.currOrderId)
            else:
                self.currBundleId = random.sample(self.orders[self.currOrderId], 1)

        self.changeSignal.emit(self.currOrderId, self.currBundleId, self.currElement)

        self.paintTree(self.orders)

    def orderCompleted(self, orderId):
        self.wc.orderCompleted(orderId)
        #self.refresh()
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

    def setupUi(self):

        self.centralWidget = QtWidgets.QWidget(self)
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
        self.gridLayout.addWidget(self.refreshButton, 1, 0, 1, 2)
        self.printButton = QtWidgets.QPushButton(self.groupBox)
        self.printButton.setObjectName("printButton")
        self.gridLayout.addWidget(self.printButton, 2, 0, 1, 2)
        self.horizontalLayout.addWidget(self.groupBox)
        self.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(self)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 726, 19))
        self.menuBar.setObjectName("menuBar")
        self.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(self)
        self.mainToolBar.setObjectName("mainToolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(self)
        self.statusBar.setObjectName("statusBar")
        self.setStatusBar(self.statusBar)
        self.retranslateUi(self)

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
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
