from gen.simplified_javaVisitor import simplified_javaVisitor
from gen.simplified_javaParser import simplified_javaParser

class analizadorSemantico(simplified_javaVisitor):
    funcTable = {}

    def __init__(self):
        self.funcTable = {'main': {"funcType": 'void', "funcParameters": {}, "funcDecs": []}, 'print': {"funcType": 'void', "funcParameters": {"txt": 'str'}, "funcDecs": []}, 'scanf': {"funcType": 'void', "funcParameters": {"input": 'int'}, "funcDecs": []}}

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

        for i in ctx.cmmd():
            self.visitCmmd(i, funcID)

    def visitFuncMain(self, ctx:simplified_javaParser.FuncMainContext):
        funcID = 'main' # Se uma função main já foi definida, dará erro de sintaxe
        funcType = 'void'
        funcParameters = {}

        if ctx.varField():
            funcDecs = self.visitVarField(ctx.varField(), funcID)
        else:
            funcDecs = []

        self.funcTable[funcID] = {"funcType": funcType, "funcParameters": funcParameters, "funcDecs": funcDecs}

        for i in ctx.cmmd():
            self.visitCmmd(i, funcID)


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

    def visitDecConst(self, ctx: simplified_javaParser.DecConstContext):
        decConst = ctx.getText()[5:-1]
        ID, value = decConst.split("=", 1)

        return [ID, "const", self.defineType(value), value]

    def visitCmmd(self, ctx:simplified_javaParser.CmmdContext, scopeId):
        if ctx.inst():
            self.visitInst(ctx.inst(), scopeId)

    def visitInst(self, ctx:simplified_javaParser.InstContext, scopeId):
        instId = str(ctx.ID())
        funcIds = list(self.funcTable.keys())

        # verifica se a função chamada existe
        if instId not in funcIds:
            raise Exception(f"Function ID {instId} not defined.")

        # pega a lista de parametros da função chamada
        funcParams = self.funcTable[instId]["funcParameters"]

        if ctx.instParamList():
            # verifica se a quantidade de parametros passados é igual a quantidade de parametros da função chamada
            if len(ctx.instParamList().instParam()) != len(funcParams):
                raise Exception(f"Number of parameters passed to function {instId} is different from the number of parameters defined.")

            # verifica se ps parametros são do mesmo tipo definido
            for instType, decType in zip(self.visitInstParamList(ctx.instParamList(), scopeId), funcParams.values()):
                if instType != decType:
                    raise Exception(f"Parameter type passed to function {instId} is different from the parameter type defined.")

        else: # se não tiver parametros passados
            # verifica se a quantidade de parametros da função chamada é igual a 0
            if len(funcParams) != 0:
                raise Exception(f"Number of parameters passed to function {instId} is different from the number of parameters defined.")

    def visitInstParamList(self, ctx:simplified_javaParser.InstParamListContext, funcID):
        paramList = []

        for i in ctx.instParam():
            paramList.append(self.visitInstParam(i, funcID))

        # retorna uma lista com o tipo de cada parametro passado
        return paramList

    def visitInstParam(self, ctx:simplified_javaParser.InstParamContext, funcID):
        if ctx.ID():
            # pega a lista de variaveis e constantes daquele escopo
            varConsType = self.funcTable[funcID]["funcDecs"]

            # verifica se a variavel ou constante existe
            if ctx.ID().getText() not in [x[0] for x in varConsType]:
                raise Exception(f"Variable or Constant {ctx.ID().getText()} not defined in this scope.")

            # retorna o tipo da variavel ou constante
            return varConsType[[x[0] for x in varConsType].index(ctx.ID().getText())][2]

        if ctx.value():
            return self.defineType(ctx.value().getText())

    def show(self):
        return self.funcTable
