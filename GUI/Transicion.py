class Transicion:
    def __init__(self, estado, simb1 = None, simb2 = None):
        self.__simb1 = simb1
        if simb2 != None:
            self.__simb2 = simb2
        else:
            self.__simb2 = simb1
        self.__estado = estado

    def setTransicion(self, estado, simb1, simb2 = None):
        self.__simb1 = simb1
        if simb2 != None:
            self.__simb2 = simb2
        else:
            self.__simb2 = simb1
        self.__estado = estado

    def toString(self):
        print(ord(self.__simb1))
        print(ord(self.__simb2))
        print(self.__estado)

    def getSimb1(self):
        return self.__simb1

    def getSimb2(self):
        return self.__simb2

    def getEstado(self, simb):
        #print("simb1={}, simb2={},simb={}".format(self.__simb1,self.__simb2, simb))
        if ord(self.__simb1) <= ord(simb) and ord(simb) <= ord(self.__simb2):
            return self.__estado
        else:
            return None

    def setSimb1(self, simb1):
        self.__simb1 = simb1

    def setSimb2(self, simb2):
        self.__simb2 = simb2

    def imprime_Transicion(self):
        imprime = "[Estado: "
        imprime += str(self.__estado.getIdEstado())
        imprime += "  Simb1: "
        imprime += str(self.__simb1)
        imprime += "  Simb2: "
        imprime += str(self.__simb2)
        imprime += "] "
        return imprime

    def imprime_Transicion_Prueba(self):
        imprime = "Estado: "
        imprime += str(self.__estado.imprime_Estado())
        imprime += "  Simb1: "
        imprime += str(self.__simb1)
        imprime += "  Simb2: "
        imprime += str(self.__simb2)
        return imprime
