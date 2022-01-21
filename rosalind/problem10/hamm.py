def get_hammingdistance(p,q):
    hd = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hd += 1
    return hd

existing = [
'AGTC',
'GTCA',
'TCAG',
'CAGT'
]
brute = [
'AAGC',
'AATT',
'ACAC',
'ACTG',
'AGAG',
'AGCA',
'AGGT',
'ATCC',
'ATTA',
'CATC',
'CGGC',
'CGTT',
'GGCC',
'GGTA',
'GTTC',
'TCTC',
'TGAC',
'TGTG',
]
hd = []
for i in existing:
    for j in brute:
        hd.append(get_hammingdistance(i,j))

print(hd)
