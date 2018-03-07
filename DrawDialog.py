# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog,  QMessageBox
from Ui_DrawDialog import Ui_Dialog
from Draw import Draw
#from DrawThread import DrawThread
from PyQt5.QtCore import QTimer,  Qt
import random

class DrawDialog(QDialog,  Ui_Dialog):
    def __init__(self):
        super(QDialog,  self).__init__()
        self.setupUi(self)
        self.initUI()
        self.loadPlateSet()
    
    def initUI(self):
        self.buttonDraw.clicked.connect(self.drawAllLuckyPlates)
        self.draw = Draw()
        self.plates_file_name = 'a.txt'
        self.out_file_name = "out.txt"
        self.plates = self.draw.read_plates(self.plates_file_name)
        self.labelPlate.setText(random.choice(self.plates))
        
        self.luckyPlateCount = 0
        self.maxCount = 100
        self.updateLabelLuckyPlate(self.luckyPlateCount,  self.maxCount)
        self.timer = QTimer(self)
        #self.timer.timeout.connect(self.updateLabelPlate)
        self.timer.timeout.connect(self.updateLabelLuckyPlates)
        #self.showFullScreen()
        
    def loadPlateSet(self):
        self.plateSet = set()
        self.luckyPlates = []

    def updateLabelLuckyPlate(self,  count,  maxCount):
        self.labelLuckyPlate.setText("重庆高速公路2017安全文明积极参与者抽奖活动（{}/{})".format(count, maxCount))
        
    def updateLabelPlate(self):
        luckyPlate = random.choice(self.plates)
        self.labelPlate.setText(luckyPlate)
    
    def keyPressEvent(self,  e):
        if e.key() == Qt.Key_Space:
            self.drawLuckyPlate()
        if e.key() == Qt.Key_Escape:
            self.close()
        QDialog.keyPressEvent(self,  e)
    
    def drawAllLuckyPlates(self):
        #self.labelLuckyPlates.setText(((self.labelPlate.text() + '\t') * 10 + '\n') * 10)
        self.luckyPlateCount = 0
        self.labelLuckyPlates.setText('')
        self.timer.start(100)
        
    def updateLabelLuckyPlates(self):
        self.buttonDraw.setEnabled(False)
        if self.luckyPlateCount >= 100:
            self.timer.stop()
            QMessageBox.warning(self,  '抽奖结束',  "{}个幸运车牌已全部抽出".format(self.maxCount))
        if self.luckyPlateCount % 5 == 0 and self.luckyPlateCount > 0:
            self.labelLuckyPlates.setText(self.labelLuckyPlates.text() + '\n'+ random.choice(self.plates)+'(蓝)')
        elif self.luckyPlateCount == 0:
             self.labelLuckyPlates.setText(self.labelLuckyPlates.text() + random.choice(self.plates)+'(蓝)')
        else:
            self.labelLuckyPlates.setText(self.labelLuckyPlates.text() + '\t'+ random.choice(self.plates)+'(蓝)')
        self.luckyPlateCount += 1
        
    def drawLuckyPlate(self):
        if "开  始" ==self.buttonDraw.text():
            self.buttonDraw.setText("停  止")
            #for i in range(10):
                          
            self.timer.start(50)
        else:
            self.buttonDraw.setText("开  始")
            self.timer.stop()
            self.luckyPlateCount += 1
            self.updateLabelLuckyPlate(self.luckyPlateCount,  self.maxCount)
            with open(self.out_file_name,  'a') as f:
                f.write(self.labelPlate.text() + '\n')
            if self.luckyPlateCount == self.maxCount:
                QMessageBox.warning(self,  '抽奖结束',  "{}个幸运车牌已全部抽出".format(self.maxCount))
                self.buttonDraw.setEnabled(False)
        #QMessageBox.warning(self,  'hello',  'world')

