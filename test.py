import unittest

global A


def birthday_present(P, n, t):
    global A    
    A = [[None for i in range(t + 1)] for j in range(n + 1)]
    return birthday_present_aux(P, n, t)


def birthday_present_aux(P, n, t):
    print A
    print "---------------------------"
    print len(A)
    if (n == 0) and (t == 0):
        return True
    if (n == 0):
        return False
    elif (t == 0):
        return false
    elif (P[n-1] > t):
        if A[n][t] == None:
            A[n][t] = t
            return birthday_present_aux(P, n-1, t)
        else:
            return A[t][n]
    else:
        if A[n][t] == None:
            A[n][t] = t
            return birthday_present_aux(P, n-1, t) or birthday_present_aux(P,n-1,t-P[n-1])
        else:
            return A[n][t]

print(birthday_present([2,2,3,4],4,6))
print A
#print(birthday_present([11,33,22,100,2,36,5],7,220))
#print(birthday_present([1,3,7,8],4,11))

