from lib import *

def string(li):
    return ''.join(map(str,li))

def reconstruct(kmers):
    ret = []
    for i in range(len(kmers)):
        ret[i:] = list(kmers[i])
    return string(ret)

def test():
    data = "".join(open('rosalind_ba3d.txt')).split()
    k = int(len*(data[0])) - 1
    print(data)

def isnext(km1,km2):
    return km1[1:] == km2[0:-1]

def desort(kmers):
    ret = []
    for i,j in kmers:
        if True:
            return 0

def prefix(kmers):
    ret = []
    for i in kmers:
        prefix = i[0:-1]
        suffix = i[1:]
        ret.append((prefix,suffix))
    return ret

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

def test():
    data = "".join(open('rosalind_ba3e.txt')).split()
    ass = prefix(data)
    printlst(ass)
    teg = adj21(ass)
    #printdict(teg)

test()
