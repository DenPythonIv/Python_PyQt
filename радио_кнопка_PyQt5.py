"""
Диалоговое окно,выполнения дествия при нажатии радио кнопки.
"""
from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton, QDialog, QHBoxLayout, QLabel,QVBoxLayout
import sys
from PyQt5.QtCore import QRect,QSize
from PyQt5.QtGui import QIcon, QFont


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()

        self.ui()

    def ui(self):
        self.setWindowTitle('Диалоговое окно,выполнения дествия при нажатии радио кнопки.')
        self.setGeometry(320,320,200,150)
        # Создаем горизонтальный контейнер.
        self.hbox = QHBoxLayout()

        # Создание радио кнопки.
        self.radio_btn = QRadioButton('Футбол')
        # Устанавливаем шрифт текста.
        self.radio_btn.setFont(QFont('ubuntu',15))
        self.radio_btn.setIcon(QIcon('user_blank.png'))
        self.radio_btn.setIconSize(QSize(40,40))
        self.radio_btn.toggled.connect(self.button_actions)
        # Упаковываем горизонтальный модуль.
        self.hbox.addWidget(self.radio_btn)
        # Создание радио кнопки.
        self.radio_btn_2 = QRadioButton('Баскетбол')
        # Устанавливаем шрифт текста.
        self.radio_btn_2.setFont(QFont('ubuntu', 15))
        self.radio_btn_2.setIcon(QIcon('basketball.png'))
        self.radio_btn_2.setIconSize(QSize(40, 40))
        self.radio_btn_2.toggled.connect(self.button_actions)
        # Упаковываем горизонтальный модуль.
        self.hbox.addWidget(self.radio_btn_2)
        # Создание радио кнопки.
        self.radio_btn_3 = QRadioButton('Воллебол')
        # Устанавливаем шрифт текста.
        self.radio_btn_3.setFont(QFont('ubuntu', 15))
        self.radio_btn_3.setIcon(QIcon('bbb.png'))
        self.radio_btn_3.setIconSize(QSize(40, 40))
        self.radio_btn_3.toggled.connect(self.button_actions)
        # Упаковываем горизонтальный модуль.
        self.hbox.addWidget(self.radio_btn_3)
        self.label = QLabel(self)
        self.label.setFont(QFont('ubuntu',20))
        # Создаем вертикальный модуль.
        self.vbox = QVBoxLayout()
        # Комплектовка вертикального модуля.
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.label)

        # Отображаем виджеты на мониторе.
        self.setLayout(self.vbox)
        self.show()

    def button_actions(self):
        if self.radio_btn.isChecked():
            self.label.setText('Мой любимый вид спорта {0}'.format(self.radio_btn.text()))
        elif self.radio_btn_2.isChecked():
            self.label.setText('Мой любимый вид спорта {0}'.format(self.radio_btn_2.text()))
        elif self.radio_btn_3.isChecked():
            self.label.setText('Мой любимый вид спорта {0}'.format(self.radio_btn_3.text()))

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window  = Window()
    sys.exit(App.exec())
