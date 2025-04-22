from PyQt5.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem, QLineEdit, QLabel, QVBoxLayout
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QTextDocument
from ui.yazdir import Ui_MainWindow
from utils.database import Database

class YazdirWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = Database()
        self.selected_questions = []

        self.pushButton.clicked.connect(self.print_question)
        self.listWidget.itemSelectionChanged.connect(self.select_questions)

        self.load_questions()

    def load_questions(self):
        questions = self.db.get_all_questions()
        self.listWidget.clear()
        for question in questions:
            item = QListWidgetItem(f"{question[0]} - {question[1]}")
            self.listWidget.addItem(item)

    def filter_questions(self):
        keyword = self.filter_input.text().lower()
        questions = self.db.get_all_questions()
        self.listWidget.clear()
        for question in questions:
            if keyword in question[1].lower():  # Sorunun metninde anahtar kelimeyi ara
                item = QListWidgetItem(f"{question[0]} - {question[1]}")
                self.listWidget.addItem(item)

    def select_questions(self):
        self.selected_questions = []
        for index in range(self.listWidget.count()):
            item = self.listWidget.item(index)
            if item.isSelected():
                self.selected_questions.append(item.text().split(" - ")[0])

    def print_question(self):
        if not self.selected_questions:
            QMessageBox.warning(self, "Hata", "Lütfen yazdırmak için en az bir soru seçin.")
            return

        try:
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName("sorular.pdf")

            document = QTextDocument()
            content = ""

            for question_id in self.selected_questions:
                question = self.db.cursor.execute(
                    "SELECT * FROM sorular WHERE id = ?", (question_id,)
                ).fetchone()

                if question:
                    content += f"<b>Soru {question[0]}:</b><br>{question[1]}<br><br>"
                    content += f"A) {question[2]}<br>"
                    content += f"B) {question[3]}<br>"
                    content += f"C) {question[4]}<br>"
                    content += f"D) {question[5]}<br><br>"
                    content += f"<b>Doğru Cevap:</b> {question[6]}<br><hr><br>"

            document.setHtml(content)
            document.print_(printer)

            QMessageBox.information(self, "Başarılı", "Seçilen sorular başarıyla 'sorular.pdf' dosyasına yazdırıldı.")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Yazdırma sırasında bir hata oluştu: {str(e)}")

    def closeEvent(self, event):
        self.db.close()
        super().closeEvent(event)
