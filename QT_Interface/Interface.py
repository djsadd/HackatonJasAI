import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
from ui_main_sec import Ui_MainWindow
from ui_reg import Ui_Form
import Find_Person
import Upload_Person_To_db
import psqlpt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.other_form = None

        self.ui.New.clicked.connect(self.open_other_form)
        self.ui.Find.clicked.connect(self.search_person)
        self.db = psqlpt.create_connection('hackatosjasai', 'postgres', '', 'localhost', '5432')

    def open_other_form(self):
        self.other_form = RegDialog()
        self.other_form.show()

        self.other_form.ui.photo.clicked.connect(self.other_form.open_file_dialog)

    def open_file_dialog(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self.other_form, 'Выбрать фото', '', 'Изображения (*.png *.jpg *.bmp *.gif)')

    def search_person(self):
        file_path, _ = QFileDialog.getOpenFileName(self.other_form, 'Выбрать фото', '', 'Изображения (*.png *.jpg *.bmp *.gif)')
        Find_Person.get_person(file_path, self.db)


class RegDialog(QDialog):
    def __init__(self):
        super(RegDialog, self).__init__()
        self.file_path = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.next.clicked.connect(self.save_data)

    def save_data(self):
        name = self.ui.Name.text()
        print(name)
        if self.file_path:
            print(self.file_path)

        Upload_Person_To_db.add_person_to_db(name, self.file_path)
        QMessageBox.information(self, 'Успех', 'Данные сохранены в базу данных')

    def open_file_dialog(self):
        self.file_path, _ = QFileDialog.getOpenFileName(
            self, 'Выбрать фото', '', 'Изображения (*.png *.jpg *.bmp *.gif)')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
