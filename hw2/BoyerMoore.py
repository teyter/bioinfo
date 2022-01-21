def BM(P,T):
    m = len(T)
    n = len(P)
    for i in range(m-n+1):
        t = T[i:i+n]
        for j in range(-1,n-1,-1):
            if t[j] != p[j] and t[j] not in p:
                i = i+n
                return 0

def BMM(P,T):
    m = len(T)
    n = len(P)
    i = 0
    while i < m-n+1:
        t = T[i:i+n]
        j = n-1
        count = 0
        while j >= 0:
            tj = t[j]
            pj = P[j]
            if tj != pj and tj not in P:
                i = i+j
                j-=1
                break
            if tj != pj and tj in P:
                j-=1
            if tj == pj:
                if count == n-1:
                    return i
                j-=1
                count+=1
        i+=1
    return -1
        

a = "a"
b = "b"
m = 5
n = 3
T = (a*m)+(b*n)
P = (a*n)+(b*n)
print(BMM(P,T))

