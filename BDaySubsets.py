n=7
t=6
A = [[None for i in range(n)] for j in range(t+1)]
B = [None for i in range(t+1)]

def birthday_present(P,n,t):
    if (n == 0) and (t == 0):
        A[t][n-1] = True
        return A[t][n-1]
    if (n == 0):
        return False
    elif t == 0:
        A[t][n-1] = True
        return A[t][n-1]
    elif P[n-1] > t:
      if A[t][n-1] is None:
         A[t][n-1] = birthday_present(P, n-1, t)
      return A[t][n-1]
    else:
      if A[t][n-1] is None:
         A[t][n-1] = birthday_present(P, n-1, t)
      if A[t-P[n-1]][n-1] is None:
         A[t-P[n-1]][n-1] = birthday_present(P,n-1,t-P[n-1])
      if A[t-P[n-1]][n-1] == True:
         B[t-P[n-1]] = P[n-1]
    return A[t][n-1] or A[t-P[n-1]][n-1]


print(birthday_present([9,3,1,4,8,2,12],7,6))
print(B)
