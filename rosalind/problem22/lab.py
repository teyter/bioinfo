from random import randint

#a = "0310216324254658798796"
a = "1234"
al = list(a)

def printlst(lst):
    for i in lst:
        print(i)

def parse(lst):
    ret = []
    for i in range(len(lst)): 
        right = []
        for j in range(1,len(lst[i])):
            item = lst[i][j]
            if item.isnumeric():
                right.append(int(item))
        ret.append((int(lst[i][0]),right))
    return ret
            
def xparse(lst):
    ret = []
    for i in lst:
        lraw, rraw = raw.split(" -> ", 1)
        left = int(lraw)
        nraw = rraw.split(",")
        right = [int(i) for i in nraw]
        ret.append((left,right))
    return ret
        
def test(): 
    bla = [1,2,3,4,5]
    print(bla[::-1])


test()
