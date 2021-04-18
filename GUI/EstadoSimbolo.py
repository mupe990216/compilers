class EstadoSimbolo:
	def __init__(self, estado, simbolo):
		self.estado = frozenset(estado)
		self.simbolo = simbolo

	def __hash__(self):
		return hash((self.estado, self.simbolo))

	def __eq__(self, other):
		return (self.estado, self.simbolo) == (other.estado, other.simbolo)