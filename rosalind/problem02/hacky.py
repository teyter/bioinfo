# solution without overlap
import numpy as np

def Count(Text,Pattern):
    count = 0
    lenText = len(Text)
    lenPatt = len(Pattern)
    listText = list(Text)
    listPatt = list(Pattern)
    for i in range(lenText-lenPatt):
        if listText[i:i+lenPatt] == listPatt[0:lenPatt]:
            count += 1
            listText[i+lenPatt] = "X"
    return count
    
#---------------------------------------------------#
#---------------------------------------------------#
#---------------------------------------------------#
#---------------------------------------------------#

sample2 = "ACAACTATGCATACTATCGGGAACTATCCT"
sample3 = "CGATATATCCATAG"
pattern = "ATA"
countem = Count(sample3,pattern)

allData = np.loadtxt('rosalind_ba1a.txt',dtype='str')

text = allData[0]
pattern = allData[1]

print( Count(text,pattern) )
