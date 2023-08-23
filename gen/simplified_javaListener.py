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


    # Enter a parse tree produced by simplified_javaParser#decFuncList.
    def enterDecFuncList(self, ctx:simplified_javaParser.DecFuncListContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#decFuncList.
    def exitDecFuncList(self, ctx:simplified_javaParser.DecFuncListContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#decFunc.
    def enterDecFunc(self, ctx:simplified_javaParser.DecFuncContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#decFunc.
    def exitDecFunc(self, ctx:simplified_javaParser.DecFuncContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#funcMain.
    def enterFuncMain(self, ctx:simplified_javaParser.FuncMainContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#funcMain.
    def exitFuncMain(self, ctx:simplified_javaParser.FuncMainContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#parametersList.
    def enterParametersList(self, ctx:simplified_javaParser.ParametersListContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#parametersList.
    def exitParametersList(self, ctx:simplified_javaParser.ParametersListContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#funcType.
    def enterFuncType(self, ctx:simplified_javaParser.FuncTypeContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#funcType.
    def exitFuncType(self, ctx:simplified_javaParser.FuncTypeContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#dataType.
    def enterDataType(self, ctx:simplified_javaParser.DataTypeContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#dataType.
    def exitDataType(self, ctx:simplified_javaParser.DataTypeContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#varField.
    def enterVarField(self, ctx:simplified_javaParser.VarFieldContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#varField.
    def exitVarField(self, ctx:simplified_javaParser.VarFieldContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#decVarConst.
    def enterDecVarConst(self, ctx:simplified_javaParser.DecVarConstContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#decVarConst.
    def exitDecVarConst(self, ctx:simplified_javaParser.DecVarConstContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#decVar.
    def enterDecVar(self, ctx:simplified_javaParser.DecVarContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#decVar.
    def exitDecVar(self, ctx:simplified_javaParser.DecVarContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#decConst.
    def enterDecConst(self, ctx:simplified_javaParser.DecConstContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#decConst.
    def exitDecConst(self, ctx:simplified_javaParser.DecConstContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#value.
    def enterValue(self, ctx:simplified_javaParser.ValueContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#value.
    def exitValue(self, ctx:simplified_javaParser.ValueContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#cmmd.
    def enterCmmd(self, ctx:simplified_javaParser.CmmdContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#cmmd.
    def exitCmmd(self, ctx:simplified_javaParser.CmmdContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#inst.
    def enterInst(self, ctx:simplified_javaParser.InstContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#inst.
    def exitInst(self, ctx:simplified_javaParser.InstContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#instParamList.
    def enterInstParamList(self, ctx:simplified_javaParser.InstParamListContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#instParamList.
    def exitInstParamList(self, ctx:simplified_javaParser.InstParamListContext):
        pass


    # Enter a parse tree produced by simplified_javaParser#instParam.
    def enterInstParam(self, ctx:simplified_javaParser.InstParamContext):
        pass

    # Exit a parse tree produced by simplified_javaParser#instParam.
    def exitInstParam(self, ctx:simplified_javaParser.InstParamContext):
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