from estado import Estado
import copy


class Node:
    

    def __init__(self, state: Estado):

        self.state = state
        self.branches = self.findBranches()
        self.children = []

        self.findChildren()
    
    def __str__(self):
        return str((self.state.cannibals, self.state.missionaries, self.state.hasBoat))

    def findBranches(self):
        branches = []

        for op in range(5):
            # print("- ", op+1)
            if(self.state.verifyOperator(op+1) and self.state.getOppositeSide().verifyOperator(op+1)):
                branches.append(op+1)      

        return branches

    def findChildren(self):

        for op in self.branches:
            self.state.applyOperator(op)
            
            temp = copy.copy(self.state)
            # no = Node(temp)
            self.children.append(temp)
            # print("op: ", op, " - children: ", self.showChildren())

            self.state.applyOperator(op)

        return self.children

    def showChildren(self):
        toString = ""
        for state in self.children:
            toString = toString + str(state.getState()) + " | "
        
        print(toString)
        
        return toString