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


    # Visit a parse tree produced by simplified_javaParser#decVarConst.
    def visitDecVarConst(self, ctx:simplified_javaParser.DecVarConstContext):
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


    # Visit a parse tree produced by simplified_javaParser#cmmd.
    def visitCmmd(self, ctx:simplified_javaParser.CmmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#inst.
    def visitInst(self, ctx:simplified_javaParser.InstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#instParamList.
    def visitInstParamList(self, ctx:simplified_javaParser.InstParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#instParam.
    def visitInstParam(self, ctx:simplified_javaParser.InstParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#assign.
    def visitAssign(self, ctx:simplified_javaParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#return.
    def visitReturn(self, ctx:simplified_javaParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#if.
    def visitIf(self, ctx:simplified_javaParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#else.
    def visitElse(self, ctx:simplified_javaParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#while.
    def visitWhile(self, ctx:simplified_javaParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#break.
    def visitBreak(self, ctx:simplified_javaParser.BreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#exp.
    def visitExp(self, ctx:simplified_javaParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#logic_exp.
    def visitLogic_exp(self, ctx:simplified_javaParser.Logic_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#logic_t.
    def visitLogic_t(self, ctx:simplified_javaParser.Logic_tContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#logic_f.
    def visitLogic_f(self, ctx:simplified_javaParser.Logic_fContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#comparison.
    def visitComparison(self, ctx:simplified_javaParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#comparison_op.
    def visitComparison_op(self, ctx:simplified_javaParser.Comparison_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#arith_exp.
    def visitArith_exp(self, ctx:simplified_javaParser.Arith_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#arith_t.
    def visitArith_t(self, ctx:simplified_javaParser.Arith_tContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#arith_f.
    def visitArith_f(self, ctx:simplified_javaParser.Arith_fContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#number.
    def visitNumber(self, ctx:simplified_javaParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#comment.
    def visitComment(self, ctx:simplified_javaParser.CommentContext):
        return self.visitChildren(ctx)



del simplified_javaParser