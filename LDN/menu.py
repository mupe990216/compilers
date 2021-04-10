#crear AFN basico
#unir dos AFN's
#concatenar dos AFN's
#cerradura +
#cerradura *
#opcional ?
#unir AFN's para contruir analizador lexico
#convertir AFN a AFD
#analizar lexicamente una cadena
#fin

import sys
from SimbolosEspeciales import *
from AFN import *

def menu():
    automatas = []
    while True:
        print("programa de AFN's")
        print("1\tCrear AFN basico")
        print("2\tUnir dos AFN's")
        print("3\tConcatenar dos AFN's")
        print("4\tCerradura +")
        print("5\tCerradura *")
        print("6\tOpcional ?")
        print("7\tUnir AFN's para construcir analizador lexico")
        print("8\tConvertir AFN a AFD")
        print("9\tAnalizar lexicamente una cadena")
        print("10\tFin")
        print("# de afn = {}".format(len(automatas)))
        opcion = int(input("Introduzca su opcion:"))
        
        if opcion == 1:
            print("afn basico")
            #Generar AFN con un rango pedido
            limInf = input("Ingresa el limite inferior:")
            limSup = input("Ingresa el limite superior:")
            try:
                afn = AFN()
                afn.crearBasico(limInf, limSup)
                automatas.append(afn)
                print("afn creado exitosamente\n")
                print("ID de AFN = {}".format(afn.idAFN))
            except Exception as e:
                print("Ocurrio un error en crearBasico():{}\n".format(e))
            
        elif opcion == 2:
            print("Unir dos afn's")
            #Une los dos ultimos AFN  

            if len(automatas) == 0:
                print("No existen los suficientes afn para llevar acabo esta opcion")
            else:
                primera = int(input("Ingresa id de primer afn:"))
                segunda = int(input("Ingresa id de segundo afn:"))
                tmp = automatas[primera].unir(automatas[segunda])
                automatas.append(tmp)
                print("afn {} y afn {} unidos exitosamente y creado un afn {} nuevo con el resultado".format(primera,segunda, len(automatas)))

        elif opcion == 3:
            print("Concatenar dos afn's")
            # Concatena con dos afn indicados
            if len(automatas) == 0:
                print("No existen los suficientes afn para llevar acabo esta opcion")
            else:
                primera = int(input("Ingresa la primera posicion:"))
                segunda = int(input("Ingresa la segunda posicion:"))

                tmp = automatas[primera].concatenar(automatas[segunda])
                automatas.append(tmp)
                print("afn {} y {} concatenados y creado un afn {} con el resultado".format(primera,segunda,len(automatas)))      
        elif opcion == 4:
            print("Cerradura +")
            # crea una cerradura positiva de cierto afn
            if len(automatas) == 0:
                print("No existen los suficientes AFN para llevar acabo esta opcion")
            else:
                primera = int(input("Ingresa posicion del afn:"))
                tmp = automatas[primera].cerraduraPositiva()
                automatas.append(tmp)
                print("Afn de cerradura positiva creado y agreado a la collecion")
            
        elif opcion == 5:
            print("Cerradura *")
            #crea una cerradura positiva de cierto afn
            if len(automatas) == 0:
                print("No existen los suficientes AFN para llevar acabo esta opcion")
            else:
                primera = int(input("Ingresa posicion del afn:"))
                tmp = automatas[primera].cerraduraKleene()
                automatas.append(tmp)
                print("Afn de cerradura Kleene creado y agreado a la collecion")
            
        elif opcion == 6:
            print("Opcional ?")
            #crea una opcional de cierto afn
            if len(automatas) == 0:
                print("No existen los suficientes AFN para llevar acabo esta opcion")
            else:
                primera = int(input("Ingresa posicion del afn:"))
                tmp = automatas[primera].opcional()
                automatas.append(tmp)
                print("Afn de cerradura Kleene creado y agreado a la collecion")
            
        elif opcion == 7:
            print("Unir AFN's para un analizador lexico, automatas en total: ", len(automatas))
            afns = set()
            while True:
                res = input("Ingresa ID de automata o x para contruirlo:")
                if res != 'x':
                    afns.add(automatas[int(res)-1])
                else:
                    analizador = AFN()
                    automatas.append(analizador.afn2Analizador(afns))
                    break     
        elif opcion == 8:
            print("AFN -> AFD")
        elif opcion == 9:
            print("Analizar cadena")
        elif opcion == 10:
            print("Adios")
            sys.exit(0)
        else:
            print("Opcion invalida")

menu()
