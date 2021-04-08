import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox

def hacerOpcional(AFN, ventana):
    mBox.showinfo('Opcional','Opcional hecha con exito')
    ventana.quit()
    ventana.destroy()
    return

def creacionOpcional():
    #Crear la ventana
    ventana = tk.Tk()
    ventana.title("Operación opcional") #Titulo
    #Calcular el centro de pantalla
    x_ventana = int(ventana.winfo_screenwidth())
    x_ventana = int((x_ventana-230)/2)
    y_ventana = int(ventana.winfo_screenheight())
    y_ventana = int((y_ventana-160)/2)
    ventana.geometry('230x160+'+str(x_ventana)+'+'+str(y_ventana))#Tamaño + centro
    ventana.configure(bg='#FFFFFF') #Color de pantalla
    ventana.resizable(0,0) #No se puede editar el tamaño

    #Etiquetas
    etiquetaAplicar = ttk.Label(ventana,text="Aplicar operación ? a:")
    etiquetaAplicar.place(x=10, y=50, width=150, height=20)
    etiquetaAplicar.configure(background="#FFFFFF")

    #Listas
    AFN = tk.IntVar()
    listaAFN = ttk.Combobox(ventana, width=2, textvariable=AFN)
    listaAFN['values']=(1,2,3,4,5)
    listaAFN.place(x=170, y=45, width=50, height=30)

    #Boton
    boton = tk.Button(ventana, text="Realizar operación", command=lambda: hacerOpcional(AFN.get(),ventana))
    boton.place(x=40, y=85, width=150, height=30)

    ventana.mainloop()
