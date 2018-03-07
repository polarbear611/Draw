if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from DrawDialog import DrawDialog
    app = QApplication(sys.argv)
    drawDialog = DrawDialog()
    drawDialog.show()
    sys.exit(app.exec_())
