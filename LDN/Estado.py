class Estado:
	contIdEdo = 0

	def __init__(self):

		self.__edoAceptado = False				
		self.__idEstado = Estado.contIdEdo
		Estado.contIdEdo += 1
		self.__token = -1
		self.__transicion = set()
	
	def toString(self):
		print("id:",self.__idEstado)
		print(self.__token)
		print(self.__transicion)

	#get
	def getIdEstado(self):
		return self.__idEstado

	def getEdoAceptado(self):
		return self.__edoAceptado

	def getToken(self):
		return self.__token

	def getTransicion(self):
		return self.__transicion

	#set
	def setIdEstado(self, idEstado):
		self.__idEstado = idEstado

	def setEdoAceptado(self, edoAceptado):
		self.__edoAceptado = edoAceptado

	def setToken(self, token):
		self.__token = token	

	def setTransicion(self, transicion):
		self.__transicion.add(transicion)

	def imprime_Estado(self):
		lista_imprimible = []
		lista_imprimible.append("ID-Estado: {}".format(self.__idEstado))
		lista_imprimible.append("Token: {}".format(self.__token))
		transicion_imprimible = ""
		for x in self.__transicion:
			transicion_imprimible += str(x.imprime_Transicion())

		lista_imprimible.append("transicion: {}".format(transicion_imprimible))
		return lista_imprimible
	


	

#pruebitas jajajajaja
#a = Estado()
#a.toString()
#a.toString()
#a.setToken(20)
#a.toString()
