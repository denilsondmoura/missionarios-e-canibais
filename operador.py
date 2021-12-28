class Operador:

    def __init__(self, op: int, cannibals: int, missionaries: int):

        self.op = op
        self.cannibals = cannibals
        self.missionaries = missionaries
    
    def __init__(self, op: int):

        self.op = op

        match op:
            case 1 : 
                self.cannibals = 1
                self.missionaries = 0
            case 2 :
                self.cannibals = 2
                self.missionaries = 0
            case 3 :
                self.cannibals = 0
                self.missionaries = 1
            case 4 :  
                self.cannibals = 0
                self.missionaries = 2
            case 5 :
                self.cannibals = 1
                self.missionaries = 1  
        
    def showOperator(self):
        print("(", self.op, ",", self.cannibals , ",", self.missionaries, ")") 
