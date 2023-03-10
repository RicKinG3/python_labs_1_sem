from PyQt5 import QtCore, QtGui, QtWidgets  # Импортируем QtCore (обработка событий и сигналов)
from PyQt5.QtWidgets import QMessageBox
# QtGui — работает с графическими элементами
# QtWidgets создания классических пользовательских интерфейсов
from PyQt5.QtWidgets import QLineEdit


class Ui_MainWindow(object):  # Класс MainWindow наследуем от object
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")  # Главное окно
        MainWindow.resize(600, 666)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.in_ = QtWidgets.QLineEdit(self.centralwidget)
        self.in_.setGeometry(QtCore.QRect(0, 0, 600, 71))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.in_.setFont(font)
        self.in_.setStyleSheet("background-color: rgba(61, 170, 139, 230);\n"
                               "color: rgb(255, 255, 255);")
        self.in_.setObjectName("in_")

        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 540, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        #  Кнопка "0"
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: rgba(52, 143, 170, 200);\n"
                                 "color: rgb(255, 255, 230);")
        self.btn_0.setObjectName("btn_0")
        # Кнопка ","
        self.btn_point = QtWidgets.QPushButton(self.centralwidget)
        self.btn_point.setGeometry(QtCore.QRect(200, 540, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_point.setFont(font)
        self.btn_point.setStyleSheet("background-color: rgba(255, 207, 151, 230);\n"
                                     "color: rgb(255, 255, 255);")
        self.btn_point.setAutoRepeat(False)
        self.btn_point.setAutoExclusive(False)
        self.btn_point.setObjectName("btn_point")
        # Кнопка "="
        self.btn_eq = QtWidgets.QPushButton(self.centralwidget)
        self.btn_eq.setGeometry(QtCore.QRect(400, 540, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.btn_eq.setFont(font)
        self.btn_eq.setStyleSheet("background-color: rgba(255, 207, 151, 230);\n"
                                  "color: rgb(255, 255, 255);")
        self.btn_eq.setObjectName("btn_eq")
        # Кнопка "1"
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 440, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgba(52, 143, 170, 200);\n"
                                 "color: rgb(255, 255, 230);")
        self.btn_1.setObjectName("btn_1")
        # Кнопка "2"
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(200, 440, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgba(52, 143, 170, 200);\n"
                                 "color: rgb(255, 255, 230);")
        self.btn_2.setObjectName("btn_2")
        # Кнопка "3"
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(400, 440, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgba(52, 143, 170, 200);\n"
                                 "color: rgb(255, 255, 230);")
        self.btn_3.setObjectName("btn_3")
        # Кнопка "4"
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 340, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgba(52, 143, 170, 200);\n"
                                 "color: rgb(255, 255, 230);")
        self.btn_4.setObjectName("btn_4")
        # Кнопка "5"
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(200, 340, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgba(52, 143, 170, 200);\n"
                                 "color: rgb(255, 255, 230);")
        self.btn_5.setObjectName("btn_5")
        # Кнопка "6"
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(400, 340, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgba(52, 143, 170, 200);\n"
                                 "color: rgb(255, 255, 230);")
        self.btn_6.setObjectName("btn_6")
        # Кнопка "7"
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(200, 240, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgba(52, 143, 170, 200);\n"
                                 "color: rgb(255, 255, 230);")
        self.btn_7.setObjectName("btn_7")
        # Кнопка "8"
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(0, 240, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgba(52, 143, 170, 200);\n"
                                 "color: rgb(255, 255, 230);")
        self.btn_8.setObjectName("btn_8")
        # Кнопка "9"
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(400, 240, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgba(52, 143, 170, 200);\n"
                                 "color: rgb(255, 255, 230);")
        self.btn_9.setObjectName("btn_9")
        # combobox "10<->6"
        self.comboBox_10 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_10.setGeometry(QtCore.QRect(0, 140, 91, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_10.setFont(font)
        self.comboBox_10.setStyleSheet("background-color: rgba(170, 46, 160, 230);\n"
                                       "color: rgb(255, 255, 230);")
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        # Значек стрелочки
        self.arrow = QtWidgets.QLabel(self.centralwidget)
        self.arrow.setGeometry(QtCore.QRect(90, 140, 71, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.arrow.setFont(font)
        self.arrow.setStyleSheet("background-color: rgba(255, 207, 151, 230);")
        self.arrow.setObjectName("arrow")
        # combobox "10<->6"
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(160, 140, 81, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setStyleSheet("background-color: rgba(170, 46, 160, 230);\n"
                                      "color: rgb(255, 255, 230);")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        # Кнопка удаления одного символа
        self.btn_clear_one = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear_one.setGeometry(QtCore.QRect(501, 140, 101, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear_one.setFont(font)
        self.btn_clear_one.setStyleSheet("background-color: rgba(0, 65, 196, 230);\n"
                                         "color: rgb(255, 255, 255);")
        self.btn_clear_one.setObjectName("btn_clear_one")
        # Кнопка удаления ввода
        self.btn_clear_in = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear_in.setGeometry(QtCore.QRect(330, 140, 71, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear_in.setFont(font)
        self.btn_clear_in.setStyleSheet("background-color: rgba(215, 71, 107, 230);\n"
                                        "")
        self.btn_clear_in.setObjectName("btn_clear_in")
        # Поле вывода
        self.out = QtWidgets.QLabel(self.centralwidget)
        self.out.setGeometry(QtCore.QRect(0, 70, 600, 71))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.out.setFont(font)
        self.out.setStyleSheet("background-color: rgb(69, 139, 208);\n"
                               "color: rgb(255, 255, 255);")
        self.out.setObjectName("out")
        # Кнопка удаления всего
        self.btn_clear_all = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear_all.setGeometry(QtCore.QRect(240, 140, 91, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear_all.setFont(font)
        self.btn_clear_all.setStyleSheet("background-color: rgb(255, 255, 127);\n"
                                         "\n"
                                         "")
        self.btn_clear_all.setObjectName("btn_clear_all")
        # Кнопка минуса
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(400, 140, 101, 100))
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(255, 170, 255);\n"
                                     "\n"
                                     "")
        self.btn_minus.setObjectName("btn_minus")

        self.add_function()  # создаем метод для обработки событий (для всех кнопок)

        # МЕНЮ
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 18))
        self.menubar.setObjectName("menubar")
        self.menu_translation = QtWidgets.QMenu(self.menubar)
        self.menu_translation.setObjectName("menu_translation")
        self.menu_clear = QtWidgets.QMenu(self.menubar)
        self.menu_clear.setObjectName("menu_clear")
        self.menu_info = QtWidgets.QMenu(self.menubar)
        self.menu_info.setObjectName("menu_info")
        MainWindow.setMenuBar(self.menubar)
        self.menu_ten_in_six = QtWidgets.QAction(MainWindow)
        self.menu_ten_in_six.setObjectName("menu_ten_in_six")
        self.menu_clear_all = QtWidgets.QAction(MainWindow)
        self.menu_clear_all.setObjectName("menu_clear_all")
        self.menu_clear_in = QtWidgets.QAction(MainWindow)
        self.menu_clear_in.setObjectName("menu_clear_in")
        self.menu_info_prog = QtWidgets.QAction(MainWindow)
        self.menu_info_prog.setObjectName("menu_info_prog")
        self.menu_info_avtor = QtWidgets.QAction(MainWindow)
        self.menu_info_avtor.setObjectName("menu_info_avtor")
        self.menu_clear_out = QtWidgets.QAction(MainWindow)
        self.menu_clear_out.setObjectName("menu_clear_out")
        self.menu_translation.addAction(self.menu_ten_in_six)
        self.menu_clear.addAction(self.menu_clear_all)
        self.menu_clear.addAction(self.menu_clear_in)
        self.menu_clear.addAction(self.menu_clear_out)
        self.menu_info.addAction(self.menu_info_prog)
        self.menu_info.addAction(self.menu_info_avtor)
        self.menubar.addAction(self.menu_translation.menuAction())
        self.menubar.addAction(self.menu_clear.menuAction())
        self.menubar.addAction(self.menu_info.menuAction())
        # События менюшки
        self.menu_info_prog.triggered.connect(lambda: self.Dialog_about_prog())
        self.menu_info_avtor.triggered.connect(lambda: self.Dialog_about_avtor())
        self.menu_clear_in.triggered.connect(lambda: self.del_in())
        self.menu_clear_all.triggered.connect(lambda: self.del_all())
        self.menu_clear_out.triggered.connect(lambda: self.del_one())
        self.menu_ten_in_six.triggered.connect(lambda: self.results(self.in_.text()))



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Имена кнопок и всего

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My Calc"))
        self.in_.setText(_translate("MainWindow", ""))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_point.setText(_translate("MainWindow", "."))
        self.btn_eq.setText(_translate("MainWindow", "="))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "8"))
        self.btn_8.setText(_translate("MainWindow", "7"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "10"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "6"))
        self.arrow.setText(_translate("MainWindow", "  →"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "10"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "6"))
        self.btn_clear_one.setText(_translate("MainWindow", "⌫"))
        self.btn_clear_in.setText(_translate("MainWindow", "c"))
        self.out.setText(_translate("MainWindow", ""))
        self.btn_clear_all.setText(_translate("MainWindow", "CE"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.menu_translation.setTitle(_translate("MainWindow", "Перевод"))
        self.menu_clear.setTitle(_translate("MainWindow", "Очистка"))
        self.menu_info.setTitle(_translate("MainWindow", "Инфо"))
        self.menu_ten_in_six.setText(_translate("MainWindow", "Выполнить перевод"))
        self.menu_clear_all.setText(_translate("MainWindow", "Удалить все"))
        self.menu_clear_in.setText(_translate("MainWindow", "Удалить поле ввода"))
        self.menu_info_prog.setText(_translate("MainWindow", "О программе"))
        self.menu_info_avtor.setText(_translate("MainWindow", "О авторе"))
        self.menu_clear_out.setText(_translate("MainWindow", "Удалить один символ"))
        # Функция для обработки событий

    def add_function(self):
        # Событие меню

        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_0.setShortcut('0')

        # Обращаемся к btn_0  потом к clicked->connect (какой метод будет срабатывать) -> lambda
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_point.clicked.connect(lambda: self.write_number(self.btn_point.text()))
        self.btn_clear_in.clicked.connect(self.del_in)
        self.btn_clear_one.clicked.connect(self.del_one)
        self.btn_clear_all.clicked.connect(self.del_all)
        # обработка события "="
        self.btn_eq.clicked.connect(lambda: self.results(self.in_.text()))

        # обработка события "-"
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))

    def del_in(self):
        if self.in_.text() != '0':
            self.in_.setText('')

    def del_one(self):
        self.in_.setText(self.in_.text()[:-1])

    def del_all(self):
        self.in_.setText('')
        self.out.setText('')

        # Функция для ввода цифр

    def write_number(self, number):

        if self.in_.text() == "":
            self.in_.setText(number)
        else:
            self.in_.setText(self.in_.text() + number)
            self.check_in_minus()
            self.check_in_point()

    def check_in_minus(self):
        if '-' in self.in_.text()[1::] and '-' == self.in_.text()[0]:
            self.in_.setText(self.in_.text()[:-1])
        elif '-' in self.in_.text()[1::] and '-' != self.in_.text()[0]:
            self.in_.setText('-' + self.in_.text()[:-1])

    def check_in_point(self):
        if '.' == self.in_.text()[0]:
            self.in_.setText('0' + self.in_.text())
        elif ('.' in self.in_.text()[:-1]) and (self.in_.text()[-1] == '.'):
            self.in_.setText(self.in_.text()[:-1])

    # Функция для вывода резульата
    def results(self, number):
        res_left = self.comboBox_10.currentText()  # считываем выбор из комбобокса слева
        res_right = self.comboBox_6.currentText()
        alfa = '''qwertyuiop[]asdfghjkl;'zxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,/!@#$%^&*()_+йцукенгшщзхъ\|фывапролджэячсмитьбю!"№;%:?ЙУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'''

        for i in number:
            if i in alfa:
                self.in_.setText('')
                self.out.setText('')
                self.Dialog_error_str()
                break

        if res_right == res_left or self.in_.text() == '':
            self.in_.setText('')
            self.out.setText('')
            if res_right == res_left:
                self.Dialog_error_onetype()
        elif self.in_.text() == '0' or self.in_.text() == '0.0' or self.in_.text() == '-0' or self.in_.text() == '-0.0':
            if self.in_.text() == '0' or self.in_.text() == '-0':
                self.out.setText('0')
            elif self.in_.text() == '0.0' or self.in_.text() == '-0.0':
                self.out.setText('0.0')
        elif self.in_.text()[-1] == '.':
            self.in_.setText(self.in_.text()[:-1])

        else:
            flag_minus = False
            if res_left == '10':
                if float(number) < 0:
                    number = number[1:]
                    flag_minus = True
                self.translate_10_in_6(number, flag_minus)
            else:
                f = False
                if '6' in number or '7' in number or '8' in number or '9' in number or '9' in number:
                    self.Dialog_error_six()
                    self.in_.setText('')
                    self.out.setText('')
                    f = True
                elif float(number) < 0:
                    number = number[1:]
                    flag_minus = True
                self.translate_6_in_10(number, flag_minus, f)

    # числа > 5
    def Dialog_error_six(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("Вы ввели цифры > 5 ")
        self.msgBox.setWindowTitle("ОшИбКа_226")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = self.msgBox.exec()

    # Один тип перевода
    def Dialog_error_onetype(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("Вы выброли одну СС")
        self.msgBox.setWindowTitle("ОшИбКа_227")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = self.msgBox.exec()

    # Диалоговое окно ошибки символьные
    def Dialog_error_str(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("Вы ввели недопустимые символы!")
        self.msgBox.setWindowTitle("ОшИбКа_228")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # self.msgBox.buttonClicked.connect(self.msgButtonClick)

        returnValue = self.msgBox.exec()
        # if returnValue == QMessageBox.Ok:
        # print('OK clicked')

    # ДИалоговое окошко меню о проги
    def Dialog_about_prog(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("На данную прогу я потратил слишком много времени( ")
        self.msgBox.setWindowTitle("О Программе")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = self.msgBox.exec()

    def Dialog_about_avtor(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("Вольняга Максим ИУ7-26Б")
        self.msgBox.setWindowTitle("О Авторе")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = self.msgBox.exec()

    def translate_10_in_6(self, number, flag):

        if '.' in number:
            new_num_int = ''
            new_num_float = ''
            num_int = int(str(number).split('.')[0])
            num_float = str(number).split('.')[1]

            while num_int > 0:
                new_num_int = str(num_int % 6) + new_num_int
                num_int //= 6

            count = 0
            num_float = '0.' + num_float
            while count != 8:
                num_float = float(num_float) * 6
                if int(str(num_float).split('.')[0]) >= 1:
                    new_num_float += str(num_float).split('.')[0]
                    num_float = str('0.' + str(num_float).split('.')[1])
                else:
                    new_num_float += str(num_float).split('.')[0]
                num_float = float(num_float)
                count += 1
            num_in_6 = str(new_num_int + '.' + new_num_float)
            if flag:
                self.out.setText('-' + num_in_6)
            else:
                self.out.setText(num_in_6)
        else:
            num_int = int(number)
            new_num_int = ''
            while num_int > 0:
                new_num_int = str(num_int % 6) + new_num_int
                num_int //= 6
            if flag:
                self.out.setText('-' + new_num_int)
            else:
                self.out.setText(new_num_int)
        if self.in_.text()[0] == '0' and self.in_.text()[1] == '.':
            self.out.setText('0.' + new_num_float)
        # return num_in_6

    def translate_6_in_10(self, num, flag, f):
        new_num_int = 0
        new_num_float = 0
        num = float(num)
        if f:
            self.in_.setText('')

        elif isinstance(num, float):
            num_int = str(num).split('.')[0]
            num_float = str(num).split('.')[1]
            len_num_int = len(str(num_int)) - 1
            len_num_float = len(str(num_float))

            for i in range(len_num_int + 1):
                new_num_int += int(str(num_int[i])) * (6 ** len_num_int)
                len_num_int -= 1

            for i in range(len_num_float):
                new_num_float += int(str(num_float[i])) * (6 ** (-(i + 1)))
        else:
            num_int = int(num)
            len_num_int = len(str(num_int)) - 1
            for i in range(len_num_int + 1):
                new_num_int += int(str(num_int[i])) * (6 ** len_num_int)
                len_num_int -= 1

        if flag and not f:
            self.out.setText('-' + str(new_num_int) + '.' + str(new_num_float).split('.')[1])
        elif not flag and not f:
            self.out.setText(str(new_num_int) + '.' + str(new_num_float).split('.')[1])

    # return str(new_num_int) + '.' + str(new_num_float).split('.')[1]


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)  # обыект, который хранит информацию
    # настроек компе который запустил скрипт
    MainWindow = QtWidgets.QMainWindow()  # окно прилодения
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()  # Показ окна
    sys.exit(app.exec_())  # Коректное завершение проги
