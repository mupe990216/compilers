from AFN import *

class AnalizadorSintacticoGramatica:
    analizadores = []
    resultado = []
    SIMBOLO = ""

    def __init__(self, AnalizadorLex):
        self.analizadores = []
        self.analizadores.append(AnalizadorLex)

    def IniEval(self):
        v = []
        token = 0
        sino, v = self.G(v)
        if sino:
            token = self.analizadores[0].yylex()
            if token == 50:
                token = self.analizadores[0].yylex()
            if token == "Fin":
                self.resultado = v
                return True
        return False

    def G(self, v):
        sino, v = self.ListaReglas(v)
        if sino:
            return True, v
        return False, v

    def ListaReglas(self, v):
        sino, v = self.Regla(v)
        if sino:
            token = self.analizadores[0].yylex()
            if token == 50:
                token = self.analizadores[0].yylex()
            if token == 20:
                sino, v = self.ListaReglasp(v)
                if sino:
                    return True, v
        return False, v

    def ListaReglasp(self, v):
        token = self.analizadores[0].yylex()
        if token == 50:
            token = self.analizadores[0].yylex()
        if token == "Fin":
            self.analizadores[0].undoToken()
            return True, v
        self.analizadores[0].undoToken()
        self.analizadores.append(self.analizadores[0])
        sino, v = self.Regla(v)
        if sino:
            token = self.analizadores[0].yylex()
            if token == 50:
                token = self.analizadores[0].yylex()
            if token == 20:
                sino, v = self.ListaReglasp(v)
                if sino:
                    return True, v
            return False, v
        self.analizadores[0]=self.analizadores[1]
        return True, v

    def Regla(self, v):
        sino = self.LadoIzq()
        if sino:
            token = self.analizadores[0].yylex()
            if token == 50:
                token = self.analizadores[0].yylex()
            if token == 30:
                sino, v = self.LadosDerechos(v)
                if sino:
                    return True, v
        return False, v

    def LadoIzq(self):
        token = self.analizadores[0].yylex()
        if token == 50:
            token = self.analizadores[0].yylex()
        if token == 10:
            self.SIMBOLO = self.analizadores[0].miLexema()
            return True
        return False

    def LadosDerechos(self, v):
        sino, N = self.LadoDerecho()
        if sino:
            v.append(N)
            sino, v = self.LadosDerechosp(v)
            if sino:
                return True, v
        return False, v

    def LadosDerechosp(self, v):
        token = self.analizadores[0].yylex()
        if token == 50:
            token = self.analizadores[0].yylex()
        if token == 40:
            sino, N = self.LadoDerecho()
            if sino:
                v.append(N)
                sino, v = self.LadosDerechosp(v)
                if sino:
                    return True, v
            return False, v
        self.analizadores[0].undoToken()
        return True, v

    def LadoDerecho(self):
        N = []
        N.append(self.SIMBOLO)
        token = self.analizadores[0].yylex()
        if token == 50:
            token = self.analizadores[0].yylex()
        if token == 10:
            N.append(self.analizadores[0].miLexema())
            sino, N = self.LadoDerechop(N)
            if sino:
                return True, N
        return False, N

    def LadoDerechop(self, N):
        token = self.analizadores[0].yylex()
        if token == 50:
            token = self.analizadores[0].yylex()
        if token == 10:
            N.append(self.analizadores[0].miLexema())
            sino, N = self.LadoDerechop(N)
            if sino:
                return True, N
        self.analizadores[0].undoToken()
        N.append(None)
        return True, N

    def getResultado(self):
        return self.resultado
