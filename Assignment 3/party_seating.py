#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 3: Party seating problem

Team Number: 13
Student Names: Daniel Ågstrand, Linnea Andersson
'''
import unittest
import networkx as nx
try:
    import matplotlib.pyplot as plt
    HAVE_PLT = True
except ImportError:
    HAVE_PLT = False

# If your solution needs a queue, you can use this one:
from collections import deque

def party(known):
    """
    Sig:    int[1..m, 1..n] ==> boolean, int[1..j], int[1..k]
    Pre:    None
    Post:   True if there exists seating arrangement and
            two arrays that represent seating arrangement,
            otherwise fasle and two empty lists
    Ex:     [[1,2],[0],[0]] ==> True, [0], [1,2]
    """
    global nodes
    G=nx.Graph()
    for i in range(len(known)):
        #Variant: len(known) - i
        G.add_node(i)
    for i in range(len(known)):
        #Variant: len(known) - i
        for j in range(len(known[i])):
            #Variant: len(known[i]) - j
            G.add_edge(i,known[i][j])
    nx.set_node_attributes(G,'color','white')
    nodes = nx.get_node_attributes(G,'color')
    bol = BFS_color(G)
    table1 = []
    table2 = []
    if bol is True:
        for i in range(len(nodes)):
            #Variant: len(nodes) - i
            if nodes[i] is 'red':
                table1.append(i)
            else:
                table2.append(i)

    return bol, table1, table2

def BFS_color(G):
    """
    Sig:    graph G(V,E) ==> boolean
    Pre:    None
    Post:   True if graph is bipartite, otherwise false
    """
    queue = []
    for s in G.nodes():
        #Variant: G.nodes() - s
        if nodes[s] is 'white':
            queue.append(s)
            nodes[s] = 'red'
        while queue != []:
            #Variant: queue 
            u = queue.pop()
            for n in G.neighbors(u):
                #Variant: G.neighbors(u) - n 
                if nodes[n] == 'white' and nodes[u] == 'red':
                    nodes[n] = 'blue'
                    queue.append(n)
                elif nodes[n] == 'white' and nodes[u] == 'blue':
                    nodes[n] = 'red'
                    queue.append(n)
                elif nodes[n] == 'blue' and nodes[u] == 'blue':
                    return False
                elif nodes[n] == 'red' and nodes[u] == 'red':
                    return False
    return True
