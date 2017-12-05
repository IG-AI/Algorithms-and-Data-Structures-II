#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 2: Ring Detection

Team Number: 13
Student Names: Daniel Ågstrand, Linnea Andersson
'''
import unittest
import networkx as nx
from networkx.classes.function import all_neighbors
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
    Post: Returns true if there is a ring in the graph
    Example: 
        ring(g1) ==> False
        ring(g2) ==> True
    """
    global nodes
    global cycle
    global ringlist
    global done
    ringlist = []
    cycle = False
    done = False
    nx.set_node_attributes(G, 'white','color')
    nodes = nx.get_node_attributes(G, 'color')
    for n in G:
        if nodes[n] == 'white':
            nodes[n] = 'red'
        #for k in G.neighbors(n):
            DFS_visit(n,G,n)
            if cycle is True:
                print nodes
                print ringlist
                return True
        nodes[n] = 'blue'
    return False
        
def DFS_visit(u,G,previous):
    """
    Sig: node u, graph G(node,edge) ==> boolean
    Pre:
    Post: Returns true if a node has been vistited before
    Example: 
        DFS_visit(node u1, graph G1) ==> False
        DFS_visit(node u2, graph G2) ==> True
    """
    global cycle 
    global done
    nodes[u] = 'red'
    for j in G.neighbors(u):
        if cycle is True:
            break
        if nodes[j] is 'white':
            nodes[j] = 'red'
            print j
            DFS_visit(j,G,u) 
        elif nodes[j] is 'red' and j != previous:
            print 'hej'
            print j
            cycle = True
    if cycle is True and done is False:
        ringlist.append(u)
        if u in G.neighbors(ringlist[0]) and len(ringlist) > 2:
            done = True
            ringlist.append(ringlist[0])
    if cycle is False:
        nodes[u] = 'blue'    



def ring_extended(G):
    """
    Sig: graph G(node,edge) ==> boolean, int[0..j-1]
    Pre:
    Post:
    Example: 
        ring(g1) ==> False, []
        ring(g2) ==>  True, [3,7,8,6,3]
    """
    if ring(G) is False:
        return False, []
    else:
        print ringlist
        return True, ringlist
        '''temp = []
        k = 0
        nodelist = list(G.nodes)
        index = 0
        for i in nodelist:
            if nodelist[i] is 'red':
                index = i
                break
        for j in G.neighbors(index):
            if nodes[j] is 'red':
                k += 1
        if k is 2:
            temp.append(nodelist[index])
        nodelist.remove(index)
        for i in nodelist:
            if nodes[i] is 'red':
                temp.append(nodelist[i-1])
        return True, temp'''

    
    '''if ring(G) is False:
        return False, []
    else:
        tic = 0
        vlength = len(visited)-1
        temp = []
        temp.append(visited[vlength])
        lastnode = visited[vlength]
        for i in range(vlength+1):
            if lastnode in G.neighbors(visited[vlength-i-1]):
                tic += 1
                temp.append(visited[vlength - i-1])
                if tic == 2:
                    temp.append(visited[vlength])
                    break 
            elif visited[vlength-i-1] in G.neighbors(visited[vlength-i]):
                temp.append(visited[vlength-i-1])
                
        final = []
        
        for n in range(len(temp)):
            tic = 0
            for i in range(len(G.neighbors(temp[n]))):
                neighborslist = G.neighbors(temp[n])
                if neighborslist[i] in temp:
                    tic += 1
                if tic == 2:
                    final.append(temp[n])
                    break
                      
        return True, final'''
    
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
        testgraph = nx.Graph([(0,1),(0,2),(0,3),(2,4),(2,5),(3,6),(3,7),(7,8)])
        #self.assertFalse(ring(testgraph))
        testgraph.add_edge(8,6)
        testgraph.add_edge(3,8)
        #self.assertTrue(ring(testgraph))
        #nx.draw(testgraph)
        #plt.show()
        
    def test_extended_sanity(self):
        """sanity test for returned ring"""
        #testgraph = nx.Graph([(0,2),(0,3),(2,4),(2,5),(3,6),(3,7),(3,1),(6,8),(1,2)])
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
        G.add_edge(4, 7);
        G.add_edge(2, 7);
        G.add_edge(1, 3);
        G.add_edge(3, 8);

        found, thering = ring_extended(G)
        print ring_extended(G)
        self.assertFalse(found)
        self.is_ring(G, thering)
        #Uncomment to visualize the graph and returned ring:
        draw_graph(G,thering)
    @classmethod
    def tearDownClass(cls):
        if HAVE_PLT:
            plt.show()
if __name__ == '__main__':
    unittest.main()
