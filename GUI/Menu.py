from tkinter import *
from CreacionBasico import creacionBasico
from UnionAFN import creacionUnion
from OperacionCerradura import creacionCerradura
from ConcatenacionAFN  import creacionConcatenacion
from OperacionCerraduraMas import creacionCerraduraMas
from OperacionOpcional import creacionOpcional
from VentanaToken import crearVentanaToken
from tabulate import tabulate
from tkinter import messagebox as mBox
from AFN import *
from AnalizadorLexico import *
from EvaluadorExpresion import *
from EvaluadorExpresionPostfijo import *
from ExpresionRegular import *
from AnalizadorSintacticoGramatica import *
from LL1 import *
from AnalisisSintacticoLL1 import *
import tkinter as tk
from tkinter import simpledialog

datos = [
	["a,b,c,d,e,f,a,b,c,d,e,f,a,b,c,d,e,f,a,b,c,d,e,f","a,b","f,e","0"],
	["a,b,c,d,e,f,a,b,c,d,e,f,a,b,c,d,e,f,a,b,c,d,e,f","a,b","f,e","0"],
	["a,b,c,d,e,f,a,b,c,d,e,f,a,b,c,d,e,f,a,b,c,d,e,f","a,b","f,e","0"]
]

misAFNs = []
AFD = []

#Funcion para actualizar la caja de Texto
def imprime_Tabla():
	datos = []
	for afn in misAFNs:
		columna = []
		imprime = ""
		lista = []
		for x in afn.alfabeto:
		    lista.append(x)
		imprime = str(sorted(lista))
		columna.append(imprime)
		columna.append(afn.estadoInicial.imprime_Estado())
		imprime = ""
		for x in afn.estadosAceptados:
		    imprime += str("{}\n".format(x.imprime_Estado()))
		columna.append(imprime)
		datos.append(columna)
	etiquetaTexto = Text(marco_scrollable, width=250, height=40, bg="#CCEEFF", font=("Monospace",11))
	etiquetaTexto.grid(row=0,column=0,sticky='nsew',padx=0,pady=0)
	etiquetaTexto.insert(1.0,tabulate(
	datos,
	headers=["index","Alfabeto","Edos Inicia","Edos Acepta"],
	showindex='always',
	tablefmt='fancy_grid',
	numalign="center",
	stralign="center")
	)
	etiquetaTexto.configure(state='disable')

def crearEspecial():
	global misAFNs
	aux = AFN()
	especial = aux.afnAnalizador(misAFNs)
	misAFNs = []
	misAFNs.append(especial)
	mBox.showinfo('Especial','Especial creado con exito')

def crearAFD():
	AFN = misAFNs.pop()
	AFD = AFN.ConvAFNaAFD()
	"""Lexico = AnalisisLexico(AFD)
	Lexicos.append(Lexico)"""
	mBox.showinfo('AFD','AFD creado con exito')

def analizarCadena():
	#Obtenemos el AFD del archivo creado previamente
	direccion = simpledialog.askstring("Archivo","Ingrese la dirección del archivo a analizar", parent=ventana)
	archivo = open(direccion,'r')
	mensaje = archivo.read()
	archivo.close()
	texto = ""
	columna = []
	AFD = []
	bandera = False
	for x in mensaje:
		if x == "\t":
			if bandera:
				texto = int(texto)
			columna.append(texto)
			texto = ""
		elif x == "\n":
			AFD.append(columna)
			columna = []
			bandera = True
		else:
			texto += x
	#Preparamos el AFD
	Lexico = AnalisisLexico(AFD)
	#Ingresamos las cadenas
	cadena = simpledialog.askstring("Cadena", "Ingrese la cadena a analizar",parent=ventana)
	Lexico.analizarCadena(cadena)
	token = Lexico.getToken()
	lexema = Lexico.getLexema()
	#Imprimimos los tokens
	tabla = []
	tabla.append(token)
	tabla.append(lexema)
	crearVentanaToken(tabla)
	"""evaluador = EvaluadorExpresion(Lexicos[0])
	salida = evaluador.IniEval()
	if salida:
		resultado = evaluador.getResultado()
		mBox.showinfo('Resultado','El resultado es '+str(resultado))
	else:
		mBox.showinfo('Resultado','El evaluador de expresion marca error')"""

def calcular():
	#Obtenemos el AFD del archivo creado previamente
	archivo = open("./Calculadora.txt",'r')
	mensaje = archivo.read()
	archivo.close()
	texto = ""
	columna = []
	AFD = []
	bandera = False
	for x in mensaje:
		if x == "\t":
			if bandera:
				texto = int(texto)
			columna.append(texto)
			texto = ""
		elif x == "\n":
			AFD.append(columna)
			columna = []
			bandera = True
		else:
			texto += x
	#Preparamos el AFD
	Lexico = AnalisisLexico(AFD)
	#Ingresamos las cadenas
	cadena = simpledialog.askstring("Cadena", "Ingrese la cadena a analizar",parent=ventana)
	Lexico.analizarCadena(cadena)
	token = Lexico.getToken()
	lexema = Lexico.getLexema()
	#Realzamos el analisis de expresión y mostramos resultados
	evaluador = EvaluadorExpresion(Lexico)
	salida = evaluador.IniEval()
	if salida:
		resultado = evaluador.getResultado()
		mBox.showinfo('Resultado','El resultado es '+str(resultado))
	else:
		mBox.showinfo('Resultado','El evaluador de expresion marca error')

def postfijo():
	#Obtenemos el AFD del archivo creado previamente
	archivo = open("./Calculadora.txt",'r')
	mensaje = archivo.read()
	archivo.close()
	texto = ""
	columna = []
	AFD = []
	bandera = False
	for x in mensaje:
		if x == "\t":
			if bandera:
				texto = int(texto)
			columna.append(texto)
			texto = ""
		elif x == "\n":
			AFD.append(columna)
			columna = []
			bandera = True
		else:
			texto += x
	#Preparamos el AFD
	Lexico = AnalisisLexico(AFD)
	#Ingresamos las cadenas
	cadena = simpledialog.askstring("Cadena", "Ingrese la cadena a analizar",parent=ventana)
	Lexico.analizarCadena(cadena)
	token = Lexico.getToken()
	lexema = Lexico.getLexema()
	#Realzamos el analisis de expresión y mostramos resultados
	evaluador = EvaluadorExpresionPostfijo(Lexico)
	salida = evaluador.IniEval()
	if salida:
		resultado = evaluador.getResultado()
		mBox.showinfo('Resultado','El postfijo es '+resultado)
	else:
		mBox.showinfo('Resultado','El evaluador de expresion marca error')

def AFNCadena():
	#Obtenemos el AFD del archivo creado previamente
	archivo = open("./AFN.txt",'r')
	mensaje = archivo.read()
	archivo.close()
	texto = ""
	columna = []
	AFD = []
	bandera = False
	for x in mensaje:
		if x == "\t":
			if bandera:
				texto = int(texto)
			columna.append(texto)
			texto = ""
		elif x == "\n":
			AFD.append(columna)
			columna = []
			bandera = True
		else:
			texto += x
	#Preparamos el AFD
	Lexico = AnalisisLexico(AFD)
	#Ingresamos las cadenas
	cadena = simpledialog.askstring("Cadena", "Ingrese la cadena del AFN",parent=ventana)
	Lexico.analizarCadena(cadena)
	token = Lexico.getToken()
	lexema = Lexico.getLexema()
	#Realzamos el analisis de expresión y mostramos resultados
	evaluador = ExpresionRegular(Lexico)
	salida = evaluador.IniEval()
	if salida:
		misAFNs.append(evaluador.getResultado())
		mBox.showinfo('Resultado','El AFN fue creado con exito')
	else:
		mBox.showinfo('Resultado','Hay un error en el AFN')

def AnalizadorGramatica():
	#Obtenemos el AFD del archivo creado previamente
	archivo = open("./GramaticaGramaticas.txt",'r')
	mensaje = archivo.read()
	archivo.close()
	texto = ""
	columna = []
	AFD = []
	bandera = False
	for x in mensaje:
		if x == "\t":
			if bandera:
				texto = int(texto)
			columna.append(texto)
			texto = ""
		elif x == "\n":
			AFD.append(columna)
			columna = []
			bandera = True
		else:
			texto += x
	#Preparamos el AFD
	Lexico = AnalisisLexico(AFD)
	#Ingresamos las cadenas
	cadena = simpledialog.askstring("Cadena", "Ingrese la cadena del AFN",parent=ventana)
	Lexico.analizarCadena(cadena)
	token = Lexico.getToken()
	lexema = Lexico.getLexema()
	#Realzamos el analisis de expresión y mostramos resultados
	evaluador = AnalizadorSintacticoGramatica(Lexico)
	salida = evaluador.IniEval()
	if salida:
		arregloListas = evaluador.getResultado()
		print(arregloListas)
		#mBox.showinfo('Resultado','La gramtica es correcta')
		Vn = []
		Vt = []
		for i in range(0, len(arregloListas)):
			Vn.append(arregloListas[i][0])
			for j in arregloListas[i]:
				Vt.append(j)
		Vn = set(Vn)
		Vt = set(Vt)
		Vt = list(Vt - Vn)
		Vn = list(Vn)
		Vt.remove(None)
		LL = LL1(Vn, Vt, arregloListas)
		LL.crearTabla()
		mBox.showinfo('mensaje','La tabla LL(1) se ha creado exitosamente')
	else:
		mBox.showinfo('Error','Hay un error en la gramatica')

def analizarCadenaLL1():
	#Generamos la lista de regla y la tabla LL(1)
	direccionLL1 = simpledialog.askstring("Archivo", "Ingrese la dirección del archivo de la tabla LL(1)", parent=ventana)
	archivoLL1 = open(direccionLL1,'r')
	mensaje = archivoLL1.read()
	archivoLL1.close()
	texto = ""
	columna = []
	arregloReglas = []
	tablaLL1 = []
	bandera = True
	bandera2 = True
	for i in mensaje:
		if bandera:
			if i == "\t":
				columna.append(texto)
				texto = ""
			elif i == "\n":
				arregloReglas.append(columna)
				columna = []
			elif i == "-":
				bandera = False
			else:
				texto += i
		else:
			if bandera2:
				bandera2 = False
			else:
				if i == "\t":
					columna.append(texto)
					texto = ""
				elif i == "\n":
					tablaLL1.append(columna)
					columna = []
				else:
					texto += i
	#Obtenemos la tabla del AFD
	direccionAnalizador = simpledialog.askstring("Archivo","Ingrese la dirección del analizador léxico", parent=ventana)
	archivoAnalizador = open(direccionAnalizador, 'r')
	mensaje = archivoAnalizador.read()
	archivoAnalizador.close()
	texto = ""
	columna = []
	AFD = []
	bandera = False
	for i in mensaje:
		if i == "\t":
			if bandera:
				texto = int(texto)
			columna.append(texto)
			texto = ""
		elif i == "\n":
			AFD.append(columna)
			columna = []
			bandera = True
		else:
			texto += i
	#Obtenemos los token de la cadena a ingresar
	Lexico = AnalisisLexico(AFD)
	cadena = simpledialog.askstring("Cadena","Ingrese la cadena a analizar",parent=ventana)
	Lexico.analizarCadena(cadena)
	token = Lexico.getToken()
	#Realizamos el analisis sintactico con la tabla LL(1)
	LL1 = AnalisisSintacticoLL1(arregloReglas, tablaLL1)
	salida = LL1.analizar(token)
	if salida:
		mBox.showinfo("Correcto","La cadena es correcta")
	else:
		mBox.showinfo("Error","La cadena es incorrecta")

#Función de prueba
def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()

#Crear la ventana
ventana = Tk()
ventana.title("Constructor de automatas") #Titulo
#Calcular el centro de pantalla
x_ventana = int(ventana.winfo_screenwidth())
x_ventana = int((x_ventana-1000)/2)
y_ventana = int(ventana.winfo_screenheight())
y_ventana = int((y_ventana-500)/2)
ventana.geometry('1000x500+'+str(x_ventana)+'+'+str(y_ventana))#Tamaño + centro
ventana.configure(bg="#CCEEFF") #Color de pantalla
ventana.resizable(width=False,height=False)

#Crear la barra de menu
barra_menu = Menu(ventana)
barra_menu.config(bg="#99DDDD",font=("Monospace",13))
ventana.config(menu=barra_menu)

#Agregamos opciones al menú
opciones_menu = Menu(barra_menu)
opciones_menu.config(bg="#99DDDD",font=("Monospace",12))
opciones_menu.add_command(label="Básico", command=lambda: creacionBasico(misAFNs))
opciones_menu.add_command(label="Unir", command=lambda: creacionUnion(misAFNs))
opciones_menu.add_command(label="Concatenar", command=lambda: creacionConcatenacion(misAFNs))
opciones_menu.add_command(label="Cerradura +", command=lambda: creacionCerraduraMas(misAFNs))
opciones_menu.add_command(label="Cerradura *", command=lambda: creacionCerradura(misAFNs))
opciones_menu.add_command(label="Opcional", command=lambda: creacionOpcional(misAFNs))
opciones_menu.add_separator()
opciones_menu.add_command(label="Unión para analizador léxico", command=crearEspecial)
opciones_menu.add_command(label="Convertir AFN a AFD", command=crearAFD)
opciones_menu.add_command(label="Analizar una cadena", command=analizarCadena)
opciones_menu.add_separator()
opciones_menu.add_command(label="Salir", command=funcion_salir)
barra_menu.add_cascade(label="-> Menu Opciones <-", menu=opciones_menu)

#Opciones de analisis sintactico
opciones_analisis = Menu(barra_menu)
opciones_analisis.config(bg="#99DDDD",font=("Monospace",12))
opciones_analisis.add_command(label="Calculadora", command=calcular)
opciones_analisis.add_command(label="Postfijo", command=postfijo)
barra_menu.add_cascade(label="-> Analisis Sintáctico <-", menu=opciones_analisis)

#Opciones para crear un AFN desde una cadena
opciones_cadena = Menu(barra_menu)
opciones_cadena.config(bg="#99DDDD", font=("Monospace", 12))
opciones_cadena.add_command(label="AFN desde cadena", command=AFNCadena)
barra_menu.add_cascade(label="-> AFN desde cadena <-", menu=opciones_cadena)

#Opciones para crear una gramatica
opciones_gramatica = Menu(barra_menu)
opciones_gramatica.config(bg="#99DDDD", font=("Monospace", 12))
opciones_gramatica.add_command(label="Crear tabla LL(1) por medio de una gramatica", command=AnalizadorGramatica)
opciones_gramatica.add_command(label="Analisis sintactico", command=analizarCadenaLL1)
barra_menu.add_cascade(label="-> Gramaticas <-", menu=opciones_gramatica)

#Creacion De marco donde se pondra la caja de texto
marco=Frame(ventana)
marco.grid(row=0, column=0, sticky="nsew")
marco.config(bg="#CCEEFF")
marco_Texto=Frame(ventana)
marco_Texto.grid()

#Creacion de un lienzo sobre el que se dibujara la caja de texto
lienzo = Canvas(marco_Texto, bg="#CCEEFF",height=450,width=985)

#Creacion de scrolls para desplazar el lienzo uniformemente
scroll_y = Scrollbar(marco_Texto, orient="vertical",command=lienzo.yview)
scroll_x = Scrollbar(marco_Texto, orient="horizontal",command=lienzo.xview)
marco_scrollable = Frame(lienzo)

marco_scrollable.bind(
	"<Configure>",
	lambda e: lienzo.configure(
		scrollregion=lienzo.bbox("all")
		)
	)

#Configurar lienzo con los scroll
lienzo.create_window((0,0),window=marco_scrollable,anchor="nw")
lienzo.configure(yscrollcommand=scroll_y.set)
lienzo.configure(xscrollcommand=scroll_x.set)
lienzo.grid(row=0,column=0)
scroll_y.grid(row=0,column=1,sticky="nsew")
scroll_x.grid(row=1,column=0,sticky="nsew")

#Botonon
ver_automatas = Button(marco, text="-> Ver tabla de Autómatas <-",bg="#99DDDD",fg="black",font=("Monospace",12),command=imprime_Tabla,cursor="hand2")
ver_automatas.grid(row=0,column=0,padx=340,pady=0,sticky="w")

ventana.mainloop()
