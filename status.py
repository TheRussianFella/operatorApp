# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'status.ui'
#
# Created: Sat Aug 20 16:11:32 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Status(object):
    def setupUi(self, Status):
        Status.setObjectName("Status")
        Status.resize(400, 171)
        self.progressBar = QtWidgets.QProgressBar(Status)
        self.progressBar.setGeometry(QtCore.QRect(20, 130, 361, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.statusLabel = QtWidgets.QLabel(Status)
        self.statusLabel.setGeometry(QtCore.QRect(50, 50, 291, 16))
        self.statusLabel.setObjectName("statusLabel")

        self.retranslateUi(Status)
        QtCore.QMetaObject.connectSlotsByName(Status)

    def retranslateUi(self, Status):
        _translate = QtCore.QCoreApplication.translate
        Status.setWindowTitle(_translate("Status", "Dialog"))
        self.statusLabel.setText(_translate("Status", "Status"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Status = QtWidgets.QDialog()
    ui = Ui_Status()
    ui.setupUi(Status)
    Status.show()
    sys.exit(app.exec_())

