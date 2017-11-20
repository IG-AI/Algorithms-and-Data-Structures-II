#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 2: Search String Replacement

Team Number: 13
Student Names: Daniel Ågstrand, Linnea Andersson
'''
import unittest

# Sample matrix provided by us:
from string import ascii_lowercase

def padding(u, r):
    n = abs(len(u) - len(r))
    if len(u) > len(r):
        for i in range(n):
            r = r + '-'
    else:
        for i in range(n):
            u = u + '-'
    return (u, r)


def difference(u,r,R):
    """
    Sig:    string, string, int[0..|A|, 0..|A|] ==> int
    Pre:    
    Post:    
    Example: Let R be the resemblance matrix where every change and skip costs 1
             difference("dinamck","dynamic",R) ==> 3
    """
    if len(u) != len(r):
        temp = padding(u, r)
        u = temp[0]
        r = temp[1]
    c = 0
    print R['s']['p']
    temp = difference_aux(u,r,c,R)
    return temp


def difference_align(u,r,R):
    if len(u) != len(r):
        temp = padding(u, r)
        u = temp[0]
        r = temp[1]
    else:
        c = 0
        temp = difference_align_aux(u,r,c,R)
    return temp


# Solution to part b:
def difference_aux(u,r,c,R):
    """
    Sig:    string, string, int[0..|A|, 0..|A|] ==> int
    Pre:    
    Post:    
    Example: Let R be the resemblance matrix where every change and skip costs 1
             difference("dinamck","dynamic",R) ==> 3
    """
    # To get the resemblance between two letters, use code like this:
    # difference = R['a']['b']

    rn = len(r) - 1
    un = len(u) - 1
    u = list(u)
    r = list(r)
    print u
    print r
    print c
    if rn == 0:
        print c + R[u[un]][r[rn]]
        return c + R[u[un]][r[rn]]
    elif un == 0 and rn != 0:
        return float("inf")
    elif un == 0:
        return c + R[u[un]][r[rn]]
    elif r[rn] == '-' and u[un] != '-':
        r.pop()
        return difference_aux(u,r,c,R)
    elif r[rn] == u[un]:
        r.pop()
        u.pop()
        return difference_aux(u,r,c,R)
    else:
        tempr = list(r)
        cost = R[u[un]][r[rn]]
        r.pop()
        u.pop()
        return min(difference_aux(u,tempr,c+1,R), difference_aux(u,r,c+cost,R))


# Solution to part c:
def difference_align_aux(u,r,c,R):
    """
    Sig:    string, string, int[0..|A|, 0..|A|] ==> int, string, string
    Pre:    
    Post:    
    Example: Let R be the resemblance matrix where every change and skip costs 1
             difference_align("dinamck","dynamic",R) ==>
                                    3, "dinam-ck", "dynamic-"
    """

def qwerty_distance():
    """Generates a QWERTY Manhattan distance resemblance matrix

    Costs for letter pairs are based on the Manhattan distance of the
    corresponding keys on a standard QWERTY keyboard.
    Costs for skipping a character depends on its placement on the keyboard:
    adding a character has a higher cost for keys on the outer edges,
    deleting a character has a higher cost for keys near the middle.
oh
    Usage:
        R = qwerty_distance()
        R['a']['b']  # result: 5
    """
    from collections import defaultdict
    import math
    R = defaultdict(dict)
    R['-']['-'] = 0
    zones = ["dfghjk", "ertyuislcvbnm", "qwazxpo"]
    keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    for num, content in enumerate(zones):
        for char in content:
            R['-'][char] = num + 1
            R[char]['-'] = 3 - num
    for a in ascii_lowercase:
        rowA = None
        posA = None
        for num, content in enumerate(keyboard):
            if a in content:
                rowA = num
                posA = content.index(a)
        for b in ascii_lowercase:
            for rowB, contentB in enumerate(keyboard):
                if b in contentB:
                    R[a][b] = math.fabs(rowB - rowA) + math.fabs(posA - contentB.index(b))
    return R

class DifferenceTest(unittest.TestCase):
    """Test Suite for search string replacement problem

    Any method named "test_something" will be run when this file is
    executed. Use the sanity check as a template for adding your own test
    cases if you wish.
    (You may delete this class from your submitted solution.)
    """

    def test_diff_sanity(self):
        """Difference sanity test

        Given a simple resemblance matrix, test that the reported
        difference is the expected minimum. Do NOT assume we will always
        use this resemblance matrix when testing!
        """
        alphabet = ascii_lowercase + '-'
        # The simplest (reasonable) resemblance matrix:
        """R = dict([(
            a,
            dict([(b, (0 if a == b else 1)) for b in alphabet])
        ) for a in alphabet])"""
        R = {'-': {'-': 0, 'a': 3, 'c': 2, 'b': 2, 'e': 2, 'd': 1, 'g': 1, 'f': 1, 'i': 2, 'h': 1, 'k': 1, 'j': 1,
                         'm': 2, 'l': 2, 'o': 3, 'n': 2, 'q': 3, 'p': 3, 's': 2, 'r': 2, 'u': 2, 't': 2, 'w': 3, 'v': 2,
                         'y': 2, 'x': 3, 'z': 3},
                   'a': {'-': 1, 'a': 0.0, 'c': 3.0, 'b': 5.0, 'e': 3.0, 'd': 2.0, 'g': 4.0, 'f': 3.0, 'i': 8.0,
                         'h': 5.0, 'k': 7.0, 'j': 6.0, 'm': 7.0, 'l': 8.0, 'o': 9.0, 'n': 6.0, 'q': 1.0, 'p': 10.0,
                         's': 1.0, 'r': 4.0, 'u': 7.0, 't': 5.0, 'w': 2.0, 'v': 4.0, 'y': 6.0, 'x': 2.0, 'z': 1.0},
                   'c': {'-': 2, 'a': 3.0, 'c': 0.0, 'b': 2.0, 'e': 2.0, 'd': 1.0, 'g': 3.0, 'f': 2.0, 'i': 7.0,
                         'h': 4.0, 'k': 6.0, 'j': 5.0, 'm': 4.0, 'l': 7.0, 'o': 8.0, 'n': 3.0, 'q': 4.0, 'p': 9.0,
                         's': 2.0, 'r': 3.0, 'u': 6.0, 't': 4.0, 'w': 3.0, 'v': 1.0, 'y': 5.0, 'x': 1.0, 'z': 2.0},
                   'b': {'-': 2, 'a': 5.0, 'c': 2.0, 'b': 0.0, 'e': 4.0, 'd': 3.0, 'g': 1.0, 'f': 2.0, 'i': 5.0,
                         'h': 2.0, 'k': 4.0, 'j': 3.0, 'm': 2.0, 'l': 5.0, 'o': 6.0, 'n': 1.0, 'q': 6.0, 'p': 7.0,
                         's': 4.0, 'r': 3.0, 'u': 4.0, 't': 2.0, 'w': 5.0, 'v': 1.0, 'y': 3.0, 'x': 3.0, 'z': 4.0},
                   'e': {'-': 2, 'a': 3.0, 'c': 2.0, 'b': 4.0, 'e': 0.0, 'd': 1.0, 'g': 3.0, 'f': 2.0, 'i': 5.0,
                         'h': 4.0, 'k': 6.0, 'j': 5.0, 'm': 6.0, 'l': 7.0, 'o': 6.0, 'n': 5.0, 'q': 2.0, 'p': 7.0,
                         's': 2.0, 'r': 1.0, 'u': 4.0, 't': 2.0, 'w': 1.0, 'v': 3.0, 'y': 3.0, 'x': 3.0, 'z': 4.0},
                   'd': {'-': 3, 'a': 2.0, 'c': 1.0, 'b': 3.0, 'e': 1.0, 'd': 0.0, 'g': 2.0, 'f': 1.0, 'i': 6.0,
                         'h': 3.0, 'k': 5.0, 'j': 4.0, 'm': 5.0, 'l': 6.0, 'o': 7.0, 'n': 4.0, 'q': 3.0, 'p': 8.0,
                         's': 1.0, 'r': 2.0, 'u': 5.0, 't': 3.0, 'w': 2.0, 'v': 2.0, 'y': 4.0, 'x': 2.0, 'z': 3.0},
                   'g': {'-': 3, 'a': 4.0, 'c': 3.0, 'b': 1.0, 'e': 3.0, 'd': 2.0, 'g': 0.0, 'f': 1.0, 'i': 4.0,
                         'h': 1.0, 'k': 3.0, 'j': 2.0, 'm': 3.0, 'l': 4.0, 'o': 5.0, 'n': 2.0, 'q': 5.0, 'p': 6.0,
                         's': 3.0, 'r': 2.0, 'u': 3.0, 't': 1.0, 'w': 4.0, 'v': 2.0, 'y': 2.0, 'x': 4.0, 'z': 5.0},
                   'f': {'-': 3, 'a': 3.0, 'c': 2.0, 'b': 2.0, 'e': 2.0, 'd': 1.0, 'g': 1.0, 'f': 0.0, 'i': 5.0,
                         'h': 2.0, 'k': 4.0, 'j': 3.0, 'm': 4.0, 'l': 5.0, 'o': 6.0, 'n': 3.0, 'q': 4.0, 'p': 7.0,
                         's': 2.0, 'r': 1.0, 'u': 4.0, 't': 2.0, 'w': 3.0, 'v': 1.0, 'y': 3.0, 'x': 3.0, 'z': 4.0},
                   'i': {'-': 2, 'a': 8.0, 'c': 7.0, 'b': 5.0, 'e': 5.0, 'd': 6.0, 'g': 4.0, 'f': 5.0, 'i': 0.0,
                         'h': 3.0, 'k': 1.0, 'j': 2.0, 'm': 3.0, 'l': 2.0, 'o': 1.0, 'n': 4.0, 'q': 7.0, 'p': 2.0,
                         's': 7.0, 'r': 4.0, 'u': 1.0, 't': 3.0, 'w': 6.0, 'v': 6.0, 'y': 2.0, 'x': 8.0, 'z': 9.0},
                   'h': {'-': 3, 'a': 5.0, 'c': 4.0, 'b': 2.0, 'e': 4.0, 'd': 3.0, 'g': 1.0, 'f': 2.0, 'i': 3.0,
                         'h': 0.0, 'k': 2.0, 'j': 1.0, 'm': 2.0, 'l': 3.0, 'o': 4.0, 'n': 1.0, 'q': 6.0, 'p': 5.0,
                         's': 4.0, 'r': 3.0, 'u': 2.0, 't': 2.0, 'w': 5.0, 'v': 3.0, 'y': 1.0, 'x': 5.0, 'z': 6.0},
                   'k': {'-': 3, 'a': 7.0, 'c': 6.0, 'b': 4.0, 'e': 6.0, 'd': 5.0, 'g': 3.0, 'f': 4.0, 'i': 1.0,
                         'h': 2.0, 'k': 0.0, 'j': 1.0, 'm': 2.0, 'l': 1.0, 'o': 2.0, 'n': 3.0, 'q': 8.0, 'p': 3.0,
                         's': 6.0, 'r': 5.0, 'u': 2.0, 't': 4.0, 'w': 7.0, 'v': 5.0, 'y': 3.0, 'x': 7.0, 'z': 8.0},
                   'j': {'-': 3, 'a': 6.0, 'c': 5.0, 'b': 3.0, 'e': 5.0, 'd': 4.0, 'g': 2.0, 'f': 3.0, 'i': 2.0,
                         'h': 1.0, 'k': 1.0, 'j': 0.0, 'm': 1.0, 'l': 2.0, 'o': 3.0, 'n': 2.0, 'q': 7.0, 'p': 4.0,
                         's': 5.0, 'r': 4.0, 'u': 1.0, 't': 3.0, 'w': 6.0, 'v': 4.0, 'y': 2.0, 'x': 6.0, 'z': 7.0},
                   'm': {'-': 2, 'a': 7.0, 'c': 4.0, 'b': 2.0, 'e': 6.0, 'd': 5.0, 'g': 3.0, 'f': 4.0, 'i': 3.0,
                         'h': 2.0, 'k': 2.0, 'j': 1.0, 'm': 0.0, 'l': 3.0, 'o': 4.0, 'n': 1.0, 'q': 8.0, 'p': 5.0,
                         's': 6.0, 'r': 5.0, 'u': 2.0, 't': 4.0, 'w': 7.0, 'v': 3.0, 'y': 3.0, 'x': 5.0, 'z': 6.0},
                   'l': {'-': 2, 'a': 8.0, 'c': 7.0, 'b': 5.0, 'e': 7.0, 'd': 6.0, 'g': 4.0, 'f': 5.0, 'i': 2.0,
                         'h': 3.0, 'k': 1.0, 'j': 2.0, 'm': 3.0, 'l': 0.0, 'o': 1.0, 'n': 4.0, 'q': 9.0, 'p': 2.0,
                         's': 7.0, 'r': 6.0, 'u': 3.0, 't': 5.0, 'w': 8.0, 'v': 6.0, 'y': 4.0, 'x': 8.0, 'z': 9.0},
                   'o': {'-': 1, 'a': 9.0, 'c': 8.0, 'b': 6.0, 'e': 6.0, 'd': 7.0, 'g': 5.0, 'f': 6.0, 'i': 1.0,
                         'h': 4.0, 'k': 2.0, 'j': 3.0, 'm': 4.0, 'l': 1.0, 'o': 0.0, 'n': 5.0, 'q': 8.0, 'p': 1.0,
                         's': 8.0, 'r': 5.0, 'u': 2.0, 't': 4.0, 'w': 7.0, 'v': 7.0, 'y': 3.0, 'x': 9.0, 'z': 10.0},
                   'n': {'-': 2, 'a': 6.0, 'c': 3.0, 'b': 1.0, 'e': 5.0, 'd': 4.0, 'g': 2.0, 'f': 3.0, 'i': 4.0,
                         'h': 1.0, 'k': 3.0, 'j': 2.0, 'm': 1.0, 'l': 4.0, 'o': 5.0, 'n': 0.0, 'q': 7.0, 'p': 6.0,
                         's': 5.0, 'r': 4.0, 'u': 3.0, 't': 3.0, 'w': 6.0, 'v': 2.0, 'y': 2.0, 'x': 4.0, 'z': 5.0},
                   'q': {'-': 1, 'a': 1.0, 'c': 4.0, 'b': 6.0, 'e': 2.0, 'd': 3.0, 'g': 5.0, 'f': 4.0, 'i': 7.0,
                         'h': 6.0, 'k': 8.0, 'j': 7.0, 'm': 8.0, 'l': 9.0, 'o': 8.0, 'n': 7.0, 'q': 0.0, 'p': 9.0,
                         's': 2.0, 'r': 3.0, 'u': 6.0, 't': 4.0, 'w': 1.0, 'v': 5.0, 'y': 5.0, 'x': 3.0, 'z': 2.0},
                   'p': {'-': 1, 'a': 10.0, 'c': 9.0, 'b': 7.0, 'e': 7.0, 'd': 8.0, 'g': 6.0, 'f': 7.0, 'i': 2.0,
                         'h': 5.0, 'k': 3.0, 'j': 4.0, 'm': 5.0, 'l': 2.0, 'o': 1.0, 'n': 6.0, 'q': 9.0, 'p': 0.0,
                         's': 9.0, 'r': 6.0, 'u': 3.0, 't': 5.0, 'w': 8.0, 'v': 8.0, 'y': 4.0, 'x': 10.0, 'z': 11.0},
                   's': {'-': 2, 'a': 1.0, 'c': 2.0, 'b': 4.0, 'e': 2.0, 'd': 1.0, 'g': 3.0, 'f': 2.0, 'i': 7.0,
                         'h': 4.0, 'k': 6.0, 'j': 5.0, 'm': 6.0, 'l': 7.0, 'o': 8.0, 'n': 5.0, 'q': 2.0, 'p': 9.0,
                         's': 0.0, 'r': 3.0, 'u': 6.0, 't': 4.0, 'w': 1.0, 'v': 3.0, 'y': 5.0, 'x': 1.0, 'z': 2.0},
                   'r': {'-': 2, 'a': 4.0, 'c': 3.0, 'b': 3.0, 'e': 1.0, 'd': 2.0, 'g': 2.0, 'f': 1.0, 'i': 4.0,
                         'h': 3.0, 'k': 5.0, 'j': 4.0, 'm': 5.0, 'l': 6.0, 'o': 5.0, 'n': 4.0, 'q': 3.0, 'p': 6.0,
                         's': 3.0, 'r': 0.0, 'u': 3.0, 't': 1.0, 'w': 2.0, 'v': 2.0, 'y': 2.0, 'x': 4.0, 'z': 5.0},
                   'u': {'-': 2, 'a': 7.0, 'c': 6.0, 'b': 4.0, 'e': 4.0, 'd': 5.0, 'g': 3.0, 'f': 4.0, 'i': 1.0,
                         'h': 2.0, 'k': 2.0, 'j': 1.0, 'm': 2.0, 'l': 3.0, 'o': 2.0, 'n': 3.0, 'q': 6.0, 'p': 3.0,
                         's': 6.0, 'r': 3.0, 'u': 0.0, 't': 2.0, 'w': 5.0, 'v': 5.0, 'y': 1.0, 'x': 7.0, 'z': 8.0},
                   't': {'-': 2, 'a': 5.0, 'c': 4.0, 'b': 2.0, 'e': 2.0, 'd': 3.0, 'g': 1.0, 'f': 2.0, 'i': 3.0,
                         'h': 2.0, 'k': 4.0, 'j': 3.0, 'm': 4.0, 'l': 5.0, 'o': 4.0, 'n': 3.0, 'q': 4.0, 'p': 5.0,
                         's': 4.0, 'r': 1.0, 'u': 2.0, 't': 0.0, 'w': 3.0, 'v': 3.0, 'y': 1.0, 'x': 5.0, 'z': 6.0},
                   'w': {'-': 1, 'a': 2.0, 'c': 3.0, 'b': 5.0, 'e': 1.0, 'd': 2.0, 'g': 4.0, 'f': 3.0, 'i': 6.0,
                         'h': 5.0, 'k': 7.0, 'j': 6.0, 'm': 7.0, 'l': 8.0, 'o': 7.0, 'n': 6.0, 'q': 1.0, 'p': 8.0,
                         's': 1.0, 'r': 2.0, 'u': 5.0, 't': 3.0, 'w': 0.0, 'v': 4.0, 'y': 4.0, 'x': 2.0, 'z': 3.0},
                   'v': {'-': 2, 'a': 4.0, 'c': 1.0, 'b': 1.0, 'e': 3.0, 'd': 2.0, 'g': 2.0, 'f': 1.0, 'i': 6.0,
                         'h': 3.0, 'k': 5.0, 'j': 4.0, 'm': 3.0, 'l': 6.0, 'o': 7.0, 'n': 2.0, 'q': 5.0, 'p': 8.0,
                         's': 3.0, 'r': 2.0, 'u': 5.0, 't': 3.0, 'w': 4.0, 'v': 0.0, 'y': 4.0, 'x': 2.0, 'z': 3.0},
                   'y': {'-': 2, 'a': 6.0, 'c': 5.0, 'b': 3.0, 'e': 3.0, 'd': 4.0, 'g': 2.0, 'f': 3.0, 'i': 2.0,
                         'h': 1.0, 'k': 3.0, 'j': 2.0, 'm': 3.0, 'l': 4.0, 'o': 3.0, 'n': 2.0, 'q': 5.0, 'p': 4.0,
                         's': 5.0, 'r': 2.0, 'u': 1.0, 't': 1.0, 'w': 4.0, 'v': 4.0, 'y': 0.0, 'x': 6.0, 'z': 7.0},
                   'x': {'-': 1, 'a': 2.0, 'c': 1.0, 'b': 3.0, 'e': 3.0, 'd': 2.0, 'g': 4.0, 'f': 3.0, 'i': 8.0,
                         'h': 5.0, 'k': 7.0, 'j': 6.0, 'm': 5.0, 'l': 8.0, 'o': 9.0, 'n': 4.0, 'q': 3.0, 'p': 10.0,
                         's': 1.0, 'r': 4.0, 'u': 7.0, 't': 5.0, 'w': 2.0, 'v': 2.0, 'y': 6.0, 'x': 0.0, 'z': 1.0},
                   'z': {'-': 1, 'a': 1.0, 'c': 2.0, 'b': 4.0, 'e': 4.0, 'd': 3.0, 'g': 5.0, 'f': 4.0, 'i': 9.0,
                         'h': 6.0, 'k': 8.0, 'j': 7.0, 'm': 6.0, 'l': 9.0, 'o': 10.0, 'n': 5.0, 'q': 2.0, 'p': 11.0,
                         's': 2.0, 'r': 5.0, 'u': 8.0, 't': 6.0, 'w': 3.0, 'v': 3.0, 'y': 7.0, 'x': 1.0, 'z': 0.0}}
        self.assertEqual(difference('zmph', 'st', R),7)
    """def test_align_sanity(self):
        Simple alignment

        Passes if the returned alignment matches the expected one.
        
        alphabet = ascii_lowercase + '-'
        # QWERTY resemblance matrix:
        R = qwerty_distance();
        diff, u, r = difference_align("polynomial", "exponential", R)
        # Warning: we may (read: 'will') use another matrix!
        self.assertEqual(diff, 15)
        # Warning: there may be other optimal matchings!
        self.assertEqual(u, '--polynomial')
        self.assertEqual(r, 'expo-nential')"""
if __name__ == '__main__':
    unittest.main()
