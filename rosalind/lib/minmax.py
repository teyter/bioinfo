# problem 3
def findMultiMax(li):
    # find max number
    max = 0
    for i in range(len(li)):
        temp = int(li[i][0])
        if temp > max:
            max = temp
    # list all patterns with max nr
    ret = []
    for i in range(len(li)):
        temp = int(li[i][0])
        if temp == max:
            ret.append(li[i][1])
    return ret

def findMax(li):
    max = 0
    bag = []
    for i in range(len(li)):
        count = li[i][0]
        item = li[i][1]
        if count > max:
            bag.clear()
            max = li[i][0]
            bag.append(li[i][1])
        if count == max:
            bag.append(li[i][1])

def allmin(li):
    ret = []
    m = min(li)
    for i in range(len(li)):
        if li[i] == m:
            ret.append(i)
    return ret

def bagmax(tli):
    ret = []
    currentMax = 0
    for i in range(len(tli)):
        nr = tli[i][0]
        item = tli[i][1]
        allt = tli[i] # debug
        if nr > currentMax:
            currentMax = nr
            ret.clear()
            ret.append(allt)
        elif nr == currentMax:
            ret.append(allt)
    return ret

def bagmax_index(tli):
    ret = []
    currentMax = 0
    for i in range(len(tli)):
        index = tli[i][0]
        score = tli[i][1]
        item = tli[i][2]
        allt = tli[i] # debug, sja nr og item
        if score > currentMax:
            currentMax = score
            ret.clear()
            ret.append(allt)
        elif score == currentMax:
            ret.append(allt)
    return ret

def bagmax3(tli):
    ret = []
    currentMax = 0
    for i in range(len(tli)):
        index = tli[i][0]
        score = tli[i][1]
        item = tli[i][2]
        allt = tli[i] # debug, sja nr og item
        if score > currentMax:
            currentMax = score
            ret.clear()
            ret.append(allt)
        elif score == currentMax:
            ret.append(allt)
    return ret

def bagmin2(tli):
    ret = []
    currentMin = min(tli)[0]
    for i in range(len(tli)):
        score = tli[i][0]
        item = tli[i][1]
        allt = tli[i] # debug, sja nr og item
        if currentMin == score:
            ret.append(allt)
    return ret

def bagmin3(tli):
    ret = []
    currentMin = min(tli)[1]
    for i in range(len(tli)):
        index = tli[i][0]
        score = tli[i][1]
        item = tli[i][2]
        allt = tli[i] # debug, sja nr og item
        if currentMin == score:
            ret.append(allt)
    return ret
