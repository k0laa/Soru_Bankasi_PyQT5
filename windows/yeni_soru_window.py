from PyQt5.QtWidgets import QMainWindow
from ui.yeni_soru import YeniSoruWindowUI

class YeniSoruWindow(QMainWindow, YeniSoruWindowUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

