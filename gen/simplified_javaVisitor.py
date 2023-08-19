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


    # Visit a parse tree produced by simplified_javaParser#func.
    def visitFunc(self, ctx:simplified_javaParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#func_main.
    def visitFunc_main(self, ctx:simplified_javaParser.Func_mainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#parameters_list.
    def visitParameters_list(self, ctx:simplified_javaParser.Parameters_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#type.
    def visitType(self, ctx:simplified_javaParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#dec_list.
    def visitDec_list(self, ctx:simplified_javaParser.Dec_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#dec_var.
    def visitDec_var(self, ctx:simplified_javaParser.Dec_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#dec_const.
    def visitDec_const(self, ctx:simplified_javaParser.Dec_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#value.
    def visitValue(self, ctx:simplified_javaParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#comd.
    def visitComd(self, ctx:simplified_javaParser.ComdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#inst.
    def visitInst(self, ctx:simplified_javaParser.InstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by simplified_javaParser#value_list.
    def visitValue_list(self, ctx:simplified_javaParser.Value_listContext):
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