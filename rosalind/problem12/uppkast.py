from teitlib import *

def d(Pattern,Text):
    k = len(p)
    count = 0
    hd = []
    for i in range(len(t)-k+1):
        x = t[i:i+k]
        hd.append( get_hammingdistance(x,p) )
    return min(hd)

def dd(Pattern,Dna):
    ret = []
    for i in range(len(Dna)):
        ret.append(d(Pattern,Dna[i]))
    return sum(ret)

p = "ACGT"
t = "AAATTGACGCAT"
dna = [
"AAATTGACGCAT",
"GACGACCACGTT",
"CGTCAGCGCCTG",
"GCTGAGCACCGG",
"AGTACGGGACAG",
]

print(dd(p,dna))
