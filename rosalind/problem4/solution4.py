import numpy as np

# the old fashioned way
def reverse(s):
    s = list(s)
    half = int(len(s)/2)
    b = 0
    e = len(s)-1
    if (len(s) % 2 == 1):
        for i in range(half):
            temp = s[b]
            s[b] = s[e]
            s[e] = temp
            b+=1
            e-=1
    if (len(s) % 2 == 0):
        for i in range(half+1):
            temp = s[b]
            s[b] = s[e]
            s[e] = temp
            b+=1
            e-=1
    return string(s)

def string(li):
    s = ""
    for i in li:
        s += i
    return s

# the python way
def rev(s):
    s = list(s)
    s.reverse()
    return string(s)

def complement(s):
    li = []
    for i in s:
        if i == 'A':
            li.append('T')
        elif i == 'T':
            li.append('A')
        elif i == 'C':
            li.append('G')
        elif i == 'G':
            li.append('C')
    li.reverse()
    return(string(li))


bla = open('rosalind_ba1c.txt', 'r')
x = bla.read().strip()
print(complement(x))
