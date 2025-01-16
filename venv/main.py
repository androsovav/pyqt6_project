import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel,
    QFileDialog, QVBoxLayout, QWidget, QMessageBox
)
import filtered

# Здесь находится скрипт для работы с CSV-файлом
def process_csv(file_path):
    # Функция для обработки выбранного CSV файла
    try:
        filtered.script(file_path)
    except Exception as e:
        QMessageBox.critical(None, "Ошибка", f"Произошла ошибка: {str(e)}")

class MainWindow(QMainWindow):
    def __init__(self):
        # Инициализация главного окна приложения
        super().__init__()

        # Установка заголовка окна
        self.setWindowTitle("CSV Processor")
        # Установка начального размера окна
        self.setGeometry(300, 300, 400, 200)

        # Переменная для хранения пути к выбранному файлу
        self.csv_file_path = ""

        # Инициализация пользовательского интерфейса
        self.init_ui()

    def init_ui(self):
        # Создание и настройка элементов интерфейса

        # Метка, которая будет отображать текст
        self.label = QLabel("Выберите CSV файл", self)
        self.label.setStyleSheet("font-size: 16px;")

        # Кнопка для выбора файла
        self.choose_file_button = QPushButton("Выбрать файл", self)
        # Подключаем событие нажатия кнопки к методу выбора файла
        self.choose_file_button.clicked.connect(self.choose_file)

        # Кнопка для обработки файла
        self.process_button = QPushButton("Обработать файл", self)
        # По умолчанию кнопка отключена (активируется после выбора файла)
        self.process_button.setEnabled(False)
        # Подключаем событие нажатия кнопки к методу обработки файла
        self.process_button.clicked.connect(self.process_file)

        # Создаем вертикальный макет для размещения элементов
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.choose_file_button)
        layout.addWidget(self.process_button)

        # Устанавливаем центральный виджет и применяем макет
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def choose_file(self):
        # Метод для выбора файла через диалог
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("CSV and Text Files (*.csv *.txt)")  # Фильтр для отображения файлов CSV и TXT
        if file_dialog.exec():
            # Получаем список выбранных файлов
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                # Сохраняем путь к выбранному файлу
                self.csv_file_path = selected_files[0]
                # Отображаем путь в метке
                self.label.setText(f"Выбран файл: {self.csv_file_path}")
                # Активируем кнопку обработки
                self.process_button.setEnabled(True)

    def process_file(self):
        # Метод для обработки выбранного файла
        if self.csv_file_path:
            # Передаем путь к файлу в функцию обработки
            process_csv(self.csv_file_path)
        else:
            # Если файл не выбран, выводим предупреждение
            QMessageBox.warning(self, "Внимание", "Файл не выбран!")

if __name__ == "__main__":
    # Создаем экземпляр приложения
    app = QApplication(sys.argv)

    # Создаем и отображаем главное окно
    window = MainWindow()
    window.show()

    # Запускаем главный цикл событий приложения
    sys.exit(app.exec())
