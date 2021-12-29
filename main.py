from node import Node
from estado import Estado
from operador import Operador

operations = []
nodes = []

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
# node = Node(state)
# print(node.showChildren())
# print(node.state.getState())
# print(node.branches)
# print(node.children)

n = Node(state)
nodes.append(n)
# operations.append("")

while(True):

    for node in nodes:
        i = nodes.index(node)
        # print(nodes.index(node))

        operations = operations + node.branches

        if(len(nodes) == 0 or node.state.isItGone()):
            break

        else:
            for stt in node.children:
                nd = Node(stt)
                nodes.append(nd)

            if(i < 10):
                # print(operations)
                toString = ""
                for nod in nodes:
                    toString = toString + str(nod.state.getState()) + " | "
                print(toString)

                for op in node.branches:
                    print(len(node.branches))
                    print(len(node.children))
                    print(node.branches.index(op))
                    print(nodes[0].children[node.branches.index(op)].getState())
                    # print(i," - op", operations[0], "sobre o estado", nodes[0].state.getState(), "=>", nodes[0].children[node.branches.index(op)])
                    operations.pop(0)
                
            nodes.pop(0)
            


    if(node.state.isItGone()):
        print("Acabou!")
        break

       