import random
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import *


class Canvas(QWidget):
    def __init__(self):
        super(Canvas, self).__init__()
        self.pb_clicked = False

    def paintEvent(self, event):
        if self.pb_clicked:
            p = QPainter()
            p.begin(self)
            p.setBrush(QColor('yellow'))
            w, h = self.width(), self.height()
            a = max(min(w, h) // 2, 5)
            n = random.randint(1, 10)
            for i in range(n):
                d = random.randint(5, a)
                x = random.randint(0, w - d)
                y = random.randint(0, h - d)
                p.drawEllipse(x, y, d, d)
            p.end()
            self.pb_clicked = False


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.canvas = Canvas()
        self.verticalLayout.addWidget(self.canvas)
        self.pushButton.clicked.connect(self.repaint_canvas)

    def repaint_canvas(self):
        self.canvas.pb_clicked = True
        self.canvas.repaint()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
