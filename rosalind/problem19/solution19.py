def string(li):
    return ''.join(map(str,li))

def reconstruct(kmers):
    ret = []
    for i in range(len(kmers)):
        ret[i:] = list(kmers[i])
    return string(ret)

def main():
    kmers = "".join(open('rosalind_ba3b.txt')).split()
    result = reconstruct(kmers)
    print(result)

main()
