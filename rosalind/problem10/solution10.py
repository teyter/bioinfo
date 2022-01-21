import numpy as np
from math import floor
from time import time

start = time()

def bagmax(tli):
    ret = []
    currentMax = 0
    for i in range(len(tli)):
        nr = tli[i][0]
        item = tli[i][1]
        allt = tli[i] # debug
        if nr > currentMax:
            currentMax = nr
            ret.clear()
            ret.append(allt)
        elif nr == currentMax:
            ret.append(allt)
    return ret

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

def kmers_intext(Text,k):
    AllPatterns = []
    for i in range(len(Text)-k):
        AllPatterns.append( Text[i:i+k] )
    return AllPatterns

def get_hamminglist(Text,AllPatterns,d):
    # god forgive me
    L = [(CountD(Text,AllPatterns[i],d), AllPatterns[i]) for i in range(len(AllPatterns))]
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

def real():
    #allData = np.loadtxt('sample.txt',dtype='str')
    allData = np.loadtxt('rosalind_ba1i.txt',dtype='str')
    text = allData[0]
    k = int(allData[1])
    d = int(allData[2])
    kmersText = kmers_intext(text,k)
    hlist = get_hamminglist(text,kmersText,d)
    print("existing")
    printlist(bagmax(hlist))
#   with open('k7.txt') as f:
#       allK = f.read().splitlines()
    allK = bruteforce(k)
    hlist2 = get_hamminglist(text,allK,d)
    x = bagmax(hlist2)
    print("brute")
    printlist(x)

def testdebug():
    text = "AGTCAGTC"
    k = 4
    d = 2
    kmersText = kmers_intext(text,k)
    hlist = get_hamminglist(text,kmersText,d)
    print("existing")
    printlist(bagmax(hlist))
#   with open('k4.txt') as f:
#       bruteK = f.read().splitlines()
    hlist2 = get_hamminglist(text,bruteK,d)
    winners = bagmax(hlist2)
    print("brute")
    printlist(winners)

real()

# time
end = time()
secs = end-start
print(secs,"seconds")
print(secs/60,"minutes")
