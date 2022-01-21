def printlist(li):
    for i in li:
        print(i)

def comp2(Text,k):
    # create list of all k patterns
    kmers = []
    for i in range(len(Text)-k+1):
        kmers.append( Text[i:i+k] )
    return kmers

def composition_k(Text,k): # aka listAllK
    return [Text[i:i+k] for i in range(len(Text)-k+1)]

def lst2tpl(kmers): # aka listAllK
    return [(kmers[i],kmers[i+1]) for i in range(len(kmers)-1)]

def printdict(dct):
    L = []
    for key, value in dct.items():
        print(key, '->', ','.join(value))

def dix(lst): # where lst is list of tuples
    return {k: v for k, v in lst}

def adj(Text,k):
    kmers = [Text[i:i+k] for i in range(len(Text)-k+1)]
    tpl =  [(kmers[i],kmers[i+1]) for i in range(len(kmers)-1)]
    tpl.sort()
    dic = {}
    for i in tpl:
        key = i[0]
        value = i[1]
        dic.setdefault(key, [])
        dic[key].append(value)
    return dic

def adj2(tpl):
    dic = {}
    for i in tpl:
        key = i[0]
        value = i[1]
        dic.setdefault(key, [])
        dic[key].append(value)
    return dic

def test2():
    data = "".join(open('sample.txt')).split()
    k = int(data[0]) - 1
    text = data[1]
    comp = composition_k(text,k)
    tpl = lst2tpl(comp)
    tpl.sort()
    dic = adj2(tpl)
    printdict(dic)

def test():
    data = "".join(open('sample.txt')).split()
    k = int(data[0]) - 1
    text = data[1]
    res = adj(text,k)
    printdict(res)

test()
