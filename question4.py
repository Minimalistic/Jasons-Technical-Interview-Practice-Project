#!/usr/bin/python3

from my_helpers import myPrint,         \
                       headerPrint,     \
                       subHeaderPrint   # Some simple text rendering functions
                       
#------------------------------ Question #4 ------------------------------------

# Udacity text:
    # Find the least common ancestor between two nodes on a binary search tree. 
    # The least common ancestor is the farthest node from the root that is an 
    # ancestor of both nodes. For example, the root is a common ancestor of all
    # nodes on the tree, but if both nodes are descendents of the root's left 
    # child, then that left child might be the lowest common ancestor. You can 
    # assume that both nodes are in the tree, and the tree itself adheres to all
    # BST properties. The function definition should look like 
    # question4(T, r, n1, n2), where T is the tree represented as a matrix, 
    # where the index of the list is equal to the integer stored in that node 
    # and a 1 represents a child node, r is a non-negative integer representing 
    # the root, and n1 and n2 are non-negative integers representing the two 
    # nodes in no particular order. For example, one test case might be

        # question4([[0, 1, 0, 0, 0],
            #        [0, 0, 0, 0, 0],
            #        [0, 0, 0, 0, 0],
            #        [1, 0, 0, 0, 1],
            #        [0, 0, 0, 0, 0]],
            #        3,
            #        1,
            #        4)

    # and the answer would be 3.

def getPathToRoot(T, root, node):
    path    = [node]
    current =  node
    while current != root:
        for node2, lst in enumerate(T):
            if T[node2][current]:
                path.append(node2)
                current = node2
    return path

def question4(T, root, node1, node2):
    path1 = getPathToRoot(T, root, node1)
    path2 = getPathToRoot(T, root, node2)
    # myPrint("Path1: " + str(path1))
    # myPrint("Path2: " + str(path2))
    for node in path1:
        if node in path2:
            return node   
    return False

headerPrint('Question 4 - Find Least Common Ancestor Between Two Nodes')
subHeaderPrint('Finding the least common ancestor using the following: ')
myPrint('[0, 1, 0, 0, 0],')
myPrint('[0, 0, 0, 0, 0],')
myPrint('[1, 0, 0, 0, 1],')
myPrint('[0, 0, 0, 0, 0,]],')
myPrint(' 3,')
myPrint(' 1,')
myPrint(' 4)')

myPrint('')
subHeaderPrint('Result is: ')

myPrint(question4([[0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [1, 0, 0, 0, 1],
                   [0, 0, 0, 0, 0]],
                    3,
                    1,
                    4)
    )

print('')
input('Press the enter key to continue...')
