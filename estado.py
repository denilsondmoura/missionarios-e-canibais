from operador import Operador


class Estado:
    # Construtor do objeto Estado
    def __init__(self, cannibals: int, missionaries: int, hasBoat):

        self.cannibals = cannibals
        self.missionaries = missionaries
        self.hasBoat = hasBoat

    # Recebe um operador de 1 a 5 e aplica ao estado
    def applyOperator(self, op: int):
        operator = Operador(op)
        # Se o barco estiver nessa margem, então irei ENVIAR missionaios e/ou canibais para a outra margem
        if (self.hasBoat):      
            self.missionaries = self.missionaries - operator.missionaries
            self.cannibals = self.cannibals - operator.cannibals

        # Se o barco NÂO estiver nessa margem, então irei RECEBER missionaios e/ou canibais vindos da outra margem
        else:
            self.missionaries = self.missionaries + operator.missionaries
            self.cannibals = self.cannibals + operator.cannibals

        # Sempre que um operador é aplicado a um estado, a variavel hasBoat recebe a sua negação
        self.hasBoat = int(not self.hasBoat)

    # Recebe um operador e verifica se ele gera um estado permitido pelo problema
    def verifyOperator(self, operator: int):
        # Para verificar a validade do operador, é preciso aplica-lo...
        self.applyOperator(operator)
        # Após aplicado o operador, faz-se as devidas verificações...
        if ((self.cannibals > self.missionaries and self.missionaries == 0) 
            or self.cannibals <= self.missionaries and self.cannibals >= 0 and self.missionaries >= 0):
            # Após as verificações, o mesmo operador é aplicado ao estado, revertendo a primeira aplicação
            self.applyOperator(operator)
            return True
        else:
            self.applyOperator(operator)
            return False

    # verifica se alcançamos o estado final: (3,3,1)
    def isItGone(self):
        return (self.cannibals == 3 and self.missionaries == 3 and self.hasBoat ==1)
    
    # Retorna o estado oposto ao estado atual, ou seja, a margem oposta
    def getOppositeSide(self):
        oppositeSide = Estado(3-self.cannibals, 3-self.missionaries, int(not self.hasBoat))
        return oppositeSide
