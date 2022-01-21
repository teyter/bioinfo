def cycle(lst):
    ret = []
    i = 0
    ret.append(lst[i][0])
    while lst:
        right = lst[i][1][0]
        rlist = lst[i][1]
        if not rlist:
            return ret
        ret.append(right)
        rlist.pop(0)
        i = find(lst,right)
        if i == -1:
            return ret
        print(ret)
    return 0
        
def xcycle(lst,i):
    ret = []
    ret.append(lst[i][0])
    while lst:
        rlist = lst[i][1]
        if not rlist:
            #ret.append(left)
            return ret
        rand = randint(0,len(rlist)-1)
        right = lst[i][1][rand]
        ret.append(right)
        rlist.remove(right)
        #lst[i][1][0] = -1
        i = find(lst,right)
        #print(ret)
    return 0

def find(lst,x):
    for i in range(len(lst)):
        if lst[i][0] == x:
            return i
    return -1

def parse(lst):
    ret = []
    count = 0
    for i in range(len(lst)): 
        right = []
        for j in range(1,len(lst[i])):
            item = lst[i][j]
            if item.isnumeric():
                right.append(int(item))
        ret.append((int(lst[i][0]),right))
        count += 1*len(right)
    return count,ret

def xparse(lst):
    ret = []
    for i in lst:
        lraw, rraw = i.split(" -> ", 1)
        left = int(lraw)
        nraw = rraw.split(",")
        right = [int(i) for i in nraw]
        ret.append((left,right))
    return dict(ret)

def test(): 
#   with open('rosalind_ba3f.txt') as f:
    with open('sample.txt') as f:
        data = f.read().splitlines()
    adjlst = xparse(data)
    dic = dict(adjlst)
#   printdict(dic)
    result = EulerianCycleProblem(dic)
    string(result)
    #print(len(result))
#   printlst(adjlst)
#   best = []
#   max = 1
#   for i in range(1000):
#       adjlst = xparse(data)
#       adjlst.sort()
#       y = xcycle(adjlst,i%10)
#       best.append((len(y),y))
#   maxx = bagmax(best)
#   for i in maxx:
#       string(i)
