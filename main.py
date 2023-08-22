import sys
from PyQt5.QtWidgets import QApplication
from ui import InitialScreen

from antlr4 import *
from gen.simplified_javaLexer import simplified_javaLexer
from gen.simplified_javaParser import simplified_javaParser
from semantico import analizadorSemantico

from antlr4.error.ErrorListener import ConsoleErrorListener

def main():
    input_stream = FileStream("simp_java_example.txt")  # Nome do arquivo de entrada
    lexer = simplified_javaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = simplified_javaParser(stream)
    tree = parser.init()

    semantic_analyzer = analizadorSemantico()
    semantic_analyzer.visit(tree)
    semantic_analyzer.show()

# class SyntaxErrorListener(ConsoleErrorListener):
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         raise Exception(f"Syntax Error: {msg} at line {line}, column {column}")
#
# def main():
#     app = QApplication(sys.argv)
#     janela = InitialScreen(run_antlr_parser)
#     janela.show()
#     sys.exit(app.exec())
#
# def run_antlr_parser(input_code):
#     input_stream = InputStream(input_code)
#     lexer = simplified_javaLexer(input_stream)
#     stream = CommonTokenStream(lexer)
#
#     try:
#         parser = simplified_javaParser(stream)
#         parser.removeErrorListeners()
#         parser.addErrorListener(SyntaxErrorListener())
#
#         tree = parser.init()
#
#         semantic_analyzer = analizadorSemantico()
#
#         semantic_analyzer.visit(tree)
#         return "Análise bem-sucedida: Sintaxe correta"
#     except Exception as e:
#         return f"Erro de Sintaxe: {str(e)}"


if __name__ == "__main__":
    main()
