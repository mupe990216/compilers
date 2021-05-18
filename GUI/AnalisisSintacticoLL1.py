class AnalisisSintacticoLL1:
    arregloReglas = []
    tablaLL1 = []

    def __init__(self, arregloReglas, tablaLL1):
        self.arregloReglas = arregloReglas
        self.tablaLL1 = tablaLL1

    #Convertimos los tokens en palabras que el LL(1) pueda entender
    def convertirToken(self, valor):
        if valor == 10:
            return "MAS"
        elif valor == 20:
            return "MENOS"
        elif valor == 30:
            return "MULTIPLICACION"
        elif valor == 40:
            return "DIVISION"
        elif valor == 50:
            return "PAR_I"
        elif valor == 60:
            return "PAR_D"
        elif valor == 70:
            return "NUM"
        elif valor == "$":
            return "$"
        else:
            return "ERROR"

    def analizar(self, tokens):
        #Preparamos la pila
        tokens[-1] = "$"
        pila = []
        pila.append("$")
        pila.append(self.arregloReglas[0][0])
        contador = 0
        #Hasta que la pila este vacia
        while pila != []:
            estado = pila.pop()
            #Buscamos en la tabla LL(1)
            for fila in self.tablaLL1:
                if fila[0] == estado:
                    valor = self.convertirToken(tokens[contador])
                    for indice, columna in enumerate(self.tablaLL1[0]):
                        if columna == valor:
                            #Obtenemos la accion en la celda de la tabla
                            accion = fila[indice]
                            #Casos dependiendo de la accion
                            if accion == "":
                                return False
                            elif accion == "POP":
                                contador += 1
                            elif accion == "ACEPTACION":
                                return True
                            else:
                                regla = self.arregloReglas[int(accion)]
                                regla = regla[1:-1]
                                regla = regla[::-1]
                                for i in regla:
                                    pila.append(i)
        return False
