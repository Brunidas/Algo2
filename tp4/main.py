# Bruno Fuentes
# bruno.e.fuentes97@gmail.com
# 12401
# https://repl.it/@BrunoFuentes/tp4


from algo1 import*
from print_tree import*
from linkedlist import*
from binarytree import*
from stack import *
from trie import*

class Trie:
	root = None

class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False



T = Trie()

insertTrie( T,"OSO")
insertTrie( T,"OSA")
insertTrie( T,"TERNA")
printTrie( T ) 
print("- - - - - - - -")
a = autoCompletar( T,"T" )
print( a )

# T2 = Trie()

# insertTrie( T2,"RT")
# insertTrie( T2,"cnnes")
# insertTrie( T2,"abc")
# insertTrie( T2,"cnn")
# printTrie( T2 )

# mismoDocumento( T, T2 )


















