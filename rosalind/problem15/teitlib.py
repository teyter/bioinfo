def bagmax3(tli):
    ret = []
    currentMax = 0
    for i in range(len(tli)):
        index = tli[i][0]
        score = tli[i][1]
        item = tli[i][2]
        allt = tli[i] # debug, sja nr og item
        if score > currentMax:
            currentMax = score
            ret.clear()
            ret.append(allt)
        elif score == currentMax:
            ret.append(allt)
    return ret

def bagmin2(tli):
    ret = []
    currentMin = min(tli)[0]
    for i in range(len(tli)):
        score = tli[i][0]
        item = tli[i][1]
        allt = tli[i] # debug, sja nr og item
        if currentMin == score:
            ret.append(allt)
    return ret

def printlist(li):
    for i in li:
        print(i)
def get_slice(li,k):
    ret = []
    for i in li:
        ret.append(i[0:k])
    return ret

def Score(Motifs):
    acgt = "ACGT"
    Motifs = transpose(Motifs)
    score = 0
    for i in Motifs:
        score += len(i) - freq_letter(i)
    return score

def freq_letter(s):
    li = []
    acgt = "ACGT"
    for i in range(len(acgt)):
        li.append(findCount(s,acgt[i]))
    return max(li)
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

def Profile(li):
    li = transpose(li)
    matrix = []
    ACGT = "ACGT"
    t = len(li[0])
    for i in range(4):
        vector = []
        for j in range(len(li)):
            vector.append((findCount(li[j],ACGT[i])/t)+1)
        matrix.append(vector)
    return matrix


def Pr(Pattern,Profile):
    A = Profile[0]
    C = Profile[1]
    G = Profile[2]
    T = Profile[3]
    pr = 1.0
    for i in range(len(Pattern)):
        if Pattern[i] == "A":
            pr *= A[i]
        if Pattern[i] == "C":
            pr *= C[i]
        if Pattern[i] == "G":
            pr *= G[i]
        if Pattern[i] == "T":
            pr *= T[i]
    return pr

def listAllK(Text,k):
    # create list of all k patterns
    kmers = []
    for i in range(len(Text)-k+1):
        kmers.append( Text[i:i+k] )
    return kmers
