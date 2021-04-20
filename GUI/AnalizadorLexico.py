class AnalisisLexico:

	AFD = []
	Token = []
	Lexema = []
	contador = -1

	def __init__(self, AFD):
		self.AFD = AFD
		self.contador = -1

	def analizarCadena(self, cadena):
		self.Token = []
		self.Lexema = []
		self.contador = -1
		Token = -1
		Lexema = ""
		Estado = 0
		Columna = 0
		i = 0
		while i < len(cadena):
			caracter = cadena[i]
			Columna = self.AFD[Estado+1]
			Estado = Columna[ord(caracter)-30]
			if Estado == -1:
				Token = Columna[-1]
				self.Token.append(Token)
				self.Lexema.append(Lexema)
				Estado = 0
				Token = -1
				Lexema = ""
				i -= 1
			else:
				Lexema += caracter
			i += 1
		Columna = self.AFD[Estado+1]
		Estado = Columna[ord(caracter)-30]
		Token = Columna[-1]
		self.Token.append(Token)
		self.Lexema.append(Lexema)
		self.Token.append("Fin")
		self.Lexema.append("Fin")

	def getToken(self):
		return self.Token

	def getLexema(self):
		return self.Lexema

	def yylex(self):
		self.contador += 1
		return self.Token[self.contador]

	def undoToken(self):
		self.contador -= 1

	def miLexema(self):
		return self.Lexema[self.contador]
