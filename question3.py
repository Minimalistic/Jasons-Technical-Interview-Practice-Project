#!/usr/bin/python3

from my_helpers import myPrint,         \
                       headerPrint,     \
                       subHeaderPrint   # Some simple text rendering functions

#------------------------------ Question #3 ------------------------------------

# Udacity text:
    # Given an undirected graph G, find the minimum spanning tree within G. 
    # A minimum spanning tree connects all vertices in a graph with the smallest
    # possible total weight of edges. Your function should take in and return an
    # adjacency list.  
    # Vertices are represented as unique strings. The function definition should
    # be question3(G)

# Adjacency list (with additions) that was in Udacity assignment.
G =  {'A': [('B', 2), ('C',132)],
      'B': [('A', 2), ('C', 8)],
      'C': [('B', 5), ('A', 42)]}

def question3(G):
    """ Determines Minimum Spanning Tree (MST) by analysing given Graph (G) """

    # Prep for Minimum Spanning Tree
    MST   = {}

    # Initialization for `edges`
    edges = []

    # Extract the graph information into easier to use format
    for union in G.keys():
        for (vertex, weight) in G[union]:
            edges.append((weight, union, vertex))

    # Sort `edges` by `weight`
    for (weight, union, vertex) in sorted(edges):

        # Add `edges` that don't contain `union` to `MST``
        if union not in MST.keys() or vertex not in MST.keys():
            
            if union not in MST.keys():
                MST[union]  = []

            if vertex not in MST.keys():
                MST[vertex] = []

            # Append cleared data
            MST[union].append((vertex, weight))
            MST[vertex].append((union, weight))

    return MST

headerPrint('Question 3 - Finding Minimum Spanning Tree')
subHeaderPrint('This is the full starting graph provided to the program:')
myPrint(G)
myPrint('')
subHeaderPrint('Determining Minimum Spanning Tree (MST)...')
myPrint('Result: ' )
myPrint(question3(G))

print('')
input('Press the enter key to continue...')

