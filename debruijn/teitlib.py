from math import floor

def oneline(result):
    print(' '.join(map(str,result)))

def string(li):
    return ''.join(map(str,li))

def printlst(lst):
    for i in lst: print(i)

def printdict(dct):
    for key, value in dct.items():
        print(key, '->', value)

def path_output(lst):
    print( '->'.join(map(str,lst)))

def path_outputV(lst):
    return( '->'.join(map(str,lst)))

def listAllK(Text,k):
    # create list of all k patterns
    kmers = []
    for i in range(len(Text)-k+1):
        kmers.append( Text[i:i+k] )
    return kmers

def most_freq(kmers):
    # create list with frequency of patterns
    lit = [(kmers.count(i),i) for i in kmers]
    # delete duplicates and return
    return list(dict.fromkeys(lit))

def bagmax(tli):
    ret = []
    currentMax = 0
    for i in range(len(tli)):
        nr = tli[i][0]
        item = tli[i][1]
        allt = tli[i] # debug, sja nr og item
        if nr > currentMax:
            currentMax = nr
            ret.clear()
            ret.append(item)
        elif nr == currentMax:
            ret.append(item)
    return ret

def bagmin(tli):
    ret = []
    currentMin = 99
    for i in range(len(tli)):
        nr = tli[i][0]
        item = tli[i][1]
        allt = tli[i] # debug
        if nr < currentMin:
            currentMin = nr
            ret.clear()
            ret.append(item)
        elif nr == currentMin:
            ret.append(item)
    return ret

def bagmax2(tli):
    ret = []
    currentMax = max(tli)[0]

def listmin(tli):
    ret = []
    minn = min(tli)[0]
    for i in tli:
        nr = i[0]
        item = i[1]
        if nr == minn:
            ret.append(item)
    return ret

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

def CountD1(t,p,d):
    k = len(p)
    count = 0
    for i in range(len(t)-k+1):
        x = get_hammingdistance(t[i:i+k],p)
        if x <= d:
            count = 1
    return count

def get_hamminglist(Text,AllPatterns,d):
    # god forgive me
    L = [(CountD1(Text,AllPatterns[i],d), AllPatterns[i]) for i in range(len(AllPatterns))]
    return list(dict.fromkeys(L))

def bruteforce(k):
    a = ["A","C","G","T"]
    b = [i for i in range(k-1,-1,-1)]
    ret = []
    base = len(a)
    sic = base**k
    for i in range(sic):
        s = []
        for j in range(k):
            x = floor(i/base**b[j]) % base 
            s.append(a[x])
        s = string(s)
        ret.append(s)
    return ret

def xparse(lst):
    ret = []
    for i in lst:
        lraw, rraw = i.split(" -> ", 1)
        left = int(lraw)
        nraw = rraw.split(",")
        right = [int(i) for i in nraw]
        ret.append((left,right))
    return dict(ret)

def DeBruijnGraph(kmers):
    tplst = []
    for i in kmers:
        prefix = i[0:-1]
        suffix = i[1:]
        tplst.append((prefix,suffix))
    tplst.sort()
    dic = {}
    for i in tplst:
        key = i[0]
        value = i[1]
        dic.setdefault(key, [])
        dic[key].append(value)
    return dic

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
    for n,i,o in zip(nodes,inn,out):
        print(n,"\t",i-o,"\t",o-i)
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

def getBalanceCount(adj_list):
    balanced_count = dict.fromkeys(adj_list.keys(), 0)
    # Look for nodes balancing
    for node in adj_list.keys():
        #  If is in the sum 1 to balance, if out rest 1
        #print node
        for out in adj_list[node]:
            balanced_count[node] -= 1
            # Possibly there is a node with no out edges
            try:
                balanced_count[out] += 1
            except:
                balanced_count[out] = 1
    return balanced_count

def EulerianPath(adj_list):
    # Choose a unbalanced vertex (with out edge) and push into stack
    stack=[]
    balanced_count = getBalanceCount(adj_list)
    stack.append([k for k, v in balanced_count.items() if v==-1][0])
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

def sparse(lst):
    ret = []
    for i in lst:
        lraw, rraw = i.split(" -> ", 1)
        left = lraw
        nraw = rraw.split(",")
        right = [i for i in nraw]
        ret.append((left,right))
    return dict(ret)
