import numpy as np
from teitlib import *

def interpol(setlist):
    for i in range(len(setlist)):
        set1 = setlist[0]
        set1.intersection_update(setlist[i])
    return set1

def MotifEnum(dna,k,d):
    Patterns = []
    sli = [] # list of sets
    #every_string = len(dna)
    bruteK = bruteforce(k)
    for Pattern in dna:
        hl = get_hamminglist(Pattern,bruteK,d)
        sett = set()
        for i in range(len(hl)):
            number = hl[i][0]
            string = hl[i][1]
            if number == 1:
                sett.add(string)
        sli.append(sett)
    return interpol(sli)

def test():
    data = "".join(open('sample.txt')).split()
    k = int(data[0])
    d = int(data[1])
    dna = data[2:]
    printlist(MotifEnum(dna,k,d))

test()
