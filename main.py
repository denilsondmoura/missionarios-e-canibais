from estado import Estado
from operador import Operador

pilha = []

# Definindo estados 
state = Estado(0,0,0)
begin = Estado(0,0,0)
goal = Estado(3,3,1)

# Definindo operadores
umCanibal = Operador(1)
doisCanibal = Operador(2)
umMissionario = Operador(3)
doisMissionario = Operador(4)
umCanUmMis = Operador(5)

# Aplicando os operadores 

while(True):
    state.showState()
    pilha = pilha + state.findBranches()
    print("LENGTH: ", len(pilha))
    print("PILHA: ", pilha)
    print("OPERATOR: ", pilha[0])
    print()

    tempState = state
    for op in pilha:

        state.applyOperator(op)
    pilha.pop(0)

    if(len(pilha) == 0 or state.isItGone()):
        break

print("acabou")


       