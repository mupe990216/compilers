import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from AFN import *

#Pequeño mensaje del boton y destrucción de la ventana
def crearAFN(inf, sup, ventana, misAFNs):
    automata = AFN()
    if sup.get() == "":
        automata.crearBasico(inf.get())
    else:
        automata.crearBasico(inf.get(), sup.get())
    misAFNs.append(automata)
    mBox.showinfo('AFN creado', 'AFN creado con exito')
    ventana.quit()
    ventana.destroy()
    return

def creacionBasico(misAFNs):
    #Crear la ventana
    ventana = tk.Tk()
    ventana.title("Creación de AFN básico") #Titulo
    #Calcular el centro de pantalla
    x_ventana = int(ventana.winfo_screenwidth())
    x_ventana = int((x_ventana-230)/2)
    y_ventana = int(ventana.winfo_screenheight())
    y_ventana = int((y_ventana-160)/2)
    ventana.geometry('230x160+'+str(x_ventana)+'+'+str(y_ventana))#Tamaño + centro
    ventana.configure(bg='#FFFFFF') #Color de pantalla
    ventana.resizable(0,0) #No se puede editar el tamaño

    #Agregar etiquetas
    etiquetaCaracterInf = ttk.Label(ventana, text="Caracter Inf")
    etiquetaCaracterInf.place(x=10, y=15, width=100, height=20)
    etiquetaCaracterInf.configure(background='#FFFFFF')
    etiquetaCaracterSup = ttk.Label(ventana, text="Caracter Sup")
    etiquetaCaracterSup.place(x=10, y=50, width=100, height=20)
    etiquetaCaracterSup.configure(background='#FFFFFF')

    #Agregar cuadros de texto
    inf = tk.StringVar()
    CuadroInf = tk.Entry(ventana, width="1", textvariable=inf)
    CuadroInf.place(x=120, y=10, width=100, height=30)
    sup = tk.StringVar()
    CuadroSup = tk.Entry(ventana, width="1", textvariable=sup)
    CuadroSup.place(x=120, y=45, width=100, height=30)

    #Agregar boton
    boton = ttk.Button(ventana, text="Crear AFN", command=lambda: crearAFN(CuadroInf, CuadroSup, ventana, misAFNs))
    boton.place(x=10, y=120, width=210, height=30)

    ventana.mainloop()
