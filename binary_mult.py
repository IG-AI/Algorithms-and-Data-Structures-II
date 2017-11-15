#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Binary Multiplication

Team Number: 13
Student Names: Daniel Ågstrand, Linnea Andersson 
'''
import unittest

def shift_left(l, n):
    for i in range(n):
        l.append(0)
    return l


def shift_right(l, n):
    for i in range(n):
        l.insert(0,0)
    return l


def full_adder(A,B):
    Carry = 0
    if len(A) != len(B):
        n = abs(len(A) - len(B))
        if n > 0:
            if len(A) > len(B):
                for i in range(n):
                    B.insert(0,0)
            else:
                for i in range(n):
                    A.insert(0,0)
                    
    C = [0] * len(A)
    for i in range(len(A)):
        if i == (len(A) - 1) and (A[-i-1] == 1 and B[-i-1] == 1 and Carry == 1):
            C[-i-1] = 1
            C.insert(0,1)
        elif i == (len(A) - 1) and (A[-i-1] != B[-i-1] and Carry == 1):
            C[-i-1] = 0
            C.insert(0,1)
        elif i == (len(A) - 1) and (A[-i-1] == 1 and B[-i-1] == 1 and Carry == 0):
            C[-i-1] = 0
            C.insert(0,1)
            
        else:
            if A[-i-1] == B[-i-1] and Carry == 0:
                if A[-i-1] == 0:
                    C[-i-1] = 0
                else:
                    C[-i-1] = 0
                    Carry = 1
            elif A[-i-1] == B[-i-1]:
                if A[-i-1] == 1:
                    C[-i-1] = 1
                    Carry = 1
                else:
                    C[-i-1] = 1
                    Carry = 0
            else:
                if Carry == 1:
                    C[-i-1] = 0
                else:
                    C[-i-1] = 1
                    Carry = 0
    return C


def binary_mult(A,B):
    temp = binary_mult_aux(A,B)
    if len(temp) != len(A):
        n = abs(len(temp) - len(A*2))
        for i in range(n):
            temp.insert(0,0)
    return temp


def binary_mult_aux(A,B):
    """
    Sig:    int[0..n-1], int[0..n-1] ==> int[0..2*n-1]
    Pre:    
    Post:   
    Var:    
    Example:    binary_mult([0,1,1],[1,0,0]) = [0,0,1,1,0,0]
    """
    
    if len(A) != len(B):
        t = abs(len(A) - len(B))
        if len(A) > len(B):
            for i in range(t):
                B.insert(0,0)
        else:
            for i in range(t):
                A.insert(0,0)
                
    n = len(A)
    if n == 1:
        return [A[0] * B[0]] 
    else:
        m = n - n/2

        print 'A = ', format(A)
        print 'B = ', format(B)

        a = A[:n/2]
        b = A[n/2:n]
        c = B[:n/2]
        d = B[n/2:n]

        print 'a = ', format(a)
        print 'b = ', format(b)
        print 'c = ', format(c)
        print 'd = ', format(d)

        e = binary_mult_aux(a,c)
        f = binary_mult_aux(b,d)
        g = binary_mult_aux(b,c)
        h = binary_mult_aux(a,d)
                        
        print 'e = ', format(e)
        print 'f = ', format(f)
        print 'g = ', format(g)
        print 'h = ', format(h)

        t1 = shift_left(e, n)
        t2 = full_adder(g,h)
        t3 = shift_left(t2, m)
        t4 = full_adder(t1, t3)

        print 't1 = ', format(t1)
        print 't2 = ', format(t2)
        print 't3 = ', format(t3)
        print 't4 = ', format(t4)
                        
        final = full_adder(t4, f)
        
        print 'final = ', format(final)

    return final
            
    
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
        
        A = [1,0,1]
        B = [1,1,1]
        answer = binary_mult(A, B)
        self.assertEqual(answer, [0,0,0,0,1,1,0,0])

if __name__ == '__main__':
    unittest.main()
