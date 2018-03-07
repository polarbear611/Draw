# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog,  QMessageBox
from Ui_DrawDialog import Ui_Dialog
from Draw import Draw
#from DrawThread import DrawThread
from PyQt5.QtCore import QTimer,  Qt
import random, xlrd,  xlwt

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
        self.plateSet = []
        self.luckyPlates = []
        self.plateSheet = xlrd.open_workbook("报名.xlsx").sheet_by_index(0)
        for i in range(1,  self.plateSheet.nrows):
            if self.plateSheet.cell(i,  self.plateSheet.ncols - 1) != "错误车牌":
                self.plateSet.append(i)
        self.labelLuckyPlates.setText(str(len(self.plateSet)))
    
    def chooseOnePlate(self):
        plateNumber = random.choice(self.plateSet)
        try:
            plate = '{}({})'.format(self.plateSheet.cell(plateNumber,  1).value ,  self.plateSheet.cell(plateNumber,  2).value[0])
        except TypeError:
            plate = '{}({})'.format(str(self.plateSheet.cell(plateNumber,  1).value) ,  self.plateSheet.cell(plateNumber,  2).value[0])
        self.plateSet.remove(plateNumber)
        self.luckyPlates.append(plateNumber)
        return plate

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
        self.timer.start(10)
        
    def updateLabelLuckyPlates(self):
        self.buttonDraw.setEnabled(False)
        if self.luckyPlateCount >= 100:
            self.timer.stop()
            self.outputLuckyPlates('抽奖结果.xls')
            QMessageBox.warning(self,  '抽奖结束',  "{}个幸运车牌已全部抽出".format(self.maxCount))
        plate = self.chooseOnePlate()
        if self.luckyPlateCount % 5 == 0 and self.luckyPlateCount > 0:
            self.labelLuckyPlates.setText(self.labelLuckyPlates.text() + '\n'+ plate)
        elif self.luckyPlateCount == 0:
             self.labelLuckyPlates.setText(self.labelLuckyPlates.text() + plate)
        else:
            self.labelLuckyPlates.setText(self.labelLuckyPlates.text() + '\t'+ plate)
        self.luckyPlateCount += 1
    
    def outputLuckyPlates(self,  out_file_name):
        if out_file_name.split('.')[-1] == 'txt':
            with open(out_file_name,  'w') as f:
                f.write('{}\t{}\t{}\t{}\n'.format("序号", "编号",  "车牌号",  "车牌颜色"))
                for i in range(len(self.luckyPlates)):
                    nrow = self.luckyPlates[i]
                    serial = i + 1
                    number = str(int(self.plateSheet.cell(nrow,  0).value)).zfill(4)
                    plate = self.plateSheet.cell(nrow,  1).value
                    color = self.plateSheet.cell(nrow,  2).value
                    f.write('{}\t{}\t{}\t{}\n'.format(serial,  number,  plate,  color))
        if out_file_name.split('.')[-1] == 'xls':
            out_workbook = xlwt.Workbook()
            out_sheet = out_workbook.add_sheet("抽奖结果")
            out_sheet.write(0,  0,  "序号")
            for c in range(self.plateSheet.ncols):
                
                out_sheet.write(0,  c + 1,  self.plateSheet.cell(0,  c).value)
            for i in range(len(self.luckyPlates)):
                out_sheet.write(i + 1,  0,  i)
                for c in range(self.plateSheet.ncols):
                    out_sheet.write(i + 1,  c + 1,  self.plateSheet.cell(i,  c).value)
            out_workbook.save(out_file_name)
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

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    drawDialog = DrawDialog()
    drawDialog.show()
    sys.exit(app.exec_())

