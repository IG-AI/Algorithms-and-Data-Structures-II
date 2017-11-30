#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 2: Ring Detection

Team Number:
Student Names:
'''
import unittest
import networkx as nx
"""IMPORTANT:
We're using networkx only to provide a reliable graph
object.  Your solution may NOT rely on the networkx implementation of
any graph algorithms.  You can use the node/edge creation functions to
create test data, and you can access node lists, edge lists, adjacency
lists, etc. DO NOT turn in a solution that uses a networkx
implementation of a graph traversal algorithm, as doing so will result
in a score of 0.
"""
try:
    import matplotlib.pyplot as plt
    HAVE_PLT = True
except ImportError:
    HAVE_PLT = False

def ring(G):
    """
    Sig: graph G(node,edge) ==> boolean
    Pre:
    Post:
    Example: 
        ring(g1) ==> False
        ring(g2) ==> True
    """
    global nodes
    global previous
    nx.set_node_attributes(G, 'color', 'white')
    nodes = nx.get_node_attributes(G, 'color')
    for n in G:
        previous = None
        if nodes[n] is 'white':
            nodes[n] = 'red'
            if previous is None:
                for k in G.neighbors(n):
                    previous = n
                    if DFS_visit(k,G) is True:
                        return True
            else:
                temp = G.neighbors(n)
                temp.remove(previous)
                for j in temp:
                    previous = n
                    if DFS_visit(j,G) is True:
                        return True
    return False
        
def DFS_visit(u,G):
    global previous
    nodes[u] = 'red'
    temp = G.neighbors(u)
    temp.remove(previous)
    if temp is []:
        return
    for j in temp:
        if nodes[j] is 'white':
            nodes[j] = 'red'
            previous = u
            if DFS_visit(j,G) is True:
                return True
        else:
            return True
        
            


def ring_extended(G):
    """
    Sig: graph G(node,edge) ==> boolean, int[0..j-1]
    Pre:
    Post:
    Example: 
        ring(g1) ==> False, []
        ring(g2) ==>  True, [3,7,8,6,3]
    """
    
    
def draw_graph(G,r):
    """Draw graph and the detected ring
    """
    if not HAVE_PLT:
        return
    pos = nx.spring_layout(G)
    plt.axis('off')
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_edges(G,pos,style='dotted') # graph edges drawn with dotted lines
    nx.draw_networkx_labels(G,pos)
    
    # add solid edges for the detected ring
    if len(r) > 0:
        T = nx.Graph()
        T.add_path(r)
        for (a,b) in T.edges():
            if G.has_edge(a,b):
                T.edge[a][b]['color']='g' # green edges appear in both ring and graph
            else:
                T.edge[a][b]['color']='r' # red edges are in the ring, but not in the graph
        nx.draw_networkx_edges(
            T,pos, 
            edge_color=[edata['color'] for (a,b,edata) in T.edges(data=True)], 
            width=4)
    plt.show()
    
class RingTest(unittest.TestCase):
    """Test Suite for ring detection problem
    
    Any method named "test_something" will be run when this file is 
    executed. Use the sanity check as a template for adding your own test 
    cases if you wish.
    (You may delete this class from your submitted solution.)
    """
    def is_ring(self, graph, path):
        """Asserts that the nodes in path from a ring in graph"""
        traversed = nx.Graph()
        for v in range(len(path) - 1):
            self.assertTrue(
                path[v + 1] in graph.neighbors(path[v]), 
                "({},{}) is not an edge in the graph\ngraph: {}".format(
                    path[v],
                    path[v+1],
                    graph.edges())
                    )
            self.assertFalse(
                traversed.has_edge(path[v],path[v+1]), 
                "duplicated edge: ({},{})".format(path[v],path[v+1]))
            traversed.add_edge(path[v],path[v+1])
        self.assertEqual(
            path[0], path[-1], 
            "start and end not equal: {} != {}".format(path[0],path[-1]))
            
        
    def test_sanity(self):
        """Sanity Test
        
        This is a simple sanity check for your function;
        passing is not a guarantee of correctness.
        """
        """testgraph = nx.Graph([(0,1),(0,2),(0,3),(2,4),(2,5),(3,6),(3,7),(7,8)])
        self.assertFalse(ring(testgraph))
        testgraph.add_edge(6,8)"""
        G = nx.Graph();
        G.add_node(0);
        G.add_node(1);
        G.add_node(2);
        G.add_node(3);
        G.add_node(4);
        G.add_node(5);
        G.add_node(6);
        G.add_node(7);
        G.add_node(8);
        G.add_edge(1, 4);
        G.add_edge(4, 5);
        G.add_edge(2, 8);
        G.add_edge(3, 5);
        G.add_edge(0, 3);
        G.add_edge(6, 8);
        G.add_edge(1, 5);
        G.add_edge(5, 8);
        G.add_edge(4, 8);
        G.add_edge(0, 3);
        self.assertTrue(ring(G))
        
    """def test_extended_sanity(self):
        #sanity test for returned ring
        testgraph = nx.Graph([(0,1),(0,2),(0,3),(2,4),(2,5),(3,6),(3,7),(7,8),(6,8)])
        found, thering = ring_extended(testgraph)
        self.assertTrue(found)
        self.is_ring(testgraph, thering)
        # Uncomment to visualize the graph and returned ring:
        draw_graph(testgraph,thering)"""
    @classmethod
    def tearDownClass(cls):
        if HAVE_PLT:
            plt.show()
if __name__ == '__main__':
    unittest.main()
