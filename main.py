
from antlr4 import *
from gen.simplified_javaLexer import simplified_javaLexer
from gen.simplified_javaParser import simplified_javaParser

from antlr4.error.ErrorListener import ConsoleErrorListener

from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import (
    QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit, QLabel, QApplication,
    QMessageBox, QListWidget, QListWidgetItem
)
from PyQt5.QtGui import QColor, QIcon
import sys
import qdarkstyle

from semantico import analizadorSemantico

class SyntaxErrorListener(ConsoleErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax Error: {msg} at line {line}, column {column}")

def antlr_parser_func(input_text):
    input_stream = InputStream(input_text)
    lexer = simplified_javaLexer(input_stream)
    stream = CommonTokenStream(lexer)

    try:
        parser = simplified_javaParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(SyntaxErrorListener())

        tree = parser.init()

        semantic_analyzer = analizadorSemantico()

        semantic_analyzer.visit(tree)
        return "Análise bem-sucedida: Sintaxe correta"

    except Exception as e:
        return f"Erro de Sintaxe: {str(e)}"

def get_symbol_table(input_text):
    input_stream = InputStream(input_text)
    lexer = simplified_javaLexer(input_stream)
    stream = CommonTokenStream(lexer)

    try:
        parser = simplified_javaParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(SyntaxErrorListener())

        tree = parser.init()

        semantic_analyzer = analizadorSemantico()

        semantic_analyzer.visit(tree)

        return semantic_analyzer.show()

    except:
        return ""

class InitialScreen(QMainWindow):
    def __init__(self, antlr_parser_func):
        super().__init__()

        self.setWindowTitle("JAVA SIMPLIFIED COMPILER")
        self.setGeometry(300, 100, 800, 600)
        self.setWindowIcon(QIcon("images/jython.png"))

        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout()  # Layout horizontal para acomodar a tabela de símbolos e o resto da interface
        self.central_widget.setLayout(self.layout)

        # Layout para a tabela de símbolos
        self.symbol_table_layout = QVBoxLayout()
        self.layout.addLayout(self.symbol_table_layout)

        self.symbol_table_label = QLabel("Tabela de Símbolos")
        self.symbol_table_label.setStyleSheet("font-weight: bold;")
        self.symbol_table_layout.addWidget(self.symbol_table_label)

        self.symbol_table_list = QListWidget()
        self.symbol_table_list.setStyleSheet("background-color: #2b2b2b; color: white; border: 1px solid #444;")
        self.symbol_table_layout.addWidget(self.symbol_table_list)
        #self.update_symbol_table()

        # Layout para o restante da interface
        self.interface_layout = QVBoxLayout()
        self.layout.addLayout(self.interface_layout)

        # Botão "Anexar Arquivo" com ícone
        self.attach_file_button = QPushButton("Anexar Arquivo")
        self.attach_file_button.setIcon(QIcon("images/pasta-aberta.png"))  # Substitua pelo caminho real do ícone
        self.attach_file_button.clicked.connect(self.attach_file_clicked)
        self.interface_layout.addWidget(self.attach_file_button)

        # Botão "Executar" com ícone
        self.execute_button = QPushButton("Executar")
        self.execute_button.setIcon(QIcon("images/executar.png"))  # Substitua pelo caminho real do ícone
        self.execute_button.clicked.connect(self.execute_clicked)
        self.execute_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.interface_layout.addWidget(self.execute_button)

        # Text Edit para entrada do programa
        self.text_edit = QTextEdit()
        self.interface_layout.addWidget(self.text_edit)

        # Label para saída do programa
        self.output_label = QLabel()
        self.output_label.setAlignment(Qt.AlignTop)
        self.output_label.setStyleSheet(
            "background-color: #2b2b2b; color: #33FC0A; padding: 10px; border: 1px solid #444;")
        self.interface_layout.addWidget(self.output_label)

        self.statusBar().showMessage("Bem-vindo ao compilador simplificado de Java!")

        self.antlr_parser_func = antlr_parser_func

        self.dark_theme = True  # Inicialmente definido como tema escuro

    def update_symbol_table(self, input):
        self.symbol_table_list.clear()
        symbol_table = get_symbol_table(input)

        for symbol in symbol_table:
            data = str(symbol_table[symbol])
            txt = f"{symbol} - {data}"
            item = QListWidgetItem(txt)
            self.symbol_table_list.addItem(item)

    def attach_file_clicked(self):
        self.animate_button(self.attach_file_button)
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Importar Arquivo", "",
                                                   "Arquivos de Texto (*.txt);;Todos os Arquivos (*)", options=options)

        if file_name:
            with open(file_name, "r") as file:
                file_content = file.read()
                self.text_edit.setPlainText(file_content)

    def execute_clicked(self):
        self.animate_button(self.execute_button)
        user_input = self.text_edit.toPlainText()

        self.update_symbol_table(user_input)
        try:
            output = self.antlr_parser_func(user_input)
        except Exception as e:
            output = str(e)
            self.show_error_dialog("Erro", "Ocorreu um erro durante a execução.")

        if "Erro de Sintaxe" in output:
            self.output_label.setStyleSheet(
                "background-color: #2b2b2b; color: #FF0000; padding: 10px; border: 1px solid #444;")
        else:
            self.output_label.setStyleSheet(
                "background-color: #2b2b2b; color: #33FC0A; padding: 10px; border: 1px solid #444;")

        self.output_label.setText(output)

    def show_error_dialog(self, title, message):
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle(title)
        error_dialog.setText(message)
        error_dialog.exec_()

    def animate_button(self, button):
        animation = QPropertyAnimation(button, b"color")
        animation.setDuration(300)
        animation.setStartValue(QColor(255, 255, 255))
        animation.setEndValue(QColor(0, 255, 0))
        animation.setEasingCurve(QEasingCurve.OutCirc)
        animation.start()

def main():
    app = QApplication(sys.argv)
    window = InitialScreen(antlr_parser_func)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

