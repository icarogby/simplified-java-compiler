from antlr4 import *
from gen.simplified_javaLexer import simplified_javaLexer
from gen.simplified_javaParser import simplified_javaParser
from gen.simplified_javaVisitor import simplified_javaVisitor

class SemanticAnalyzer(simplified_javaVisitor):
    def __init__(self):
        self.symbol_table = {}
        self.current_function_return_type = None
        self.var_table = []

    def visitDec_var(self, ctx):
        line = ctx.getText()

        vars, var_type = line.split(":")

        vars = vars.split(",")

        for var in vars:
            self.var_table.append((var, var_type[:-1]))
            print((var, var_type[:-1]))

    # def visitFunc(self, ctx):
    #     func_name = ctx.ID().getText()
    #     self.current_function_return_type = ctx.type_().getText() if ctx.type_() else "void"
    #     self.symbol_table[func_name] = self.current_function_return_type
    #
    #     if ctx.var():
    #         self.visitVarScope(ctx.var())  # Chama a função para visitar o escopo de variáveis da função
    #
    #     return self.visitChildren(ctx)

    # def visitVarScope(self, ctx):
    #     if ctx.dec_list():
    #         self.visitDecList(ctx.dec_list())  # Chama a função para visitar a declaração de variáveis

    # def visitDecList(self, ctx):
    #     for dec_var in ctx.dec_var():
    #         self.visitDecVar(dec_var)
    #     return "void"

    # def visitVar(self, ctx):
    #     dec_list = ctx.dec_list().dec_var()
    #     for dec_var in dec_list:
    #         self.visitDec_var(dec_var)

    # def visitDec_var(self, ctx):
    #     var_list = ctx.ID()
    #     var_type = ctx.type_().getText()
    #
    #     for var in var_list:
    #         var_name = var.getText()
    #         if var_name in self.symbol_table:
    #             print(f"Error: Variable {var_name} already defined.")
    #         else:
    #             self.symbol_table[var_name] = var_type

    # def visitValue(self, ctx):
    #     value_text = ctx.getText()
    #     if value_text.isdigit():
    #         return "int"
    #     elif value_text.replace(".", "", 1).isdigit():
    #         return "float"
    #     elif value_text.lower() in ["true", "false"]:
    #       return "bool"
    #     else:
    #         if value_text not in self.symbol_table:
    #             print(f"Error: Variable {value_text} not defined.")
    #             return "undefined"
    #         return self.symbol_table[value_text]

    # def visitReturn(self, ctx):
    #     expr_type = self.visit(ctx.getChild(1))
    #     if self.current_function_return_type != expr_type:
    #         print("Error: Return type mismatch.")
    #     return expr_type

    # def visitPrint(self, ctx):
    #     args = ctx.value_list().value()
    #     for arg in args:
    #         if isinstance(arg, simplified_javaParser.ValueContext):  # Verifica se é um valor
    #             arg_type = self.visit(arg)
    #             if arg_type == "undefined":
    #                 print(f"Error: Undefined variable in print arguments: {arg.getText()}")
    #         elif isinstance(arg, simplified_javaParser.StrContext):  # Ignora strings dentro daspas duplas
    #             text = arg.getText()
    #             if text[0] == '"' and text[-1] == '"':  # Verifica se é uma string delimitada por aspas
    #                 pass
    #             else:
    #                 arg_type = self.visit(arg)
    #                 if arg_type == "undefined":
    #                     print(f"Error: Undefined variable in print arguments: {arg.getText()}")
    #     return "void"

    # def visitScanf(self, ctx):
    #     args = ctx.value_list().value()
    #     for arg in args:
    #         arg_text = arg.getText()
    #         if arg_text not in self.symbol_table:
    #             print(f"Error: Variable {arg_text} not defined.")
    #     return "void"

    # def visitVar(self, ctx):
    #     dec_list = ctx.dec_list().dec_var()
    #     for dec_var in dec_list:
    #         var_name = dec_var.ID().getText()
    #         var_type = dec_var.type().getText()
    #         if var_name in self.symbol_table:
    #             print(f"Error: Variable {var_name} already defined.")
    #         else:
    #             self.symbol_table[var_name] = var_type
    #     return "void"

    # def visitInst(self, ctx):
    #     func_name = ctx.ID().getText()
    #     func_name_lower = func_name.lower()
    #     if func_name_lower in ["print", "scanf"]:
    #         return getattr(self, f"visit{func_name.capitalize()}")(ctx)
    #     if func_name_lower not in self.symbol_table and ctx.type_():
    #         print(f"Error: Function {func_name} not defined.")
    #         return "undefined"
    #     var_type = self.symbol_table.get(func_name_lower, "undefined")
    #     if not var_type:
    #         print(f"Error: Variable {func_name} not defined.")
    #     return var_type

    # Implement other visit methods for various parts of your grammar
