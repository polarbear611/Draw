# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QMenu,  QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QPixmap

class FullScreen(QDialog):
    def __init__(self):
        super(QDialog,  self).__init__()
        #self.setStyleSheet("background-color: #FF00FF")
        self.showFullScreen()
        self.setStyleSheet("background-image: url(bg.jpg)")
        self.createContextMenu()
        
    def createContextMenu(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
    
    def showContextMenu(self):
        self. contextMenu = QMenu(self)
        self.contextMenu.setStyleSheet('background: none')
        
        self.actionLuckyOnes = self.contextMenu.addAction('查看中奖名单')
        self.actionLuckyOnes.triggered.connect(self.showLuckyOnes)
        self.contextMenu.exec_(QCursor.pos())
    
    def showLuckyOnes(self):
        QMessageBox.information(self,  '中奖名单',  'XXXXX' * 100)
        
    def keyPressEvent(self,  e):
        if e.key() == Qt.Key_Escape:
            self.close()
        QDialog.keyPressEvent(self,  e)
        
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    fullScreen = FullScreen()
    fullScreen.show()
    sys.exit(app.exec_())
