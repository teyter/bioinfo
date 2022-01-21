from math import floor

def string(li):
    s = ""
    for i in li:
        s += i
    return s

def printlist(li):
    for i in li:
        print(i)

def bruteforce(k):
    a = ["0","1","2","3"]
    b = [i for i in range(k-1,-1,-1)]
    ret = []
    base = len(a)
    sic = base**k
    for i in range(sic):
        s = []
        for j in range(k):
            x = floor(i/base**b[j]) % base 
            s.append(int(a[x]))
        ret.append(s)
    return ret

x = (bruteforce(4))
t = []
for i in range(len(x)):
    t.append( (((x[i][0]*4**3+x[i][1]*4**2+x[i][2]*4**1+x[i][3]*4**0) % 64),x[i]) )

printlist(t)
