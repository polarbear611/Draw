# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread,  pyqtSignal
import random

class DrawThread(QThread):
    choosePlate = pyqtSignal(str)
    def __init__(self):
        super(QThread,  self).__init__()
    
    def run(self):
        self.choosePlate.emit(random.choice(list('abc')))
