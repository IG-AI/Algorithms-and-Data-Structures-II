import numpy as np

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

print(birthday_present([8,1,2,4,6],4,7))
print(np.matrix(A))


