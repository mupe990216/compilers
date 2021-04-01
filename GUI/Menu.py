import tkinter as tk
from tkinter import Menu

#Funcion de prueba con parametros
def funcion_a(palabra):
    print("Estoy presionando básico XD")
    print(palabra)

#Función de prueba
def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()

#Crear la ventana
ventana = tk.Tk()
ventana.title("Constructor de automatas") #Titulo
#Calcular el centro de pantalla
x_ventana = int(ventana.winfo_screenwidth())
x_ventana = int((x_ventana-800)/2)
y_ventana = int(ventana.winfo_screenheight())
y_ventana = int((y_ventana-500)/2)
ventana.geometry('800x500+'+str(x_ventana)+'+'+str(y_ventana))#Tamaño + centro
ventana.configure(bg='#FFFFFF') #Color de pantalla

#Crear la barra de menu
barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

#Agregamos opciones al menú
opciones_menu = Menu(barra_menu)
opciones_menu.add_command(label="Básico", command=lambda: funcion_a("ok"))
opciones_menu.add_command(label="Unir")
opciones_menu.add_command(label="Concatenar")
opciones_menu.add_command(label="Cerradura +")
opciones_menu.add_command(label="Cerradura -")
opciones_menu.add_command(label="Opcional")
opciones_menu.add_separator()
opciones_menu.add_command(label="Unión para analizador léxico")
opciones_menu.add_command(label="Convertir AFN a AFD")
opciones_menu.add_command(label="Analizar una cadena")
opciones_menu.add_command(label="Probar analizador léxico")
opciones_menu.add_separator()
opciones_menu.add_command(label="Salir", command=funcion_salir)
barra_menu.add_cascade(label="AFN'S", menu=opciones_menu)

ventana.mainloop()
