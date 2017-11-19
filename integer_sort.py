#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Integer Sort

Team Number: 13
Student Names: Daniel Ågstrand, Linnea Andersson
'''
import unittest


def integer_sort(A, k):
    '''
    Sig:  int array[1..n], int -> int array[1..n]
    Pre:  k has to be bigger or equal to zero, max(A) <= k
    Post: A is an increasingly sorted list 
    Example: integer_sort([5, 3, 6, 7, 12, 3, 6, 1, 4, 7]), 12) = 
                 [1, 3, 3, 4, 5, 6, 6, 7, 7, 12]
    '''
    # Initialize the help list, Y
    # Type: int[0] * (k + 1)
    Y = ([0] * (k + 1))

    for i in range(len(A)):
        # Variant: len(A) - i
        for x in range(len(Y)):
            # Variant: len(Ý) - x
            if A[i] == x:
                Y[x] = Y[x] + 1

    i = 0
    for x in range(len(Y)):
        # Variant: len(Y) - x
        for t in range(len(A)):
            # Variant: len(A) - t
            if Y[x] == t and t > 0:
                for j in range(t):
                    # Variant: t - j
                    A[i] = x
                    i = i + 1

    return A
