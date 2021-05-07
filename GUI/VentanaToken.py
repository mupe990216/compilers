from tkinter import *

def crearVentanaToken(tabla):
	ventana = Tk()

	ventana.title("Tokens") #Titulo
	ventana.resizable(width=False,height=False)

	token = tabla[0]
	lexema = tabla[1]
	height = 2
	width = len(token)
	for i in range(height):
		for j in range(width):
			b = Label(ventana, text=str(tabla[i][j]))
			b.grid(row=i,column=j)
	ventana.mainloop()
