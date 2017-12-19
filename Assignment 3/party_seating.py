#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 3: Party seating problem

Team Number:
Student Names:
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
    Pre:
    Post:
    Ex:     [[1,2],[0],[0]] ==> True, [0], [1,2]
    """
    global nodes
    G=nx.Graph()
    for i in range(len(known)):
        G.add_node(i)
    for i in range(len(known)):
        for j in range(len(known[i])):
            G.add_edge(i,known[i][j])
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos)
    plt.show()
    nx.set_node_attributes(G,'color','white')
    nodes = nx.get_node_attributes(G,'color')
    bol = BFS_color(G)
    table1 = []
    table2 = []
    if bol is True:
        for i in range(len(nodes)):
            if nodes[i] is 'red':
                table1.append(i)
            else:
                table2.append(i)
    print table1
    print table2
    print bol
    return bol, table1, table2

def BFS_color(G):
    queue = []
    for s in G.nodes():
        if nodes[s] is 'white':
            queue.append(s)
            nodes[s] = 'red'
        print nodes
        while queue != []:
            u = queue.pop()
            for n in G.neighbors(u):
                print u
                print n
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


class PartySeatingTest(unittest.TestCase):
    """Test suite for party seating problem
    """

    def test_sanity(self):
        """Sanity test

        A minimal test case.
        """
        K = [[11, 12], [], [], [], [], [], [], [], [], [], [], [0], [0]]
        (found, A, B) = party(K)
        self.assertEqual(
            len(A) + len(B),
            len(K),
            "wrong number of guests: {!s} guests, tables hold {!s} and {!s}".format(
                len(K),
                len(A),
                len(B)
                )
            )
        for g in range(len(K)):
            self.assertTrue(
                g in A or g in B,
                "Guest {!s} not seated anywhere".format(g))
        for a1 in A:
            for a2 in A:
                self.assertFalse(
                    a2 in K[a1],
                    "Guests {!s} and {!s} seated together, and know each other".format(
                        a1,
                        a2
                        )
                    )
        for b1 in B:
            for b2 in B:
                self.assertFalse(
                    b2 in K[b1],
                    "Guests {!s} and {!s} seated together, and know each other".format(
                        b1,
                        b2
                        )
                    )

if __name__ == '__main__':
    unittest.main()
