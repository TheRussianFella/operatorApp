from PyQt5 import QtCore, QtGui, QtWidgets

class helpDialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(helpDialog, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout(self)

        buttons = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel,
                                             Qt.Horizontal, self)
        buttons.accepted.connect(self.ready)
        buttons.rejected.connect(self.cancel)


    def ready(self):
        print("ok")
