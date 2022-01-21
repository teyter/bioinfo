def findCount(Text,Pattern):
    indices = []
    i = Text.find(Pattern)
    if i < 0: return i
    while (i >= 0):
        indices.append(i)
        i = Text.find(Pattern,i+1)
    return indices

p = "ATAT"
t = "GATATATGCATATACTT"

result = findCount(t,p)

#print (" ".join(result))
# print list on one line without brackets
print(', '.join(map(str,result)))
