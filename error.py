# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created: Sat Aug 20 16:11:03 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_error(object):
    def setupUi(self, error):
        error.setObjectName("error")
        error.resize(400, 183)
        self.errorLabel = QtWidgets.QLabel(error)
        self.errorLabel.setGeometry(QtCore.QRect(68, 60, 271, 20))
        self.errorLabel.setObjectName("errorLabel")
        self.okButton = QtWidgets.QPushButton(error)
        self.okButton.setGeometry(QtCore.QRect(160, 140, 81, 22))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(error)
        QtCore.QMetaObject.connectSlotsByName(error)

    def retranslateUi(self, error):
        _translate = QtCore.QCoreApplication.translate
        error.setWindowTitle(_translate("error", "Dialog"))
        self.errorLabel.setText(_translate("error", "error"))
        self.okButton.setText(_translate("error", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    error = QtWidgets.QDialog()
    ui = Ui_error()
    ui.setupUi(error)
    error.show()
    sys.exit(app.exec_())

