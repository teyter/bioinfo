import numpy as np

def hamming_distance(p,q):
    hd = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hd += 1
    return hd


p = "GGGCCGTTGGT"
q = "GGACCGTTGAC"


allData = np.loadtxt('rosalind_ba1g.txt',dtype='str')
p = allData[0]
q = allData[1]

res = hamming_distance(p,q)
print(res)
