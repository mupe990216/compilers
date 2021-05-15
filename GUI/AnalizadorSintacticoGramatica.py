from AFN import *

class AnalizadorSintacticoGramatica:
    analizadores = []
    resultado = []

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
        sino, v = self.LadoIzq(v)
        if sino:
            token = self.analizadores[0].yylex()
            if token == 50:
                token = self.analizadores[0].yylex()
            if token == 30:
                sino, v = self.LadosDerechos(v)
                if sino:
                    return True, v
        return False, v

    def LadoIzq(self, v):
        token = self.analizadores[0].yylex()
        if token == 50:
            token = self.analizadores[0].yylex()
        if token == 10:
            return True, v
        return False, v

    def LadosDerechos(self, v):
        sino,v = self.LadoDerecho(v)
        if sino:
            sino, v = self.LadosDerechosp(v)
            if sino:
                return True, v
        return False, v

    def LadosDerechosp(self, v):
        token = self.analizadores[0].yylex()
        if token == 50:
            token = self.analizadores[0].yylex()
        if token == 40:
            sino, v = self.LadoDerecho(v)
            if sino:
                sino, v = self.LadosDerechosp(v)
                if sino:
                    return True, v
            return False, v
        self.analizadores[0].undoToken()
        return True, v

    def LadoDerecho(self, v):
        token = self.analizadores[0].yylex()
        if token == 50:
            token = self.analizadores[0].yylex()
        if token == 10:
            sino, v = self.LadoDerechop(v)
            if sino:
                return True, v
        return False, v

    def LadoDerechop(self, v):
        token = self.analizadores[0].yylex()
        if token == 50:
            token = self.analizadores[0].yylex()
        if token == 10:
            sino, v = self.LadoDerechop(v)
            if sino:
                return True, v
        self.analizadores[0].undoToken()
        return True, v

    def getResultado(self):
        return self.resultado
