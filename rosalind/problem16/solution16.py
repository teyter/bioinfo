#copy of solution 15
from teitlib import*
from random import randint
from time import time

start = time()

def random_motifs(dna,k,t):
    motifs = []
    for j in range(t):
        allK = listAllK(dna[j],k)
        ayn = randint(0,len(allK)-1)
        motifs.append(allK[ayn])
    return motifs

def get_motifs_from_profile(dna,k,t,profile):
        motifs = []
        for j in range(t):
            allP = listAllK(dna[j],k)
            L = [(dna[j].find(q),Pr(q,profile),q) for q in allP]
            bag = bagmax3(L)
            motifs.append(min(bag)[2])
        return motifs

def new(): 
    with open('sampledna.txt') as f:
        dna = f.read().splitlines()
    k = 8
    final = []
    motifs = random_motifs(dna,k,len(dna))
    for i in range(1000):
        # get motifs
        motifs = random_motifs(dna,k,len(dna))
        profile = Profile(motifs)
        ret = get_motifs_from_profile(dna,k,len(dna),profile)

        final.append([Score(ret),ret])
    bagg = bagmin2(final)
    for i in bagg:
        offset = dna[0].find(i[1][0])
        i[0] += offset
    printlist(min(bagg)[1])

new()

end = time()
#print(end-start,"secs")
