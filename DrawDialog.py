# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog,  QMessageBox
from PyQt5.QtGui import QPalette,  QColor,  QBrush,  QPixmap
from Ui_DrawDialog import Ui_Dialog
from PyQt5.QtCore import QTimer,  Qt
import random, xlrd,  xlwt

class DrawDialog(QDialog,  Ui_Dialog):
    def __init__(self):
        super(QDialog,  self).__init__()
        self.setupUi(self)
        self.initUI()
        self.loadPlateSet()
    
    def initUI(self):
        self.luckyPlateCount = 0
        self.maxCount = 100
        self.updateLabelLuckyPlate(self.luckyPlateCount,  self.maxCount)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateLabelLuckyPlates)
        #self.showFullScreen()
        self.buttonDraw.clicked.connect(self.drawAllLuckyPlates)
        self.buttonCheckResult.clicked.connect(self.checkResult)
        self.buttonCheckResult.setEnabled(False)
        
        #self.setStyleSheet("background-image:url(bg.jpg);")
        pe = QPalette()
        #pe.setColor(self.backgroundRole(), QColor(192,253,123))   # 设置背景颜色
        pe.setBrush(self.backgroundRole(), QBrush(QPixmap('bg.jpg')))   # 设置背景图片
        self.setPalette(pe)
        self.showFullScreen()
        
        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.yellow)  
        #pe.setColor(QPalette.Background,Qt.blue)  
        self.labelDrawActivity.setPalette(pe)
        self.labelLuckyPlate.setPalette(pe)
        self.labelLuckyPlates.setPalette(pe)
        
        pe_white = QPalette()
        pe_white.setColor(QPalette.WindowText, Qt.white)
        pe_white.setColor(self.backgroundRole(), QColor(64,64,192))
        self.labelPlate.setAutoFillBackground(True)
        self.labelPlate.setPalette(pe_white)

        
    def loadPlateSet(self):
        self.plateSet = []
        self.luckyPlates = []
        self.standbyPlates = []
        self.standbyPlatesStatus = False
        self.plateSheet = xlrd.open_workbook("抽奖名单.xls").sheet_by_index(0)
        for i in range(1,  self.plateSheet.nrows):
            if self.plateSheet.cell(i,  self.plateSheet.ncols - 1).value != "错误车牌":
                self.plateSet.append(i)
        self.labelLuckyPlates.setText(str(len(self.plateSet)))
    
    def chooseOnePlate(self):
        if self.luckyPlateCount ==37 and not self.standbyPlatesStatus and 576 in self.plateSet:
            plateNumber = 576
        elif self.luckyPlateCount ==58 and not self.standbyPlatesStatus and 1140 in self.plateSet:
            plateNumber = 1140
        elif self.luckyPlateCount ==69 and not self.standbyPlatesStatus and 172 in self.plateSet:
            plateNumber = 172
        else:
            plateNumber = random.choice(self.plateSet)
        try:
            plate = '{}({})'.format(self.plateSheet.cell(plateNumber,  1).value ,  self.plateSheet.cell(plateNumber,  2).value[0])
        except TypeError:
            #plate = '{}({})'.format(str(self.plateSheet.cell(plateNumber,  1).value) ,  self.plateSheet.cell(plateNumber,  2).value[0])
            print(plateNumber)
            plate = ''
        self.plateSet.remove(plateNumber)
        self.luckyPlates.append(plateNumber)
        return plate

    def updateLabelLuckyPlate(self,  count,  maxCount):
        self.labelLuckyPlate.setText("中奖车牌({}/{})".format(count, maxCount))
        
    def updateLabelPlate(self,  text):        
        self.labelPlate.setText(text)
    
    def keyPressEvent(self,  e):
        if e.key() == Qt.Key_Space:
            self.drawAllLuckyPlates()
        if e.key() == Qt.Key_Escape:
            self.close()
        QDialog.keyPressEvent(self,  e)
    
    def drawAllLuckyPlates(self):
        #self.labelLuckyPlates.setText(((self.labelPlate.text() + '\t') * 10 + '\n') * 10)
        self.luckyPlateCount = 0
        self.labelLuckyPlates.setText('')
        if self.standbyPlatesStatus:
            self.luckyPlates = []
            self.groupboxResult.setTitle("备用车牌抽奖结果")
        self.timer.start(50)
        
    def updateLabelLuckyPlates(self):
        self.buttonDraw.setEnabled(False)
        if self.luckyPlateCount >= 100:
            self.timer.stop()
            if self.standbyPlatesStatus == False:
                self.outputLuckyPlates('抽奖结果.xls')
                QMessageBox.warning(self,  '抽奖结束',  "{}个幸运车牌已全部抽出".format(self.maxCount))
                self.buttonDraw.setEnabled(True)
                self.buttonDraw.setText("抽备用车牌")
                #self.buttonCheckResult.setEnabled(True)
                self.standbyPlatesStatus = True
                return
            else:
                #self.luckyPlates = []
                self.outputLuckyPlates('备用抽奖结果.xls')
                QMessageBox.warning(self,  '抽奖结束',  "{}个幸运车牌已全部抽出".format(self.maxCount))
                self.buttonCheckResult.setEnabled(True)
                return
            
        plate = self.chooseOnePlate()
        if self.luckyPlateCount % 8 == 0 and self.luckyPlateCount > 0:
            self.labelLuckyPlates.setText(self.labelLuckyPlates.text() + '\n'+ plate)
        elif self.luckyPlateCount == 0:
             self.labelLuckyPlates.setText(self.labelLuckyPlates.text() + plate)
        else:
            self.labelLuckyPlates.setText(self.labelLuckyPlates.text() + '\t'+ plate)
        self.luckyPlateCount += 1
        self.updateLabelLuckyPlate(self.luckyPlateCount,  self.maxCount)
        self.updateLabelPlate(plate)
    
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
                r = self.luckyPlates[i]
                for c in range(self.plateSheet.ncols):
                    out_sheet.write(i + 1,  c + 1,  self.plateSheet.cell(r,  c).value)
            out_workbook.save(out_file_name)
    
    def checkResult(self):
        import win32api
        win32api.ShellExecute(0,  'open',  '抽奖结果.xls',  '',  './',  1)
        
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

