#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Binary Multiplication

Team Number: 13
Student Names: Daniel Ågstrand, Linnea Andersson
'''
import unittest


def shift_left(l, n):
    """
    Sig:    int[0..len-1], int n ==> int[0..((len - 1) + n[0])]
    Pre:    None
    Post:   l is the same as input but with n zeros at the end
    Example:     shift_left([0,1,1], 1) = [0,1,1,0]
    """
    for i in range(n):
        #Variant: n - i
        l.append(0)
    return l


def full_adder(A, B):
    """
    Sig:    int[0..m], int[0..k] ==> int[0..n]
    Pre:    A and B cannot be zero
    Post:   Binary addition of A and B
    Example:     full_adder([1,1,1], [1,0,0]) = [1,0,1,1]
    """
    carry = 0
    alen = len(A)
    blen = len(B)
    if alen != blen:
        n = abs(alen - blen)
        if n > 0:
            if alen  > blen:
                for i in range(n):
                    #Variant: n - i
                    B.insert(0, 0)
            else:
                for i in range(n):
                    #Variant: n - i
                    A.insert(0, 0)

    newlen = len(A)
    # Initialize the return list, C
    # Type: int[0..n]
    C = [0] * newlen
    for i in range(newlen):
        #Variant: newlen - i
        if i == (newlen - 1) and (A[-i - 1] == 1 and B[-i - 1] == 1 and carry == 1):
            C[-i - 1] = 1
            C.insert(0, 1)
        elif i == (newlen - 1) and (A[-i - 1] != B[-i - 1] and carry == 1):
            C[-i - 1] = 0
            C.insert(0, 1)
        elif i == (newlen - 1) and (A[-i - 1] == 1 and B[-i - 1] == 1 and carry == 0):
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
    """
    Sig:    int[0..n-1], int[0..n-1] ==> int[0..2*n-1]
    Pre:    A and B cannot be empty
    Post:   Binary multiplication of A and B
    Example:    binary_mult([0,1,1],[1,0,0]) = [0,0,1,1,0,0]
    """
    if len(A) == 1 and len(B) == 1:
        return [A[0] * B[0]]

    finallen = len(A) + len(B)
    if len(A) != len(B):
        t = abs(len(A) - len(B))
        if len(A) > len(B):
            for i in range(t):
                #Variant: t - i
                B.insert(0, 0)
        else:
            for i in range(t):
                #Variant: t - i
                A.insert(0, 0)

    add = True
    power = 1
    newlen = len(A)
    while add:
        #Variant: add, power
        if newlen == (2 ** power):
            add = False
        if newlen < 2 ** power:
            n = 2 ** power - newlen
            for i in range(n):
                #Variant: n - i
                A.insert(0, 0)
                B.insert(0, 0)
            add = False
        else:
            power += 1

    nlen = len(A)
    # Initialize the return list, temp, from the recursive function binary_mult_aux(A, B, n)
    # Type: int[0..n]
    print len(A)
    temp = binary_mult_aux(A, B, nlen)
    n = len(temp) - finallen
    if n < 0:
        for i in range(abs(n)):
            #Variant: |n| - i
            temp.insert(0, 0)
    else:
        for i in range(n):
            #Variant: n - i
            temp.remove(0)

    return temp


def binary_mult_aux(A, B, n):
    """
    Sig:    int[0..n-1], int[0..n-1] ==> int[0..m]
    Pre:    A and B cannot be empty, A and B have equal length and ((len(A) & len(B)) % 2^k) == 0
    Post:   Binary multiplication of A and B
    Var:    n / 2, A / 2, B / 2
    Example:    binary_mult([0,1,1],[1,0,0]) = [0,0,1,1,0,0]
    """
    if n == 1:
        return [A[0] * B[0]]
    else:
        m = n - n / 2

        ah = A[:n / 2]
        al = A[n / 2:n]
        bh = B[:n / 2]
        bl = B[n / 2:n]

        x1 = binary_mult_aux(ah, bh, m)
        x2 = binary_mult_aux(al, bl, m)
        x3 = binary_mult_aux(al, bh, m)
        x4 = binary_mult_aux(ah, bl, m)

        t1 = shift_left(x1, n)
        t2 = full_adder(x3, x4)
        t3 = shift_left(t2, m)
        t4 = full_adder(t1, t3)

        final = full_adder(t4, x2)

    return final