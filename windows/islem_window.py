from PyQt5.QtWidgets import QMainWindow
from ui.islem import IslemWindowUI
from windows.yeni_soru_window import YeniSoruWindow
from windows.yazdir_window import YazdirWindow


class MainWindow(QMainWindow, IslemWindowUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionYeni_Soru.triggered.connect(self.open_yeni_soru_window)
        self.actionSoru_Sec.triggered.connect(self.open_yazdir_window)

    def open_yeni_soru_window(self):
        self.yeni_soru_window = YeniSoruWindow()
        self.yeni_soru_window.show()

    def open_yazdir_window(self):
        self.yazdir_window = YazdirWindow()
        self.yazdir_window.show()
