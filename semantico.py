from gen.simplified_javaVisitor import simplified_javaVisitor
from gen.simplified_javaParser import simplified_javaParser

class analizadorSemantico(simplified_javaVisitor):
    symbolTable = {}
    parameterTable = {}

    def __init__(self):
        self.symbolTable = {}
        self.parameterTable = {}

    def defineType(self, value: str):
        if value == "true" or value == "false":
            return "bool"
        try:
            int(value)
            return 'int'
        except ValueError:
            try:
                float(value)
                return 'float'
            except ValueError:
                return 'str'

        # Visit a parse tree produced by simplified_javaParser#decFunc.
    def visitDecFunc(self, ctx: simplified_javaParser.DecFuncContext):
        funcID = ctx.ID().getText()
        funcType = ctx.funcType().getText()

        # todo verificar se id esta na lista
        self.symbolTable[funcID] = ["func", funcType]
        print(self.symbolTable)  ###################################################

        print(f"bbbbbbbbbbbbbbbbb   {self.visitParametersList(ctx.parametersList())}")

        return self.visitChildren(ctx)

    def visitParametersList(self, ctx:simplified_javaParser.ParametersListContext):
        paramList = []
        for dataType, ID in zip(ctx.dataType(), ctx.ID()):
            paramList.append((dataType.getText(), ID.getText()))

        return paramList

    def visitDecVar(self, ctx: simplified_javaParser.DecVarContext):
        variables, varType = ctx.getText().split(":")

        variables = variables.split(",")
        varType = varType[:-1]

        for variable in variables:
            #  TODO checar se ja tem o id na tabela de simbolos
            self.symbolTable[variable] = ["var", varType, None]
        print(self.symbolTable) ##################################################
        return self.visitChildren(ctx)

    # Visit a parse tree produced by simplified_javaParser#decConst.
    def visitDecConst(self, ctx: simplified_javaParser.DecConstContext):
        decConst = ctx.getText()[5:-1]
        ID, value = decConst.split("=", 1)

        #  TODO checar se ja tem o id na tabela de simbolos
        self.symbolTable[ID] = ["const", self.defineType(value), value]
        print(self.symbolTable)  ###################################################################
        return self.visitChildren(ctx)