from node import Node
from estado import Estado
from operador import Operador

operations = []
nodes = []

# Definindo estados 
state = Estado(0,0,0)

def printNodes(nodes: list):
    toString = ""
    for nod in nodes:
        toString = toString + nod.getState() + " | "
    print(toString)

n = Node(state)
nodes.append(n)

while(True):

    for node in nodes:
        # print("node: ----", node)
        i = nodes.index(node)
        operations = operations + node.branches

        if(len(nodes) == 0 or node.state.isItGone()):
            break

        else:
            for stt in node.children:
                temp = Node(stt)
                nodes.append(temp)

            
            if(i < 10):
                # printNodes(nodes)
                for op in node.branches:
                    # print(len(nodes))
                    # print(len(node.branches))
                    # print(len(node.children))

                    print(i," - op", operations[0], "sobre o estado", nodes[0], "=>", nodes[0].children[node.branches.index(op)].getState())
                    operations.pop(0)
                
            nodes.pop(0)

    if(node.state.isItGone()):
        print("Acabou!")
        break

       