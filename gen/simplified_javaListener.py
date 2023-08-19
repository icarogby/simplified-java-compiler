# Generated from C:/Users/icaro/OneDrive/Documentos/GitHub/simplified-java-compiler\simplified_java.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .simplified_javaParser import simplified_javaParser
else:
    from simplified_javaParser import simplified_javaParser

# This class defines a complete listener for a parse tree produced by simplified_javaParser.
class simplified_javaListener(ParseTreeListener):

    # Enter a parse tree produced by simplified_javaParser#init.
    def enterInit(self, ctx:simplified_javaParser.InitContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#init.
    def exitInit(self, ctx:simplified_javaParser.InitContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#func.
    def enterFunc(self, ctx:simplified_javaParser.FuncContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#func.
    def exitFunc(self, ctx:simplified_javaParser.FuncContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#func_main.
    def enterFunc_main(self, ctx:simplified_javaParser.Func_mainContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#func_main.
    def exitFunc_main(self, ctx:simplified_javaParser.Func_mainContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#parameters_list.
    def enterParameters_list(self, ctx:simplified_javaParser.Parameters_listContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#parameters_list.
    def exitParameters_list(self, ctx:simplified_javaParser.Parameters_listContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#type.
    def enterType(self, ctx:simplified_javaParser.TypeContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#type.
    def exitType(self, ctx:simplified_javaParser.TypeContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#dec_list.
    def enterDec_list(self, ctx:simplified_javaParser.Dec_listContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#dec_list.
    def exitDec_list(self, ctx:simplified_javaParser.Dec_listContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#dec_var.
    def enterDec_var(self, ctx:simplified_javaParser.Dec_varContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#dec_var.
    def exitDec_var(self, ctx:simplified_javaParser.Dec_varContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#dec_const.
    def enterDec_const(self, ctx:simplified_javaParser.Dec_constContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#dec_const.
    def exitDec_const(self, ctx:simplified_javaParser.Dec_constContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#value.
    def enterValue(self, ctx:simplified_javaParser.ValueContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#value.
    def exitValue(self, ctx:simplified_javaParser.ValueContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#comd.
    def enterComd(self, ctx:simplified_javaParser.ComdContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#comd.
    def exitComd(self, ctx:simplified_javaParser.ComdContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#inst.
    def enterInst(self, ctx:simplified_javaParser.InstContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#inst.
    def exitInst(self, ctx:simplified_javaParser.InstContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#value_list.
    def enterValue_list(self, ctx:simplified_javaParser.Value_listContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#value_list.
    def exitValue_list(self, ctx:simplified_javaParser.Value_listContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#assign.
    def enterAssign(self, ctx:simplified_javaParser.AssignContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#assign.
    def exitAssign(self, ctx:simplified_javaParser.AssignContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#return.
    def enterReturn(self, ctx:simplified_javaParser.ReturnContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#return.
    def exitReturn(self, ctx:simplified_javaParser.ReturnContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#if.
    def enterIf(self, ctx:simplified_javaParser.IfContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#if.
    def exitIf(self, ctx:simplified_javaParser.IfContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#else.
    def enterElse(self, ctx:simplified_javaParser.ElseContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#else.
    def exitElse(self, ctx:simplified_javaParser.ElseContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#while.
    def enterWhile(self, ctx:simplified_javaParser.WhileContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#while.
    def exitWhile(self, ctx:simplified_javaParser.WhileContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#break.
    def enterBreak(self, ctx:simplified_javaParser.BreakContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#break.
    def exitBreak(self, ctx:simplified_javaParser.BreakContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#exp.
    def enterExp(self, ctx:simplified_javaParser.ExpContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#exp.
    def exitExp(self, ctx:simplified_javaParser.ExpContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#logic_exp.
    def enterLogic_exp(self, ctx:simplified_javaParser.Logic_expContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#logic_exp.
    def exitLogic_exp(self, ctx:simplified_javaParser.Logic_expContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#logic_t.
    def enterLogic_t(self, ctx:simplified_javaParser.Logic_tContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#logic_t.
    def exitLogic_t(self, ctx:simplified_javaParser.Logic_tContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#logic_f.
    def enterLogic_f(self, ctx:simplified_javaParser.Logic_fContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#logic_f.
    def exitLogic_f(self, ctx:simplified_javaParser.Logic_fContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#comparison.
    def enterComparison(self, ctx:simplified_javaParser.ComparisonContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#comparison.
    def exitComparison(self, ctx:simplified_javaParser.ComparisonContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#comparison_op.
    def enterComparison_op(self, ctx:simplified_javaParser.Comparison_opContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#comparison_op.
    def exitComparison_op(self, ctx:simplified_javaParser.Comparison_opContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#arith_exp.
    def enterArith_exp(self, ctx:simplified_javaParser.Arith_expContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#arith_exp.
    def exitArith_exp(self, ctx:simplified_javaParser.Arith_expContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#arith_t.
    def enterArith_t(self, ctx:simplified_javaParser.Arith_tContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#arith_t.
    def exitArith_t(self, ctx:simplified_javaParser.Arith_tContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#arith_f.
    def enterArith_f(self, ctx:simplified_javaParser.Arith_fContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#arith_f.
    def exitArith_f(self, ctx:simplified_javaParser.Arith_fContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#number.
    def enterNumber(self, ctx:simplified_javaParser.NumberContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#number.
    def exitNumber(self, ctx:simplified_javaParser.NumberContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#comment.
    def enterComment(self, ctx:simplified_javaParser.CommentContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#comment.
    def exitComment(self, ctx:simplified_javaParser.CommentContext):
        pass



del simplified_javaParser