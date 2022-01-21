li = ("2 abc", "1 cbc", "2 abd",)

def bla(yali):
    oskar = []
    oskar.append("0 abc")
    for i in range(len(yali)):
        freq = int(yali[i][0])
        if freq > int(oskar[0][0]):
            oskar.clear()
            oskar.append(yali[i])
        if freq == int(oskar[0][0]):
            oskar.append(yali[i])
    return oskar

def fla(bali):
    max = 0
    for i in range(len(bali)):
        temp = int(bali[i][0])
        if temp > max:
            max = temp
    ret = []
    for i in range(len(bali)):
        temp = int(bali[i][0])
        if temp == max:
            ret.append(bali[i])
    return ret
        
#print( bla(li) )
print( fla(li) )
def final(yali):
    oskar = []
    oskar.append(0)
    for i in range(len(yali)):
        freq = yali[i][0]
        if freq > int(oskar[0]):
            oskar.clear()
            oskar.append(yali[i])
        if int(freq) == int(oskar[0]):
            oskar.append(yali[i])
    return oskar
