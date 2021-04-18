class AnalisisLexico:

	AFD = []
	Token = []
	Lexema = []
	Contador = -1

	def __init__(self, AFD):
		self.AFD = AFD
		Contador = -1

	def analizarCadena(self, cadena):
		Token = -1
		Lexema = ""
		Estado = 0
		Columna = 0
		i = 0
		while i < len(cadena):
			caracter = cadena[i]
			Columna = self.AFD[Estado+1]
			Estado = Columna[ord(caracter)-30]
			Token = Columna[-1]
			if Estado == -1:
				self.Token.append(Token)
				self.Lexema.append(Lexema)
				Estado = 0
				Token = -1
				Lexema = ""
				i -= 1
			else:
				Lexema += caracter
			i += 1
		self.Token.append(Token)
		self.Lexema.append(Lexema)
		self.Token.append("Fin")
		self.Lexema.append("Fin")

	def getToken(self):
		return self.Token

	def getLexema(self):
		return self.Lexema

	def yylex():
		contador += 1
		return self.Token[contador], self.Lexema[contador]

	def undoToken():
		contador -= 1
