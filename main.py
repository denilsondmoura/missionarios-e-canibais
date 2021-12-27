from estado import Estado
from operador import Operador

# Definindo estados 
state = Estado(0,0,0)
begin = Estado(0,0,0)
goal = Estado(3,3,1)

# Definindo operadores
umCanibal = Operador(1,1,0)
doisCanibal = Operador(2,2,0)
umMissionario = Operador(3,0,1)
doisMissionario = Operador(4,0,2)
umCanUmMis = Operador(5,1,1)


print("boat: ", boat.canibais)