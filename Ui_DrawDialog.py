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
        Dialog.resize(800, 733)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(True)
        self.labelPlate = QtWidgets.QLabel(Dialog)
        self.labelPlate.setGeometry(QtCore.QRect(200, 150, 400, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.labelPlate.setFont(font)
        self.labelPlate.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelPlate.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelPlate.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPlate.setObjectName("labelPlate")
        self.buttonDraw = QtWidgets.QPushButton(Dialog)
        self.buttonDraw.setGeometry(QtCore.QRect(240, 270, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonDraw.setFont(font)
        self.buttonDraw.setFlat(False)
        self.buttonDraw.setObjectName("buttonDraw")
        self.labelLuckyPlate = QtWidgets.QLabel(Dialog)
        self.labelLuckyPlate.setGeometry(QtCore.QRect(200, 100, 400, 40))
        self.labelLuckyPlate.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLuckyPlate.setObjectName("labelLuckyPlate")
        self.labelDrawActivity = QtWidgets.QLabel(Dialog)
        self.labelDrawActivity.setGeometry(QtCore.QRect(180, 30, 440, 47))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelDrawActivity.setFont(font)
        self.labelDrawActivity.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDrawActivity.setObjectName("labelDrawActivity")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 350, 741, 371))
        self.groupBox.setObjectName("groupBox")
        self.labelLuckyPlates = QtWidgets.QLabel(self.groupBox)
        self.labelLuckyPlates.setGeometry(QtCore.QRect(20, 30, 701, 321))
        self.labelLuckyPlates.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelLuckyPlates.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelLuckyPlates.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelLuckyPlates.setObjectName("labelLuckyPlates")
        self.buttonDraw_2 = QtWidgets.QPushButton(Dialog)
        self.buttonDraw_2.setGeometry(QtCore.QRect(430, 270, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonDraw_2.setFont(font)
        self.buttonDraw_2.setFlat(False)
        self.buttonDraw_2.setObjectName("buttonDraw_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelPlate.setText(_translate("Dialog", "渝BAG993(蓝色)"))
        self.buttonDraw.setToolTip(_translate("Dialog", "开始抽奖"))
        self.buttonDraw.setText(_translate("Dialog", "开  始"))
        self.labelLuckyPlate.setText(_translate("Dialog", "幸运车牌号（1/100)"))
        self.labelDrawActivity.setText(_translate("Dialog", "重庆高速2017安全文明积极参与者抽奖活动"))
        self.groupBox.setTitle(_translate("Dialog", "抽奖结果"))
        self.labelLuckyPlates.setText(_translate("Dialog", "渝BAG993(蓝色)"))
        self.buttonDraw_2.setToolTip(_translate("Dialog", "开始抽奖"))
        self.buttonDraw_2.setText(_translate("Dialog", "抽 奖 结 果"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

