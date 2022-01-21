import numpy as np
from teitlib import *


def string(li):
    return ''.join(map(str,li))
def patternExists(Text,Pattern):
    return Text.find(Pattern) >= 0

def putin(Text,Pattern):
    while not patternExists(Text,Pattern):
        return 0

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

def get_hammingindex(t,p):
    k = len(p)
    count = []
    for i in range(len(t)-k+1):
        pt = t[i:i+k]
        x = get_hammingdistance(pt,p)
        count.append(x)
    minnst = min(count)
    ret = []
    for i in range(len(t)-k+1):
        pt = t[i:i+k]
        x = get_hammingdistance(pt,p)
        if x == minnst:
            ret.append(exer(pt,p))
    return ret
    
def edit_matrix(string,matrix):
    acgt = "acgt"
    i = 0
    j = 0
    for y in range(len(string)):
        i = y
        letter = string[y]
        index = acgt.find(letter)
        if index >= 0:
            j = index
            matrix[i][j] = 0.0
    return matrix


def letter(vector):
    dic = {
       vector[0] : "A",
       vector[1] : "C",
       vector[2] : "G",
       vector[3] : "T"
    }
    return dic[max(vector)]

def kmer(matrix):
    string = ""
    for i in range(len(matrix)):
        string += letter(matrix[i])
    return string

def debug():
    # debug test
    matrix = np.loadtxt('debug_matrix.txt').T
    text = "AGCAGCTTTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATCTGAACTGGTTACCTGCCGTGAGTAAAT"
    pattern = kmer(matrix)
    print(pattern)
    if patternExists(text,pattern):
        return pattern
    else:
        alt_patterns= get_hammingindex(text,pattern)
        print("AGCAGCTT goal")
        print(alt_patterns[0])
        alt_patterns.reverse() # debug
#       print(alt_patterns)
        for i in alt_patterns:
            edit_matrix(i,matrix)
            newpattern = kmer(matrix)
            if text.find(newpattern) >= 0:
                print(i,"winner")
                return newpattern
            else:
                edit_matrix(i,matrix)
                newpattern = kmer(matrix)
                if text.find(newpattern) >= 0:
                    print(i,"winner")
                    return newpattern
                else:
                    edit_matrix(i,matrix)
                    newpattern = kmer(matrix)
                    if text.find(newpattern) >= 0:
                        print(i,"winner")
                        return newpattern
            matrix = np.loadtxt('sample_matrix.txt').T
        return -1


def sample():
    # debug test
    print("CCGAG goals")
    matrix = np.loadtxt('sample_matrix.txt').T
    text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
    pattern = kmer(matrix)
    print(pattern)
    if patternExists(text,pattern):
        return pattern
    else:
        alt_patterns= get_hammingindex(text,pattern)
        alt_patterns.reverse() # debug
        print(alt_patterns)
        for i in alt_patterns:
            edit_matrix(i,matrix)
            newpattern = kmer(matrix)
            print(newpattern)
            if text.find(newpattern) >= 0:
                print(i,"winner")
                return newpattern
            else:
                edit_matrix(i,matrix)
                newpattern = kmer(matrix)
                if text.find(newpattern) >= 0:
                    print(i,"winner")
                    return newpattern
                else:
                    edit_matrix(i,matrix)
                    newpattern = kmer(matrix)
                    if text.find(newpattern) >= 0:
                        print(i,"winner")
                        return newpattern
            matrix = np.loadtxt('sample_matrix.txt').T


                

print(sample())
