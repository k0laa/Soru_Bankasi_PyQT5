from PyQt5.QtWidgets import QMainWindow
from ui.islem import IslemWindowUI
from windows.yeni_soru_window import YeniSoruWindow

class MainWindow(QMainWindow, IslemWindowUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionYeni_Soru.triggered.connect(self.open_yeni_soru)

    def open_yeni_soru(self):
        self.yeni_soru_window = YeniSoruWindow()
        self.yeni_soru_window.show()
