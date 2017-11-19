#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 1: Birthday Present

Team Number: 13
Student Names: Daniel Ågstrand, Linnea Andersson
'''
import unittest


def birthday_present(P, n, t):
    '''
    Sig:  int[0..n-1], int, int --> Boolean
    Pre:  Elements in P must be > 0
    Post: Returns true if there exist elements in P
          whose sum is t, otherwise false
    Example: P = [2, 32, 234, 35, 12332, 1, 7, 56]
             birthday_present(P, len(P), 299) = True
             birthday_present(P, len(P), 11) = False
    '''
    # Initialize the dynamic programming matrix, A
    # Type: Boolean[0..n][0..t]
    global A
    if t <= 0:
        return False
    A = [[None for i in range(t + 1)] for j in range(n + 1)]
    return birthday_present_aux(P, n, t)


def birthday_present_aux(P, n, t):
    '''
    Sig:  int[0..n-1], int, int --> Boolean
    Pre:  Elements in P must be > 0
    Post: Returns true if there exist elements in P
          whose sum is t, otherwise false
    Var:  n-1, t or t-P[n-1]
    Example: P = [2, 32, 234, 35, 12332, 1, 7, 56]
             birthday_present(P, len(P), 299) = True
             birthday_present(P, len(P), 11) = False
    '''
    if n == 0 and t == 0:
        A[n - 1][t] = True
        return A[n - 1][t]
    if n == 0:
        return False
    elif t == 0:
        A[n - 1][t] = True
        return A[n - 1][t]
    elif P[n - 1] > t:
        if A[n - 1][t] is None:
            A[n - 1][t] = birthday_present_aux(P, n - 1, t)
        return A[n - 1][t]
    else:
        if A[n - 1][t] is None:
            A[n - 1][t] = birthday_present_aux(P, n - 1, t)
        if A[n - 1][t - P[n - 1]] is None:
            A[n - 1][t - P[n - 1]] = birthday_present_aux(P, n - 1, t - P[n - 1])
    return A[n - 1][t] or A[n - 1][t - P[n - 1]]


def birthday_present_subset(P, n, t):
    '''
    Sig:  int[0..n-1], int, int --> int[0..m]
    Pre:  Elements in P must be > 0
    Post: Returns a list of elements whose sum is t
    Example: P = [2, 32, 234, 35, 12332, 1, 7, 56]
             birthday_present_subset(P, len(P), 299) = [56, 7, 234, 2]
             birthday_present_subset(P, len(P), 11) = []
    '''
    # Initialize return list, R
    # Type: int[0..n]
    R = []
    # Initialize the dynamic programming matrix, A
    # Type: Boolean[0..n][0..t]
    A = [[None for i in range(t + 1)] for j in range(n + 1)]
    if t <= 0:
        return R

    for i in range(t + 1):
        # Variant: (t+1) - i
        for j in range(n + 1):
            # Variant: (n+1) - j
            if i == 0 and j == 0:
                A[j][i] = True
            elif i == 0:
                A[j][i] = True
            elif j == 0:
                A[j][i] = False
            elif P[j - 1] > i:
                A[j][i] = A[j - 1][i]
            else:
                A[j][i] = A[j - 1][i] or A[j - 1][i - P[j - 1]]
    if A[n][t] == False:
        return R
    while True:
        # Variant: none
        i = 0
        while A[i][t - sum(R)] == False:
            # Variant: A[i][t - sum(R)] - i
            i = i + 1
        R.append(P[i - 1])
        if t == sum(R):
            return R