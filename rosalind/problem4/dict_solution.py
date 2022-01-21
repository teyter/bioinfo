dic = { 
    'A' : 'T',
    'T' : 'A',
    'C' : 'G',
    'G' : 'C'
}

rawdata = open('rosalind_ba1c.txt', 'r')
data = list(rawdata.read().strip())
data.reverse()
result = "".join([dic[i] for i in data])
print(result)
