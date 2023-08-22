from gen.simplified_javaVisitor import simplified_javaVisitor
from gen.simplified_javaParser import simplified_javaParser

class analizadorSemantico(simplified_javaVisitor):
    funcTable = {}

    def __init__(self):
        self.funcTable = {'main': None}

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
        funcParameters = self.visitParametersList(ctx.parametersList())

        try:
            funcDecs = self.visitVarField(ctx.varField())
        except:
            funcDecs = []

        # todo verificar se id esta na lista
        self.funcTable[funcID] = {"funcType": funcType, "funcParameters": funcParameters, "funcDecs": funcDecs}

    def visitFuncMain(self, ctx:simplified_javaParser.FuncMainContext):
        funcID = 'main'
        funcType = 'void'
        funcParameters = {}

        try:
            funcDecs = self.visitVarField(ctx.varField())
        except:
            funcDecs = []

        # todo verificar se id esta na lista
        self.funcTable[funcID] = {"funcType": funcType, "funcParameters": funcParameters, "funcDecs": funcDecs}

    def visitParametersList(self, ctx):
        paramList = {}

        for dataType, ID in zip(ctx.dataType(), ctx.ID()):
            paramList[ID.getText()] = dataType.getText()

        return paramList

    def visitVarField(self, ctx):
        decList = []

        for i in ctx.decVarConst():
            try:
                for var in self.visitDecVar(i):
                    decList.append(var)
            except:
                decList.append(self.visitDecConst(i))

        return decList

    def visitDecVar(self, ctx: simplified_javaParser.DecVarContext):
        vars = []
        variables, varType = ctx.getText().split(":")

        variables = variables.split(",")
        varType = varType[:-1]

        for variable in variables:
            #  TODO checar se ja tem o id na tabela de simbolos
            vars.append([variable, "var", varType, None])

        return vars

    # Visit a parse tree produced by simplified_javaParser#decConst.
    def visitDecConst(self, ctx: simplified_javaParser.DecConstContext):
        decConst = ctx.getText()[5:-1]
        ID, value = decConst.split("=", 1)

        #  TODO checar se ja tem o id na tabela de simbolos
        return [ID, "const", self.defineType(value), value]

    def show(self):
        print(self.funcTable)
