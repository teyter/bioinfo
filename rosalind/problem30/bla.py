def overlap_assignment(v,w,match_bonus=+1,mismatch_cost=2,indel_cost=2):
    def dynamic_programming(v,w):
        distances = create_distance_matrix(len(v)+1,len(w)+1)
        path      = {}
        for i in range(1,len(v)+1):
            for j in range(1,len(w)+1):
                moves           = [(i-1,j),(i,j-1),(i-1,j-1)]
                scores          = [distances[i-1][j]   - indel_cost,
                                   distances[i][j-1]   - indel_cost,
                                   distances[i-1][j-1] + (match_bonus if v[i-1]==w[j-1] else -mismatch_cost)]
                index           = argmax(scores)
                distances[i][j] = scores[index]
                path[(i,j)]      = moves[index]
        
        i        = len(v)
        j        = argmax(distances[i])
        distance = distances[i][j]
        v1       = []
        w1       = []
        while i>0 and j>0:
            i1,j1 = path[(i,j)]
            v1.append(v[i1] if i1<i else '-')
            w1.append(w[j1] if j1<j else '-')
            i,j=i1,j1
    
        print(distance,v1[::-1],w1[::-1])
        return distance,v1[::-1],w1[::-1]

def test(): 
#   with open('rosalind_ba3f.txt') as f:
    with open('sample.txt') as f:
        data = f.read().splitlines()
    kmers = "".join(open('sample.txt')).split()
    v = kmers[0]
    w = kmers[1]
    res = overlap_assignment(v,w)

test()

