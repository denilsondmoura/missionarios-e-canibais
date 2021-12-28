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
state.showState()
print("branches: ", state.findBranches())

# while(not state.isItGone()):
#     state.showState()
#     print("branches: ", state.findBranches())
#     pilha.append(state.findBranches())
#     state.applyOperator(pilha[0])
#     pilha.pop(0)

# print("acabou")