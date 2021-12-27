from operador import Operador

class Estado:

    def __init__(self, cannibals, missionaries, hasBoat):

        self.cannibals = cannibals
        self.missionaries = missionaries
        self.hasBoat = hasBoat

    def applyOperator(self, op):
        self.hasBoat = self.hasBoat