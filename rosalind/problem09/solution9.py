import numpy as np

#allData = np.loadtxt('rosalind_ba1h.txt',dtype='str')
allData = np.loadtxt('sample10.txt',dtype='str')
pattern = allData[0]
text = allData[1]
d = int(allData[2])

def hamming_distance(p,q):
    hd = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hd += 1
    return hd

def approx(p,t,d):
    ret = []
    k = len(p)
    for i in range(len(t)-k):
        x = hamming_distance(t[i:i+len(p)],p)
        if x <= d:
            ret.append(i)
    return ret


def oneline(li):
    print(' '.join(map(str,li)))

y = approx(pattern,text,d)

oneline(y)

