def Score(Motifs):
    acgt = "ACGT"
    Motifs = transpose(Motifs)
    score = 0
    for i in Motifs:
        score += len(i) - Score(i)
    return score

def findCount(Text,Pattern):
    count = 0
    i = Text.find(Pattern)
    if i < 0: return count
    while (i >= 0):
        count+=1
        i = Text.find(Pattern,i+1)
    return count
def freq_letter(s):
    li = []
    acgt = "ACGT"
    for i in range(len(acgt)):
        li.append(findCount(s,acgt[i]))
    return max(li)


print(Score(["ACGTT","TTTAG"]))
