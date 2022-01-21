dic = { 
    'A' : 'T',
    'T' : 'A',
    'C' : 'G',
    'G' : 'C'
}
bla = open('rosalind_ba1c.txt', 'r')
x = bla.read().strip()
print(complement(x))

sample = list("AAAACCCGGT")
sample.reverse()
pre = "".join([dic[i] for i in sample])
print(pre)
