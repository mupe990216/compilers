class EvaluadorExpresionPostfijo:
    analizadores = []
    resultado = ""

    def __init__(self, AnalizadorLex):
        self.analizadores = []
        self.analizadores.append(AnalizadorLex)

    def IniEval(self):
        v = ""
        token = 0
        sino, v = self.E(v)
        if sino:
            token = self.analizadores[0].yylex()
            if token == "Fin":
                self.resultado = v
                return True
        return False

    def E(self, v):
        sino, v = self.T(v)
        if sino:
            sino, v = self.Ep(v)
            if sino:
                return True, v
        return False, v

    def Ep(self, v):
        token = 0
        v2 = ""
        aux = ""
        token = self.analizadores[0].yylex()
        if token == 10 or token == 20:
            sino, v2 = self.T(v2)
            if sino:
                if token == 10:
                    aux = "+"
                else:
                    aux = "-"
                v = v + " " + v2 + " " + aux
                sino, v = self.Ep(v)
                if sino:
                    return True, v
            return False, v
        self.analizadores[0].undoToken()
        return True, v

    def T(self, v):
        sino, v = self.F(v)
        if sino:
            sino, v = self.Tp(v)
            if sino:
                return True, v
        return False, v

    def Tp(self, v):
        token = 0
        v2 = ""
        aux = ""
        token = self.analizadores[0].yylex()
        if token == 30 or token == 40:
            sino, v2 = self.F(v2)
            if sino:
                if token == 30:
                    aux = "*"
                else:
                    aux = "/"
                v = v + " " + v2 + " " + aux
                sino, v = self.Tp(v)
                if sino:
                    return True, v
            return False, v
        self.analizadores[0].undoToken()
        return True, v

    def F(self, v):
        token = 0
        token = self.analizadores[0].yylex()
        if token == 50:
            sino, v = self.E(v)
            if sino:
                token = self.analizadores[0].yylex()
                if token == 60:
                    return True, v
            return False, v
        elif token == 70:
            v = str(self.analizadores[0].miLexema())
            return True, v
        return False, v

    def getResultado(self):
        return self.resultado
