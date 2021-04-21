class Submarine:

    def __init__(self, p1, p2):
    	self._name = p1
    	self._hour = p2

    def display(self):
    	n = self._name
    	h = str(self._hour)
    	return n + " - " + h
