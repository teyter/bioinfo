from teitlib import *
from random import randint
import numpy as np

def Twenty(dna,k,t,N):
    i = 0
    xbestmotifs = random_motifs(dna,k,t)
    while i < 20:
        motifs = GibbsSampler(dna,k,t,N)
        if Score(motifs) < Score(xbestmotifs):
            xbestmotifs = motifs
        i = i+1
    return xbestmotifs

def GibbsSampler(dna,k,t,N):
    motifs = random_motifs(dna,k,t)
    bestmotifs = motifs
    for j in range(N):
        i = randint(0,t-1)
        profile = Profile(motifs[0:i]+motifs[i+1:len(motifs)])
        motifs = bla(dna[i],profile,k,i,motifs)
        #motifs[i] = fla(dna[i],profile,k)
        #print(motifs == bestmotifs)
        if Score(motifs) < Score(bestmotifs):
            bestmotifs = motifs
    return bestmotifs

def bla(motif,profile,k,i,motifs):
    allK = listAllK(motif,k)
    p = [Pr(i,profile) for i in allK]
    return motifs[0:i]+[Random(allK,p)]+motifs[i+1:len(motifs)]

def fla(motif,profile,k):
    allK = listAllK(motif,k)
    p = [Pr(i,profile) for i in allK]
    return Random(allK,p)

def Random(lst,p):
    summa = sum(p)
    p = [i/summa for i in p]
    return np.random.choice(lst,p=p)

def main():
    data = "".join(open('sample.txt')).split()
    k = int(data[0])
    t = int(data[1])
    N = int(data[2])
    dna = data[3:]
    result = Twenty(dna,k,t,N)
    printlist(result)

main()
