from teitlib import *
import numpy as np

def string(li):
    return ''.join(map(str,li))
def patternExists(Text,Pattern):
    return Text.find(Pattern) >= 0

def exer(p,q):
    p = list(p)
    q = list(q)
    ret = ""
    for i in range(len(p)):
        if p[i] == q[i]:
            ret += p[i]
        else:
            ret += q[i].lower()
    return ret

def get_hammingdistance(p,q):
    hd = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hd += 1
    return hd

def minham(t,p):
    k = len(p)
    count = []
    for i in range(len(t)-k+1):
        pt = t[i:i+k]
        x = get_hammingdistance(pt,p)
        count.append((x,p,pt))
    return min(count)


def steamedham(t,p):
    k = len(p)
    count = []
    for i in range(len(t)-k+1):
        pt = t[i:i+k]
        x = get_hammingdistance(pt,p)
        count.append(x)
    print(count)
    return min(count)

def test():
    m = np.loadtxt('debug_matrix.txt')
    text = "AGCAGCTTTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATCTGAACTGGTTACCTGCCGTGAGTAAAT"
    pattern = [
        "AGCAAAGC",
        "AGCAACGC",
        "AGCAATGC",
        "ATCAAAGC",
        "ATCAACGC",
        "ATCAATGC"
    ]
    HD = [minham(text,i) for i in pattern]
    printlist(HD)
#   minHD = listmin(HD)

test()
