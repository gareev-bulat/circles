import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_MainWindow
from random import randint


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.setWindowTitle('Генерация окружностей')
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        radius = randint(5, 80)
        x, y = randint(radius, 800), randint(radius, 510)
        if radius < x < 800 - radius and radius < y < 510 - radius:
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            qp.setBrush(color)
            qp.drawEllipse(x, y, x + radius, x + radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())