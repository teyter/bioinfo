p = "CATGGGCATCGGCCATACGCC"
sample = "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"

def skew(p):
    skew = []
    G = 0
    C = 0
    for i in p:
        skew.append(G-C)
        if i == 'G': G+=1
        if i == 'C': C+=1
    skew.append(G-C)
    return(skew)

def printlist(li):
    for i in range(len(li)):
        print(i,li[i])

def allmin(li):
    ret = []
    m = min(li)
    for i in range(len(li)):
        if li[i] == m:
            ret.append(i)

    return ret

def oneline(li):
    print(' '.join(map(str,li)))


bla = open('rosalind_ba1f.txt', 'r')
data = bla.read().strip()

x = skew(data)
final = allmin(x)
oneline(final)
