# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QLabel,  QWidget
from PyQt5.QtGui import QPainter,  QImage,  QPixmap,  QPen,  QGuiApplication
from PyQt5.QtCore import QRect,  Qt
import cv2

class myLabel(QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False

    def mousePressEvent(self,event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()
    def mouseReleaseEvent(self,event):
        self.flag = False

    def mouseMoveEvent(self,event):
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()
    def paintEvent(self, event):
        super().paintEvent(event)
        rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red,4,Qt.SolidLine))
        painter.drawRect(rect)

        pqscreen  = QGuiApplication.primaryScreen()
        pixmap2 = pqscreen.grabWindow(self.winId(), self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
        pixmap2.save('555.png')
    
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(675, 300)
        self.setWindowTitle('opencv、PyQt5的小小融合')

        self.lb = myLabel(self)
        self.lb.setGeometry(QRect(140, 30, 511, 241))

        img = cv2.imread('xxx.jpg')
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(QImg)

        self.lb.setPixmap(pixmap)
        self.lb.setCursor(Qt.CrossCursor)

        self.show()

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())
