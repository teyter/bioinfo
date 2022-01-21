from teitlib import *

def printlst(lst):
    for item in lst: print(item)
    #for item in lst: print("%.1f" % item)

def printmatrix(matrix):
    for vector in matrix:
        print(["{0:0.1f}".format(pr) for pr in vector])

def R(lst):
    for i in range(len(lst)):
        y = lst[i].find("R")
        if y >= 0:
            x = list(lst[i])
            x[y] = "AG"
            lst[i] = string(x)
    return lst

def Profile(Motifs):
    Motifs = transpose(Motifs)
    Motifs = R(Motifs)
    matrix = []
    ACGT = "ACGT"
    t = len(Motifs)
    for i in range(4):
        vector = []
        for j in range(len(Motifs)):
            vector.append((findCount(Motifs[j],ACGT[i])/t))
        matrix.append(vector)
    return matrix

def transpose(li):
    ret = []
    for i in range(len(li[0])):
        s = ""
        for j in range(len(li)):
            s+= li[j][i] 
        ret.append(s)
    return ret

def findCount(Text,Pattern):
    count = 0
    i = Text.find(Pattern)
    if i < 0: return count
    while (i >= 0):
        count+=1
        i = Text.find(Pattern,i+1)
    return count



def main():
    kmers = "".join(open('Nbook.txt')).split()
    k1 = [kmers[0]]
    profile = Profile(kmers)
    printmatrix(profile)

main()
