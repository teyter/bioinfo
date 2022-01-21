from time import time
start = time()
Genome = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
k = 5
L = 75
t = 5

def printlist_oneline(li):
    print('  '.join(map(str,li)))

def printlist(li):
    for i in li: print(i)

def findCount(Text,Pattern):
    count = 0
    i = Text.find(Pattern)
    if i < 0: return count
    while (i >= 0):
        count+=1
        i = Text.find(Pattern,i+1)
    return count

# from problem 3
def listAllK(Interval,k):
    # create list of all k-mers
    kmers = []
    for i in range(len(Interval)-k):
        kmers.append( Interval[i:i+k] )

    # create listo tuples with frequency of patterns
    lit = [(kmers.count(i),i) for i in kmers]

    # delete duplicates and return
    return list(dict.fromkeys(lit))

def interval(Genome,k,L,t):
    tlist = []
    for i in range(len(Genome)-L):
        allK = listAllK(Genome[i:i+L],k)
        for j in range(len(allK)):
            if int(allK[j][0]) == t:
                tlist.append(allK[j])
    return list(dict.fromkeys(tlist))
   
text_file = open("genome.txt","r")
#text_file = open("E_coli.txt","r")
Genome = text_file.read()
text_file.close()
k = 9
L = 575
t = 20
   
result = interval(Genome,k,L,t)
printlist(result)

end = time()
print( int(end-start),"seconds" )
print( int(end-start)/60,"minutes" )
print( int(end-start)/60/60,"hours" )
