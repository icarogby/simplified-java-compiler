# Generated from C:/Users/icaro/OneDrive/Documentos/GitHub/simplified-java-compiler\simplified_java.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,121,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,3,0,30,8,0,1,0,1,0,1,1,4,1,35,8,1,11,1,12,1,36,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,46,8,2,1,2,5,2,49,8,2,10,2,12,2,52,9,2,1,2,1,2,
        1,3,1,3,1,3,3,3,59,8,3,1,3,5,3,62,8,3,10,3,12,3,65,9,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,76,8,4,10,4,12,4,79,9,4,3,4,81,8,4,
        1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,4,8,93,8,8,11,8,12,8,94,
        1,9,1,9,1,9,5,9,100,8,9,10,9,12,9,103,9,9,1,9,1,9,1,9,1,9,1,10,1,
        10,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,13,0,0,14,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,4,1,0,7,11,1,0,7,10,2,0,17,
        17,19,21,1,0,23,24,117,0,29,1,0,0,0,2,34,1,0,0,0,4,38,1,0,0,0,6,
        55,1,0,0,0,8,80,1,0,0,0,10,82,1,0,0,0,12,84,1,0,0,0,14,86,1,0,0,
        0,16,92,1,0,0,0,18,96,1,0,0,0,20,108,1,0,0,0,22,114,1,0,0,0,24,116,
        1,0,0,0,26,118,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,29,30,1,0,0,0,
        30,31,1,0,0,0,31,32,3,6,3,0,32,1,1,0,0,0,33,35,3,4,2,0,34,33,1,0,
        0,0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,3,1,0,0,0,38,39,
        5,18,0,0,39,40,5,1,0,0,40,41,3,8,4,0,41,42,5,2,0,0,42,43,5,3,0,0,
        43,45,3,10,5,0,44,46,3,14,7,0,45,44,1,0,0,0,45,46,1,0,0,0,46,50,
        1,0,0,0,47,49,3,26,13,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,
        0,50,51,1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,53,54,5,4,0,0,54,5,1,
        0,0,0,55,56,5,5,0,0,56,58,5,3,0,0,57,59,3,14,7,0,58,57,1,0,0,0,58,
        59,1,0,0,0,59,63,1,0,0,0,60,62,3,26,13,0,61,60,1,0,0,0,62,65,1,0,
        0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,
        5,4,0,0,67,7,1,0,0,0,68,69,3,12,6,0,69,70,5,18,0,0,70,77,1,0,0,0,
        71,72,5,6,0,0,72,73,3,12,6,0,73,74,5,18,0,0,74,76,1,0,0,0,75,71,
        1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,81,1,0,0,0,
        79,77,1,0,0,0,80,68,1,0,0,0,80,81,1,0,0,0,81,9,1,0,0,0,82,83,7,0,
        0,0,83,11,1,0,0,0,84,85,7,1,0,0,85,13,1,0,0,0,86,87,5,12,0,0,87,
        88,5,3,0,0,88,89,3,16,8,0,89,15,1,0,0,0,90,93,3,18,9,0,91,93,3,20,
        10,0,92,90,1,0,0,0,92,91,1,0,0,0,93,94,1,0,0,0,94,92,1,0,0,0,94,
        95,1,0,0,0,95,17,1,0,0,0,96,101,5,18,0,0,97,98,5,6,0,0,98,100,5,
        18,0,0,99,97,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,
        0,0,102,104,1,0,0,0,103,101,1,0,0,0,104,105,5,3,0,0,105,106,3,12,
        6,0,106,107,5,13,0,0,107,19,1,0,0,0,108,109,5,14,0,0,109,110,5,18,
        0,0,110,111,5,15,0,0,111,112,3,22,11,0,112,113,5,13,0,0,113,21,1,
        0,0,0,114,115,7,2,0,0,115,23,1,0,0,0,116,117,7,3,0,0,117,25,1,0,
        0,0,118,119,5,16,0,0,119,27,1,0,0,0,11,29,36,45,50,58,63,77,80,92,
        94,101
    ]

class simplified_javaParser ( Parser ):

    grammarFileName = "simplified_java.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':'", "'end'", "'main'", 
                     "','", "'int'", "'float'", "'str'", "'bool'", "'void'", 
                     "'var'", "';'", "'const'", "'='", "'opa'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOOL", "ID", "INT", "FLOAT", "STR", 
                      "ESC", "LINE_COMMENT", "BLOCK_COMMENT", "WS" ]

    RULE_init = 0
    RULE_decFuncList = 1
    RULE_decFunc = 2
    RULE_funcMain = 3
    RULE_parametersList = 4
    RULE_funcType = 5
    RULE_dataType = 6
    RULE_varField = 7
    RULE_decVarConstList = 8
    RULE_decVar = 9
    RULE_decConst = 10
    RULE_value = 11
    RULE_comment = 12
    RULE_cmmd = 13

    ruleNames =  [ "init", "decFuncList", "decFunc", "funcMain", "parametersList", 
                   "funcType", "dataType", "varField", "decVarConstList", 
                   "decVar", "decConst", "value", "comment", "cmmd" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    BOOL=17
    ID=18
    INT=19
    FLOAT=20
    STR=21
    ESC=22
    LINE_COMMENT=23
    BLOCK_COMMENT=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcMain(self):
            return self.getTypedRuleContext(simplified_javaParser.FuncMainContext,0)


        def decFuncList(self):
            return self.getTypedRuleContext(simplified_javaParser.DecFuncListContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = simplified_javaParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 28
                self.decFuncList()


            self.state = 31
            self.funcMain()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecFuncListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decFunc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.DecFuncContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.DecFuncContext,i)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_decFuncList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecFuncList" ):
                listener.enterDecFuncList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecFuncList" ):
                listener.exitDecFuncList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecFuncList" ):
                return visitor.visitDecFuncList(self)
            else:
                return visitor.visitChildren(self)




    def decFuncList(self):

        localctx = simplified_javaParser.DecFuncListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decFuncList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 33
                self.decFunc()
                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==18):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(simplified_javaParser.ID, 0)

        def parametersList(self):
            return self.getTypedRuleContext(simplified_javaParser.ParametersListContext,0)


        def funcType(self):
            return self.getTypedRuleContext(simplified_javaParser.FuncTypeContext,0)


        def varField(self):
            return self.getTypedRuleContext(simplified_javaParser.VarFieldContext,0)


        def cmmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.CmmdContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.CmmdContext,i)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_decFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecFunc" ):
                listener.enterDecFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecFunc" ):
                listener.exitDecFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecFunc" ):
                return visitor.visitDecFunc(self)
            else:
                return visitor.visitChildren(self)




    def decFunc(self):

        localctx = simplified_javaParser.DecFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(simplified_javaParser.ID)
            self.state = 39
            self.match(simplified_javaParser.T__0)
            self.state = 40
            self.parametersList()
            self.state = 41
            self.match(simplified_javaParser.T__1)
            self.state = 42
            self.match(simplified_javaParser.T__2)
            self.state = 43
            self.funcType()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 44
                self.varField()


            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 47
                self.cmmd()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.match(simplified_javaParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncMainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varField(self):
            return self.getTypedRuleContext(simplified_javaParser.VarFieldContext,0)


        def cmmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.CmmdContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.CmmdContext,i)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_funcMain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncMain" ):
                listener.enterFuncMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncMain" ):
                listener.exitFuncMain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncMain" ):
                return visitor.visitFuncMain(self)
            else:
                return visitor.visitChildren(self)




    def funcMain(self):

        localctx = simplified_javaParser.FuncMainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcMain)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(simplified_javaParser.T__4)
            self.state = 56
            self.match(simplified_javaParser.T__2)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 57
                self.varField()


            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 60
                self.cmmd()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(simplified_javaParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.DataTypeContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.DataTypeContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(simplified_javaParser.ID)
            else:
                return self.getToken(simplified_javaParser.ID, i)

        def getRuleIndex(self):
            return simplified_javaParser.RULE_parametersList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametersList" ):
                listener.enterParametersList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametersList" ):
                listener.exitParametersList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametersList" ):
                return visitor.visitParametersList(self)
            else:
                return visitor.visitChildren(self)




    def parametersList(self):

        localctx = simplified_javaParser.ParametersListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parametersList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0):
                self.state = 68
                self.dataType()
                self.state = 69
                self.match(simplified_javaParser.ID)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 71
                    self.match(simplified_javaParser.T__5)
                    self.state = 72
                    self.dataType()
                    self.state = 73
                    self.match(simplified_javaParser.ID)
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return simplified_javaParser.RULE_funcType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncType" ):
                listener.enterFuncType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncType" ):
                listener.exitFuncType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncType" ):
                return visitor.visitFuncType(self)
            else:
                return visitor.visitChildren(self)




    def funcType(self):

        localctx = simplified_javaParser.FuncTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3968) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return simplified_javaParser.RULE_dataType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataType" ):
                listener.enterDataType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataType" ):
                listener.exitDataType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataType" ):
                return visitor.visitDataType(self)
            else:
                return visitor.visitChildren(self)




    def dataType(self):

        localctx = simplified_javaParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decVarConstList(self):
            return self.getTypedRuleContext(simplified_javaParser.DecVarConstListContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_varField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarField" ):
                listener.enterVarField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarField" ):
                listener.exitVarField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarField" ):
                return visitor.visitVarField(self)
            else:
                return visitor.visitChildren(self)




    def varField(self):

        localctx = simplified_javaParser.VarFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_varField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(simplified_javaParser.T__11)
            self.state = 87
            self.match(simplified_javaParser.T__2)
            self.state = 88
            self.decVarConstList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecVarConstListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decVar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.DecVarContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.DecVarContext,i)


        def decConst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.DecConstContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.DecConstContext,i)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_decVarConstList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecVarConstList" ):
                listener.enterDecVarConstList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecVarConstList" ):
                listener.exitDecVarConstList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecVarConstList" ):
                return visitor.visitDecVarConstList(self)
            else:
                return visitor.visitChildren(self)




    def decVarConstList(self):

        localctx = simplified_javaParser.DecVarConstListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_decVarConstList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 92
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [18]:
                    self.state = 90
                    self.decVar()
                    pass
                elif token in [14]:
                    self.state = 91
                    self.decConst()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 94 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14 or _la==18):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(simplified_javaParser.ID)
            else:
                return self.getToken(simplified_javaParser.ID, i)

        def dataType(self):
            return self.getTypedRuleContext(simplified_javaParser.DataTypeContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_decVar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecVar" ):
                listener.enterDecVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecVar" ):
                listener.exitDecVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecVar" ):
                return visitor.visitDecVar(self)
            else:
                return visitor.visitChildren(self)




    def decVar(self):

        localctx = simplified_javaParser.DecVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_decVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(simplified_javaParser.ID)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 97
                self.match(simplified_javaParser.T__5)
                self.state = 98
                self.match(simplified_javaParser.ID)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(simplified_javaParser.T__2)
            self.state = 105
            self.dataType()
            self.state = 106
            self.match(simplified_javaParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(simplified_javaParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(simplified_javaParser.ValueContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_decConst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecConst" ):
                listener.enterDecConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecConst" ):
                listener.exitDecConst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecConst" ):
                return visitor.visitDecConst(self)
            else:
                return visitor.visitChildren(self)




    def decConst(self):

        localctx = simplified_javaParser.DecConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_decConst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(simplified_javaParser.T__13)
            self.state = 109
            self.match(simplified_javaParser.ID)
            self.state = 110
            self.match(simplified_javaParser.T__14)
            self.state = 111
            self.value()
            self.state = 112
            self.match(simplified_javaParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(simplified_javaParser.INT, 0)

        def FLOAT(self):
            return self.getToken(simplified_javaParser.FLOAT, 0)

        def STR(self):
            return self.getToken(simplified_javaParser.STR, 0)

        def BOOL(self):
            return self.getToken(simplified_javaParser.BOOL, 0)

        def getRuleIndex(self):
            return simplified_javaParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = simplified_javaParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3801088) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE_COMMENT(self):
            return self.getToken(simplified_javaParser.LINE_COMMENT, 0)

        def BLOCK_COMMENT(self):
            return self.getToken(simplified_javaParser.BLOCK_COMMENT, 0)

        def getRuleIndex(self):
            return simplified_javaParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = simplified_javaParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return simplified_javaParser.RULE_cmmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmmd" ):
                listener.enterCmmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmmd" ):
                listener.exitCmmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmmd" ):
                return visitor.visitCmmd(self)
            else:
                return visitor.visitChildren(self)




    def cmmd(self):

        localctx = simplified_javaParser.CmmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_cmmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(simplified_javaParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





