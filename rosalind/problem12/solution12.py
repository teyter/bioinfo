from teitlib import *

with open('dna.txt') as f:
    dna = f.read().splitlines()
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

def joinlists(abc):
    ABC = []
    for i in range(len(abc)):
        ABC += abc[i]
    return ABC

def listlistAllK(TextList,k):
    listlist = []
    for i in TextList:
        listlist.append(listAllK(i,k))
    return joinlists(listlist)

k = 6
kmers = listlistAllK(dna,k)
mosfreq = most_freq(kmers)
print(bagmax(mosfreq))

# GCTGAG
