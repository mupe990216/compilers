from tkinter import *
from CreacionBasico import creacionBasico
from UnionAFN import creacionUnion
from OperacionCerradura import creacionCerradura
from ConcatenacionAFN  import creacionConcatenacion
from OperacionCerraduraMas import creacionCerraduraMas
from OperacionOpcional import creacionOpcional
from tabulate import tabulate

datos = [
	["a,b,c,d,e,f,a,b,c,d,e,f,a,b,c,d,e,f,a,b,c,d,e,f","a,b","f,e","0"],
	["a,b,c,d,e,f,a,b,c,d,e,f,a,b,c,d,e,f,a,b,c,d,e,f","a,b","f,e","0"],
	["a,b,c,d,e,f,a,b,c,d,e,f,a,b,c,d,e,f,a,b,c,d,e,f","a,b","f,e","0"]
]

#Funcion para actualizar la caja de Texto
def imprime_Tabla():
	etiquetaTexto = Text(marco_scrollable, width=250, height=40, bg="#CCEEFF", font=("Monospace",11))
	etiquetaTexto.grid(row=0,column=0,sticky='nsew',padx=0,pady=0)
	etiquetaTexto.insert(1.0,tabulate(
	datos, 
	headers=["index","Alfabeto","Edos Inicia","Edos Acepta","Token"], 
	showindex='always',
	tablefmt='fancy_grid',
	numalign="center",
	stralign="center")
	)
	etiquetaTexto.configure(state='disable')	


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
x_ventana = int((x_ventana-800)/2)
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
opciones_menu.add_command(label="Básico", command=creacionBasico)
opciones_menu.add_command(label="Unir", command=creacionUnion )
opciones_menu.add_command(label="Concatenar", command=creacionConcatenacion)
opciones_menu.add_command(label="Cerradura +", command=creacionCerraduraMas)
opciones_menu.add_command(label="Cerradura *", command=creacionCerradura)
opciones_menu.add_command(label="Opcional", command=creacionOpcional)
opciones_menu.add_separator()
opciones_menu.add_command(label="Unión para analizador léxico")
opciones_menu.add_command(label="Convertir AFN a AFD")
opciones_menu.add_command(label="Analizar una cadena")
opciones_menu.add_command(label="Probar analizador léxico")
opciones_menu.add_separator()
opciones_menu.add_command(label="Salir", command=funcion_salir)
barra_menu.add_cascade(label="-> Menu Opciones <-", menu=opciones_menu)

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
