import math
import operator
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import kalk


class Example(QMainWindow, kalk.Ui_MainWindow):
    def __init__(self):
        self.isTrue = False
        self.is_point = False
        self.op = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}
        self.s1 = '0'
        self.chis = '0'
        self.operat = ''
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # числа
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

        # вызов функции операторов
        self.addB.clicked.connect(self._add_def)
        self.decreaceB.clicked.connect(self._dec_def)
        self.mulB.clicked.connect(self._mul_def)
        self.delB.clicked.connect(self._del_def)
        self.ravnoB.clicked.connect(self._ravn_def)

        # вызов функций спецоператоров

        # self.log2xB.clicked.connect(self.logx2_def)
        self.fact.clicked.connect(self._fact)
        # self.hex.isCheck.connect(lambda: self.vyvod.setMode("Hex"))
        self.point.clicked.connect(self._point_def)

    #
    # def logx2_def(self):
    #     self.chis = str(math.log2(int(self.chis)))
    #     self.vyvid_def()

    def vyvid_def(self):
        self.vyvod.display(self.chis)

    def _point_def(self):
        self.is_point = True
        self.chis = str(self.chis + '.')
        self.vyvod.display(self.chis)

    def clear_display(self):
        self.vyvod.display = ''
        self.chis = ''

    #
    def _fact(self):
        if self.chis < '35':
            self.chis = str(math.factorial(int(self.chis)))
            self.isTrue = True
        self.vyvid_def()

    def _1(self):
        if self.isTrue:
            self.chis = '' + '1'
            self.isTrue = False
        else:
            self.chis = str(int(self.chis + '1'))
        self.vyvid_def()

    def _0(self):
        if self.isTrue:
            self.chis = '' + '0'
            self.isTrue = False
        else:
            self.chis = str(int(self.chis + '0'))
        self.vyvid_def()

    def _2(self):
        if self.isTrue:
            self.chis = '' + '2'
            self.isTrue = False
        else:
            self.chis = str(int(self.chis + '2'))
        self.vyvid_def()

    def _3(self):
        if self.isTrue:
            self.chis = '' + '3'
            self.isTrue = False
        else:
            self.chis = str(int(self.chis + '3'))
        self.vyvid_def()

    def _4(self):
        if self.isTrue:
            self.chis = '' + '4'
            self.isTrue = False
        else:
            self.chis = str(int(self.chis + '4'))
        self.vyvid_def()

    def _5(self):
        if self.isTrue:
            self.chis = '' + '5'
            self.isTrue = False
        else:
            self.chis = str(int(self.chis + '5'))
        self.vyvid_def()

    def _6(self):
        if self.isTrue:
            self.chis = '' + '6'
            self.isTrue = False
        else:
            self.chis = str(int(self.chis + '6'))
        self.vyvid_def()

    def _7(self):
        if self.isTrue:
            self.chis = '' + '7'
            self.isTrue = False
        else:
            self.chis = str(int(self.chis + '7'))
        self.vyvid_def()

    def _8(self):
        if self.isTrue:
            self.chis = '' + '8'
            self.isTrue = False
        else:
            self.chis = str(int(self.chis + '8'))
        self.vyvid_def()

    def _9(self):
        if self.isTrue:
            self.chis = '' + '9'
            self.isTrue = False
        else:
            self.chis = str(int(self.chis + '9'))
        self.vyvid_def()

    def _ravn_def(self):
        # print(self.chis, self.s1, self.operat)
        if (self.operat == '/' and self.chis != '0') or self.operat in '*-+' and self.is_point:
            self.chis = str(float(self.op.get(self.operat)(int(self.s1), int(self.chis))))
        else:
            self.chis = str(int(self.op.get(self.operat)(int(self.s1), int(self.chis))))
        self.vyvid_def()
        self.isTrue = True
        self.is_point = False

    def _add_def(self):
        self.s1 = self.chis
        self.chis = ''
        if self.s1 != '' and self.chis == '':
            self.operat = '+'
        self.vyvid_def()

    def _dec_def(self):
        self.s1 = self.chis
        self.chis = ''
        if self.s1 != '' and self.chis == '':
            self.operat = '-'
        self.vyvid_def()

    def _mul_def(self):
        self.s1 = self.chis
        self.chis = ''
        if self.s1 != '' and self.chis == '':
            self.operat = '*'
        self.vyvid_def()

    def _del_def(self):
        self.s1 = self.chis
        self.chis = ''
        if self.s1 != '' and self.chis == '':
            self.operat = '/'
        self.vyvid_def()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
