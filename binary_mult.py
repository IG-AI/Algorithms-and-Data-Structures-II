#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Binary Multiplication

Team Number: 13
Student Names: Daniel Ågstrand, Linnea Andersson 
'''
import unittest

def shift(seq, n):
    return seq[n:]+seq[:n]



def binary_mult(A,B):
    """
    Sig:    int[0..n-1], int[0..n-1] ==> int[0..2*n-1]
    Pre:    
    Post:   
    Var:    
    Example:    binary_mult([0,1,1],[1,0,0]) = [0,0,1,1,0,0]
    """
    global n
    n = len(A)
    i = 0
    if len(A) == len(B):
        print 'n = ', format(n)
        if n == 1:
            i = i + 1
            print 'i = ', format(i)
            return [A[0] * B[0]] 
        else:
            a1 = A[0:n/2]
            b1 = A[0:n/2]
            a2 = A[n/2:n]
            b2 = A[n/2:n]


            x1 = binary_mult(a2,b2)
            x2 = binary_mult(a2,b1)
            x3 = binary_mult(a1,b2)
            x4 = binary_mult(a1,b1)

            #print x1
            #print x2
            #print x4

            x2 = x2 + x3
            x1 = shift(x1, n)
            x2 = shift(x2, n/2)

        return [x1[i] + x2[i] + x4[i] for i in range(min(len(x1), len(x2), len(x4)))]
    else:
        return -1
    
class BinaryMultTest(unittest.TestCase):
    """Test Suite for binary multiplication problem
    
    Any method named "test_something" will be run when this file is 
    executed. Use the sanity check as a template for adding your own 
    tests if you wish. 
    (You may delete this class from your submitted solution.)
    """
    
    def test_sanity(self):
        """Sanity Test
        
        This is a simple sanity check for your function;
        passing is not a guarantee of correctness.
        """
        A = [0,1,0,1]
        B = [0,1,1,0]
        answer = binary_mult(A, B)
        self.assertEqual(answer, [0,0,0,0,1,1,0,0])

if __name__ == '__main__':
    unittest.main()
