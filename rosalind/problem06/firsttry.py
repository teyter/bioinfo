import numpy as np


def listAllK(Text,k):
    # create list of all k patterns
    window = []
    for i in range(len(Text)-k):
        window.append( Text[i:i+k] )
    # create list with frequency of patterns
    li = []
    for i in window:
        # nr of appearances + " " + pattern
        li.append(str(window.count(i)) + ' ' + i)
    # delete duplicates and return
    return list(dict.fromkeys(li))

def listMostFreqWord(li):
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
            ret.append(li[i])
    return ret

def printlist(li):
    for i in li:
        print(i)

######################################################################


k = 10
text_file = open("genome.txt","r")
text = text_file.read()
text_file.close()
"""
text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
Genome = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
first = listAllK(text,k)
result = listMostFreqWord(first)
"""
#printlist(result)
L = 496
allKall = listAllK(text,10)
mostFreq = listMostFreqWord(allKall)
print(mostFreq)
#print(' '.join(map(str,result)))
