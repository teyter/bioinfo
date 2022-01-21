def printlst(lst):
    for i in lst: print(i)

def printdict(dct):
    for key, value in dct.items():
        print(key, '->', ','.join(value))

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

def test():
    data = "".join(open('rosalind_ba3d.txt')).split()
    data = "".join(open('sample.txt')).split()
    k = int(data[0]) - 1
    text = data[1]
    print(text)
    res = adj(text,k)
    printdict(res)

test()
