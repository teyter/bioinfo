## problem 2
def findCount(Text,Pattern):
    count = 0
    i = Text.find(Pattern)
    if i < 0: return count
    while (i >= 0):
        count+=1
        i = Text.find(Pattern,i+1)
    return count

def listAllK(Text,k):
    # create list of all k patterns
    kmers = []
    for i in range(len(Text)-k+1):
        kmers.append( Text[i:i+k] )
    return kmers

def mostFreqKmer(Text,k):
    # create list of all k patterns
    kmers = []
    for i in range(len(Text)-k+1):
        kmers.append( Text[i:i+k] )
    # create list with frequency of patterns
    lit = [(kmers.count(i),i) for i in kmers]
    # delete duplicates and return
    return list(dict.fromkeys(lit))

## problem 3
# the old fashioned way
def reverse(s):
    s = list(s)
    half = int(len(s)/2)
    b = 0
    e = len(s)-1
    if (len(s) % 2 == 1):
        for i in range(half):
            temp = s[b]
            s[b] = s[e]
            s[e] = temp
            b+=1
            e-=1
    if (len(s) % 2 == 0):
        for i in range(half+1):
            temp = s[b]
            s[b] = s[e]
            s[e] = temp
            b+=1
            e-=1
    return string(s)

def string(li):
    s = ""
    for i in li:
        s += i
    return s

def string(li):
    return ''.join(map(str,li))

# the python way
def rev(s):
    s = list(s)
    s.reverse()
    return string(s)

def complement(s):
    li = []
    for i in s:
        if i == 'A':
            li.append('T')
        elif i == 'T':
            li.append('A')
        elif i == 'C':
            li.append('G')
        elif i == 'G':
            li.append('C')
    li.reverse()
    return(string(li))

## problem 6 - clump finding problem
def interval(Genome,k,L,t):
    tlist = []
    for i in range(len(Genome)-L):
        allK = listAllK(Genome[i:i+L],k)
        for j in range(len(allK)):
            if int(allK[j][0]) == t:
                tlist.append(allK[j])
    return list(dict.fromkeys(tlist))

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

## problem 7
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

## problem 8
def hamming_distance(p,q):
    hd = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hd += 1
    return hd

## problem 9
def approx(p,t,d):
    ret = []
    k = len(p)
    for i in range(len(t)-k):
        x = hamming_distance(t[i:i+len(p)],p)
        if x <= d:
            ret.append(i)
    return ret

## problem 10
def get_hammingdistance(p,q):
    hd = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hd += 1
    return hd

def CountD(t,p,d):
    k = len(p)
    count = 0
    for i in range(len(t)-k+1):
        x = get_hammingdistance(t[i:i+k],p)
        if x <= d:
            count+=1
    return count

def kmers_intext(Text,k):
    AllPatterns = []
    for i in range(len(Text)-k):
        AllPatterns.append( Text[i:i+k] )
    return AllPatterns

def get_hamminglist(Text,AllPatterns,d):
    # god forgive me
    L = [(CountD(Text,AllPatterns[i],d), AllPatterns[i]) for i in range(len(AllPatterns))]
    return list(dict.fromkeys(L))

def bruteforce(k):
    a = ["A","C","G","T"]
    b = [i for i in range(k-1,-1,-1)]
    ret = []
    base = len(a)
    sic = base**k
    for i in range(sic):
        s = []
        for j in range(k):
            x = floor(i/base**b[j]) % base 
            s.append(a[x])
        s = string(s)
        ret.append(s)
    return ret

## problem 11
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

def CountD1(t,p,d):
    k = len(p)
    count = 0
    for i in range(len(t)-k+1):
        x = get_hammingdistance(t[i:i+k],p)
        if x <= d:
            count = 1
    return count

## problem 12
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

def d(Pattern,Text):
    k = len(p)
    count = 0
    hd = []
    for i in range(len(t)-k+1):
        x = t[i:i+k]
        hd.append( get_hammingdistance(x,p) )
    return min(hd)

def dd(Pattern,Dna):
    ret = []
    for i in range(len(Dna)):
        ret.append(d(Pattern,Dna[i]))
    return sum(ret)

## problem 13
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

## problem 14
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

def Profile(li):
    li = transpose(li)
    matrix = []
    ACGT = "ACGT"
    t = len(li[0])
    for i in range(4):
        vector = []
        for j in range(len(li)):
            vector.append(findCount(li[j],ACGT[i])/t)
        matrix.append(vector)
    return matrix

## problem 15
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

## problem 16
def OneThousand(dna,k,t):
    i = 0
    xbestmotifs = random_motifs(dna,k,t)
    while i < 1000:
        motifs = RandomizedMotifSearch(dna,k,t)
        if Score(motifs) < Score(xbestmotifs):
            xbestmotifs = motifs
            print("master",xbestmotifs)
        i = i+1
    return xbestmotifs

def RandomizedMotifSearch(dna,k,t):
    motifs = random_motifs(dna,k,t)
    bestmotifs = motifs
    while True:
        profile = Profile(motifs)
        motifs = get_motifs_from_profile(dna,k,t,profile)
        if Score(motifs) < Score(bestmotifs):
            bestmotifs = motifs
        else:
            return bestmotifs

def get_motifs_from_profile(dna,k,t,profile):
        motifs = []
        for j in range(t):
            allP = listAllK(dna[j],k)
            L = [(dna[j].find(q),Pr(q,profile),q) for q in allP]
            bag = bagmax3(L)
            motifs.append(min(bag)[2])
        return motifs

def random_motifs(dna,k,t):
    motifs = []
    for j in range(t):
        allK = listAllK(dna[j],k)
        ayn = randint(0,len(allK)-1)
        motifs.append(allK[ayn])
    return motifs

def random_motif(dnaline,k):
    allK = listAllK(dnaline,k)
    ayn = randint(0,len(allK)-1)
    motif = allK[ayn]
    return motif

## problem 17
def Twenty(dna,k,t,N):
    i = 0
    best_motifs = [k * t, None]
    while i < 20:
        motifs = GibbsSampler(dna,k,t,N)
        if motifs[0] < best_motifs[0]:
            bestmotifs = motifs
        i = i+1
    return bestmotifs

def pla(dna, k, prof):
    nuc_loc = {nucleotide: index for index, nucleotide in enumerate('ACGT')}
    probs = []
    prof = transpose_matrix(prof)
    for i in range(len(dna) - k):
        current_prob = 1.
        for j, nucleotide in enumerate(dna[i:i + k]):
            current_prob *= prof[j][nuc_loc[nucleotide]]
        probs.append(current_prob)
    i = np.random.choice(len(probs), p = np.array(probs) / np.sum(probs))
    return dna[i:i + k]

def GibbsSampler(dna,k,t,N):
    motifs = random_motifs(dna,k,t)
    best_score = [Score(motifs), motifs]
    for j in range(N):
        i = randint(0,t-1)
        profile = Profile(motifs[0:i]+motifs[i+1:len(motifs)])
        #motifs = bla(dna[i],profile,k,i,motifs)
        motifs[i] = fla(dna[i],profile,k)
        if Score(motifs) < best_score[0]:
            best_score = [Score(motifs), motifs]
    return best_score

def bla(motif,profile,k,i,motifs):
    allK = listAllK(motif,k)
    p = [Pr(i,profile) for i in allK]
    return motifs[0:i]+[Random(allK,p)]+motifs[i+1:len(motifs)]

def fla(motif,profile,k):
    allK = listAllK(motif,k)
    p = [Pr(i,profile) for i in allK]
    return Random(allK,p)

def Random(lst,p):
    summa = sum(p)
    p = [i/summa for i in p]
    choice = np.random.choice(lst,p=p)
    return choice

## problem 18
def composition_k(Text,k): # aka listAllK
    # create list of all k patterns
    kmers = []
    for i in range(len(Text)-k+1):
        kmers.append( Text[i:i+k] )
    return kmers

## problem 19
def reconstruct(kmers):
    ret = []
    for i in range(len(kmers)):
        ret[i:] = list(kmers[i])
    return string(ret)

## problem 20
def adj(Text,k):
    kmers = [Text[i:i+k] for i in range(len(Text)-k+1)]
    tplst =  [(kmers[i],kmers[i+1]) for i in range(len(kmers)-1)]
    tplst.sort()
    printlst(tplst)
    dic = {}
    for i in tplst:
        key = i[0]
        value = i[1]
        dic.setdefault(key, [])
        dic[key].append(value)
    return dic

## solution 21
def prefix(kmers):
    ret = []
    for i in kmers:
        prefix = i[0:-1]
        suffix = i[1:]
        ret.append((prefix,suffix))
    return ret

def adj21(tplst):
    tplst.sort()
    dic = {}
    for i in tplst:
        key = i[0]
        value = i[1]
        dic.setdefault(key, [])
        dic[key].append(value)
    return dic

def allK(Text,k):
    return [Text[i:i+k] for i in range(len(Text)-k+1)]

def DeBrujinGraph(kmers):
    tplst = []
    for i in kmers:
        prefix = i[0:-1]
        suffix = i[1:]
        tplst.append((prefix,suffix))
    tplst.sort()
    dic = {}
    for i in tplst:
        key = i[0]
        value = i[1]
        dic.setdefault(key, [])
        dic[key].append(value)
    return dic

## problem 22
# adjecency list to dict
def xparse(lst):
    ret = []
    for i in lst:
        lraw, rraw = i.split(" -> ", 1)
        left = int(lraw)
        nraw = rraw.split(",")
        right = [int(i) for i in nraw]
        ret.append((left,right))
    return dict(ret)
# broken
def xcycle(lst,i):
    ret = []
    ret.append(lst[i][0])
    while lst:
        rlist = lst[i][1]
        if not rlist:
            #ret.append(left)
            return ret
        rand = randint(0,len(rlist)-1)
        right = lst[i][1][rand]
        ret.append(right)
        rlist.remove(right)
        #lst[i][1][0] = -1
        i = find(lst,right)
        #print(ret)
    return 0
