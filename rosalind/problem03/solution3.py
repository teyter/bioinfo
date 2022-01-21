import numpy as np


def listAllK(Text,k):
    # create list of all k patterns
    kmers = []
    for i in range(len(Text)-k+1):
        kmers.append( Text[i:i+k] )
    # create list with frequency of patterns
    lit = [(kmers.count(i),i) for i in kmers]
    # delete duplicates and return
    return list(dict.fromkeys(lit))

def findMultiMax(li):
    # find max number
    max = 0
    for i in range(len(li)):
        temp = int(li[i][0])
        if temp > max:
            max = temp
    # list all patterns with max nr
    ret = []
    for i in range(len(li)):
        temp = int(li[i][0])
        if temp == max:
            ret.append(li[i][1])
    return ret

def printlist(li):
    for i in li:
        print(i)

def findMax(li):
    max = 0
    bag = []
    for i in range(len(li)):
        count = li[i][0]
        item = li[i][1]
        if count > max:
            bag.clear()
            max = li[i][0]
            bag.append(li[i][1])
        if count == max:
            bag.append(li[i][1])
######################################################################


text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4

#allData = np.loadtxt('rosalind_ba1b.txt',dtype='str')
#text = allData[0]
#k = int(allData[1])
first = listAllK(text,k)
result = findMultiMax(first)
#printList(result)

print(' '.join(map(str,result)))

#actually finds k. is not given k as parameter.
"""   
allWindows = []
for i in range(3,int(len(text)/2)):
    allWindows.append( listAllK(text,i) )
"""
