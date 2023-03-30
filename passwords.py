from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWinExtras import QtWin
from PyQt5.QtWidgets import QMessageBox
import random, configparser, urllib, os, datetime, requests, pyautogui as pag
import os.path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.default_palette = QtGui.QGuiApplication.palette()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(379, 245)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(30, 0, 350, 55))
        self.display.setObjectName("display")
        self.display_2 = QtWidgets.QLabel(self.centralwidget)
        self.display_2.setGeometry(QtCore.QRect(5, 60, 0, 0))
        self.display_2.setObjectName("display_2")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.update())
        self.btn_update.setGeometry(QtCore.QRect(380, 200, 150, 30))
        self.btn_update.setObjectName("btn_update")
        self.btn_update.setText("Сохранить изменения")
        self.display_passwords = QtWidgets.QTextEdit(MainWindow)
        self.display_passwords.setGeometry(QtCore.QRect(380, 5, 300, 200))
        self.display_passwords.setObjectName("display_passwords")
        self.display_passwords.textChanged.connect(lambda: self.izm())
        self.btn_Change_password = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Change_password())
        self.btn_Change_password.setGeometry(QtCore.QRect(530, 200, 150, 30))
        self.btn_Change_password.setObjectName("btn_Change_password")
        self.btn_Change_password.setText("Сменить\\убрать пароль")
        self.create = QtWidgets.QPushButton(self.centralwidget, clicked  = lambda: self.create_password())
        self.create.setGeometry(QtCore.QRect(55, 150, 120, 70))
        self.create.setObjectName("create")
        self.show_passwords_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.show_passwords())
        self.show_passwords_button.setGeometry(QtCore.QRect(240, 45, 0, 0))
        self.show_passwords_button.setObjectName("show_passwords_button")
        self.show_passwords_button.setText("Показать пароли")
        self.show_passwords_button.adjustSize()
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.change_btn_plus())
        self.btn_plus.setGeometry(QtCore.QRect(130, 50, 20, 20))
        self.btn_plus.setObjectName("btn_plus")
        self.btn_plus.setText("+")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.change_btn_minus())
        self.btn_minus.setGeometry(QtCore.QRect(130, 70, 20, 20))
        self.btn_minus.setObjectName("btn_minus")
        self.btn_minus.setText("-")
        self.btn_copy = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.copy_password())
        self.btn_copy.setGeometry(QtCore.QRect(15, 110, 0, 0))
        self.btn_copy.setObjectName("btn_copy")
        self.btn_copy.setText("Копировать")
        self.btn_copy.setEnabled(False)
        self.btn_copy.adjustSize()
        self.btn_save = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.save_password())
        self.btn_save.setGeometry(QtCore.QRect(135, 110, 0, 0))
        self.btn_save.setObjectName("btn_save")
        self.btn_save.setText("Сохранить")
        self.btn_save.setEnabled(False)
        self.btn_save.adjustSize()
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.reset())
        self.btn_reset.setGeometry(QtCore.QRect(0, 15, 25, 25))
        self.btn_reset.setObjectName("btn_reset")
        self.btn_reset.setText("⭯")
        self.btn_reset.setEnabled(False)
        self.checkBox_nums = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_nums.setGeometry(QtCore.QRect(240, 120, 81, 20))
        self.checkBox_nums.setObjectName("checkBox_nums")
        self.checkBox_nums.clicked.connect(lambda: self.check())
        self.checkBox_other = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_other.setGeometry(QtCore.QRect(240, 80, 81, 20))
        self.checkBox_other.setObjectName("checkBox_other")
        self.checkBox_other.clicked.connect(lambda: self.check())
        self.checkBox_lettrs_big = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_lettrs_big.setGeometry(QtCore.QRect(240, 160, 81, 20))
        self.checkBox_lettrs_big.setObjectName("checkBox_lettrs_big")
        self.checkBox_lettrs_big.clicked.connect(lambda: self.check())
        self.checkBox_lettrs_little = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_lettrs_little.setGeometry(QtCore.QRect(240, 200, 81, 20))
        self.checkBox_lettrs_little.setObjectName("checkBox_lettrs_little")
        self.checkBox_lettrs_little.clicked.connect(lambda: self.check())
        self.btn_Theme = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Theme_Change_color())
        self.btn_Theme.setGeometry(QtCore.QRect(0, 185, 35, 35))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.password_n = None
        self.saves = 0
        self.position = False
        self.password_file = ""
        self.password = ""
        self.chang = False
        self.action = False
        self.check_condition()
        self.Theme_Change()
        self.load_settings()
        self.check()

    def configurate(self):
        config = configparser.ConfigParser()
        config['DEFAULT'] = {"x": "12", 'other': True, 'nums': True, 'letters_big': True, 'letters_little': True}
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)

    def load_settings(self):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        self.x = (config["DEFAULT"].getint("x"))
        self.display_2.setText("Число символов: " + str(self.x))
        self.display_2.adjustSize()
        self.checkBox_other.setChecked(config["DEFAULT"].getboolean("other"))
        self.checkBox_nums.setChecked(config["DEFAULT"].getboolean("nums"))
        self.checkBox_lettrs_big.setChecked(config["DEFAULT"].getboolean("letters_big"))
        self.checkBox_lettrs_little.setChecked(config["DEFAULT"].getboolean("letters_little"))

    def check(self):
        if self.checkBox_other.isChecked() and self.checkBox_lettrs_big.isChecked() and self.checkBox_lettrs_little.isChecked() and self.checkBox_nums.isChecked() and self.x == 12:
            self.btn_reset.setEnabled(False)
        else:
            self.btn_reset.setEnabled(True)
        self.save_settings()

    def save_settings(self):
        config2 = configparser.ConfigParser()
        config2['DEFAULT'] = {'x': self.x, 'other': self.checkBox_other.isChecked(), 'nums': self.checkBox_nums.isChecked(), 'letters_big': self.checkBox_lettrs_big.isChecked(), 'letters_little': self.checkBox_lettrs_little.isChecked()}
        with open('settings.ini', 'w') as configfile:
            config2.write(configfile)

    def reset(self):
        self.x = 12
        self.display_2.setText("Число символов: " + str(self.x))
        self.display_2.adjustSize()
        self.checkBox_nums.setChecked(True)
        self.checkBox_lettrs_little.setChecked(True)
        self.checkBox_lettrs_big.setChecked(True)
        self.checkBox_other.setChecked(True)
        self.btn_reset.setEnabled(False)
        self.save_settings()

    def err(self):
        error = QMessageBox()
        error.setIcon(QMessageBox.Warning)
        error.setWindowTitle("Error")
        error.setText("Ошибка сети\nмогут возникнуть проблемы")
        error.setStandardButtons(QMessageBox.Ok|QMessageBox.Close)
        error.setDefaultButton(QMessageBox.Close)
        error.buttonClicked.connect(self.fix)
        error.exec_()

    def check_condition(self):
        try:
            urllib.request.urlopen("http://google.com")
            self.internet = True
        except IOError:
            self.internet = False
        self.img = os.path.exists("sun.jpg")
        self.set = os.path.exists("settings.ini")
        if self.internet == False and self.img == True or self.internet == True and self.img == True:
            self.Theme_Change()
        if self.internet == True and self.img == False:
            self.download_img()
        if self.set == False:
            self.configurate()
        if self.internet == False and self.img == False:
            self.err()

    def fix(self, btn):
        if btn.text() == "Close":
            sys.exit()
        else:
            pass

    def Theme_Change_color(self):
        with open("Theme.txt", "r") as col:
            self.colors = col.read()
        with open("Theme.txt", "w") as color:
            if self.colors == "White":
                color.write("Dark")
                self.btn_Theme.setIcon(QIcon('sun.jpg'))
                self.Dark()
            if self.colors == "Dark":
                color.write("White")
                self.btn_Theme.setIcon(QIcon('moon.jpg'))
                self.White()

    def download_icn(self):
        url3 = "https://i.stack.imgur.com/8Iggk.png"
        name3 = "icn.png"
        img3 = requests.get(url3)
        img_option3 = open(name3, "wb")
        img_option3.write(img3.content)
        img_option3.close()

    def Theme_Change(self):
        try:
            with open("Theme.txt", "r") as Th:
                try:
                    myappid = 'mycompany.myproduct.subproduct.version'
                    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
                except ImportError:
                    pass
                MainWindow.setWindowIcon(QIcon("icn.png"))
                if Th.read() == "Dark":
                    self.btn_Theme.setIcon(QIcon('sun.jpg'))
                    self.btn_Theme.setIconSize(QSize(34, 34))
                    self.Dark()
                else:
                    self.btn_Theme.setIcon(QIcon('moon.jpg'))
                    self.btn_Theme.setIconSize(QSize(34, 34))
                    self.White()
        except:
            with open("Theme.txt", "w") as erro:
                erro.write("Dark")
            self.Theme_Change()

    def download_img(self):
        try:
            url = "https://catherineasquithgallery.com/uploads/posts/2021-02/1614438374_7-p-solntse-na-temnom-fone-8.jpg"
            url2 = "https://follizin.com/img/cms/Moon.png"
            name = "sun.jpg"
            name2 = "moon.jpg"
            img = requests.get(url)
            img2 = requests.get(url2)
            img_option = open(name, "wb")
            img_option.write(img.content)
            img_option.close()
            img_option2 = open(name2, "wb")
            img_option2.write(img2.content)
            img_option2.close()
            self.download_icn()
            self.Theme_Change()
        except:
            self.err()

    def Dark(self):
        self.color = False
        self.show_passwords_button.setStyleSheet("color: black;")
        self.show_passwords_button.setStyleSheet("background-color: rgb(41, 44, 51);")
        darkpalette = QtGui.QPalette()
        darkpalette.setColor(QtGui.QPalette.Window, QtGui.QColor(41, 44, 51))
        darkpalette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
        darkpalette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
        darkpalette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(41, 44, 51))
        darkpalette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
        darkpalette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
        darkpalette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        darkpalette.setColor(QtGui.QPalette.Button, QtGui.QColor(41, 44, 51))
        darkpalette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
        darkpalette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
        darkpalette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(100, 100, 225))
        darkpalette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
        QtGui.QGuiApplication.setPalette(darkpalette)

    def White(self):
        self.color = True
        self.show_passwords_button.setStyleSheet("background-color: white; color: black;")
        QtGui.QGuiApplication.setPalette(self.default_palette)

    def btn_save_None(self):
        if self.password_n != None:
            self.btn_save.setEnabled(True)
        else:
            pass

    def izm(self):
        self.chang = True
        self.btn_update.setText("Сохранить изменения")
        self.btn_update.setEnabled(True)

    def Change_password(self):
        self.show_passwords_button.setEnabled(False)
        self.btn_save.setEnabled(False)
        self.btn_Change_password.setEnabled(False)
        new_password = pag.prompt("Введите новый пароль и запомните его:\n(нечего не вводите чтобы отключить ввод пароля)")
        for i in range(666):
            QApplication.processEvents()
            pass
        self.show_passwords_button.setEnabled(True)
        self.btn_save_None()
        self.btn_Change_password.setEnabled(True)
        if new_password != None:
            with open("password_file.txt", "w") as np:
                try:
                    np.write(new_password)
                    self.password = new_password
                    if self.password == "":
                        self.btn_Change_password.setText("Установить пароль")
                    else:
                        self.btn_Change_password.setText("Сменить\\убрать пароль")
                except:
                    pass
        else:
            pass

    def update(self):
        with open("st.txt", "w") as m:
            m.write(self.display_passwords.toPlainText())
            self.btn_update.setText("Изменения сохранены!")
            self.btn_update.setEnabled(False)
            self.chang = False

    def show_passwords(self):
        if self.position == False:
            try:
                with open("password_file.txt", "r") as password_file:
                        self.password_file = password_file.read()
                if self.password_file == "":
                    self.btn_Change_password.setText("Установить пароль")
                else:
                    self.btn_Change_password.setText("Сменить\\убрать пароль")
            except:
                with open("password_file.txt", "a") as er:
                    er.write("")
            if self.password_file != "":
                self.show_passwords_button.setEnabled(False)
                self.btn_save.setEnabled(False)
                self.btn_Change_password.setEnabled(False)
                self.password = pag.prompt("Введите пароль")
                self.action = True
                for i in range(666):
                    QApplication.processEvents()
                    pass
                self.action = False
                self.show_passwords_button.setEnabled(True)
                self.btn_save_None()
                self.btn_Change_password.setEnabled(True)
            else:
                pass
            if self.password == self.password_file:
                if self.color == True:
                    self.show_passwords_button.setStyleSheet("background-color: white;")
                elif self.color == False:
                    self.show_passwords_button.setStyleSheet("background-color: rgb(41, 44, 51);")
                MainWindow.setFixedSize(685, 255)
                self.show_passwords_button.setText("Скрыть пароли")
                self.show_passwords_button.adjustSize()
                self.position = True
                try:
                    with open("st.txt", "r") as file:
                        if self.chang == False:
                            self.display_passwords.setPlainText(str(file.read()))
                        else:
                            pass
                except:
                    with open("st.txt", "a") as re:
                        re.write("")
                if self.chang == True:
                    self.btn_update.setEnabled(False)
            else:
                if self.password == None:
                    pass
                else:
                    self.show_passwords_button.setStyleSheet("background-color: red;")
                    self.show_passwords_button.setText("Неверный пароль!")
                    self.show_passwords_button.adjustSize()
        else:
            self.update()
            self.show_passwords_button.setText("Показать пароли")
            self.show_passwords_button.adjustSize()
            self.position = False
            MainWindow.setFixedSize(379, 245)

    def save_password(self):
            with open("st.txt", "a") as f:
                try:
                    self.show_passwords_button.setEnabled(False)
                    self.btn_save.setEnabled(False)
                    self.btn_Change_password.setEnabled(False)
                    coment = pag.prompt("Прокоментировать:")
                    for i in range(666):
                        QApplication.processEvents()
                        pass
                    self.show_passwords_button.setEnabled(True)
                    self.btn_save.setEnabled(True)
                    self.btn_Change_password.setEnabled(True)
                    f.write("\n\n" + self.password_n + "  -  " + coment)
                    self.btn_save.setText("Сохранено!")
                    self.saves += 1
                    if self.saves < 2:
                        with open("st.txt", "a") as g:
                            date = datetime.datetime.today()
                            g.write("\n\n\nПароли от " + date.strftime(' %d.%m.%Y   %H:%M:%S:'))
                    else:
                        pass
                except:
                    pass
            with open("st.txt", "r") as file:
                self.display_passwords.setPlainText(str(file.read()))
            self.btn_update.setEnabled(False)

    def copy_password(self):
            clip = QApplication.clipboard()
            clip.setText(str(self.password_n))
            self.btn_copy.setText("Скопировано!")
            self.btn_copy.adjustSize()
            self.btn_copy.setEnabled(False)

    def change_btn_plus(self):
        if self.x < 21:
            self.x += 1
            self.check()
            self.display_2.setText("Число символов: " + str(self.x))
            self.display_2.adjustSize()
        else:
            pass

    def change_btn_minus(self):
        if self.x > 1:
            self.x -= 1
            self.check()
            self.display_2.setText("Число символов: " + str(self.x))
            self.display_2.adjustSize()
        else:
            pass

    def create_password(self):
        for x in range(1):
            pw = ""
            if self.checkBox_nums.isChecked():
                pw += "1234567890"
            if self.checkBox_lettrs_big.isChecked():
                pw += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if self.checkBox_lettrs_little.isChecked():
                pw += "abcdefghijklmnopqrstuvwxyz"
            if self.checkBox_other.isChecked():
                pw += "+-/*_!&$#@?=@<>^%()[]{|}:;\"\'"
            self.password_n = ""
            for i in range(self.x):
                try:
                    self.password_n += random.choice(pw)
                    self.display.setText("Сгенерированый пароль:  " + str(self.password_n))
                    self.btn_copy.setText("Копировать")
                    self.btn_copy.adjustSize()
                    self.btn_save.setText("Сохранить")
                    self.btn_copy.setEnabled(True)
                    if self.action == False:
                        if self.password_n == None:
                            self.btn_save.setEnabled(False)
                            self.btn_copy.setEnabled(False)
                        else:
                            self.btn_save.setEnabled(True)
                            self.btn_copy.setEnabled(True)
                    else:
                        pass
                except:
                    self.display.setText("Укажите хотя-бы один параметр!")
                    self.btn_save.setEnabled(False)
                    self.btn_copy.setEnabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор паролей"))
        self.display.setText(_translate("MainWindow", "Сгенерированый пароль:  "))
        self.create.setText(_translate("MainWindow", "Создать пароль"))
        self.checkBox_nums.setText(_translate("MainWindow", "Цифры"))
        self.checkBox_lettrs_big.setText(_translate("MainWindow", "Прописные буквы"))
        self.checkBox_lettrs_big.adjustSize()
        self.checkBox_lettrs_little.setText(_translate("MainWindow", "Строчные буквы"))
        self.checkBox_lettrs_little.adjustSize()
        self.checkBox_other.setText(_translate("MainWindow", "Спец. символы"))
        self.checkBox_other.adjustSize()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())