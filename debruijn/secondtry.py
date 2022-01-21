from teitlib import *

def string(li):
    return ''.join(map(str,li))

def printlst(lst):
    for i in lst: print(i)

def printdict(dct):
    for key, value in dct.items():
        print(key, '->', ','.join(value))

def reconstruct(kmers):
    ret = []
    for i in range(len(kmers)):
        ret[i:] = list(kmers[i])
    return string(ret)


def allK(Text,k):
    return [Text[i:i+k] for i in range(len(Text)-k+1)]

# 440
def main():
    data = "".join(open('s24.txt')).split()
    k = int(data[0])
    kmers = data[1:]
    teg = DeBruijnGraph(kmers)
    printdict(teg)
    osh = EulerianPath(teg)
    final = reconstruct(osh)
    print(final)
    print(allK(final,3))

main()
