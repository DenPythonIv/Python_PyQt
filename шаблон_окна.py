"""
Пустой шаблон окна.
"""
from PyQt5.QtWidgets import QMainWindow,QApplication
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):
        self.setWindowTitle('Шаблон окна')
        self.setGeometry(320,320,650,450)

        self.show()



if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())