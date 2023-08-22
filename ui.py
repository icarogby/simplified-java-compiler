from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget, QTextEdit, QLabel
from PyQt5.QtGui import QColor

class InitialScreen(QMainWindow):
    def __init__(self, antlr_parser_func):
        super().__init__()

        self.setWindowTitle("Tela Inicial")
        self.setGeometry(300, 100, 800, 600)

        self.setStyleSheet("background-color: #303030; color: #f0f0f0;")

        self.layout = QVBoxLayout()

        self.central_widget = QPushButton("Entrar com Arquivo TXT", self)
        self.central_widget.clicked.connect(self.open_file_dialog)
        self.central_widget.setStyleSheet("background-color: #6C6A6A; color: white;")
        self.layout.addWidget(self.central_widget)

        self.text_edit = QTextEdit(self)
        self.layout.addWidget(self.text_edit)

        self.execute_button = QPushButton("Executar", self)
        self.execute_button.clicked.connect(self.execute_action)
        self.execute_button.setStyleSheet("background-color: #6C6A6A; color: white;")
        self.layout.addWidget(self.execute_button)

        self.output_label = QLabel(self)
        self.output_label.setAlignment(Qt.AlignTop)
        self.output_label.setStyleSheet("background-color: #2b2b2b; color: #33FC0A; padding: 10px; border: 1px solid #444;")
        self.layout.addWidget(self.output_label)

        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.antlr_parser_func = antlr_parser_func

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Importar Arquivo", "",
                                                   "Arquivos de Texto (*.txt);;Todos os Arquivos (*)", options=options)

        if file_name:
            with open(file_name, "r") as file:
                file_content = file.read()
                self.text_edit.setPlainText(file_content)

    def execute_action(self):
        user_input = self.text_edit.toPlainText()
        output = self.antlr_parser_func(user_input)
        self.output_label.setText(output)