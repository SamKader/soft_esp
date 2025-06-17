from PySide6.QtWidgets import QApplication, QMainWindow
from gui.interface import Ui_MainWindow
from gui.ressources import icons_rc  # pour charger les SVG et autres ressources

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
