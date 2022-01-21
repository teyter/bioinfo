from teitlib import*
from random import randint
from time import time

start = time()
def OneThousand(dna,k,t):
    i = 0
    xbestmotifs = random_motifs(dna,k,t)
    while i < 1000:
        motifs = RandomizedMotifSearch(dna,k,t)
        if Score(motifs) < Score(xbestmotifs):
            xbestmotifs = motifs
            print("master",xbestmotifs)
        i = i+1
    return xbestmotifs

def RandomizedMotifSearch(dna,k,t):
    motifs = random_motifs(dna,k,t)
    bestmotifs = motifs
    while True:
        profile = Profile(motifs)
        motifs = get_motifs_from_profile(dna,k,t,profile)
        if Score(motifs) < Score(bestmotifs):
            bestmotifs = motifs
        else:
            return bestmotifs

def get_motifs_from_profile(dna,k,t,profile):
        motifs = []
        for j in range(t):
            allP = listAllK(dna[j],k)
            L = [(dna[j].find(q),Pr(q,profile),q) for q in allP]
            bag = bagmax3(L)
            motifs.append(min(bag)[2])
        return motifs

def random_motifs(dna,k,t):
    motifs = []
    for j in range(t):
        allK = listAllK(dna[j],k)
        ayn = randint(0,len(allK)-1)
        motifs.append(allK[ayn])
    return motifs

def random_motif(dnaline,k):
    allK = listAllK(dnaline,k)
    ayn = randint(0,len(allK)-1)
    motif = allK[ayn]
    return motif

def main(): 
    with open('sampledna.txt') as f:
        dna = f.read().splitlines()
    k = 8
    t = len(dna)
    printlist(OneThousand(dna,k,t))

main()

end = time()
#print(end-start,"secs")
