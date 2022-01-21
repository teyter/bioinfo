def printlist(li):
    for i in li:
        print(i)

def composition_k(Text,k): # aka listAllK
    # create list of all k patterns
    kmers = []
    for i in range(len(Text)-k+1):
        kmers.append( Text[i:i+k] )
    return kmers

def main():
    data = "".join(open('rosalind_ba3a.txt')).split()
    k = int(data[0])
    t = data[1]
    result = composition_k(t,k)
    #result.sort()
    printlist(result)

main()
