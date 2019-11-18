import math
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import kalk


class Example(QMainWindow, kalk.Ui_MainWindow):
    def __init__(self):
        self.s1 = ''
        self.chis = '0'
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.one.clicked.connect(self._1)
        self.two.clicked.connect(self._2)
        self.three.clicked.connect(self._3)
        self.four.clicked.connect(self._4)
        self.five.clicked.connect(self._5)
        self.six.clicked.connect(self._6)
        self.seven.clicked.connect(self._7)
        self.vosem.clicked.connect(self._8)
        self.nine.clicked.connect(self._9)
        self.zero.clicked.connect(self._0)

        self.fact.clicked.connect(self._fact)
        # self.hex.isCheck.connect(lambda: self.vyvod.setMode("Hex"))

    def vyvid_def(self):
        self.vyvod.display(self.chis)

    def clear_display(self):
        self.vyvod.display = ''
        self.s1 = self.chis

    def _fact(self):
        if self.chis < '35':
            self.chis = str(math.factorial(int(self.chis)))
        print(self.chis)
        self.vyvid_def()

    def _1(self):
        self.chis = str(int(self.chis + '1'))
        self.vyvid_def()

    def _0(self):
        self.chis = str(int(self.chis + '0'))
        self.vyvid_def()

    def _2(self):
        self.chis = str(int(self.chis + '2'))
        self.vyvid_def()

    def _3(self):
        self.chis = str(int(self.chis + '3'))
        self.vyvid_def()

    def _4(self):
        self.chis = str(int(self.chis + '4'))
        self.vyvid_def()

    def _5(self):
        self.chis = str(int(self.chis + '5'))
        self.vyvid_def()

    def _6(self):
        self.chis = str(int(self.chis + '6'))
        self.vyvid_def()

    def _7(self):
        self.chis = str(int(self.chis + '7'))
        self.vyvid_def()

    def _8(self):
        self.chis = str(int(self.chis + '8'))
        self.vyvid_def()

    def _9(self):
        self.chis = str(int(self.chis + '9'))
        self.vyvid_def()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
