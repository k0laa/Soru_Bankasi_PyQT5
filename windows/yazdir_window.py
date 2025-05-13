from PyQt5.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QTextDocument
from ui.yazdir import Ui_MainWindow
from utils.excel import ExcelOperations

class YazdirWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.excel = ExcelOperations()
        self.selected_questions = []

        self.pushButton.clicked.connect(self.print_question)
        self.listWidget.itemSelectionChanged.connect(self.select_questions)

        self.load_questions()

    def load_questions(self):
        questions = self.excel.read_data()
        self.listWidget.clear()
        for question in questions:
            item = QListWidgetItem(f"{question[0]} - {question[1]}")
            self.listWidget.addItem(item)

    def select_questions(self):
        self.selected_questions = []
        for index in range(self.listWidget.count()):
            item = self.listWidget.item(index)
            if item.isSelected():
                self.selected_questions.append(int(item.text().split(" - ")[0]))

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

            questions = self.excel.read_data()
            for question in questions:
                if question[0] in self.selected_questions:
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
        self.excel.close()
        super().closeEvent(event)
