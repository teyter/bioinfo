def string(lst):
    return ''.join(map(str,lst))

def printlst(lst):
    for i in lst: print(i)

def pt(lst):
    for i in lst: oneline(i)

def oneline(lst):
    print(''.join(map(str,lst)))

def pz(x,y):
    for i,j in zip(x,y):
        print(i,j)

def transform(s):
    ret = []
    s += "$"
    S = s*len(s)
    for i in range(0,len(S)-1,len(s)-1):
        ret.append(S[i:i+len(s)])
    ret.pop()
    printlst(ret)
    print()
    ret.sort()
    return ret

def sip(lc,lst):
    ret = []
    for i in range(len(lc)):
        ret.append(lc[i]+''.join(map(str,lst[i])))
    return ret

def last_column(lst):
    return [i[-1] for i in lst]

def first_column(lst):
    ret = last_column(lst)
    ret.sort()
    return ret

def reconstruct(lc):
    fc = lc.copy()
    fc.sort()
    for i in range(len(lc)-1):
        fc = sip(lc,fc)
        fc.sort()
    return fc[0][1:]

        
def ti(tlst,c): # tuple list index
    for i in range(len(tlst)):
        if tlst[i][0] == c:
            return i
    return -1

def first_last(lc):
    fc = lc.copy()
    fc.sort()
    fc = countOccurence(fc)
    lc = countOccurence(lc)
    tlst = list(zip(fc,lc))
    stack = []
    i = ti(tlst,tlst[0][0])
    while tlst:
        right = tlst[i][1]
        x = right[0]
        stack.append( x )
        tlst.pop(i)
        i = ti(tlst,right)
        if i == -1:
            stack.pop()
            return string(stack[::-1])

def countOccurence(s):
    dic = dict.fromkeys(s,1)
    ret = []
    for i in s:
        ret.append((i,dic[i]))
        dic[i] += 1
    return ret

s = "ACTACTGAT"
cr = (transform(s))
printlst(cr)
print()
lc = last_column(cr)
recon = (reconstruct(lc))
print(recon)
print()
# last-first property
print(first_last(lc))

s = "T$TGAATACC"
s = list(s)
print(reconstruct(s))
