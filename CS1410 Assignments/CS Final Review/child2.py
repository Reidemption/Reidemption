import submarine

class Child2(submarine.Submarine):
	def __init__(self, name):
		super().__init__(name, 12)