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
        4,1,42,324,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,74,8,1,1,1,3,1,77,8,1,1,1,5,1,80,8,1,
        10,1,12,1,83,9,1,1,1,1,1,1,2,1,2,1,2,3,2,90,8,2,1,2,5,2,93,8,2,10,
        2,12,2,96,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,107,8,3,10,
        3,12,3,110,9,3,3,3,112,8,3,1,4,1,4,1,5,1,5,1,5,1,5,4,5,120,8,5,11,
        5,12,5,121,1,6,1,6,1,6,5,6,127,8,6,10,6,12,6,130,9,6,1,6,1,6,1,6,
        1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,3,9,152,8,9,1,10,1,10,1,10,3,10,157,8,10,1,10,1,10,1,11,1,11,
        1,11,1,11,3,11,165,8,11,1,11,1,11,1,11,1,11,1,11,3,11,172,8,11,5,
        11,174,8,11,10,11,12,11,177,9,11,1,12,1,12,1,12,1,12,1,12,1,13,1,
        13,1,13,1,13,3,13,188,8,13,1,13,1,13,1,14,1,14,1,14,1,14,3,14,196,
        8,14,1,14,1,14,1,14,5,14,201,8,14,10,14,12,14,204,9,14,1,14,3,14,
        207,8,14,1,14,1,14,1,15,1,15,1,15,5,15,214,8,15,10,15,12,15,217,
        9,15,1,16,1,16,1,16,1,16,3,16,223,8,16,1,16,1,16,1,16,5,16,228,8,
        16,10,16,12,16,231,9,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,3,18,
        240,8,18,1,19,1,19,1,19,1,19,1,19,1,19,5,19,248,8,19,10,19,12,19,
        251,9,19,1,20,1,20,1,20,1,20,1,20,1,20,5,20,259,8,20,10,20,12,20,
        262,9,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,271,8,21,1,22,1,
        22,1,22,1,22,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,
        24,5,24,288,8,24,10,24,12,24,291,9,24,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,5,25,302,8,25,10,25,12,25,305,9,25,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,3,26,314,8,26,1,27,1,27,1,27,1,27,3,27,320,
        8,27,1,28,1,28,1,28,0,4,38,40,48,50,29,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,0,4,1,0,
        8,11,2,0,34,34,36,38,1,0,24,29,1,0,40,41,340,0,61,1,0,0,0,2,66,1,
        0,0,0,4,86,1,0,0,0,6,111,1,0,0,0,8,113,1,0,0,0,10,115,1,0,0,0,12,
        123,1,0,0,0,14,135,1,0,0,0,16,141,1,0,0,0,18,151,1,0,0,0,20,153,
        1,0,0,0,22,164,1,0,0,0,24,178,1,0,0,0,26,183,1,0,0,0,28,191,1,0,
        0,0,30,210,1,0,0,0,32,218,1,0,0,0,34,234,1,0,0,0,36,239,1,0,0,0,
        38,241,1,0,0,0,40,252,1,0,0,0,42,270,1,0,0,0,44,272,1,0,0,0,46,276,
        1,0,0,0,48,278,1,0,0,0,50,292,1,0,0,0,52,313,1,0,0,0,54,319,1,0,
        0,0,56,321,1,0,0,0,58,60,3,2,1,0,59,58,1,0,0,0,60,63,1,0,0,0,61,
        59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,3,4,2,
        0,65,1,1,0,0,0,66,67,5,35,0,0,67,68,5,1,0,0,68,69,3,6,3,0,69,70,
        5,2,0,0,70,73,5,3,0,0,71,74,3,8,4,0,72,74,5,4,0,0,73,71,1,0,0,0,
        73,72,1,0,0,0,74,76,1,0,0,0,75,77,3,10,5,0,76,75,1,0,0,0,76,77,1,
        0,0,0,77,81,1,0,0,0,78,80,3,18,9,0,79,78,1,0,0,0,80,83,1,0,0,0,81,
        79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,5,0,
        0,85,3,1,0,0,0,86,87,5,6,0,0,87,89,5,3,0,0,88,90,3,10,5,0,89,88,
        1,0,0,0,89,90,1,0,0,0,90,94,1,0,0,0,91,93,3,18,9,0,92,91,1,0,0,0,
        93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,94,1,
        0,0,0,97,98,5,5,0,0,98,5,1,0,0,0,99,100,3,8,4,0,100,101,5,35,0,0,
        101,108,1,0,0,0,102,103,5,7,0,0,103,104,3,8,4,0,104,105,5,35,0,0,
        105,107,1,0,0,0,106,102,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,
        108,109,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,111,99,1,0,0,0,111,
        112,1,0,0,0,112,7,1,0,0,0,113,114,7,0,0,0,114,9,1,0,0,0,115,116,
        5,12,0,0,116,119,5,3,0,0,117,120,3,12,6,0,118,120,3,14,7,0,119,117,
        1,0,0,0,119,118,1,0,0,0,120,121,1,0,0,0,121,119,1,0,0,0,121,122,
        1,0,0,0,122,11,1,0,0,0,123,128,5,35,0,0,124,125,5,7,0,0,125,127,
        5,35,0,0,126,124,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,
        1,0,0,0,129,131,1,0,0,0,130,128,1,0,0,0,131,132,5,3,0,0,132,133,
        3,8,4,0,133,134,5,13,0,0,134,13,1,0,0,0,135,136,5,14,0,0,136,137,
        5,35,0,0,137,138,5,15,0,0,138,139,3,16,8,0,139,140,5,13,0,0,140,
        15,1,0,0,0,141,142,7,1,0,0,142,17,1,0,0,0,143,152,3,28,14,0,144,
        152,3,24,12,0,145,152,3,32,16,0,146,152,3,26,13,0,147,152,3,34,17,
        0,148,149,3,20,10,0,149,150,5,13,0,0,150,152,1,0,0,0,151,143,1,0,
        0,0,151,144,1,0,0,0,151,145,1,0,0,0,151,146,1,0,0,0,151,147,1,0,
        0,0,151,148,1,0,0,0,152,19,1,0,0,0,153,154,5,35,0,0,154,156,5,1,
        0,0,155,157,3,22,11,0,156,155,1,0,0,0,156,157,1,0,0,0,157,158,1,
        0,0,0,158,159,5,2,0,0,159,21,1,0,0,0,160,165,5,35,0,0,161,165,3,
        16,8,0,162,165,3,20,10,0,163,165,3,36,18,0,164,160,1,0,0,0,164,161,
        1,0,0,0,164,162,1,0,0,0,164,163,1,0,0,0,165,175,1,0,0,0,166,171,
        5,7,0,0,167,172,5,35,0,0,168,172,3,16,8,0,169,172,3,20,10,0,170,
        172,3,36,18,0,171,167,1,0,0,0,171,168,1,0,0,0,171,169,1,0,0,0,171,
        170,1,0,0,0,172,174,1,0,0,0,173,166,1,0,0,0,174,177,1,0,0,0,175,
        173,1,0,0,0,175,176,1,0,0,0,176,23,1,0,0,0,177,175,1,0,0,0,178,179,
        5,35,0,0,179,180,5,15,0,0,180,181,3,36,18,0,181,182,5,13,0,0,182,
        25,1,0,0,0,183,187,5,16,0,0,184,188,5,35,0,0,185,188,3,16,8,0,186,
        188,3,36,18,0,187,184,1,0,0,0,187,185,1,0,0,0,187,186,1,0,0,0,188,
        189,1,0,0,0,189,190,5,13,0,0,190,27,1,0,0,0,191,192,5,17,0,0,192,
        195,5,1,0,0,193,196,3,38,19,0,194,196,5,34,0,0,195,193,1,0,0,0,195,
        194,1,0,0,0,196,197,1,0,0,0,197,198,5,2,0,0,198,202,5,3,0,0,199,
        201,3,18,9,0,200,199,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,
        203,1,0,0,0,203,206,1,0,0,0,204,202,1,0,0,0,205,207,3,30,15,0,206,
        205,1,0,0,0,206,207,1,0,0,0,207,208,1,0,0,0,208,209,5,5,0,0,209,
        29,1,0,0,0,210,211,5,18,0,0,211,215,5,3,0,0,212,214,3,18,9,0,213,
        212,1,0,0,0,214,217,1,0,0,0,215,213,1,0,0,0,215,216,1,0,0,0,216,
        31,1,0,0,0,217,215,1,0,0,0,218,219,5,19,0,0,219,222,5,1,0,0,220,
        223,3,38,19,0,221,223,5,34,0,0,222,220,1,0,0,0,222,221,1,0,0,0,223,
        224,1,0,0,0,224,225,5,2,0,0,225,229,5,3,0,0,226,228,3,18,9,0,227,
        226,1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,
        232,1,0,0,0,231,229,1,0,0,0,232,233,5,5,0,0,233,33,1,0,0,0,234,235,
        5,20,0,0,235,236,5,13,0,0,236,35,1,0,0,0,237,240,3,38,19,0,238,240,
        3,48,24,0,239,237,1,0,0,0,239,238,1,0,0,0,240,37,1,0,0,0,241,242,
        6,19,-1,0,242,243,3,40,20,0,243,249,1,0,0,0,244,245,10,1,0,0,245,
        246,5,21,0,0,246,248,3,40,20,0,247,244,1,0,0,0,248,251,1,0,0,0,249,
        247,1,0,0,0,249,250,1,0,0,0,250,39,1,0,0,0,251,249,1,0,0,0,252,253,
        6,20,-1,0,253,254,3,42,21,0,254,260,1,0,0,0,255,256,10,1,0,0,256,
        257,5,22,0,0,257,259,3,42,21,0,258,255,1,0,0,0,259,262,1,0,0,0,260,
        258,1,0,0,0,260,261,1,0,0,0,261,41,1,0,0,0,262,260,1,0,0,0,263,264,
        5,23,0,0,264,271,3,42,21,0,265,266,5,1,0,0,266,267,3,38,19,0,267,
        268,5,2,0,0,268,271,1,0,0,0,269,271,3,44,22,0,270,263,1,0,0,0,270,
        265,1,0,0,0,270,269,1,0,0,0,271,43,1,0,0,0,272,273,3,48,24,0,273,
        274,3,46,23,0,274,275,3,48,24,0,275,45,1,0,0,0,276,277,7,2,0,0,277,
        47,1,0,0,0,278,279,6,24,-1,0,279,280,3,50,25,0,280,289,1,0,0,0,281,
        282,10,2,0,0,282,283,5,30,0,0,283,288,3,50,25,0,284,285,10,1,0,0,
        285,286,5,31,0,0,286,288,3,50,25,0,287,281,1,0,0,0,287,284,1,0,0,
        0,288,291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,49,1,0,0,0,
        291,289,1,0,0,0,292,293,6,25,-1,0,293,294,3,52,26,0,294,303,1,0,
        0,0,295,296,10,2,0,0,296,297,5,32,0,0,297,302,3,52,26,0,298,299,
        10,1,0,0,299,300,5,33,0,0,300,302,3,52,26,0,301,295,1,0,0,0,301,
        298,1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,0,303,304,1,0,0,0,304,
        51,1,0,0,0,305,303,1,0,0,0,306,314,3,54,27,0,307,308,5,31,0,0,308,
        314,3,52,26,0,309,310,5,1,0,0,310,311,3,48,24,0,311,312,5,2,0,0,
        312,314,1,0,0,0,313,306,1,0,0,0,313,307,1,0,0,0,313,309,1,0,0,0,
        314,53,1,0,0,0,315,320,5,35,0,0,316,320,5,36,0,0,317,320,5,37,0,
        0,318,320,3,20,10,0,319,315,1,0,0,0,319,316,1,0,0,0,319,317,1,0,
        0,0,319,318,1,0,0,0,320,55,1,0,0,0,321,322,7,3,0,0,322,57,1,0,0,
        0,33,61,73,76,81,89,94,108,111,119,121,128,151,156,164,171,175,187,
        195,202,206,215,222,229,239,249,260,270,287,289,301,303,313,319
    ]

class simplified_javaParser ( Parser ):

    grammarFileName = "simplified_java.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':'", "'void'", "'end'", 
                     "'main'", "','", "'int'", "'float'", "'str'", "'bool'", 
                     "'var'", "';'", "'const'", "'='", "'return'", "'if'", 
                     "'else'", "'while'", "'break'", "'or'", "'and'", "'!'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'=>'", "'+'", 
                     "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BOOL", "ID", "INT", "FLOAT", 
                      "STR", "ESC", "LINE_COMMENT", "BLOCK_COMMENT", "WS" ]

    RULE_init = 0
    RULE_func = 1
    RULE_func_main = 2
    RULE_parameters_list = 3
    RULE_type = 4
    RULE_dec_list = 5
    RULE_dec_var = 6
    RULE_dec_const = 7
    RULE_value = 8
    RULE_comd = 9
    RULE_inst = 10
    RULE_value_list = 11
    RULE_assign = 12
    RULE_return = 13
    RULE_if = 14
    RULE_else = 15
    RULE_while = 16
    RULE_break = 17
    RULE_exp = 18
    RULE_logic_exp = 19
    RULE_logic_t = 20
    RULE_logic_f = 21
    RULE_comparison = 22
    RULE_comparison_op = 23
    RULE_arith_exp = 24
    RULE_arith_t = 25
    RULE_arith_f = 26
    RULE_number = 27
    RULE_comment = 28

    ruleNames =  [ "init", "func", "func_main", "parameters_list", "type", 
                   "dec_list", "dec_var", "dec_const", "value", "comd", 
                   "inst", "value_list", "assign", "return", "if", "else", 
                   "while", "break", "exp", "logic_exp", "logic_t", "logic_f", 
                   "comparison", "comparison_op", "arith_exp", "arith_t", 
                   "arith_f", "number", "comment" ]

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
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    BOOL=34
    ID=35
    INT=36
    FLOAT=37
    STR=38
    ESC=39
    LINE_COMMENT=40
    BLOCK_COMMENT=41
    WS=42

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

        def func_main(self):
            return self.getTypedRuleContext(simplified_javaParser.Func_mainContext,0)


        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.FuncContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.FuncContext,i)


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
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 58
                self.func()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.func_main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(simplified_javaParser.ID, 0)

        def parameters_list(self):
            return self.getTypedRuleContext(simplified_javaParser.Parameters_listContext,0)


        def type_(self):
            return self.getTypedRuleContext(simplified_javaParser.TypeContext,0)


        def dec_list(self):
            return self.getTypedRuleContext(simplified_javaParser.Dec_listContext,0)


        def comd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.ComdContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.ComdContext,i)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = simplified_javaParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(simplified_javaParser.ID)
            self.state = 67
            self.match(simplified_javaParser.T__0)
            self.state = 68
            self.parameters_list()
            self.state = 69
            self.match(simplified_javaParser.T__1)
            self.state = 70
            self.match(simplified_javaParser.T__2)
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11]:
                self.state = 71
                self.type_()
                pass
            elif token in [4]:
                self.state = 72
                self.match(simplified_javaParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 75
                self.dec_list()


            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34361507840) != 0):
                self.state = 78
                self.comd()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(simplified_javaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_mainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dec_list(self):
            return self.getTypedRuleContext(simplified_javaParser.Dec_listContext,0)


        def comd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.ComdContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.ComdContext,i)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_func_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_main" ):
                listener.enterFunc_main(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_main" ):
                listener.exitFunc_main(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_main" ):
                return visitor.visitFunc_main(self)
            else:
                return visitor.visitChildren(self)




    def func_main(self):

        localctx = simplified_javaParser.Func_mainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(simplified_javaParser.T__5)
            self.state = 87
            self.match(simplified_javaParser.T__2)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 88
                self.dec_list()


            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34361507840) != 0):
                self.state = 91
                self.comd()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(simplified_javaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameters_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.TypeContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.TypeContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(simplified_javaParser.ID)
            else:
                return self.getToken(simplified_javaParser.ID, i)

        def getRuleIndex(self):
            return simplified_javaParser.RULE_parameters_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters_list" ):
                listener.enterParameters_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters_list" ):
                listener.exitParameters_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters_list" ):
                return visitor.visitParameters_list(self)
            else:
                return visitor.visitChildren(self)




    def parameters_list(self):

        localctx = simplified_javaParser.Parameters_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parameters_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0):
                self.state = 99
                self.type_()
                self.state = 100
                self.match(simplified_javaParser.ID)
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 102
                    self.match(simplified_javaParser.T__6)
                    self.state = 103
                    self.type_()
                    self.state = 104
                    self.match(simplified_javaParser.ID)
                    self.state = 110
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return simplified_javaParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = simplified_javaParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
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


    class Dec_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dec_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.Dec_varContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.Dec_varContext,i)


        def dec_const(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.Dec_constContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.Dec_constContext,i)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_dec_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDec_list" ):
                listener.enterDec_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDec_list" ):
                listener.exitDec_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec_list" ):
                return visitor.visitDec_list(self)
            else:
                return visitor.visitChildren(self)




    def dec_list(self):

        localctx = simplified_javaParser.Dec_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dec_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(simplified_javaParser.T__11)
            self.state = 116
            self.match(simplified_javaParser.T__2)
            self.state = 119 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 119
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [35]:
                        self.state = 117
                        self.dec_var()
                        pass
                    elif token in [14]:
                        self.state = 118
                        self.dec_const()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 121 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dec_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(simplified_javaParser.ID)
            else:
                return self.getToken(simplified_javaParser.ID, i)

        def type_(self):
            return self.getTypedRuleContext(simplified_javaParser.TypeContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_dec_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDec_var" ):
                listener.enterDec_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDec_var" ):
                listener.exitDec_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec_var" ):
                return visitor.visitDec_var(self)
            else:
                return visitor.visitChildren(self)




    def dec_var(self):

        localctx = simplified_javaParser.Dec_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dec_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(simplified_javaParser.ID)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 124
                self.match(simplified_javaParser.T__6)
                self.state = 125
                self.match(simplified_javaParser.ID)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(simplified_javaParser.T__2)
            self.state = 132
            self.type_()
            self.state = 133
            self.match(simplified_javaParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dec_constContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(simplified_javaParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(simplified_javaParser.ValueContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_dec_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDec_const" ):
                listener.enterDec_const(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDec_const" ):
                listener.exitDec_const(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec_const" ):
                return visitor.visitDec_const(self)
            else:
                return visitor.visitChildren(self)




    def dec_const(self):

        localctx = simplified_javaParser.Dec_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dec_const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(simplified_javaParser.T__13)
            self.state = 136
            self.match(simplified_javaParser.ID)
            self.state = 137
            self.match(simplified_javaParser.T__14)
            self.state = 138
            self.value()
            self.state = 139
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
        self.enterRule(localctx, 16, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 498216206336) != 0)):
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


    class ComdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(simplified_javaParser.IfContext,0)


        def assign(self):
            return self.getTypedRuleContext(simplified_javaParser.AssignContext,0)


        def while_(self):
            return self.getTypedRuleContext(simplified_javaParser.WhileContext,0)


        def return_(self):
            return self.getTypedRuleContext(simplified_javaParser.ReturnContext,0)


        def break_(self):
            return self.getTypedRuleContext(simplified_javaParser.BreakContext,0)


        def inst(self):
            return self.getTypedRuleContext(simplified_javaParser.InstContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_comd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComd" ):
                listener.enterComd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComd" ):
                listener.exitComd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComd" ):
                return visitor.visitComd(self)
            else:
                return visitor.visitChildren(self)




    def comd(self):

        localctx = simplified_javaParser.ComdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comd)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.if_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.while_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.return_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 147
                self.break_()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 148
                self.inst()
                self.state = 149
                self.match(simplified_javaParser.T__12)
                pass


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

        def value_list(self):
            return self.getTypedRuleContext(simplified_javaParser.Value_listContext,0)


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
        self.enterRule(localctx, 20, self.RULE_inst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(simplified_javaParser.ID)
            self.state = 154
            self.match(simplified_javaParser.T__0)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 534731816962) != 0):
                self.state = 155
                self.value_list()


            self.state = 158
            self.match(simplified_javaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(simplified_javaParser.ID)
            else:
                return self.getToken(simplified_javaParser.ID, i)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.ValueContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.ValueContext,i)


        def inst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.InstContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.InstContext,i)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.ExpContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.ExpContext,i)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_value_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_list" ):
                listener.enterValue_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_list" ):
                listener.exitValue_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_list" ):
                return visitor.visitValue_list(self)
            else:
                return visitor.visitChildren(self)




    def value_list(self):

        localctx = simplified_javaParser.Value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_value_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 160
                self.match(simplified_javaParser.ID)
                pass

            elif la_ == 2:
                self.state = 161
                self.value()
                pass

            elif la_ == 3:
                self.state = 162
                self.inst()
                pass

            elif la_ == 4:
                self.state = 163
                self.exp()
                pass


            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 166
                self.match(simplified_javaParser.T__6)
                self.state = 171
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 167
                    self.match(simplified_javaParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 168
                    self.value()
                    pass

                elif la_ == 3:
                    self.state = 169
                    self.inst()
                    pass

                elif la_ == 4:
                    self.state = 170
                    self.exp()
                    pass


                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(simplified_javaParser.ID, 0)

        def exp(self):
            return self.getTypedRuleContext(simplified_javaParser.ExpContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = simplified_javaParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(simplified_javaParser.ID)
            self.state = 179
            self.match(simplified_javaParser.T__14)
            self.state = 180
            self.exp()
            self.state = 181
            self.match(simplified_javaParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(simplified_javaParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(simplified_javaParser.ValueContext,0)


        def exp(self):
            return self.getTypedRuleContext(simplified_javaParser.ExpContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)




    def return_(self):

        localctx = simplified_javaParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(simplified_javaParser.T__15)
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 184
                self.match(simplified_javaParser.ID)
                pass

            elif la_ == 2:
                self.state = 185
                self.value()
                pass

            elif la_ == 3:
                self.state = 186
                self.exp()
                pass


            self.state = 189
            self.match(simplified_javaParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic_exp(self):
            return self.getTypedRuleContext(simplified_javaParser.Logic_expContext,0)


        def BOOL(self):
            return self.getToken(simplified_javaParser.BOOL, 0)

        def comd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.ComdContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.ComdContext,i)


        def else_(self):
            return self.getTypedRuleContext(simplified_javaParser.ElseContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = simplified_javaParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(simplified_javaParser.T__16)
            self.state = 192
            self.match(simplified_javaParser.T__0)
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 23, 31, 35, 36, 37]:
                self.state = 193
                self.logic_exp(0)
                pass
            elif token in [34]:
                self.state = 194
                self.match(simplified_javaParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 197
            self.match(simplified_javaParser.T__1)
            self.state = 198
            self.match(simplified_javaParser.T__2)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34361507840) != 0):
                self.state = 199
                self.comd()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 205
                self.else_()


            self.state = 208
            self.match(simplified_javaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.ComdContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.ComdContext,i)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse" ):
                return visitor.visitElse(self)
            else:
                return visitor.visitChildren(self)




    def else_(self):

        localctx = simplified_javaParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(simplified_javaParser.T__17)
            self.state = 211
            self.match(simplified_javaParser.T__2)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34361507840) != 0):
                self.state = 212
                self.comd()
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic_exp(self):
            return self.getTypedRuleContext(simplified_javaParser.Logic_expContext,0)


        def BOOL(self):
            return self.getToken(simplified_javaParser.BOOL, 0)

        def comd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.ComdContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.ComdContext,i)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = simplified_javaParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(simplified_javaParser.T__18)
            self.state = 219
            self.match(simplified_javaParser.T__0)
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 23, 31, 35, 36, 37]:
                self.state = 220
                self.logic_exp(0)
                pass
            elif token in [34]:
                self.state = 221
                self.match(simplified_javaParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 224
            self.match(simplified_javaParser.T__1)
            self.state = 225
            self.match(simplified_javaParser.T__2)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34361507840) != 0):
                self.state = 226
                self.comd()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 232
            self.match(simplified_javaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return simplified_javaParser.RULE_break

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak" ):
                listener.enterBreak(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak" ):
                listener.exitBreak(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak" ):
                return visitor.visitBreak(self)
            else:
                return visitor.visitChildren(self)




    def break_(self):

        localctx = simplified_javaParser.BreakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(simplified_javaParser.T__19)
            self.state = 235
            self.match(simplified_javaParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic_exp(self):
            return self.getTypedRuleContext(simplified_javaParser.Logic_expContext,0)


        def arith_exp(self):
            return self.getTypedRuleContext(simplified_javaParser.Arith_expContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = simplified_javaParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exp)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.logic_exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.arith_exp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic_t(self):
            return self.getTypedRuleContext(simplified_javaParser.Logic_tContext,0)


        def logic_exp(self):
            return self.getTypedRuleContext(simplified_javaParser.Logic_expContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_logic_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_exp" ):
                listener.enterLogic_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_exp" ):
                listener.exitLogic_exp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_exp" ):
                return visitor.visitLogic_exp(self)
            else:
                return visitor.visitChildren(self)



    def logic_exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = simplified_javaParser.Logic_expContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_logic_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.logic_t(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = simplified_javaParser.Logic_expContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_exp)
                    self.state = 244
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 245
                    self.match(simplified_javaParser.T__20)
                    self.state = 246
                    self.logic_t(0) 
                self.state = 251
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logic_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic_f(self):
            return self.getTypedRuleContext(simplified_javaParser.Logic_fContext,0)


        def logic_t(self):
            return self.getTypedRuleContext(simplified_javaParser.Logic_tContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_logic_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_t" ):
                listener.enterLogic_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_t" ):
                listener.exitLogic_t(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_t" ):
                return visitor.visitLogic_t(self)
            else:
                return visitor.visitChildren(self)



    def logic_t(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = simplified_javaParser.Logic_tContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_logic_t, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.logic_f()
            self._ctx.stop = self._input.LT(-1)
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = simplified_javaParser.Logic_tContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_t)
                    self.state = 255
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 256
                    self.match(simplified_javaParser.T__21)
                    self.state = 257
                    self.logic_f() 
                self.state = 262
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logic_fContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic_f(self):
            return self.getTypedRuleContext(simplified_javaParser.Logic_fContext,0)


        def logic_exp(self):
            return self.getTypedRuleContext(simplified_javaParser.Logic_expContext,0)


        def comparison(self):
            return self.getTypedRuleContext(simplified_javaParser.ComparisonContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_logic_f

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_f" ):
                listener.enterLogic_f(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_f" ):
                listener.exitLogic_f(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_f" ):
                return visitor.visitLogic_f(self)
            else:
                return visitor.visitChildren(self)




    def logic_f(self):

        localctx = simplified_javaParser.Logic_fContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_logic_f)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(simplified_javaParser.T__22)
                self.state = 264
                self.logic_f()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.match(simplified_javaParser.T__0)
                self.state = 266
                self.logic_exp(0)
                self.state = 267
                self.match(simplified_javaParser.T__1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 269
                self.comparison()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arith_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplified_javaParser.Arith_expContext)
            else:
                return self.getTypedRuleContext(simplified_javaParser.Arith_expContext,i)


        def comparison_op(self):
            return self.getTypedRuleContext(simplified_javaParser.Comparison_opContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = simplified_javaParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.arith_exp(0)
            self.state = 273
            self.comparison_op()
            self.state = 274
            self.arith_exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return simplified_javaParser.RULE_comparison_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_op" ):
                listener.enterComparison_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_op" ):
                listener.exitComparison_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison_op" ):
                return visitor.visitComparison_op(self)
            else:
                return visitor.visitChildren(self)




    def comparison_op(self):

        localctx = simplified_javaParser.Comparison_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_comparison_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
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


    class Arith_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arith_t(self):
            return self.getTypedRuleContext(simplified_javaParser.Arith_tContext,0)


        def arith_exp(self):
            return self.getTypedRuleContext(simplified_javaParser.Arith_expContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_arith_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_exp" ):
                listener.enterArith_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_exp" ):
                listener.exitArith_exp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArith_exp" ):
                return visitor.visitArith_exp(self)
            else:
                return visitor.visitChildren(self)



    def arith_exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = simplified_javaParser.Arith_expContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_arith_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.arith_t(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 289
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 287
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = simplified_javaParser.Arith_expContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arith_exp)
                        self.state = 281
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 282
                        self.match(simplified_javaParser.T__29)
                        self.state = 283
                        self.arith_t(0)
                        pass

                    elif la_ == 2:
                        localctx = simplified_javaParser.Arith_expContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arith_exp)
                        self.state = 284
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 285
                        self.match(simplified_javaParser.T__30)
                        self.state = 286
                        self.arith_t(0)
                        pass

             
                self.state = 291
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Arith_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arith_f(self):
            return self.getTypedRuleContext(simplified_javaParser.Arith_fContext,0)


        def arith_t(self):
            return self.getTypedRuleContext(simplified_javaParser.Arith_tContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_arith_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_t" ):
                listener.enterArith_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_t" ):
                listener.exitArith_t(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArith_t" ):
                return visitor.visitArith_t(self)
            else:
                return visitor.visitChildren(self)



    def arith_t(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = simplified_javaParser.Arith_tContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_arith_t, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.arith_f()
            self._ctx.stop = self._input.LT(-1)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 301
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = simplified_javaParser.Arith_tContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arith_t)
                        self.state = 295
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 296
                        self.match(simplified_javaParser.T__31)
                        self.state = 297
                        self.arith_f()
                        pass

                    elif la_ == 2:
                        localctx = simplified_javaParser.Arith_tContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arith_t)
                        self.state = 298
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 299
                        self.match(simplified_javaParser.T__32)
                        self.state = 300
                        self.arith_f()
                        pass

             
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Arith_fContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(simplified_javaParser.NumberContext,0)


        def arith_f(self):
            return self.getTypedRuleContext(simplified_javaParser.Arith_fContext,0)


        def arith_exp(self):
            return self.getTypedRuleContext(simplified_javaParser.Arith_expContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_arith_f

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_f" ):
                listener.enterArith_f(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_f" ):
                listener.exitArith_f(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArith_f" ):
                return visitor.visitArith_f(self)
            else:
                return visitor.visitChildren(self)




    def arith_f(self):

        localctx = simplified_javaParser.Arith_fContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_arith_f)
        try:
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35, 36, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.number()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.match(simplified_javaParser.T__30)
                self.state = 308
                self.arith_f()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 309
                self.match(simplified_javaParser.T__0)
                self.state = 310
                self.arith_exp(0)
                self.state = 311
                self.match(simplified_javaParser.T__1)
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


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(simplified_javaParser.ID, 0)

        def INT(self):
            return self.getToken(simplified_javaParser.INT, 0)

        def FLOAT(self):
            return self.getToken(simplified_javaParser.FLOAT, 0)

        def inst(self):
            return self.getTypedRuleContext(simplified_javaParser.InstContext,0)


        def getRuleIndex(self):
            return simplified_javaParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = simplified_javaParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_number)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.match(simplified_javaParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.match(simplified_javaParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 317
                self.match(simplified_javaParser.FLOAT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 318
                self.inst()
                pass


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
        self.enterRule(localctx, 56, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            _la = self._input.LA(1)
            if not(_la==40 or _la==41):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.logic_exp_sempred
        self._predicates[20] = self.logic_t_sempred
        self._predicates[24] = self.arith_exp_sempred
        self._predicates[25] = self.arith_t_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logic_exp_sempred(self, localctx:Logic_expContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def logic_t_sempred(self, localctx:Logic_tContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def arith_exp_sempred(self, localctx:Arith_expContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def arith_t_sempred(self, localctx:Arith_tContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         




