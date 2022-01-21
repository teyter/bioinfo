from math import floor
from time import time

start = time()

def string(li):
    return ''.join(map(str,li))
def printlist(li):
    for i in li:
        print(i)

def bruteforce(k):
    a = ["A","C","G","T"]
    b = [i for i in range(k-1,-1,-1)]
    ret = []
    base = len(a)
    sic = base**k
    for i in range(sic):
        s = []
        for j in range(k):
            x = floor(i/base**b[j]) % base 
            s.append(a[x])
        s = string(s)
        ret.append(s)
    return ret
    
k = 2
#pr = bruteforce(k)
printlist(pr)

# time
end = time()
secs = end-start
t = end-start
#print(t,"seconds")
