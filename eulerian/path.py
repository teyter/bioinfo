from teitlib import *

def get_inout(adj):
    k = set(adj.keys())
    right = [item for sublist in list(adj.values()) for item in sublist]
    v = set(right)
    nodes = list(k.union(v))
    out = []
    for i in nodes:
        try:
            out.append(len(adj[i]))
        except:
            out.append(0)
    dic = dict.fromkeys(nodes,0)
    for i in right:
        try: dic[i]+=1
        except: pass
    inn = list(dic.values())
    return nodes,inn,out

def isPath(nodes,inn,out):
    start = 0
    scount = 0
    ecount = 0
    for p,i,j in zip(nodes,inn,out):
        oi = j-i
        io = i-j
        if oi == 1:
            start = p
            scount+=1
            if scount > 1:
                return -1
        if io == 1:
            ecount+=1
            if ecount > 1:
                return -1
    return start
            
def path(adj):
    nodes,inn,out = get_inout(adj)
    start = isPath(nodes,inn,out)
    if start == -1: return -1
    stack = [start]
    path = []
    while stack:
        u_v = stack[-1]
        try:
            w = adj[u_v][0]
            stack.append(w)
            adj[u_v].remove(w)
        except:
            path.append(stack.pop())
    return path[::-1]

            
# is there eulerian path in graph}
# if true, return start and end nodes
# if false, reject

###########################################################
def cringe():
    #with open('rosalind_ba3g.txt') as f:
    #with open('extra.txt') as f:
    with open('sample.txt') as f:
        data = f.read().splitlines()

    with open('extra_solution.txt') as f:
        sol = f.read().splitlines()

    with open('out.txt') as f:
        buts = f.read().splitlines()

    adj = xparse(data)

    x = path(adj)
    print(x)
    rosa = sol[0]
    mitt = path_outputV(x)
    butt = (buts[0])

def prof():
    with open('prof.txt') as f:
        data = f.read().splitlines()
    adj = sparse(data) 
    printdict(adj)
    x = path(adj)
    print(reconstruct(x))

prof()
