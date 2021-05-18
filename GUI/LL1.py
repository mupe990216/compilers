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
		if lista[0] in set(self.Vt):
			listaFirst.add(lista[0])
			return listaFirst
		elif lista[0] in set(self.Vn):
			for reglaNT in self.arregloReglas:
				if reglaNT[0] == lista[0]:
					listaFirst1 = self.first(reglaNT[1:])
					listaFirst = listaFirst | listaFirst1
			if "EPSILON" in listaFirst:
				if len(lista) == 1:
					return listaFirst
				listaFirst.discard("EPSILON")
				listaFirst1 = self.first(lista[1:])
				listaFirst = listaFirst | listaFirst1
				return listaFirst
			return listaFirst

	def follow(self, simbolo):
		listaFollow = set([])
		listaFollow1 = set([])
		listaFirst = []
		if simbolo == self.arregloReglas[0][0]:
			listaFollow.add('$')
		for i in self.arregloReglas:
			si = False
			listaFirst = []
			for j in i[1:]:
				if si:
					listaFirst.append(j)
				if j == simbolo:
					si = True
			if si:
				listaFirst.remove(None)
				if len(listaFirst) != 0:
					listaFollow1 = self.first(listaFirst)
					if "EPSILON" in listaFollow1:
						listaFollow1.discard("EPSILON")
						listaFollow = listaFollow | listaFollow1
						listaFollow1 = self.follow(i[0])
					listaFollow = listaFollow | listaFollow1
				else:
					if i[0] != simbolo:
						listaFollow1 = self.follow(i[0])
						listaFollow = listaFollow | listaFollow1
		return listaFollow

	def crearTabla(self):
		tablaLL1 = []
		columna = []
		columna.append()
		for i in  Vt:
			columna.append(i)
		columna.append('$')
		tablaLL1.append(columna)
		columna = []
		for i in Vn:
			columna.append(i)
			#for j in self.arregloReglas:
				#if j[0] == i:
