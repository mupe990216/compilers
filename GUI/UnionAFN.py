import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox

def UnirAFNs(AFN1, AFN2, ventana):
    mBox.showinfo('Unión','AFNs unidas con exito')
    ventana.quit()
    ventana.destroy()
    return

def creacionUnion():
    #Crear la ventana
    ventana = tk.Tk()
    ventana.title("Union AFNs") #Titulo
    #Calcular el centro de pantalla
    x_ventana = int(ventana.winfo_screenwidth())
    x_ventana = int((x_ventana-250)/2)
    y_ventana = int(ventana.winfo_screenheight())
    y_ventana = int((y_ventana-160)/2)
    ventana.geometry('250x160+'+str(x_ventana)+'+'+str(y_ventana))#Tamaño + centro
    ventana.configure(bg='#FFFFFF') #Color de pantalla
    ventana.resizable(0,0) #No se puede editar el tamaño

    #Etiquetas
    etiquetaUnir = ttk.Label(ventana,text="Unir")
    etiquetaUnir.place(x=10, y=50, width=50, height=20)
    etiquetaUnir.configure(background="#FFFFFF")
    etiquetaCon = ttk.Label(ventana,text="Con")
    etiquetaCon.place(x=130, y=50, width=50, height=20)
    etiquetaCon.configure(background="#FFFFFF")

    #Listas
    AFN1 = tk.IntVar()
    listaAFN1 = ttk.Combobox(ventana, width=2, textvariable=AFN1)
    listaAFN1['values']=(1,2,3,4,5) #Valores de ejemplo
    listaAFN1.place(x=70, y=45, width=50, height=30)
    AFN2 = tk.IntVar()
    listaAFN2 = ttk.Combobox(ventana, width=2, textvariable=AFN2)
    listaAFN2['values']=(1,2,3,4,5) #Valores de ejemplo
    listaAFN2.place(x=190, y=45, width=50, height=30)

    #Boton
    boton = tk.Button(ventana, text="Unir AFNs", command=lambda: UnirAFNs(AFN1.get(),AFN2.get(),ventana))
    boton.place(x=75, y=85, width=100, height=30)

    ventana.mainloop()
