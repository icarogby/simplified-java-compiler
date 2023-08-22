# Generated from C:/Users/icaro/OneDrive/Documentos/GitHub/simplified-java-compiler\simplified_java.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .simplified_javaParser import simplified_javaParser
else:
    from simplified_javaParser import simplified_javaParser

# This class defines a complete generic visitor for a parse tree produced by simplified_javaParser.

class simplified_javaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by simplified_javaParser#init.
    def visitInit(self, ctx:simplified_javaParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#decFuncList.
    def visitDecFuncList(self, ctx:simplified_javaParser.DecFuncListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#decFunc.
    def visitDecFunc(self, ctx:simplified_javaParser.DecFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#funcMain.
    def visitFuncMain(self, ctx:simplified_javaParser.FuncMainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#parametersList.
    def visitParametersList(self, ctx:simplified_javaParser.ParametersListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#funcType.
    def visitFuncType(self, ctx:simplified_javaParser.FuncTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#dataType.
    def visitDataType(self, ctx:simplified_javaParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#varField.
    def visitVarField(self, ctx:simplified_javaParser.VarFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#decVarConstList.
    def visitDecVarConstList(self, ctx:simplified_javaParser.DecVarConstListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#decVar.
    def visitDecVar(self, ctx:simplified_javaParser.DecVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#decConst.
    def visitDecConst(self, ctx:simplified_javaParser.DecConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#value.
    def visitValue(self, ctx:simplified_javaParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#comment.
    def visitComment(self, ctx:simplified_javaParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#cmmd.
    def visitCmmd(self, ctx:simplified_javaParser.CmmdContext):
        return self.visitChildren(ctx)



del simplified_javaParser