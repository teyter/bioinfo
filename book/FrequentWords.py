# listAllK from probelm3
def listAllK(Text,k):
    # create list of all k patterns
    AllPatterns = []
    for i in range(len(Text)-k):
        AllPatterns.append( Text[i:i+k] )

    # create list of tubles ( frequency : int, pattern : str )
    # using list.count
    freqMap = [(AllPatterns.count(i),i) for i in AllPatterns]
    frequentPatterns = MaxMap(freqMap)
    # delete duplicates and return
    return list(dict.fromkeys(frequentPatterns))

def MaxMap(freqMap):
    maxFreq = 0
    fmlen = len(freqMap)
    for i in range(fmlen):
        freq = freqMap[i][0]
        if freq > maxFreq:
            maxFreq = freq
    ret = []
    for j in range(fmlen):
        freq = freqMap[j][0]
        item = freqMap[j][1]
        if freq == maxFreq:
            ret.append(item)
    return ret

print(listAllK("ACGTTTCACGTTTTACGG",3))

