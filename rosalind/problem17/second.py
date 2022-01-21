from teitlib import *
from random import randint
import numpy as np

def Twenty(dna,k,t,N):
    i = 0
    best_motifs = [k * t, None]
    while i < 20:
        motifs = GibbsSampler(dna,k,t,N)
        if motifs[0] < best_motifs[0]:
            bestmotifs = motifs
        i = i+1
    return bestmotifs

def pla(dna, k, prof):
    nuc_loc = {nucleotide: index for index, nucleotide in enumerate('ACGT')}
    probs = []
    prof = transpose_matrix(prof)
    for i in range(len(dna) - k):
        current_prob = 1.
        for j, nucleotide in enumerate(dna[i:i + k]):
            current_prob *= prof[j][nuc_loc[nucleotide]]
        probs.append(current_prob)
    i = np.random.choice(len(probs), p = np.array(probs) / np.sum(probs))
    return dna[i:i + k]

def GibbsSampler(dna,k,t,N):
    motifs = random_motifs(dna,k,t)
    best_score = [Score(motifs), motifs]
    for j in range(N):
        i = randint(0,t-1)
        profile = Profile(motifs[0:i]+motifs[i+1:len(motifs)])
        #motifs = bla(dna[i],profile,k,i,motifs)
        motifs[i] = fla(dna[i],profile,k)
        if Score(motifs) < best_score[0]:
            best_score = [Score(motifs), motifs]
    return best_score

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
    choice = np.random.choice(lst,p=p)
    return choice

def main():
    data = "".join(open('sample.txt')).split()
    k = int(data[0])
    t = int(data[1])
    N = int(data[2])
    dna = data[3:]
    result = Twenty(dna,k,t,N)
    printlist(result[1])

main()
