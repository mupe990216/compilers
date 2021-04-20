class EvaluadorExpresion:
    analizadores = []
    resultado = 0

    def __init__(self, AnalizadorLex):
        self.analizadores = []
        self.analizadores.append(AnalizadorLex)

    def IniEval(self):
        v = 0
        token = 0
        if self.E(v):
            token = self.analizadores[0].yylex()
            if token == "Fin":
                self.resultado = v
                return True

        return False

    def E(self, v):
        if self.T(v):
            if self.Ep(v):
                return True
        return False

    def Ep(self, v):
        token = 0
        v2 = 0.0
        aux = 0.0
        token = self.analizadores[0].yylex()
        if token == 10 or token == 20:
            if self.T(v2):
                if token == 10:
                    aux = v2
                else:
                    aux = -v2
                v = v + aux
                if self.Ep(v):
                    return True
            return False
        self.analizadores[0].undoToken()
        return True

    def T(self, v):
        if self.F(v):
            if self.Tp(v):
                return True
        return False

    def Tp(self, v):
        token = 0
        v2 = 0.0
        aux = 0.0
        token = self.analizadores[0].yylex()
        if token == 30 or token == 40:
            if self.F(v2):
                if token == 30:
                    aux = v2
                else:
                    aux = 1/v2
                v = v * aux
                if self.Tp(v):
                    return True
            return False
        self.analizadores[0].undoToken()
        return True

    def F(self, v):
        token = 0
        token = self.analizadores[0].yylex()
        if token == 50:
            if self.E(v):
                token = self.analizadores[0].yylex()
                if token == 60:
                    return True
            return False
        elif token == 70:
            v = float(self.analizadores[0].miLexema())
            return True
        return False

    def getResultado(self):
        return self.resultado
