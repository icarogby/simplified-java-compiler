from semantico import *

def main():
    input_stream = FileStream("simp_java_example.txt")  # Nome do arquivo de entrada
    lexer = simplified_javaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = simplified_javaParser(stream)
    tree = parser.init()

    semantic_analyzer = SemanticAnalyzer()
    semantic_analyzer.visit(tree)

if __name__ == '__main__':
    main()
