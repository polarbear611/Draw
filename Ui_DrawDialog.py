# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Develop\PyQt\Draw\DrawDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1920, 1080)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(True)
        self.labelPlate = QtWidgets.QLabel(Dialog)
        self.labelPlate.setGeometry(QtCore.QRect(689, 420, 531, 131))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(48)
        self.labelPlate.setFont(font)
        self.labelPlate.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelPlate.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelPlate.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPlate.setObjectName("labelPlate")
        self.buttonDraw = QtWidgets.QPushButton(Dialog)
        self.buttonDraw.setGeometry(QtCore.QRect(790, 570, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonDraw.setFont(font)
        self.buttonDraw.setFlat(False)
        self.buttonDraw.setObjectName("buttonDraw")
        self.labelLuckyPlate = QtWidgets.QLabel(Dialog)
        self.labelLuckyPlate.setGeometry(QtCore.QRect(750, 370, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelLuckyPlate.setFont(font)
        self.labelLuckyPlate.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLuckyPlate.setObjectName("labelLuckyPlate")
        self.labelDrawActivity = QtWidgets.QLabel(Dialog)
        self.labelDrawActivity.setGeometry(QtCore.QRect(519, 199, 851, 141))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.labelDrawActivity.setFont(font)
        self.labelDrawActivity.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDrawActivity.setObjectName("labelDrawActivity")
        self.groupboxResult = QtWidgets.QGroupBox(Dialog)
        self.groupboxResult.setGeometry(QtCore.QRect(310, 620, 1351, 441))
        self.groupboxResult.setFlat(False)
        self.groupboxResult.setObjectName("groupboxResult")
        self.labelLuckyPlates = QtWidgets.QLabel(self.groupboxResult)
        self.labelLuckyPlates.setGeometry(QtCore.QRect(10, 30, 1321, 391))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        self.labelLuckyPlates.setFont(font)
        self.labelLuckyPlates.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelLuckyPlates.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelLuckyPlates.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelLuckyPlates.setObjectName("labelLuckyPlates")
        self.buttonCheckResult = QtWidgets.QPushButton(Dialog)
        self.buttonCheckResult.setGeometry(QtCore.QRect(980, 570, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonCheckResult.setFont(font)
        self.buttonCheckResult.setFlat(False)
        self.buttonCheckResult.setObjectName("buttonCheckResult")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "重庆高速2017安全文明积极参与者抽奖活动"))
        self.labelPlate.setText(_translate("Dialog", "渝BAG993(蓝色)"))
        self.buttonDraw.setToolTip(_translate("Dialog", "开始抽奖"))
        self.buttonDraw.setText(_translate("Dialog", "开  始"))
        self.labelLuckyPlate.setText(_translate("Dialog", "幸运车牌号（1/100)"))
        self.labelDrawActivity.setText(_translate("Dialog", "重庆高速\n"
"2017\"安全文明积极参与者\"抽奖活动"))
        self.groupboxResult.setTitle(_translate("Dialog", "抽奖结果"))
        self.labelLuckyPlates.setText(_translate("Dialog", "渝BAG993(蓝色)"))
        self.buttonCheckResult.setToolTip(_translate("Dialog", "开始抽奖"))
        self.buttonCheckResult.setText(_translate("Dialog", "抽 奖 结 果"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

