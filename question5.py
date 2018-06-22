#!/usr/bin/python3

from my_helpers import myPrint,         \
                       headerPrint,     \
                       subHeaderPrint   # Some simple text rendering functions
# Question 5 -------------------------------------------------------------------

# Udacity text:
    # Find the element in a singly linked list that's m elements from the end. 
    # For example, if a linked list has 5 elements, the 3rd element from the end
    # is the 3rd element. The function definition should look like 
    # question5(ll, m), where ll is the first node of a linked list and m is the
    # "mth number from the end". You should copy/paste the Node class below to 
    # use as a representation of a node in the linked list. Return the value of 
    # the node at that position.

class Node(object): # Big-O approximation is O(n^2)
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a linked list
ll                     = Node(1)
ll.next                = Node(2)
ll.next.next           = Node(3)
ll.next.next.next      = Node(4)
ll.next.next.next.next = Node(5)

def print_ll(ll):
    """ Prints out the linked list. """
    node = ll
    while node != None:
        print(node.data)
        node = node.next

def getFromHead(ll, m):
    node = ll
    # For second element `m = 2`, we run this loop once.
    # If iteration returns `None`, abort query and return `None`
    for iter in range(1, m):
        node = node.next
        if node == None:
            return None
            
    # Node is now the mth element from the start of the linked list
    return node.data

def question5(ll, m):
    return getFromHead(ll, m)

headerPrint('Question 5 - Specific element location in singly linked list')

subHeaderPrint('Printing generated linked list with 5 nodes:')        
print_ll(ll)
myPrint('')

subHeaderPrint('Printing value of 3rd element of a linked list with 5 elements')        
myPrint(question5(ll, 3))

print('')
input('Press the enter key to continue...')
