from AFN import *

class ExpresionRegular:
    analizadores = []
    resultado = AFN()

    def __init__(self, AnalizadorLex):
        self.analizadores = []
        self.analizadores.append(AnalizadorLex)

    def IniEval(self):
        v = AFN()
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
        v2 = AFN()
        token = self.analizadores[0].yylex()
        if token == 10:
            sino, v2 = self.T(v2)
            if sino:
                v = v.unir(v2)
                sino, v = self.Ep(v)
                if sino:
                    return True, v
            return False, v
        self.analizadores[0].undoToken()
        return True, v

    def T(self, v):
        sino, v = self.C(v)
        if sino:
            sino, v = self.Tp(v)
            if sino:
                return True, v
        return False, v

    def Tp(self, v):
        v2 = AFN()
        token = self.analizadores[0].yylex()
        if token == 20:
            sino, v2 = self.C(v2)
            if sino:
                v = v.concatenar(v2)
                sino, v = self.Tp(v)
                if sino:
                    return True, v
            return False, v
        self.analizadores[0].undoToken()
        return True, v

    def C(self, v):
        sino, v = self.F(v)
        if sino:
            sino, v = self.Cp(v)
            if sino:
                return True, v
        return False, v

    def Cp(self, v):
        token = self.analizadores[0].yylex()
        if token == 30:
            v = v.cerraduraPositiva()
            sino, v = self.Cp(v)
            if sino:
                return True, v
            return False, v
        elif token == 40:
            v = v.cerraduraKleene()
            sino, v = self.Cp()
            if sino:
                return True, v
            return False, v
        elif token == 50:
            v = v.opcional()
            sino, v = self.Cp(v)
            if sino:
                return True, v
            return False, v
        else:
            self.analizadores[0].undoToken()
            return True, v

    def F(self, v):
        aux1 = ""
        aux2 = ""
        token = self.analizadores[0].yylex()
        if token == 60:
            sino, v = self.E(v)
            if sino:
                token = self.analizadores[0].yylex()
                if token == 70:
                    return True, v
            return False, v
        elif token == 80:
            token = self.analizadores[0].yylex()
            if token == 110:
                aux1 = self.analizadores[0].miLexema()
                if aux1[0] == "\\":
                    aux1 = aux1[-1]
                token = self.analizadores[0].yylex()
                if token == 100:
                    token = self.analizadores[0].yylex()
                    if token == 110:
                        aux2 = self.analizadores[0].miLexema()
                        if aux2[0] == "\\":
                            aux2 = aux1[-1]
                        token = self.analizadores[0].yylex()
                        if token == 90:
                            v.crearBasico(aux1, aux2)
                            return True, v
            return False, v
        elif token == 110:
            aux1 = self.analizadores[0].miLexema()
            if aux1[0] == "\\":
                aux1 = aux1[-1]
            v.crearBasico(aux1)
            return True, v
        return False, v

    def getResultado(self):
        return self.resultado
