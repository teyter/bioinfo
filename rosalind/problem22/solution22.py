from teitlib import *
from random import randint

def EulerianCycleProblem(adj_list):
    # Choose any vertex and push into stack
    stack=[]
    random_vertex = sorted(adj_list.keys())[0]
    #random_vertex = random.sample(adj_list.keys(), 1)[0]
    stack.append(random_vertex)
    # To save the right path
    path = []
    # Stack but fifo xD
    while stack != []:
        # top vertex
        u_v = stack[-1]
        try:
            w = adj_list[u_v][0]
            stack.append(w)
            # Removeadj_list[u][0] from available edges (edge marked)
            adj_list[u_v].remove(w)
        # No edges
        except:
            path.append(stack.pop())
    return path[::-1]

def printdict(dct):
    for key, value in dct.items():
        print(key, '->', value)

def printlst(lst):
    for i in lst: print(i)

def path_output(lst):
    print( '->'.join(map(str,lst)))

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
    dic = xparse(data)
    printdict(dic)
    result = EulerianCycleProblem(dic)
    path_output(result)

test()
