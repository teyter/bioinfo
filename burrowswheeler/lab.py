def printlst(lst):
    for i in lst: print(i)

def string(lst):
    return ''.join(map(str,lst))

def ti(tlst,c): # tuple list index
    for i in range(len(tlst)):
        if tlst[i][0] == c:
            return i
    return -1

s = "do$oodwg"
s = list(s)
def lastFirst(lc):
    fc = lc.copy()
    fc.sort()
    fc = countOccurence(fc)
    lc = countOccurence(lc)
    tlst = list(zip(fc,lc))
#   print(tlst[0])
#   print(tlst[0][1])
#   print(tlst[0][0][0])
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


res = lastFirst(s)
print(res)
