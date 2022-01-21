import numpy as np
from teitlib import *

def Pr(Pattern,Profile):
    A = Profile[0]
    C = Profile[1]
    G = Profile[2]
    T = Profile[3]
    pr = 1.0
    for i in range(len(Pattern)):
        if Pattern[i] == "A":
            pr *= A[i]
        if Pattern[i] == "C":
            pr *= C[i]
        if Pattern[i] == "G":
            pr *= G[i]
        if Pattern[i] == "T":
            pr *= T[i]
    return pr

def listAllK(Text,k):
    # create list of all k patterns
    kmers = []
    for i in range(len(Text)-k+1):
        kmers.append( Text[i:i+k] )
    return kmers

def sample():
    matrix = np.loadtxt('matrix.txt')
    text = "TCGGGGGAGCTGTTTACAAGTGGGTTTTGGCGAAGGTGTGAGTTTGGTGAGTACAACGAGTTACCGCTGGAAGGTTTAAAGCTAACCTAGCGATACAGACAATCATTCGCTATCATAATACCTCGTTTCATGGAAATAAAGTCCCGCATGAGGCAAAACTAGCAGTGTCGCCTAGGTGACATTCTATTACCGCCTCTTCT"
    k = matrix.shape[1]
    allP = listAllK(text,k)
    printlist(allP)
    L = [(Pr(i,matrix),i) for i in allP]
    printlist(L)
    printlist(max(L))

sample()
