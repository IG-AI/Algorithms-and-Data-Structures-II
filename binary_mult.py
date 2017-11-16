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


def full_adder(A, B):
    carry = 0
    if len(A) != len(B):
        n = abs(len(A) - len(B))
        if n > 0:
            if len(A) > len(B):
                for i in range(n):
                    B.insert(0, 0)
            else:
                for i in range(n):
                    A.insert(0, 0)

    C = [0] * len(A)
    for i in range(len(A)):
        if i == (len(A) - 1) and (A[-i - 1] == 1 and B[-i - 1] == 1 and carry == 1):
            C[-i - 1] = 1
            C.insert(0, 1)
        elif i == (len(A) - 1) and (A[-i - 1] != B[-i - 1] and carry == 1):
            C[-i - 1] = 0
            C.insert(0, 1)
        elif i == (len(A) - 1) and (A[-i - 1] == 1 and B[-i - 1] == 1 and carry == 0):
            C[-i - 1] = 0
            C.insert(0, 1)
        else:
            if A[-i - 1] == B[-i - 1] and carry == 0:
                if A[-i - 1] == 0:
                    C[-i - 1] = 0
                else:
                    C[-i - 1] = 0
                    carry = 1
            elif A[-i - 1] == B[-i - 1]:
                if A[-i - 1] == 1:
                    C[-i - 1] = 1
                    carry = 1
                else:
                    C[-i - 1] = 1
                    carry = 0
            else:
                if carry == 1:
                    C[-i - 1] = 0
                else:
                    C[-i - 1] = 1
                    carry = 0
    return C


def binary_mult(A, B):
    if len(A) == 1 and len(B) == 1:
        return [A[0] * B[0]]

    finallen = len(A) + len(B)
    if len(A) != len(B):
        t = abs(len(A) - len(B))
        if len(A) > len(B):
            for i in range(t):
                B.insert(0, 0)
        else:
            for i in range(t):
                A.insert(0, 0)

    add = True
    power = 1
    while add:
        if (len(A) % (2 ** power)) == 0:
            add = False
        if len(A) < 2 ** power:
            n = 2 ** power - len(A)
            for i in range(n):
                A.insert(0, 0)
                B.insert(0, 0)
            add = False
        else:
            power += 1

    temp = binary_mult_aux(A, B)
    n = len(temp) - finallen
    if n < 0:
        for i in range(abs(n)):
            temp.insert(0, 0)
    else:
        for i in range(n):
            temp.remove(0)

    return temp


def binary_mult_aux(A, B):
    """
    Sig:    int[0..n-1], int[0..n-1] ==> int[0..2*n-1]
    Pre:    
    Post:   
    Var:    
    Example:    binary_mult([0,1,1],[1,0,0]) = [0,0,1,1,0,0]
    """
    n = len(A)
    if n == 1:
        return [A[0] * B[0]]
    else:
        m = n - n / 2

        ah = A[:n / 2]
        al = A[n / 2:n]
        bh = B[:n / 2]
        bl = B[n / 2:n]

        x1 = binary_mult_aux(ah, bh)
        x2 = binary_mult_aux(al, bl)
        x3 = binary_mult_aux(al, bh)
        x4 = binary_mult_aux(ah, bl)

        t1 = shift_left(x1, n)
        t2 = full_adder(x3, x4)
        t3 = shift_left(t2, m)
        t4 = full_adder(t1, t3)

        final = full_adder(t4, x2)

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

        A = [0, 1, 1, 0]
        B = [0, 0, 1, 0]
        answer = binary_mult(A, B)
        self.assertEqual(answer, [0, 0, 0, 0, 1, 1, 0, 0])
        A = [0, 1, 0]
        B = [0, 0, 1]
        answer = binary_mult(A, B)
        self.assertEqual(answer, [0, 0, 0, 0, 1, 0])
        A = [0, 1, 1, 0]
        B = [1, 1, 0]
        answer = binary_mult(A, B)
        self.assertEqual(answer, [0, 1, 0, 0, 1, 0, 0])
        A = [1]
        B = [1]
        answer = binary_mult(A, B)
        self.assertEqual(answer, [1])
        A = [0, 1, 1, 0]
        B = [1, 1]
        answer = binary_mult(A, B)
        self.assertEqual(answer, [0, 1, 0, 0, 1, 0])


if __name__ == '__main__':
    unittest.main()
