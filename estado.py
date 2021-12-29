from operador import Operador


class Estado:

    def __init__(self, cannibals: int, missionaries: int, hasBoat):

        self.cannibals = cannibals
        self.missionaries = missionaries
        self.hasBoat = hasBoat

    def applyOperator(self, op: int):
        operator = Operador(op)

        if (self.hasBoat):      
            self.missionaries = self.missionaries - operator.missionaries
            self.cannibals = self.cannibals - operator.cannibals
        else:
            self.missionaries = self.missionaries + operator.missionaries
            self.cannibals = self.cannibals + operator.cannibals

        self.hasBoat = int(not self.hasBoat)



    def verifyOperator(self, operator: int):
        self.applyOperator(operator)

        if ((self.cannibals > self.missionaries and self.missionaries == 0) 
            or self.cannibals <= self.missionaries and self.cannibals >= 0 and self.missionaries >= 0):
            # self.showState()

            self.applyOperator(operator)
            return True
        else:
            self.applyOperator(operator)
            return False

    def findBranches(self):
        braches = []

        for op in range(5):
            # print("- ", op+1)
            if(self.verifyOperator(op+1) and self.getOppositeSide().verifyOperator(op+1)):
                braches.append(op+1)      

        return braches

    def isItGone(self):
        return (self.cannibals == 3 and self.missionaries == 3 and self.hasBoat ==1)

    def showState(self):
        print("(", self.cannibals, ",", self.missionaries, ",", self.hasBoat, ")") 
    
    def getOppositeSide(self):
        oppositeSide = Estado(3-self.cannibals, 3-self.missionaries, int(not self.hasBoat))
        return oppositeSide