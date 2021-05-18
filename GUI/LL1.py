class LL1:
	Vn = []
	Vt = []
	arregloReglas = []

	def __init__(self, Vn, Vt, arregloReglas):
		self.Vn = Vn
		self.Vt = Vt
		self.arregloReglas = arregloReglas

	def first(self, lista):
		listaFirst = set([])
		listaFirst1 = set([])
		#Si el inicio de nuestra lista es un terminal, devolverlo como resultado
		if lista[0] in set(self.Vt):
			listaFirst.add(lista[0])
			return listaFirst
		elif lista[0] in set(self.Vn):
			#Si el inicio de la lista es un no terminal, calculamos su first
			for reglaNT in self.arregloReglas:
				if reglaNT[0] == lista[0]:
					listaFirst1 = self.first(reglaNT[1:])
					listaFirst = listaFirst | listaFirst1
			#Si el first tienen un epsilon
			if "EPSILON" in listaFirst:
				#Si es la cadena final, dejamos el epsilon
				if len(lista) == 1:
					return listaFirst
				#Si no, quitamos el epsilon y calculamos first del siguiente elemento
				listaFirst.discard("EPSILON")
				listaFirst1 = self.first(lista[1:])
				listaFirst = listaFirst | listaFirst1
				return listaFirst
			return listaFirst

	def follow(self, simbolo):
		listaFollow = set([])
		listaFollow1 = set([])
		listaFirst = []
		#Si nuestro simbolo es el inicial agregamos $
		if simbolo == self.arregloReglas[0][0]:
			listaFollow.add('$')
		for i in self.arregloReglas:
			si = False
			listaFirst = []
			#Buscamos si nuestro simbolo aparece en algun lado derecho
			for j in i[1:]:
				if si:
					listaFirst.append(j)
				if j == simbolo:
					si = True
			if si:
				listaFirst.remove(None)
				#Si hay una cadena despues de nuestro simbolo, buscamos su first
				if len(listaFirst) != 0:
					listaFollow1 = self.first(listaFirst)
					#Si dentro del first hay un epsilon, buscamos su follow de la regla
					if "EPSILON" in listaFollow1:
						listaFollow1.discard("EPSILON")
						listaFollow = listaFollow | listaFollow1
						listaFollow1 = self.follow(i[0])
					listaFollow = listaFollow | listaFollow1
				else:
					#Si no hay una cadena despues, buscamos el follow de la regla
					if i[0] != simbolo:
						listaFollow1 = self.follow(i[0])
						listaFollow = listaFollow | listaFollow1
		return listaFollow

	def crearTabla(self):
		tablaLL1 = []
		columna = []
		#Creamos las columnas
		columna.append("")
		for i in self.Vt:
			columna.append(i)
		columna.append('$')
		columna.remove("EPSILON")
		tablaLL1.append(columna)
		#Creamos las filas
		columna = []
		for i in self.Vn:
			columna.append(i)
			for j in self.Vt:
				columna.append("")
			tablaLL1.append(columna)
			columna = []
		#Calculamos los first correspondiente a cada regla
		for regla, i in enumerate(self.arregloReglas):
			simbolos = list(self.first(i[1:-1]))
			#Si el first es un epsilon, calculamos follow
			if simbolos[0] == "EPSILON":
				simbolos = list(self.follow(i[0]))
			#Colocamos la regla en la tabla
			for j in tablaLL1:
				if j[0] == i[0]:
					for simbolo in simbolos:
						for numColumna, k in enumerate(tablaLL1[0]):
							if k == simbolo:
								j[numColumna] = regla
		#Agregamos los no terminales a la tabla
		for i in self.Vt:
			if i != "EPSILON":
				columna.append(i)
				for j in tablaLL1[0][1:]:
					if j == i:
						columna.append("POP")
					else:
						columna.append("")
				tablaLL1.append(columna)
				columna = []
		columna.append("$")
		for i in self.Vt:
			columna.append("")
		columna[-1] = "ACEPTACION"
		tablaLL1.append(columna)
		#Guardamos la tabla en un archivo de texto
		archivo = open("LL1.txt","w")
		for i in self.arregloReglas:
			for j in i:
				archivo.write(str(j)+"\t")
			archivo.write("\n")
		archivo.write("-\n")
		for i in tablaLL1:
			for j in i:
				archivo.write(str(j)+"\t")
			archivo.write("\n")
		archivo.close()
