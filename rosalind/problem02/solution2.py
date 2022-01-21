import numpy as np

def Count(Text,Pattern):
    count = 0
    lenText = len(Text)
    lenPatt = len(Pattern)
    for i in range(lenText-lenPatt):
        if Text[i:i+lenPatt] == Pattern:
            count += 1
    return count
    
# Method using str.find()
def findCount(Text,Pattern):
    count = 0
    i = Text.find(Pattern)
    if i < 0: return count
    while (i >= 0):
        count+=1
        i = Text.find(Pattern,i+1)
    return count
#---------------------------------------------------#
#---------------------------------------------------#
#---------------------------------------------------#
#---------------------------------------------------#

sample2 = "ACAACTATGCATACTATCGGGAACTATCCT"
sample3 = "CGATATATCCATAG"
samplePattern = "ATA"

allData = np.loadtxt('rosalind_ba1a.txt',dtype='str')

text = allData[0]
pattern = allData[1]

print( Count(text,pattern) )
