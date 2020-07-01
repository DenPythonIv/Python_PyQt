"""
Пустой шабла диалогового окна.
"""
from PyQt5.QtWidgets import QDialog,QApplication
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):
        self.setWindowTitle('Диалоговое окно')
        self.setGeometry(320,320,400,200)

        self.show()

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())