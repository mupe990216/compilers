import time
from Estado import *
from Transicion import *
from SimbolosEspeciales import *
from copy import deepcopy
from EstadoSimbolo import *
from AnalizadorLexico import *

class AFN:
    contIdAFN = 0

    def __init__(self):
        self.idAFN = AFN.contIdAFN
        AFN.contIdAFN += 1
        self.estados = set()
        self.estadoInicial = None
        self.estadosAceptados = set()
        self.alfabeto = set()

    def crearBasico(self, s1, s2 = None):
        e1 = Estado()
        e2 = Estado()

        if s2 == None:
            t = Transicion(e2, s1)
            e1.setTransicion(t)
            e2.setEdoAceptado(True)

            self.alfabeto.add(s1)
            self.estadoInicial = e1
            self.estados.add(e1)
            self.estados.add(e2)
            self.estadosAceptados.add(e2)
        else:
            t = Transicion(e2, s1, s2)
            e1.setTransicion(t)
            e2.setEdoAceptado(True)

            for i in range(ord(s1), ord(s2) + 1):
                self.alfabeto.add(chr(i))
            self.estadoInicial = e1
            self.estados.add(e1)
            self.estados.add(e2)
            self.estadosAceptados.add(e2)

    def unir(self, afn):
        copiaAFN1 = deepcopy(self)
        copiaAFN1.idAFN = AFN.contIdAFN
        AFN.contIdAFN += 1
        copiaAFN2 = deepcopy(afn)
        e1 = Estado()
        e2 = Estado()
        t1 = Transicion(copiaAFN1.estadoInicial, SimbolosEspeciales.epsilon)
        t2 = Transicion(copiaAFN2.estadoInicial, SimbolosEspeciales.epsilon)

        e1.setTransicion(t1)
        e1.setTransicion(t2)

        for e in copiaAFN1.estadosAceptados:
            e.setTransicion(Transicion(e2, SimbolosEspeciales.epsilon))
            e.setEdoAceptado(False)

        for e in copiaAFN2.estadosAceptados:
            e.setTransicion(Transicion(e2, SimbolosEspeciales.epsilon))
            e.setEdoAceptado(False)

        copiaAFN1.estadosAceptados.clear()
        copiaAFN2.estadosAceptados.clear()

        copiaAFN1.estadoInicial = e1
        e2.setEdoAceptado(True)

        copiaAFN1.estadosAceptados.add(e2)
        copiaAFN1.estados.update(copiaAFN2.estados)
        copiaAFN1.estados.add(e1)
        copiaAFN1.estados.add(e2)
        copiaAFN1.alfabeto.update(copiaAFN2.alfabeto)
        return copiaAFN1

    def concatenar(self, afn):
        copiaAFN1 = deepcopy(self)
        copiaAFN2 = deepcopy(afn)
        copiaAFN1.idAFN = AFN.contIdAFN
        AFN.contIdAFN += 1
        for t in copiaAFN2.estadoInicial.getTransicion():
            for e in copiaAFN1.estadosAceptados:
                e.setTransicion(t)
                e.setEdoAceptado(False)

        copiaAFN2.estados.remove(copiaAFN2.estadoInicial)
        copiaAFN1.estadosAceptados = copiaAFN2.estadosAceptados
        copiaAFN1.estados.update(copiaAFN2.estados)
        copiaAFN1.alfabeto.update(copiaAFN2.alfabeto)
        return copiaAFN1

    def cerraduraPositiva(self):
        copiaAFN1 = deepcopy(self)
        copiaAFN1.idAFN = AFN.contIdAFN
        AFN.contIdAFN += 1
        eIni = Estado()
        eFin = Estado()
        eIni.setTransicion(Transicion(copiaAFN1.estadoInicial, SimbolosEspeciales.epsilon))

        for e in copiaAFN1.estadosAceptados:
            e.setTransicion(Transicion(copiaAFN1.estadoInicial, SimbolosEspeciales.epsilon))
            e.setTransicion(Transicion(eFin, SimbolosEspeciales.epsilon))
            e.setEdoAceptado(False)

        copiaAFN1.estadoInicial = eIni
        eFin.setEdoAceptado(True)
        copiaAFN1.estadosAceptados.clear()
        copiaAFN1.estadosAceptados.add(eFin)
        copiaAFN1.estados.add(eIni)
        copiaAFN1.estados.add(eFin)
        return copiaAFN1

    def cerraduraKleene(self):
        copiaAFN1 = deepcopy(self)
        copiaAFN1.idAFN = AFN.contIdAFN
        AFN.contIdAFN += 1
        eIni = Estado()
        eFin = Estado()
        eIni.setTransicion(Transicion(copiaAFN1.estadoInicial, SimbolosEspeciales.epsilon))
        eIni.setTransicion(Transicion(eFin, SimbolosEspeciales.epsilon))

        for e in copiaAFN1.estadosAceptados:
            e.setTransicion(Transicion(eFin,SimbolosEspeciales.epsilon))
            e.setTransicion(Transicion(copiaAFN1.estadoInicial, SimbolosEspeciales.epsilon))
            e.setEdoAceptado(False)

        copiaAFN1.estadoInicial = eIni
        eFin.setEdoAceptado(True)
        copiaAFN1.estadosAceptados.clear()
        copiaAFN1.estadosAceptados.add(eFin)
        copiaAFN1.estados.add(eIni)
        copiaAFN1.estados.add(eFin)
        return copiaAFN1


    def opcional(self):
        copiaAFN1 = deepcopy(self)
        copiaAFN1.idAFN = AFN.contIdAFN
        AFN.contIdAFN += 1
        eIni = Estado()
        eFin = Estado()
        eIni.setTransicion(Transicion(copiaAFN1.estadoInicial, SimbolosEspeciales.epsilon))
        eIni.setTransicion(Transicion(eFin, SimbolosEspeciales.epsilon))

        for e in copiaAFN1.estadosAceptados:
            e.setTransicion(Transicion(eFin, SimbolosEspeciales.epsilon))
            e.setEdoAceptado(False)

        copiaAFN1.estadoInicial = eIni
        eFin.setEdoAceptado(True)
        copiaAFN1.estadosAceptados.clear()
        copiaAFN1.estadosAceptados.add(eFin)
        copiaAFN1.estados.add(eIni)
        copiaAFN1.estados.add(eFin)
        return copiaAFN1

    def afnAnalizador(self, afns):
        #crear el primer estado que conecta a las otras regex
        token = 10
        analizador = AFN()
        inicio = Estado()
        analizador.estadoInicial = inicio
        analizador.estados.add(inicio)

        for afn in afns:
            copia = deepcopy(afn)
            for e in copia.estadosAceptados:
                e.setToken(token)
            token += 10
            #conectar con el inicio de cada regex
            t = Transicion(copia.estadoInicial, SimbolosEspeciales.epsilon)
            copia.estadoInicial = None
            inicio.setTransicion(t)

            analizador.alfabeto = copia.alfabeto | analizador.alfabeto
            analizador.estados = copia.estados | analizador.estados
            analizador.estadosAceptados = copia.estadosAceptados | analizador.estadosAceptados

        return analizador


    def cerraduraEpsilon(self, edos):
        R = set()
        S = []
        aux = Estado()
        edo = Estado()

        if type(edos)  is set:
            for e in edos:
                S.append(e)
            while len(S) != 0:
                aux = S.pop()
                R.add(aux)
                for t in aux.getTransicion():
                    edo = t.getEstado(SimbolosEspeciales.epsilon)
                    if edo != None:
                        if edo not in R:
                            S.append(edo)
            return R
        else:
            S.append(edos)
            while len(S) != 0:
                aux = S.pop()
                R.add(aux)
                for t in aux.getTransicion():
                    edo = t.getEstado(SimbolosEspeciales.epsilon)
                    if edo != None:
                        if edo not in R:
                            S.append(edo)
            return R


    def mover(self, edos, simbolo):
        C = set()
        aux = Estado()
        if type(edos)  is set:

            for edo in edos:
                for t in edo.getTransicion():
                    aux = t.getEstado(simbolo)
                    if aux != None:
                        C.add(aux)
            return C
        else:
            for t in edos.getTransicion():
                aux = t.getEstado(simbolo)

                if aux != None:
                    C.add(aux)
            return C

    def irA(self, edos, simbolo):
        C = set()
        C = self.cerraduraEpsilon(self.mover(edos, simbolo))
        return C

    def ConvAFNaAFD(self):
        AFD = []
        titulo = []
        estados = []
        cola = []
        estadosCreados = []
        existe = False
        nuevaColuma = []
        contador = 0

        #Agregar titulos
        titulo.append('')
        titulo.append('')
        for i in range(32, 127):
            titulo.append(chr(i))
        titulo.append('Aceptación')
        AFD.append(titulo)

        #Agregar estado de inicio
        estados.append(contador)
        contador += 1
        estados.append(self.cerraduraEpsilon(self.estadoInicial))
        for i in range(32,127):
            estados.append(-1)
        estados.append(-1)
        for estado in estados[1]:
            if estado.getEdoAceptado():
                estados[-1] = estado.getToken()
        AFD.append(estados)

        #Inicia el analisis de los estados AFD encontrados
        cola.append(estados)
        while len(cola) != 0:
            estados = cola.pop()

            #Comparamos los estados con todos los simbolos
            for i in range(32, 127):
                estadosCreados = self.irA(estados[1],chr(i))

                #Si encontrados transición
                if len(estadosCreados) != 0:
                    existe = False

                    #Verificamos que no hayamos encontrado este estado antes
                    for j in range(1,len(AFD)):
                        columna = AFD[j]
                        if len(columna[1].symmetric_difference(estadosCreados)) == 0:
                            existe = True

                    #Si no es repetido, agregarlo
                    if(existe == False):
                        nuevaColuma = []
                        nuevaColuma.append(contador)
                        contador += 1
                        nuevaColuma.append(estadosCreados)
                        for i in range(32,127):
                            nuevaColuma.append(-1)
                        nuevaColuma.append(-1)
                        for estado in nuevaColuma[1]:
                            if estado.getEdoAceptado():
                                nuevaColuma[-1] = estado.getToken()
                        AFD.append(nuevaColuma)
                        cola.append(nuevaColuma)

        #buscamos y colocamos las transiciones en la tabla
        for k in range(1,len(AFD)):
            estados = AFD[k]
            for i in range(32, 127):
                estadosCreados = self.irA(estados[1], chr(i))
                if len(estadosCreados) != 0:
                    for j in range(1, len(AFD)):
                        columna = AFD[j]
                        if len(columna[1].symmetric_difference(estadosCreados)) == 0:
                            estados[i-30] = j-1

        #Imprimimos el archivo
        archivo = open("AFD.txt","w")
        for i in AFD:
            archivo.write(str(i[0])+"\t")
            for j in i[2:]:
                archivo.write(str(j)+"\t")
            archivo.write("\n")
        return AFD
