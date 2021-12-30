from estado import Estado
import copy


class Node:
    
    # Função cria um node apartir de um estado
    def __init__(self, state: Estado):

        self.state = state
        # Após conhecer o estado, construtor Recupera uma lista com todos os operadores que levam esse estado a um que seja permitido pelo problema
        self.branches = self.findBranches()
        # ...Também recupera todos os nós filhos que são gerados quando os operadores acima são aplicados
        self.children = []

        self.findChildren()
    
    # Implementação de um metodo semelhante ao toString()
    def __str__(self):
        return str((self.state.cannibals, self.state.missionaries, self.state.hasBoat))

    # A função basicamente verificar a validade dos operadores aplicados as duas margens e armazena
    # a intercecção de operadores em uma lista: branches
    def findBranches(self):
        branches = []

        for op in range(5):
            # print("- ", op+1)
            if(self.state.verifyOperator(op+1) and self.state.getOppositeSide().verifyOperator(op+1)):
                branches.append(op+1)      

        return branches

    # Essa função basicamente aplica os operadores validados ao estado...
    # ...selvam os novos estados em uma lista...
    # ... e reaplicam os operadores novamente pra reverter o estado a sua forma anterior
    def findChildren(self):

        for op in self.branches:
            self.state.applyOperator(op)
            temp = copy.copy(self.state)
            self.children.append(temp)
            self.state.applyOperator(op)

        return self.children
