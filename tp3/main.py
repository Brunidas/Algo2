
# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401
# https://https://repl.it/@BrunoFuentes/tp3


from algo1 import*
from binarytree import*
from print_tree import*
from queue import*
from redblacktree import*


nodeA = RedBlackNode()
nodeB = RedBlackNode()
nodeC = RedBlackNode()
nodeD = RedBlackNode()


nodeA.key = 38;
nodeA.value = "A"
nodeA.color = "BLACK" 
nodeA.leftnode = nodeB 
nodeA.rightnode = nodeC

nodeB.parent = nodeA
nodeB.key = 31;
nodeB.value = "B"
nodeB.color = "BLACK" 
nodeB.leftnode = nodeD 

nodeC.parent = nodeA
nodeC.key = 41;
nodeC.value = "C"
nodeC.color = "BLACK" 

nodeD.parent = nodeB
nodeD.key = 12;
nodeD.value = "D"
nodeD.color = "RED" 


Tree = RedBlackTree()
Tree.root = nodeA

printTree(Tree)
print(' - - - - - - - - -')
insertRB( Tree, 19, "E")
print(' - - - - - - - - -')

printTree(Tree)
