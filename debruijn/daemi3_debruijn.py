from teitlib import *

T = "ATCATTCCATCGCATTCTG"

def reconstruct(kmers):
    ret = []
    for i in range(len(kmers)):
        ret[i:] = list(kmers[i])
    return string(ret)

def printdict(dct):
    for key, value in dct.items():
        print(key, '->', ','.join(value))

def allK(Text,k):
    return [Text[i:i+k] for i in range(len(Text)-k+1)]

def r(dct):
    for v in dct.values():
        v = dict.fromkeys(v)
    return dct

def prof():
    k = 3
    printlst(allK(T,k))
    print()
    x = DeBruijnGraph(allK(T,k))
    printdict(x)
    print()
    y = path(x)
    z = reconstruct(y)
    print()
    print(z)

def prof2020():
    with open('prof.txt') as f:
        data = f.read().splitlines()
    adj = sparse(data) 
    printdict(adj)
    x = path(adj)
    p = (reconstruct(x))

    k = 5
    printlst(allK(p,k))
    print()
    x = DeBruijnGraph(allK(p,k))
    printdict(x)
    print()
    y = path(x)
    z = reconstruct(y)
    print()
    print(z)
    print(p)
    

prof2020()
