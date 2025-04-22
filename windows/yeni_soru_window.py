from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from ui.yeni_soru import YeniSoruWindowUI
from utils.database import Database

class YeniSoruWindow(QMainWindow, YeniSoruWindowUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = Database()
        self.pushButton.clicked.connect(self.save_question)

    def save_question(self):
        soru = self.textEdit.toPlainText()
        secenek1 = self.lineEdit_4.text()
        secenek2 = self.lineEdit_3.text()
        secenek3 = self.lineEdit_2.text()
        secenek4 = self.lineEdit.text()
        dogru_cevap = None

        if self.radioButton.isChecked():
            dogru_cevap = "A"
        elif self.radioButton_2.isChecked():
            dogru_cevap = "B"
        elif self.radioButton_3.isChecked():
            dogru_cevap = "C"
        elif self.radioButton_4.isChecked():
            dogru_cevap = "D"

        if not soru or not dogru_cevap:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun ve doğru cevabı seçin.")
            return

        self.db.add_question(soru, secenek1, secenek2, secenek3, secenek4, dogru_cevap)
        QMessageBox.information(self, "Başarılı", "Soru başarıyla kaydedildi.")
        self.clear_fields()

    def clear_fields(self):
        self.textEdit.clear()
        self.lineEdit_4.clear()
        self.lineEdit_3.clear()
        self.lineEdit_2.clear()
        self.lineEdit.clear()
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)

    def closeEvent(self, event):
        self.db.close()
        super().closeEvent(event)

