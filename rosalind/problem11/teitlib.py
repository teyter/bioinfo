from math import floor

def oneline(result):
    print(' '.join(map(str,result)))

def string(li):
    return ''.join(map(str,li))

def printlist(li):
    for i in li:
        print(i)

def get_hammingdistance(p,q):
    hd = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hd += 1
    return hd

def CountD(t,p,d):
    k = len(p)
    count = 0
    for i in range(len(t)-k+1):
        x = get_hammingdistance(t[i:i+k],p)
        if x <= d:
            count+=1
    return count

def CountD1(t,p,d):
    k = len(p)
    count = 0
    for i in range(len(t)-k+1):
        x = get_hammingdistance(t[i:i+k],p)
        if x <= d:
            count = 1
    return count

def get_hamminglist(Text,AllPatterns,d):
    # god forgive me
    L = [(CountD1(Text,i,d), i) for i in AllPatterns]
    return list(dict.fromkeys(L))

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
