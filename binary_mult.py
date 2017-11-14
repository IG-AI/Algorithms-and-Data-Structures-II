#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Binary Multiplication

Team Number: 13
Student Names: Daniel Ågstrand, Linnea Andersson 
'''
import unittest

def shift_left(l, n):
    return l[n:]+l[:n]


def shift_right(l, n):
    if len(l) == 1:
        return [0]
    for i in range(len(l)-1):
        l[i+1] = l[i]
    for j in range(n):
        l[j] = 0
    return l


def half_adder(A,B):
    C = [0] * len(A)
    Carry = 0
    A = list(reversed(A))
    B = list(reversed(B))
    if len(A) == len(B):
        for i in range(len(A)):
            if A[i] == B[i] and Carry == 0:
                if A[i] == 0:
                    C[i] = 0
                else:
                    C[i] = 0
                    Carry = 1
            elif A[i] == B[i]:
                if A[i] == 1:
                    C[i] = 1
                    Carry = 1
                else:
                    C[i] = 1
                    Carry = 0
            else:
                if Carry == 1:
                    C[i] = 0
                else:
                    C[i] = 1
                    Carry = 0
        return list(reversed(C))
    else:
        return -1

def binary_mult(A,B):
    global C
    C = [0] * (2*len(A))
    return binary_mult_aux(A,B)
 

def binary_mult_aux(A,B):
    """
    Sig:    int[0..n-1], int[0..n-1] ==> int[0..2*n-1]
    Pre:    
    Post:   
    Var:    
    Example:    binary_mult([0,1,1],[1,0,0]) = [0,0,1,1,0,0]
    """
    n = len(A)
    C = [0] * (2*n)
    if len(A) == len(B):
        if n == 1:
            return [A[0] * B[0]] 
        else:
            a1 = A[0:n/2]
            b1 = B[0:n/2]
            a2 = A[n/2:n]
            b2 = B[n/2:n]

            #print 'a1 = ', format(a1)
            #print 'a2 = ', format(a2)
            #print 'b1 = ', format(b1)
            #print 'b2 = ', format(b2)

            x1 = binary_mult(a1,b2)
            x2 = binary_mult(a1,b1)
            x3 = binary_mult(a2,b2)
            x4 = binary_mult(a2,b2)

             

          #  x2 = half_adder(x2,x3)
           # x1 = shift_left(x1, n)
           # x2 = shift_right(x2, n/2)
         
        #temp = half_adder(x1, x2)
        #temp = half_adder(temp, x4)

        return x1 + x2 + x3 + x4
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
        A = [0,1,1,0]
        B = [0,0,1,0]
        answer = binary_mult(A, B)
        self.assertEqual(answer, [0,0,0,0,1,1,0,0])

if __name__ == '__main__':
    unittest.main()
