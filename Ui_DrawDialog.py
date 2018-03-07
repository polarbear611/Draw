# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Develop\python\PyQt\Draw\DrawDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(True)
        self.labelPlate = QtWidgets.QLabel(Dialog)
        self.labelPlate.setGeometry(QtCore.QRect(60, 70, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.labelPlate.setFont(font)
        self.labelPlate.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelPlate.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelPlate.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPlate.setObjectName("labelPlate")
        self.buttonDraw = QtWidgets.QPushButton(Dialog)
        self.buttonDraw.setGeometry(QtCore.QRect(210, 200, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonDraw.setFont(font)
        self.buttonDraw.setFlat(False)
        self.buttonDraw.setObjectName("buttonDraw")
        self.labelLuckyPlate = QtWidgets.QLabel(Dialog)
        self.labelLuckyPlate.setGeometry(QtCore.QRect(70, 30, 251, 31))
        self.labelLuckyPlate.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLuckyPlate.setObjectName("labelLuckyPlate")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelPlate.setText(_translate("Dialog", "渝BAG993"))
        self.buttonDraw.setToolTip(_translate("Dialog", "开始抽奖"))
        self.buttonDraw.setText(_translate("Dialog", "开  始"))
        self.labelLuckyPlate.setText(_translate("Dialog", "幸运车牌号（1/100)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

