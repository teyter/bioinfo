import numpy as np

def kmer(Text,k):
    window = []
    for i in range(len(Text)-k):
        window.append( Text[i:i+k] )

    max = 0
    res = window[0] 
    for i in window: 
        freq = window.count(i) 
        if freq > max: 
            max = freq 
            res = i 
    return res, max


sample0 = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
allData = np.loadtxt('rosalind_ba1b.txt',dtype='str')

Text = allData[0]
k = int(allData[1])

print(kmer(Text,k))
