import numpy as np
from teitlib import *

def Random(lst,p):
    summa = sum(p)
    p = [i/summa for i in p]
    return np.random.choice(lst,p=p)


lst = ["ccgc","cggc","ggcg","gcgt","cgtt"]
p = [0.1,0.2,0.4,0.7,0.3]

def profile_randomized_kmer(dna, k, prof):
    nuc_loc = {nucleotide: index for index, nucleotide in enumerate('ACGT')}
    probs = []
    for i in range(len(dna) - k):
        current_prob = 1.
        for j, nucleotide in enumerate(dna[i:i + k]):
            current_prob *= prof[j][nuc_loc[nucleotide]]
        probs.append(current_prob)

    i = np.random.choice(len(probs), p = np.array(probs) / np.sum(probs))
    return dna[i:i + k]

m = [
[1,2,3],
[4,5,6],
[7,8,9]
]
print(m)
print(transpose_matrix(m))
print(transpose_matrix(transpose_matrix(m)))
