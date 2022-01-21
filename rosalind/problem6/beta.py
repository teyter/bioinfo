from time import time
start = time()
def printlist_oneline(li):
    print('  '.join(map(str,li)))

def printlist(li):
    for i in li: print(i)

def sample():
    Genome = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
    k = 5
    L = 75
    t = 4
    printlist(interval(Genome,k,L,t))

def interval(Genome,k,L,t):
    # create list of all k patterns
    kmers = []
    for i in range(len(Genome)-k):
        kmers.append( Genome[i:i+k] )

    # create list with frequency of patterns
    li = []
    for i in kmers:
        # nr of appearances + " " + pattern
        li.append(str(kmers.count(i)) + ' ' + i)
    # delete duplicates and return
    return list(dict.fromkeys(li))


    tlist = []
    for i in range(len(Genome)-L):
        allK = listAllK(Genome[i:i+L],k)
        for j in range(len(allK)):
            if int(allK[j][0]) == t:
                tlist.append(allK[j][2:])
    return list(dict.fromkeys(tlist))
   
# Inits 
text_file = open("genome.txt","r")
Genome = text_file.read()
text_file.close()
k = 10
L = 496
t = 19

# Function calls
sample()
   
# TIME
end = time()
print( int(end-start),"seconds" )
