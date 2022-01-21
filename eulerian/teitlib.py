from math import floor

def oneline(result):
    print(' '.join(map(str,result)))

def string(li):
    return ''.join(map(str,li))

def printlst(lst):
    for i in lst: print(i)

def printdict(dct):
    for key, value in dct.items():
        print(key, '->', value)

def path_output(lst):
    print( '->'.join(map(str,lst)))

def path_outputV(lst):
    return( '->'.join(map(str,lst)))

def listAllK(Text,k):
    # create list of all k patterns
    kmers = []
    for i in range(len(Text)-k+1):
        kmers.append( Text[i:i+k] )
    return kmers

def most_freq(kmers):
    # create list with frequency of patterns
    lit = [(kmers.count(i),i) for i in kmers]
    # delete duplicates and return
    return list(dict.fromkeys(lit))

def bagmax(tli):
    ret = []
    currentMax = 0
    for i in range(len(tli)):
        nr = tli[i][0]
        item = tli[i][1]
        allt = tli[i] # debug, sja nr og item
        if nr > currentMax:
            currentMax = nr
            ret.clear()
            ret.append(item)
        elif nr == currentMax:
            ret.append(item)
    return ret

def bagmin(tli):
    ret = []
    currentMin = 99
    for i in range(len(tli)):
        nr = tli[i][0]
        item = tli[i][1]
        allt = tli[i] # debug
        if nr < currentMin:
            currentMin = nr
            ret.clear()
            ret.append(item)
        elif nr == currentMin:
            ret.append(item)
    return ret

def bagmax2(tli):
    ret = []
    currentMax = max(tli)[0]

def listmin(tli):
    ret = []
    minn = min(tli)[0]
    for i in tli:
        nr = i[0]
        item = i[1]
        if nr == minn:
            ret.append(item)
    return ret

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
    L = [(CountD1(Text,AllPatterns[i],d), AllPatterns[i]) for i in range(len(AllPatterns))]
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

def xparse(lst):
    ret = []
    for i in lst:
        lraw, rraw = i.split(" -> ", 1)
        left = int(lraw)
        nraw = rraw.split(",")
        right = [int(i) for i in nraw]
        ret.append((left,right))
    return dict(ret)

def sparse(lst):
    ret = []
    for i in lst:
        lraw, rraw = i.split(" -> ", 1)
        left = lraw
        nraw = rraw.split(",")
        right = [i for i in nraw]
        ret.append((left,right))
    return dict(ret)

def reconstruct(kmers):
    ret = []
    for i in range(len(kmers)):
        ret[i:] = list(kmers[i])
    return string(ret)
