def printlst(lst):
    for i in lst: print(i)

def printdict(dct):
    for key, value in dct.items():
        print(key, '->', ','.join(value))

def allK(Text,k):
    return [Text[i:i+k] for i in range(len(Text)-k+1)]

def adj(Text,k):
    kmers = [Text[i:i+k] for i in range(len(Text)-k+1)]
    tplst =  [(kmers[i],kmers[i+1]) for i in range(len(kmers)-1)]
    tplst.sort()
    dic = {}
    for i in tplst:
        key = i[0]
        value = i[1]
        dic.setdefault(key, [])
        dic[key].append(value)
    return dic

def adj21(tplst):
    tplst.sort()
    dic = {}
    for i in tplst:
        key = i[0]
        value = i[1]
        dic.setdefault(key, [])
        dic[key].append(value)
    return dic
