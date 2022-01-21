def get_hammingdistance(p,q):
    hd = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hd += 1
    return hd

def CountD(t,p,d):
    k = len(p)
    count = 0
    for i in range(len(t)-k+1):
        x = get_hammingdistance(t[i:i+k],p)
        if x <= d:
            count+=1
    return count

def Count(Text,Pattern):
    count = 0
    lenText = len(Text)
    lenPatt = len(Pattern)
    for i in range(lenText-lenPatt):
        if Text[i:i+lenPatt] == Pattern:
            count += 1
    return count
    
# Method using str.find()
def findCount(Text,Pattern):
    count = 0
    i = Text.find(Pattern)
    if i < 0: return count
    while (i >= 0):
        count+=1
        i = Text.find(Pattern,i+1)
    return count
text = "AATTAATTGGTAGGTAGGTA"
p = "GGTA"

d = 0

print(CountD(text,p,d))
print(findCount(text,p))
