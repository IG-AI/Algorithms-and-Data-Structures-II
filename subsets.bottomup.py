

def birthday_present_subset(P,n,t):
    global A
    A = [[None for i in range(t+1)] for j in range(n+1)]
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



print(birthday_present_subset([3,2,7,1],4,5))   
print(A)     	

   


