from gen.simplified_javaVisitor import simplified_javaVisitor
from gen.simplified_javaParser import simplified_javaParser

class analizadorSemantico(simplified_javaVisitor):
    funcTable = {}

    def __init__(self):
        self.funcTable = {'main': {"funcType": 'void', "funcParameters": {}, "funcDecs": []}}

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
    def funcIdInUse(self, funcId):
        if funcId in self.funcTable:
            return True
        else:
            return False

    def visitDecFunc(self, ctx: simplified_javaParser.DecFuncContext):
        funcID = ctx.ID().getText()
        funcType = ctx.funcType().getText()
        funcParameters = self.visitParametersList(ctx.parametersList())

        if ctx.varField():
            funcDecs = self.visitVarField(ctx.varField(), funcID)
        else:
            funcDecs = []

        if self.funcIdInUse(funcID):
            raise Exception(f"Function ID {funcID} already in use.")
        else:
            self.funcTable[funcID] = {"funcType": funcType, "funcParameters": funcParameters, "funcDecs": funcDecs}

    def visitFuncMain(self, ctx:simplified_javaParser.FuncMainContext):
        funcID = 'main'
        funcType = 'void'
        funcParameters = {}

        if ctx.varField():
            funcDecs = self.visitVarField(ctx.varField(), funcID)
        else:
            funcDecs = []

        self.funcTable[funcID] = {"funcType": funcType, "funcParameters": funcParameters, "funcDecs": funcDecs}

    def visitParametersList(self, ctx):
        paramList = {}

        for dataType, ID in zip(ctx.dataType(), ctx.ID()):
            if ID.getText() in paramList:
                raise Exception(f"Parameter ID {ID.getText()} already in use.")

            paramList[ID.getText()] = dataType.getText()

        return paramList

    def visitVarField(self, ctx, funcID):
        decList = [] # lista que vai guardar as informações das variaveis e constantes em outras listas

        for i in ctx.decVarConst():
            if i.decVar():
                for var in self.visitDecVar(i):
                    IDs = [x[0] for x in decList]

                    if var[0] in IDs:
                        raise Exception(f"Variable ID {var[0]} already in use in this scope.")

                    decList.append(var)
            else:
                const = self.visitDecConst(i)

                if const[0] in [x[0] for x in decList]:
                    raise Exception(f"Constant ID {self.visitDecConst(i)[0]} already in use.")

                decList.append(self.visitDecConst(i))

        return decList

    def visitDecVar(self, ctx: simplified_javaParser.DecVarContext):
        vars = []
        variables, varType = ctx.getText().split(":")

        variables = variables.split(",")
        varType = varType[:-1]

        for variable in variables:
            vars.append([variable, "var", varType, None])

        return vars

    # Visit a parse tree produced by simplified_javaParser#decConst.
    def visitDecConst(self, ctx: simplified_javaParser.DecConstContext):
        decConst = ctx.getText()[5:-1]
        ID, value = decConst.split("=", 1)

        return [ID, "const", self.defineType(value), value]

    def show(self):
        print(self.funcTable)
