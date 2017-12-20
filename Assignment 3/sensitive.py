#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 3: Controlling Maximum Flow

Team Number: 13
Student Names: Daniel Ågstrand, Linnea Andersson
'''

import unittest
import networkx as nx
# API for networkx flow algorithms changed in v1.9:
if (list(map(lambda x: int(x), nx.__version__.split("."))) < [1, 9]):
    max_flow = nx.ford_fulkerson
else:
    max_flow = nx.maximum_flow
"""
We use max_flow() to generate flows for the included tests,
and you may of course use it as well in any tests you generate.
As always, your implementation of the senstive() function may NOT make use
of max_flow(), or any of the other graph algorithm implementations
provided by networkx.
"""

# If your solution needs a queue (like the BFS algorithm), you can use this one:
from collections import deque

try:
    import matplotlib.pyplot as plt
    HAVE_PLT = True
except ImportError:
    HAVE_PLT = False

"""
F is represented in python as a dictionary of dictionaries;
i.e., given two nodes u and v,
the computed flow from u to v is given by F[u][v].
"""

def sensitive(G, s, t, F):
    """
    Sig:   graph G(V,E), int, int, int[0..|V|-1, 0..|V|-1] ==> int, int
    Pre:   None 
    Post:  Returns sensitive node 
    Ex:    sensitive(G,0,5,F) ==> (1, 3)
    """
    mincut = []
    capacity = nx.get_edge_attributes(G,'capacity')
    maxflow = 0
    for n in G.predecessors(t):
        #Variant: G.predecessors(t) - n
        maxflow += F[n][t]
    for u,v in G.edges():
        #Variant: G.edges() - u,v
        if G[u][v]['capacity'] == F[u][v]:
            mincut.append((u,v))
    for i in mincut:
        #Variant: mincut - i
        capacity[i] -= 1
        if check_maxflow(G,i,t,capacity,F) < maxflow:
            return i
        else:
            capacity[i] += 1

    return None, None

def check_maxflow(G,i,t,capacity,F):
    """
    Sig:   graph G(V,E), node i, node t, capacity list, int[0..|V|-1, 0..|V|-1] ==> int   Pre:   None 
    Pre:   capacity cannot be empty 
    Post:  Returns new max flow
    Ex:    check_maxflow(G,i,t,capacity,F) ==> 3
    """
    queue = deque([])
    queue.append(i[1])
    nx.set_node_attributes(G,'color','white')
    nodes = nx.get_node_attributes(G,'color')
    while queue != deque([]):
        #Variant: queue - u
        u = queue.pop()
        nodes[u] = 'red'
        for n in G.successors(u):
            #Variant: G.successors(u) - n
            if nodes[n] is 'white' and F[u][n] != 0:
                nodes[n] = 'red'
                queue.appendleft(n)
                F[u][n] -= 1
    flow = 0
    for n in G.predecessors(t):
        #Variant: G.predecessors(t) - n
        flow += F[n][t]
    return flow
