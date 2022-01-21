from teitlib import *
import numpy as np

sample_m = np.loadtxt('sample_matrix.txt')
sampletext = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"

m = np.loadtxt('matrix.txt')
text = "CTTACCGAGTTCCCTGCCGTCGCATCAGCTACGAAGATTCAGATGAATGCCTCGTCCTATTGACACTCCTAACCGCTGGCAGTTGCCTCACCACGTCGTTCGCCATTTCGAACAATTCGCCTGACGTACCTTACAAATAATAGTTCCGATCTGCGGGGTGTATAACGGTAGATCCAATCGTAATATGACGTGGACACCCC"

# debug test
m = np.loadtxt('debug_matrix.txt')
text = "AGCAGCTTTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATCTGAACTGGTTACCTGCCGTGAGTAAAT"


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

def get_altpatterns(t,p):
    k = len(p)
    count = []
    for i in range(len(t)-k+1):
        pt = t[i:i+k]
        x = get_hammingdistance(pt,p)
        count.append(x)
    minnst = min(count)
    print(count)
    print(minnst)
    ret = []
    for i in range(len(t)-k+1):
        pt = t[i:i+k]
        x = get_hammingdistance(pt,p)
        if x == minnst:
            print(pt,"pt")
            print(p,"p")
            ret.append(exer(pt,p))
    return ret
    
def get_mininum_hamming_distance(t,p):
    k = len(p)
    count = []
    for i in range(len(t)-k+1):
        pt = t[i:i+k]
        x = get_hammingdistance(pt,p)
        count.append(x)
    return min(count)

def letter(vector):
    dic = {
       vector[0] : "A",
       vector[1] : "C",
       vector[2] : "G",
       vector[3] : "T"
    }
    return dic[max(vector)]

def kmer(matrix):
    mt = matrix.T
    string = ""
    for i in range(len(mt)):
        string += letter(mt[i])
    return string

def check_kmer(matrix,text):
    pattern = kmer(matrix)
    if text.find(pattern) >= 0:
        return pattern
    else:
        alt_patterns= get_altpatterns(text,pattern)
        printlist(alt_patterns)
        for i in alt_patterns:
            if text.find(i) >= 0:
                print(i)
                return i
def test()
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
    hx = get_hamminginsex)
