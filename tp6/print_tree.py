# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401


#########################################
"mostrar el arbol por pantalla v1.1"#####
#########################################

def printTree(B):
    printTreeR(B,B.root,0)


def printTreeR(L,root,level):
    if root !=None:
        currentNode=root
        printTreeR(L,currentNode.rightnode,level+1)
        ret="\t"*level
        print(ret,end="")
        print("[",currentNode.value,"~",str(currentNode.key)+"/"+str(currentNode.balanceFactor)+
        "]")
        printTreeR(L,currentNode.leftnode,level+1)
