import submarine

class Child1(submarine.Submarine):
	def __init__(self, time):
		super().__init__("Doctor", time)