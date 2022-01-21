import numpy as np

n=100
N = np.arange(n)
B = [True for i in N]
B[0] = False
B[1] = False
for i in range(2,n):
    for j in range(i+1,n):
        if N[j] % N[i] == 0:
             B[j] = False
print(N[B])
