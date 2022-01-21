def string(li):
    return ''.join(map(str,li))

def printlst(lst):
    for i in lst: print(i)

def reconstruct(kmers):
    ret = []
    for i in range(len(kmers)):
        ret[i:] = list(kmers[i])
    return string(ret)

def find_first(kmers):
    first = kmers[0]
    i = -1
    while i <= len(kmers):
        i+=1
        if isprev(first,kmers[i]):
            first = kmers[i]
            i = 0
        print(first)
    return first

def find_first(kmers):
    first = kmers[0]
    i = 0
    while kmers:
        if isprev(first,kmers[i]):
            first = kmers[i]
            kmers.remove(


def isprev(one,two):
    return one[0:-1] == two[1:]

# 440
def main():
    data = "".join(open('sample.txt')).split()
    k = int(data[0])
    kmers = data[1:]
    res = find_first(kmers)
    print(res)

main()
