import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from design import Ui_MainWindow


class Calculator(QMainWindow):
    def __int__(self):
        super(Calculator, self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # window = Calculator()
    # window.show()

    sys.exit(app.exec())
