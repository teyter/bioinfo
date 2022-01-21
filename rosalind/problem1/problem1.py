def count(data):
    countA = 0
    countC = 0
    countG = 0
    countT = 0
    for i in data:
        if i == "A": countA+=1
        if i == "C": countC+=1
        if i == "G": countG+=1
        if i == "T": countT+=1
    return countA, countC, countG, countT

sampleData = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

#a,c,g,t = count(sampleData)

text_file = open("rosalind_dna.txt","r")
bigData = text_file.read()
text_file.close()

a,c,g,t = count(bigData)
print(a,c,g,t)
