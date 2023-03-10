from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
from math import fabs

from prettytable import MSWORD_FRIENDLY


class Ui_MainWindow(object):  # Класс MainWindow наследуем от object
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")  # Главное окно
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_start = QtWidgets.QLineEdit(self.centralwidget)  # начало отрезка
        self.label_start.setGeometry(QtCore.QRect(0, 0, 191, 40))
        self.label_start.setText("")
        self.label_start.setObjectName("label_start")
        self.label_end = QtWidgets.QLineEdit(self.centralwidget)  # конец отрезка
        self.label_end.setGeometry(QtCore.QRect(190, 0, 151, 40))
        self.label_end.setText("")
        self.label_end.setObjectName("label_end")
        self.label_func = QtWidgets.QLineEdit(self.centralwidget)  # ввод функции
        self.label_func.setGeometry(QtCore.QRect(340, 0, 1920, 40))
        self.label_func.setText("")
        self.label_func.setObjectName("label_func")
        # пояснение под вводом всего
        self.text_start = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_start.setGeometry(QtCore.QRect(0, 40, 191, 30))
        self.text_start.setObjectName("text_start")
        self.text_end = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_end.setGeometry(QtCore.QRect(190, 40, 151, 30))
        self.text_end.setObjectName("text_end")
        self.text_func = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_func.setGeometry(QtCore.QRect(340, 40, 1581, 30))
        self.text_func.setObjectName("text_func")
        self.textend = QtWidgets.QTextBrowser(self.centralwidget)
        self.textend.setGeometry(QtCore.QRect(190, 160, 151, 30))
        self.textend.setObjectName("textend")

        self.label_step = QtWidgets.QLineEdit(self.centralwidget)  # шаг деление
        self.label_step.setGeometry(QtCore.QRect(0, 120, 191, 40))
        self.label_step.setText("")
        self.label_step.setObjectName("label_step")
        self.label_eps = QtWidgets.QLineEdit(self.centralwidget)  # точность
        self.label_eps.setGeometry(QtCore.QRect(190, 120, 151, 40))
        self.label_eps.setText("")
        self.label_eps.setObjectName("label_eps")
        # пояснение под вводом
        self.text_step = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_step.setGeometry(QtCore.QRect(0, 160, 191, 30))
        self.text_step.setObjectName("text_step")
        self.text_max_cut = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_max_cut.setGeometry(QtCore.QRect(340, 160, 1581, 31))
        self.text_max_cut.setObjectName("text_max_cut")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)  # максимальное кол-во итераций
        self.spinBox.setGeometry(QtCore.QRect(340, 120, 1581, 40))
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)  # кнопка вычисление
        self.pushButton.setGeometry(QtCore.QRect(0, 210, 1920, 40))
        self.pushButton.setObjectName("pushButton")

        self.out = QtWidgets.QTextBrowser(self.centralwidget)
        self.out.setGeometry(QtCore.QRect(0, 250, 1240, 600))
        self.out.setObjectName("text_max_cut")
        # self.out = QtWidgets.QLabel(self.centralwidget)
        # self.out.setGeometry(QtCore.QRect(0, 250, 1000, 600))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        # font.setPointSize(20)
        # font.setBold(True)
        # font.setWeight(75)
        self.out.setFont(font)
        # self.out.setStyleSheet("background-color: white;\n"
        #                        "color: w;")
        # self.out.setObjectName("out")

        # анатация к графику
        self.text_dop_inf = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_dop_inf.setGeometry(QtCore.QRect(0, 780, 1920, 300))
        self.text_dop_inf.setObjectName("text_dop_inf")
        # Менюшка
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.add_function()  # создаем метод для обработки событий (для всех кнопок)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Имена кнопок и всего
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_start.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Начало Отрезка</p></body></html>"))
        self.text_end.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Конец Отрезка</p></body></html>"))
        self.text_func.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Функция в аналитическом виде</p></body></html>"))
        self.textend.setHtml(_translate("MainWindow",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Точность</p></body></html>"))
        self.text_step.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Шаг Деления</p></body></html>"))
        self.text_max_cut.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                             "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Максимальное кол-во итераций</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Вычислить корни "))

        self.text_dop_inf.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Коды ошибок :</p>\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0- все в порядке</p>\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1- превышено кол-во итераций</p>\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 - не удалось найти крень на отрезке </p>\n"
                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Пояснение к графику:</p>\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">красный - корни</p>\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">синий - экстремумы </p>\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">желтый - точки перегиба</p></body></html>"))

    def table(self, sqrt_mas, otr, val, count, kod):
        mytable = PrettyTable()
        # имена полей таблицы
        mytable.field_names = ["№", "[xi, xi+1]", "x'", "f(x')", "кол-во итераций", "код ошибки"]
        # добавление данных по одной строке за раз
        for i in range(len(sqrt_mas)):
            str_f = float("%12.4e" % (val[i]))
            mytable.add_row([i, otr[i], round(sqrt_mas[i], 3), str_f, count[i], kod[i]])
            # вывод таблицы в терминал
        self.out.setText(str(mytable))

    def add_function(self):
        # обработка события "Вычислить корни"
        self.pushButton.clicked.connect(
            lambda: self.check_data(self.label_func.text(), self.label_start.text(), self.label_end.text(),
                                    self.label_step.text(), self.spinBox.text(), self.label_eps.text()))

    # функция для вычисления корня
    def check_data(self, function_1, start, end, h, nmax, eps):
        flag_error = 0
        flag_error_4diff = 0
        flag_count = False
        # проверка входных данных
        if start > end or nmax == 0 or start == end or h == 0 or eps == 0:
            self.Dialog_error()
            flag_error_4diff = 1
            flag_count = True
        try:
            start = float(start)
            end = float(end)
            h = float(h)
            eps = float(eps)
            nmax = int(nmax)
        except ValueError:
            if flag_count:
                self.Dialog_error()
            flag_error = 10
            flag_count = True
        #  проверка функции
        x = symbols('x')
        try:
            function_1 = eval(function_1)
            first_diff_1 = diff(function_1, x)
            second_diff_1 = diff(first_diff_1, x)

        except:
            if flag_count:
                self.Dialog_error()
            flag_error = 10
            flag_count = True
        # проверка сущ 4 производной
        try:
            first_diff_2 = diff(second_diff_1, x)
            second_diff_2 = diff(first_diff_2, x)
        except:
            if flag_count:
                self.Dialog_error()
            flag_error_4diff = 1

        if flag_error + flag_error_4diff == 0:
            all = self.combined_method(start, end, h, eps, nmax, function_1, first_diff_1, second_diff_1)
            sqrt_mas = all[0]
            val_in_point = []
            for i in sqrt_mas:
                val_in_point.append(self.value_function_in_point(function_1, i))
            otr = all[1]
            self.table(sqrt_mas, otr, val_in_point, all[2], all[3])

            self.paint_graf(start, end, function_1, h, second_diff_1, first_diff_2, second_diff_2, first_diff_1,
                            sqrt_mas)

    def sgn(self, x):
        if (x > 0):
            return 1
        elif (x < 0):
            return -1
        else:
            return 0
    # Функция для поиска корней, комбинированым методом
    def combined_method(self, a, b, h, eps, nmax, func, first_diff, second_diff):

        if self.sgn(self.value_function_in_point(func, a)) * self.sgn(self.value_function_in_point(func, b)) > 0:
            return None
        c = 0.5 * (a + b)
        while (True):
            c = 0.5 * (a + b)
            fc = self.value_function_in_point(func, c)  # единственное вычисление в цикле
            if (fabs(fc) < eps) or (fabs(b - a) < eps):
                return c
            elif self.sgn(self.value_function_in_point(func, a)) * self.sgn(self.value_function_in_point(func, c)) < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc

    def evalf_func(self, fun, point):
        x = symbols('x')
        return fun.evalf(subs={x: point})

    def value_function_in_point(self, fun, point):
        x = symbols('x')
        return fun.evalf(subs={x: point})

    def Dialog_error(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("Вы ввели неверные данные, пожалуйста введите их заново")
        self.msgBox.setWindowTitle("ОшИбКа_228")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = self.msgBox.exec()

    def paint_graf(self, start, end, function_1, h, second_diff_1, first_diff_2, second_diff_2, first_diff_1, sqrt_mas):

        # Количество отсчетов на заданном интервале
        count = 200
        # Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
        xlist = np.linspace(start, end, count)
        # Вычислим значение функции в заданных точках
        ylist = [self.value_function_in_point(function_1, x) for x in xlist]
        # рисуем одномерный график
        plt.plot(xlist, ylist)

        # point of sqrt
        for i in sqrt_mas:
            plt.plot(i, self.value_function_in_point(function_1, i), marker="o", c="r")

        # point of extra point
        mas_extra = self.find_extra_point(start, end, function_1)
        for i in mas_extra:
            plt.plot(i, self.value_function_in_point(function_1, i), marker="o", c="b")
        # point of infliction_point

        flag_x_more_first_step = 0
        for i in str(first_diff_1):
            if i == 'x':
                flag_x_more_first_step = 1

        if flag_x_more_first_step == 1:
            mas_infliction = self.infliction_point(start, end, h, second_diff_1, first_diff_2, second_diff_2)

            for i in mas_infliction:
                plt.plot(i, self.value_function_in_point(function_1, i), marker="o", markersize="3", c="g")

        plt.title(function_1)
        ax = plt.gca()
        # plot X - axis
        ax.axhline(y=0, color='k')
        # plot Y - axis
        ax.axvline(x=0, color='k')
        # подписи снизу с боку
        plt.xlabel(r'$x$')
        plt.ylabel(r'$f(x)$')
        plt.grid(True)  # сеточка
        # Покажем окно с нарисованным графиком
        plt.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)  # обыект, который хранит информацию
    # настроек компе который запустил скрипт
    MainWindow = QtWidgets.QMainWindow()  # окно приложения
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()  # Показ окна
    sys.exit(app.exec_())  # Коректное завершение проги
