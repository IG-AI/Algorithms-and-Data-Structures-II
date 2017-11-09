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
    global B
    A = [[None for i in range(t + 1)] for j in range(n + 1)]
    B = [None for i in range(t+1)]
    return birthday_present_aux(P, n, t)


def birthday_present_aux(P, n, t):
    if (n == 0) and (t == 0):
        A[n-1][t] = True
        return A[n-1][t]
    elif t == 0:
        A[n-1][t] = True
        return A[n-1][t]
    elif (n == 0):
        return False
    elif P[n-1] > t:
      if A[n-1][t] == None:
         A[n-1][t] = birthday_present_aux(P, n-1, t)
      return A[n-1][t]
    else:
      if A[n-1][t] == None:
         A[n-1][t] = birthday_present_aux(P, n-1, t)
      if A[n-1][t-P[n-1]] == None:
         A[n-1][t-P[n-1]] = birthday_present_aux(P,n-1,t-P[n-1])
      if A[n-1][t-P[n-1]] == True:
         B[t-P[n-1]] = P[n-1]
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
    '''
    Sig: int[0..n-1], int, int --> int[0..m]
    Pre: 
    Post: 
    Example: P = [2, 32, 234, 35, 12332, 1, 7, 56]
             birthday_present_subset(P, len(P), 299) = [56, 7, 234, 2]
             birthday_present_subset(P, len(P), 11) = []
    '''
    D = []
    i = 1
    cut = True
    if birthday_present(P, n, t) == False:
        return []
    else:
        if (t in P):
            return [t]
        else:
            E = filter(None, B)
            E.sort()
            D.append(E[0])
            while i<=(len(E) - 1):
                C = E[0] + E[i]
                if C == t:
                    D.append(E[i])
                    return D
                i = i + 1

print(birthday_present_subset([8,1,2,4,6],4,7))



