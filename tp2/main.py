from algo1 import*
from binarytree import*
from print_tree import*
from avltree import*


# nodeA =  AVLNode()
# nodeB =  AVLNode()
# nodeC =  AVLNode()
# nodeD =  AVLNode()
# nodeE =  AVLNode()
# nodeF =  AVLNode()


# avlTree = AVLTree()

# avlTree.root = nodeA

# nodeA.key = 20
# nodeB.key = 15
# nodeC.key = 40
# nodeD.key = 5
# nodeE.key = 17
# nodeF.key = 80


# nodeA.value = "A"
# nodeB.value = "B"
# nodeC.value = "C"
# nodeD.value = "D"
# nodeE.value = "E"
# nodeF.value = "F"


# nodeB.parent = nodeA
# nodeC.parent = nodeA
# nodeD.parent = nodeB
# nodeE.parent = nodeB
# nodeF.parent = nodeC




# nodeA.rightnode = nodeC
# nodeA.leftnode = nodeB
# nodeB.rightnode = nodeE  
# nodeB.leftnode = nodeD
# nodeC.rightnode = nodeF 



# nodeA.balanceFactor = 0
# nodeB.balanceFactor = 0
# nodeC.balanceFactor = 0
# nodeD.balanceFactor = 0
# nodeE.balanceFactor = 0
# nodeF.balanceFactor = 0


# insertAvl(avlTree,"G",100)


# printTree(avlTree)
# deleteKeyAvl(avlTree, 100)
# printTree(avlTree)


nodeA = AVLNode()
nodeB = AVLNode()
nodeC = AVLNode()
nodeD = AVLNode()
nodeE = AVLNode()

nodeA.key = 60
nodeB.key = 20
nodeC.key = 100
nodeD.key = 80
nodeE.key = 120

Tree = AVLTree()
Tree.root = nodeA

nodeA.value = 'A'
nodeB.value = 'B'
nodeC.value = 'C'
nodeD.value = 'D'
nodeE.value = 'E'

nodeA.leftnode = nodeB
nodeA.rightnode = nodeC
nodeC.leftnode = nodeD
nodeC.rightnode = nodeE

nodeB.parent = nodeA
nodeC.parent = nodeA
nodeD.parent = nodeC
nodeE.parent = nodeC

nodeA.balanceFactor = -1
nodeB.balanceFactor = 0
nodeC.balanceFactor = 0
nodeD.balanceFactor = 0
nodeE.balanceFactor = 0


printTree(Tree)
print(' - - - - - - - - - - - -')
insertAvl(Tree,"F",70)
printTree(Tree)


