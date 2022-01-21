# copy of solution 14
from teitlib import*


def new(): 
    with open('sampledna.txt') as f:
        dna = f.read().splitlines()
    k = 3
    best_motifs = get_slice(dna,k)
    best = Score(best_motifs)
    allF = listAllK(dna[0],k)
    final = []
    for i in range(len(allF)-1):
        ret = []
        ret.append(allF[i])
        profile = Profile(ret)
        for j in range(1,len(dna)):
            allP = listAllK(dna[j],k)
            L = [(dna[j].find(q),Pr(q,profile),q) for q in allP]
            bag = bagmax3(L)
            ret.append(min(bag)[2])
            profile = Profile(ret)
        final.append((Score(ret),ret))
        print(Score(ret),ret)

    printlist(min(final)[1])
    #bagg = bagmin2(final)
    #printlist(bagg[0][1])

new()
