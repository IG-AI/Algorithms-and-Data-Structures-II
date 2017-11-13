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
    Sig: int[0..n-1], int, int --> Boolean
    Pre:
    Post:
    Example: P = [2, 32, 234, 35, 12332, 1, 7, 56]
             birthday_present(P, len(P), 299) = True
             birthday_present(P, len(P), 11) = False
    '''
    # Initialize the dynamic programming matrix, A
    # Type: Boolean[0..n][0..t]
    global A
    A = [[None for i in range(t + 1)] for j in range(n + 1)]
    return birthday_present_aux(P, n, t)


def birthday_present_aux(P, n, t):
    if n == 0 and t == 0:
        A[n-1][t] = True
        return A[n-1][t]
    if n == 0:
        return False
    elif t == 0:
        A[n-1][t] = True
        return A[n-1][t]
    elif P[n-1] > t:
      if A[n-1][t] is None:
         A[n-1][t] = birthday_present_aux(P, n-1, t)
      return A[n-1][t]
    else:
      if A[n-1][t] is None:
         A[n-1][t] = birthday_present_aux(P, n-1, t)
      if A[n-1][t-P[n-1]] is None:
         A[n-1][t-P[n-1]] = birthday_present_aux(P,n-1,t-P[n-1])
    return A[n-1][t] or A[n-1][t-P[n-1]]


def birthday_present_subset(P, n, t):
    '''
    Sig: int[0..n-1], int, int --> int[0..m]
    Pre: 
    Post: 
    Example: P = [2, 32, 234, 35, 12332, 1, 7, 56]
             birthday_present_subset(P, len(P), 299) = [56, 7, 234, 2]
             birthday_present_subset(P, len(P), 11) = []
    '''
    R = []

    for i in range(t+1):
    	for j in range(n+1):
    	 if i == 0 and j == 0:
    		A[j][i] = True
    	 elif i == 0:
    		A[j][i] = True
    	 elif j == 0:
    		A[j][i] = False
    	 elif P[j-1] > i:
    		A[j][i] = A[j-1][i]
    	 else:
    		A[j][i] = A[j-1][i] or A[j-1][i-P[j-1]]
    while True:
      i = 0
      while A[i][t - sum(R)] == False:
    	i = i + 1
      R.append(P[i-1])
      if t == sum(R):
        return R


class BirthdayPresentTest(unittest.TestCase):
    """Test Suite for birthday present problem
    
    Any method named "test_something" will be run when this file is 
    executed. Use the sanity check as a template for adding your own 
    tests if you wish. 
    (You may delete this class from your submitted solution.)
    """
    
    def test_sat_sanity(self):
        """Sanity Test for birthday_present()
        
        This is a simple sanity check;
        passing is not a guarantee of correctness.
        """
        P = [2, 32, 234, 35, 12332, 1, 7, 56]
        n = len(P)
        t = 11
        self.assertFalse(birthday_present(P, n, t))
    def test_sol_sanity(self):
        """Sanity Test for birthday_present_subset()
        
        This is a simple sanity check;
        passing is not a guarantee of correctness.
        """
        P = [2, 32, 234, 35, 12332, 1, 7, 56]
        n = len(P)
        t = 299
        self.assertTrue(birthday_present(P, n, t))
        self.assertItemsEqual(birthday_present_subset(P, n, t), 
                              [56, 7, 234, 2])

        
if __name__ == '__main__':
    unittest.main()
