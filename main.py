# --- ESPECIFICAÇÕES ---
# python v3.10

from node import Node
from estado import Estado
from operador import Operador

# Lista com todos os nós da nossa arvore
nodes = []

# Definindo o estado inicial 
state = Estado(0,0,0)
# criando o nó raiz da nossa arvore
n = Node(state)
nodes.append(n)

# Essa rotina irá executar até que o estado final seja alcançado
while(True):

    for node in nodes:
        print(node)
        # Verifica se alcançamos o estado final
        if(node.state.isItGone()):
            break
        # Senão...
        else:
            # Adicionamos os filhos do nó atual na lista de nós da arvore...
            for stt in node.children:
                temp = Node(stt)
                nodes.append(temp)
            # ... e retiramos o nó atual da lista  
            nodes.pop(0)
    # Verifica novamente se alcançamos o estado final
    if(node.state.isItGone()):
        print("Acabou!")
        break

       