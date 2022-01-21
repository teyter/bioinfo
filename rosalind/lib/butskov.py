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
