from teitlib import *
from random import randint

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

def printdict(dct):
    for key, value in dct.items():
        print(key, '->', value)

def printlst(lst):
    for i in lst: print(i)

def path_output(lst):
    print( '->'.join(map(str,lst)))
    
def test(): 
#   with open('rosalind_ba3f.txt') as f:
    with open('extra.txt') as f:
        data = f.read().splitlines()
    dic = xparse(data)
#   printdict(dic)
    result = EulerianPathProblem(dic)
    path_output(result)

test()
