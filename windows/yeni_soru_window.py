from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from ui.yeni_soru import YeniSoruWindowUI
from utils.database import Database
from windows.yazdir_window import YazdirWindow


class YeniSoruWindow(QMainWindow, YeniSoruWindowUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = Database()
        self.pushButton.clicked.connect(self.save_question)
        self.pushButton_2.clicked.connect(self.delete_selected_question)
        self.pushButton_3.clicked.connect(self.open_yazdir_window)
        self.load_questions()

    def load_questions(self):
        self.tableWidget.setRowCount(0)
        questions = self.db.get_all_questions()
        self.tableWidget.setColumnCount(7)  # Doğru cevap sütunu dahil
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Soru", "1. Seçenek", "2. Seçenek", "3. Seçenek", "4. Seçenek", "Doğru Cevap"])
        for row_number, row_data in enumerate(questions):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def delete_selected_question(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Hata", "Lütfen silmek istediğiniz soruyu seçin.")
            return
        question_id = self.tableWidget.item(selected_row, 0).text()
        self.db.delete_question(question_id)
        QMessageBox.information(self, "Başarılı", "Soru başarıyla silindi.")
        self.load_questions()

    def load_questions(self):
        self.tableWidget.setRowCount(0)
        questions = self.db.get_all_questions()
        self.tableWidget.setColumnCount(7)  # Doğru cevap sütunu dahil
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Soru", "1. Seçenek", "2. Seçenek", "3. Seçenek", "4. Seçenek", "Doğru Cevap"])
        for row_number, row_data in enumerate(questions):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

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
        self.load_questions()

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

    def open_yazdir_window(self):
        self.yazdir_window = YazdirWindow()
        self.yazdir_window.show()
