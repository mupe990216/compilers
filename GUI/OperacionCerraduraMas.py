import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from AFN import *

def hacerCerraduraMas(AFN, ventana, misAFNs):
    automata = misAFNs[int(AFN.get())]
    automataNuevo = automata.cerraduraPositiva()
    misAFNs.remove(automata)
    misAFNs.append(automataNuevo)
    mBox.showinfo('Cerradura +','Cerradura hecha con exito')
    ventana.quit()
    ventana.destroy()
    return

def creacionCerraduraMas(misAFNs):
    #Crear la ventana
    ventana = tk.Tk()
    ventana.title("Operación cerradura +") #Titulo
    #Calcular el centro de pantalla
    x_ventana = int(ventana.winfo_screenwidth())
    x_ventana = int((x_ventana-230)/2)
    y_ventana = int(ventana.winfo_screenheight())
    y_ventana = int((y_ventana-160)/2)
    ventana.geometry('230x160+'+str(x_ventana)+'+'+str(y_ventana))#Tamaño + centro
    ventana.configure(bg='#FFFFFF') #Color de pantalla
    ventana.resizable(0,0) #No se puede editar el tamaño

    #Etiquetas
    etiquetaAplicar = ttk.Label(ventana,text="Aplicar Operación + a:")
    etiquetaAplicar.place(x=10, y=50, width=150, height=20)
    etiquetaAplicar.configure(background="#FFFFFF")

    lista = []
    for i in range(0, len(misAFNs)):
        lista.append(i)
    lista = tuple(lista)

    #Listas
    AFN = tk.IntVar()
    listaAFN = ttk.Combobox(ventana, width=2, textvariable=AFN)
    listaAFN['values']=lista
    listaAFN.place(x=170, y=45, width=50, height=30)

    #Boton
    boton = tk.Button(ventana, text="Realizar operación", command=lambda: hacerCerraduraMas(listaAFN,ventana, misAFNs))
    boton.place(x=40, y=85, width=150, height=30)

    ventana.mainloop()
