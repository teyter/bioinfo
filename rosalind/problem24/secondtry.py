def string(li):
    return ''.join(map(str,li))

def printlst(lst):
    for i in lst: print(i)

def printdict(dct):
    for key, value in dct.items():
        print(key, '->', ','.join(value))

def adj21(tplst):
    tplst.sort()
    dic = {}
    for i in tplst:
        key = i[0]
        value = i[1]
        dic.setdefault(key, [])
        dic[key].append(value)
    return dic

def reconstruct(kmers):
    ret = []
    for i in range(len(kmers)):
        ret[i:] = list(kmers[i])
    return string(ret)


def DeBrujinGraph(kmers):
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

def EulerianPathProblem(adj_list):
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

# 440
def main():
    data = "".join(open('sample.txt')).split()
    k = int(data[0])
    kmers = data[1:]
    teg = DeBrujinGraph(kmers)
    printdict(teg)
    osh = EulerianPathProblem(teg)
    final = reconstruct(osh)
    print(final)

main()
