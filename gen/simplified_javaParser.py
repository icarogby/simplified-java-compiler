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
        4,1,24,149,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,3,0,36,8,0,1,0,1,0,1,1,4,1,41,
        8,1,11,1,12,1,42,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,52,8,2,1,2,5,2,
        55,8,2,10,2,12,2,58,9,2,1,2,1,2,1,3,1,3,1,3,3,3,65,8,3,1,3,5,3,68,
        8,3,10,3,12,3,71,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,82,
        8,4,10,4,12,4,85,9,4,3,4,87,8,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,4,7,
        96,8,7,11,7,12,7,97,1,8,1,8,3,8,102,8,8,1,9,1,9,1,9,5,9,107,8,9,
        10,9,12,9,110,9,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,3,14,132,8,14,
        1,14,1,14,1,15,1,15,1,15,5,15,139,8,15,10,15,12,15,142,9,15,1,16,
        1,16,1,16,3,16,147,8,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,0,4,1,0,7,11,1,0,7,10,2,0,16,16,18,20,1,0,22,23,
        146,0,35,1,0,0,0,2,40,1,0,0,0,4,44,1,0,0,0,6,61,1,0,0,0,8,86,1,0,
        0,0,10,88,1,0,0,0,12,90,1,0,0,0,14,92,1,0,0,0,16,101,1,0,0,0,18,
        103,1,0,0,0,20,115,1,0,0,0,22,121,1,0,0,0,24,123,1,0,0,0,26,125,
        1,0,0,0,28,128,1,0,0,0,30,135,1,0,0,0,32,146,1,0,0,0,34,36,3,2,1,
        0,35,34,1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,0,37,38,3,6,3,0,38,1,1,
        0,0,0,39,41,3,4,2,0,40,39,1,0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,
        43,1,0,0,0,43,3,1,0,0,0,44,45,5,17,0,0,45,46,5,1,0,0,46,47,3,8,4,
        0,47,48,5,2,0,0,48,49,5,3,0,0,49,51,3,10,5,0,50,52,3,14,7,0,51,50,
        1,0,0,0,51,52,1,0,0,0,52,56,1,0,0,0,53,55,3,26,13,0,54,53,1,0,0,
        0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,56,
        1,0,0,0,59,60,5,4,0,0,60,5,1,0,0,0,61,62,5,5,0,0,62,64,5,3,0,0,63,
        65,3,14,7,0,64,63,1,0,0,0,64,65,1,0,0,0,65,69,1,0,0,0,66,68,3,26,
        13,0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,
        72,1,0,0,0,71,69,1,0,0,0,72,73,5,4,0,0,73,7,1,0,0,0,74,75,3,12,6,
        0,75,76,5,17,0,0,76,83,1,0,0,0,77,78,5,6,0,0,78,79,3,12,6,0,79,80,
        5,17,0,0,80,82,1,0,0,0,81,77,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,
        83,84,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,86,74,1,0,0,0,86,87,1,
        0,0,0,87,9,1,0,0,0,88,89,7,0,0,0,89,11,1,0,0,0,90,91,7,1,0,0,91,
        13,1,0,0,0,92,93,5,12,0,0,93,95,5,3,0,0,94,96,3,16,8,0,95,94,1,0,
        0,0,96,97,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,15,1,0,0,0,99,102,
        3,18,9,0,100,102,3,20,10,0,101,99,1,0,0,0,101,100,1,0,0,0,102,17,
        1,0,0,0,103,108,5,17,0,0,104,105,5,6,0,0,105,107,5,17,0,0,106,104,
        1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,111,
        1,0,0,0,110,108,1,0,0,0,111,112,5,3,0,0,112,113,3,12,6,0,113,114,
        5,13,0,0,114,19,1,0,0,0,115,116,5,14,0,0,116,117,5,17,0,0,117,118,
        5,15,0,0,118,119,3,22,11,0,119,120,5,13,0,0,120,21,1,0,0,0,121,122,
        7,2,0,0,122,23,1,0,0,0,123,124,7,3,0,0,124,25,1,0,0,0,125,126,3,
        28,14,0,126,127,5,13,0,0,127,27,1,0,0,0,128,129,5,17,0,0,129,131,
        5,1,0,0,130,132,3,30,15,0,131,130,1,0,0,0,131,132,1,0,0,0,132,133,
        1,0,0,0,133,134,5,2,0,0,134,29,1,0,0,0,135,140,3,32,16,0,136,137,
        5,6,0,0,137,139,3,32,16,0,138,136,1,0,0,0,139,142,1,0,0,0,140,138,
        1,0,0,0,140,141,1,0,0,0,141,31,1,0,0,0,142,140,1,0,0,0,143,147,5,
        17,0,0,144,147,3,22,11,0,145,147,3,28,14,0,146,143,1,0,0,0,146,144,
        1,0,0,0,146,145,1,0,0,0,147,33,1,0,0,0,14,35,42,51,56,64,69,83,86,
        97,101,108,131,140,146
    ]

class simplified_javaParser ( Parser ):

    grammarFileName = "simplified_java.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':'", "'end'", "'main'", 
                     "','", "'int'", "'float'", "'str'", "'bool'", "'void'", 
                     "'var'", "';'", "'const'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOOL", "ID", "INT", "FLOAT", "STR", "ESC", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "WS" ]

    RULE_init = 0
    RULE_decFuncList = 1
    RULE_decFunc = 2
    RULE_funcMain = 3
    RULE_parametersList = 4
    RULE_funcType = 5
    RULE_dataType = 6
    RULE_varField = 7
    RULE_decVarConst = 8
    RULE_decVar = 9
    RULE_decConst = 10
    RULE_value = 11
    RULE_comment = 12
    RULE_cmmd = 13
    RULE_inst = 14
    RULE_instParamList = 15
    RULE_instParam = 16

    ruleNames =  [ "init", "decFuncList", "decFunc", "funcMain", "parametersList", 
                   "funcType", "dataType", "varField", "decVarConst", "decVar", 
                   "decConst", "value", "comment", "cmmd", "inst", "instParamList", 
                   "instParam" ]

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
    BOOL=16
    ID=17
    INT=18
    FLOAT=19
    STR=20
    ESC=21
    LINE_COMMENT=22
    BLOCK_COMMENT=23
    WS=24

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
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 34
                self.decFuncList()


            self.state = 37
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
            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                self.decFunc()
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==17):
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
            self.state = 44
            self.match(simplified_javaParser.ID)
            self.state = 45
            self.match(simplified_javaParser.T__0)
            self.state = 46
            self.parametersList()
            self.state = 47
            self.match(simplified_javaParser.T__1)
            self.state = 48
            self.match(simplified_javaParser.T__2)
            self.state = 49
            self.funcType()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 50
                self.varField()


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 53
                self.cmmd()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
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
            self.state = 61
            self.match(simplified_javaParser.T__4)
            self.state = 62
            self.match(simplified_javaParser.T__2)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 63
                self.varField()


            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 66
                self.cmmd()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
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
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0):
                self.state = 74
                self.dataType()
                self.state = 75
                self.match(simplified_javaParser.ID)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 77
                    self.match(simplified_javaParser.T__5)
                    self.state = 78
                    self.dataType()
                    self.state = 79
                    self.match(simplified_javaParser.ID)
                    self.state = 85
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
            self.state = 88
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
            self.state = 90
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

        def decVarConst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.DecVarConstContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.DecVarConstContext,i)


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
            self.state = 92
            self.match(simplified_javaParser.T__11)
            self.state = 93
            self.match(simplified_javaParser.T__2)
            self.state = 95 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 94
                    self.decVarConst()

                else:
                    raise NoViableAltException(self)
                self.state = 97 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecVarConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decVar(self):
            return self.getTypedRuleContext(simplified_javaParser.DecVarContext,0)


        def decConst(self):
            return self.getTypedRuleContext(simplified_javaParser.DecConstContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_decVarConst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecVarConst" ):
                listener.enterDecVarConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecVarConst" ):
                listener.exitDecVarConst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecVarConst" ):
                return visitor.visitDecVarConst(self)
            else:
                return visitor.visitChildren(self)




    def decVarConst(self):

        localctx = simplified_javaParser.DecVarConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_decVarConst)
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.decVar()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.decConst()
                pass
            else:
                raise NoViableAltException(self)

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
            self.state = 103
            self.match(simplified_javaParser.ID)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 104
                self.match(simplified_javaParser.T__5)
                self.state = 105
                self.match(simplified_javaParser.ID)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self.match(simplified_javaParser.T__2)
            self.state = 112
            self.dataType()
            self.state = 113
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
            self.state = 115
            self.match(simplified_javaParser.T__13)
            self.state = 116
            self.match(simplified_javaParser.ID)
            self.state = 117
            self.match(simplified_javaParser.T__14)
            self.state = 118
            self.value()
            self.state = 119
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
            self.state = 121
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1900544) != 0)):
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
            self.state = 123
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
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

        def inst(self):
            return self.getTypedRuleContext(simplified_javaParser.InstContext,0)


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
            self.state = 125
            self.inst()
            self.state = 126
            self.match(simplified_javaParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(simplified_javaParser.ID, 0)

        def instParamList(self):
            return self.getTypedRuleContext(simplified_javaParser.InstParamListContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_inst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInst" ):
                listener.enterInst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInst" ):
                listener.exitInst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInst" ):
                return visitor.visitInst(self)
            else:
                return visitor.visitChildren(self)




    def inst(self):

        localctx = simplified_javaParser.InstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_inst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(simplified_javaParser.ID)
            self.state = 129
            self.match(simplified_javaParser.T__0)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2031616) != 0):
                self.state = 130
                self.instParamList()


            self.state = 133
            self.match(simplified_javaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instParam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.InstParamContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.InstParamContext,i)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_instParamList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstParamList" ):
                listener.enterInstParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstParamList" ):
                listener.exitInstParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstParamList" ):
                return visitor.visitInstParamList(self)
            else:
                return visitor.visitChildren(self)




    def instParamList(self):

        localctx = simplified_javaParser.InstParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_instParamList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.instParam()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 136
                self.match(simplified_javaParser.T__5)
                self.state = 137
                self.instParam()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(simplified_javaParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(simplified_javaParser.ValueContext,0)


        def inst(self):
            return self.getTypedRuleContext(simplified_javaParser.InstContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_instParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstParam" ):
                listener.enterInstParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstParam" ):
                listener.exitInstParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstParam" ):
                return visitor.visitInstParam(self)
            else:
                return visitor.visitChildren(self)




    def instParam(self):

        localctx = simplified_javaParser.InstParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_instParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 143
                self.match(simplified_javaParser.ID)
                pass

            elif la_ == 2:
                self.state = 144
                self.value()
                pass

            elif la_ == 3:
                self.state = 145
                self.inst()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





