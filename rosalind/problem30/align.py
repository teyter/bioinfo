#    Copyright (C) 2019 Greenweaves Software Limited
#
#    This is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This software is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>

# Common code for alignment problems

from numpy import argmax,argmin
from sys import float_info

def reverse(chars):
    return ''.join(c for c in chars[::-1])

# BA5A 	Find the Minimum Number of Coins Needed to Make Change 	
#
# Input: An integer money and an array Coins of positive integers.
#
# Return: The minimum number of coins with denominations Coins that changes money.
#
# http://rosalind.info/problems/ba5a/

def number_of_coins(money,coins):
    number = [0]                           # We will use Dynamic Programming, and solve 
                                           # the problem for each amount up to and including money
    for m in range(1,money+1):             # solve for m
        nn = float_info.max            # Number of coins: assume that we haven't solved
        for coin in coins:                 # Find a coin such that we can make change using it
                                           # plus a previoudly comuted value
            if m>=coin:
                if number[m-coin]+1<nn:
                    nn = number[m-coin]+1
        number.append(nn)
    return number[money]

# BA5B 	Find the Length of a Longest Path in a Manhattan-like Grid 
#
# Input: Integers n and m, followed by an n*(m+1) matrix Down and an
#        (n+1)*m matrix Right. The two matrices are separated by the "-" symbol.
#
# Return: The length of a longest path from source (0, 0) to sink (n, m)
#        in the n*m rectangular grid whose edges are defined by the matrices
#        Down and Right.
#
# http://rosalind.info/problems/ba5a/


# BA5C 	Find a Longest Common Subsequence of Two Strings
#
# Input: Two strings.
#
# Return: A longest common subsequence of these strings.
#
# http://rosalind.info/problems/ba5a/

def longest_common_subsequence(string1,string2):

    # Calculate longest path through "map" defined by the two strings
    #
    # At each point we have a state, s, which is defined as follows
    # 1. Count of matches (==path lebth from (0,0) to here
    # 2. horizonal position of predecessor of this point
    # 3. vertical position of predecessor of this point
    # 4. If this point corresponds to a matching character (in both strings)
    #    this should be that chracter, otherwise an empty string
    
    def longest_path():
        
        # Used to update distamce at each node     
        def new_s(i,j,s):
            count_horizonal,_,_,_=s[i-1][j]
            count_vertical,_,_,_=s[i][j-1]
            count_diagonal,_,_,_=s[i-1][j-1]
            if string1[i-1]==string2[j-1]:
                count_diagonal+=1
            count=max(count_horizonal,count_vertical,count_diagonal)
            if count_diagonal==count:
                return (count,\
                        i-1,\
                        j-1,
                        string1[i-1] if string1[i-1]==string2[j-1] else '')
            elif count_vertical==count:
                return (count,i,j-1,'')
            else: #count_horizonal==count
                return (count,i-1,j,'')
            
        m1=len(string1)+1
        m2=len(string2)+1
        s=[]
        for i in range(m1):
            ss=[]
            for j in range(m2):
                ss.append((0,-1,-1,''))
            s.append(ss)
        for i in range(1,m1):    
            for j in range(1,m2):
                s[i][j]=new_s(i,j,s)
        return s
    
    # Build string from status
    
    def construct_string(s):
        i=len(string1)
        j=len(string2)
        result=[]
        while i>-1 and j>-1:
            _,i,j,chars=s[i][j]
            result.append(chars)
        return ''.join(result[::-1])
    
    return construct_string(longest_path())

# BA5D 	Find the Longest Path in a DAG  	
#
# Input: An integer representing the source node of a graph, followed by an integer
#        representing the sink node of the graph, followed by an edge-weighted graph. 
#        The graph is represented by a modified adjacency list in which the notation "0->1:7"
#        indicates that an edge connects node 0 to node 1 with weight 7.
#
# Return: The length of a longest path in the graph, followed by a longest path. 
#         (If multiple longest paths exist, you may return any one.)
#
# http://rosalind.info/problems/ba5d/

def longest_path(source,sink,graph):
    def initialize_s():
        s={}
        for a,b,_ in graph:
            s[a]=-float_info.max
            s[b]=-float_info.max
        s[source]=0
        return s
    
    def create_adjacency_list():
        adjacency_list={}
        for a,b,w in graph:
            if not a in adjacency_list:
                adjacency_list[a]=[]
            adjacency_list[a].append(b)
        return adjacency_list
   
    def create_weights():
        weights={}
        for a,b,w in graph:
            weights[(a,b)]=w
        return weights
        
    def calculate_distances(ordering):
        s=initialize_s()
        weights=create_weights()        
        predecessors={}
        for b in ordering:
            for a in ordering:
                if a==b:
                    break
                
                new_s=max(s[b],s[a]+(weights[(a,b)] if (a,b) in weights else 0))
                if new_s>s[b]:
                    s[b]=new_s
                    predecessors[b]=a
        return (s,predecessors)
   
    def create_path(predecessors):
        path=[sink]
        node=sink
        while node in predecessors:
            node=predecessors[node]
            path.append(node)
        return path
    
    s,predecessors=calculate_distances(topological_order(create_adjacency_list()))
    
    return (s[sink],create_path(predecessors)[::-1])

# BA5F 	Find a Highest-Scoring Local Alignment of Two Strings  
#
# common code

# BA5E 	Find a Highest-Scoring Alignment of Two Strings
# create_distance_matrix
def create_distance_matrix(nrows,ncolumns,initial_value=-float_info.max):
    s=[]
    for i in range(nrows):
        row=[]
        for j in range(ncolumns):
            row.append(initial_value)        
        s.append(row)
    s[0][0]=0
    return s

def calculate_scores_for_alignment(s,string1, string2, weights,sigma,init_predecessors=None):
    predecessors={}
    for i in range(len(string1)+1):
        for j in range(len(string2)+1):
            predecessors[(i,j)]=init_predecessors
            if i>0:
                s_new = s[i-1][j]-sigma
                if s_new>s[i][j]:
                    s[i][j]             = s_new
                    predecessors[(i,j)] = (-1,0,i-1,j)
            if j>0:
                s_new = s[i][j-1]-sigma
                if s_new>s[i][j]:
                    s[i][j]             = s_new
                    predecessors[(i,j)] = (0,-1,i,j-1)            
                if i>0:
                    s_new = s[i-1][j-1]+score((string1[i-1],string2[j-1]),weights)
                    if s_new>s[i][j]:
                        s[i][j]             = s_new
                        predecessors[(i,j)] = (-1,-1,i-1,j-1)
    return (s,predecessors)

def create_alignment(string1, string2,s_predecessors,i_start=-1,j_start=-1):
    s,predecessors = s_predecessors
    result1        = []
    result2        = []
    i              = len(string1) if i_start==-1 else i_start
    j              = len(string2) if j_start==-1 else j_start
    while i>0 or j>0:
        x,y,i,j=predecessors[(i,j)]
        if x==-1 and y==0:
            result1.append(string1[i])
            result2.append('-')
        elif x==0 and y==-1:
            result1.append('-')
            result2.append(string2[j])
        elif x==-1 and y==-1:
            result1.append(string1[i])
            result2.append(string2[j])
        
    return (s[len(string1)][len(string2)],\
            ''.join(result1[::-1]),       \
            ''.join(result2[::-1]))

# BA5E 	Find a Highest-Scoring Alignment of Two Strings
# Find the highest-scoring alignment between two strings using a scoring matrix.
#blo
# Input: Two amino acid strings.
#
# Return: The maximum alignment score of these strings followed by an
#         alignment achieving this maximum score. Use the BLOSUM62 scoring matrix
#         and indel penalty σ = 5. (If multiple alignments achieving the maximum 
#         score exist, you may return any one.)



# BA5F 	Find a Highest-Scoring Local Alignment of Two Strings 
#
# Input: Two amino acid strings.
#
# Return: The maximum score of a local alignment of the strings, followed by
# a local alignment of these strings achieving the maximum score. Use the
# PAM250 scoring matrix and indel penalty  5. (If multiple local alignments
# achieving the maximum score exist, you may return any one.)



# create_distance_matrix
def create_distance_matrix(nrows,ncolumns):
    distances = []
    for i in range(nrows):
        distances.append([0]*ncolumns)
 
    return distances

def get_indel_cost(sigma,delta,i,j,di,dj,moves):
    return di,dj,sigma



def backtrack(s,t,matrix,moves,showPath=False):
    i     = len(s)
    j     = len(t)
    score = matrix[i][j]
    s1    = []
    t1    = []
    if showPath:
        print ('Path')
        print (i,j)
    while i>0 and j>0:
        i,j,di,dj = moves[(i,j)]
        if di==0:
            s1.append('-')
            t1.append(t[j])
        elif dj==0:
            s1.append(s[i])
            t1.append('-')
        else:
            s1.append(s[i])
            t1.append(t[j])
        if showPath:
            print (i,j,di,dj,s1[-1],t1[-1] )
    return score,s1[::-1],t1[::-1]


# EDIT 	Edit Distance http://rosalind.info/problems/edit/

def edit(s,t,indel_cost=1,replace_cost=lambda a,b: 1,show_matrix=False):
    
    def dynamic_programming(s,t):
        matrix=[[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    
        for j in range(len(t)+1):
            matrix[0][j]=j
        for i in range(len(s)+1):
            matrix[i][0]=i

        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                matrix[i][j] = min(
                    matrix[i-1][j]   + indel_cost,
                    matrix[i][j-1]   + indel_cost,
                    matrix[i-1][j-1] + (0 if s[i-1]==t[j-1] else replace_cost(s[i-1],t[j-1])))
                    
        if show_matrix:
            for i in range(0,len(s)+1):
                ii = len(matrix)-i-1
                print (s[ii] if i>0 else '#',matrix[ii])
            print (' ',['#']+t)
        
        return matrix[len(s)][len(t)],matrix
            
    return dynamic_programming([s0 for s0 in s], [t0 for t0 in t])

# EDTA Edit Distance Alignment http://rosalind.info/problems/edta/

def edta(s,t,indel_cost=1,replace_cost=lambda a,b: 1):
    def extract(s,t,matrix):
        m  = len(matrix)-1
        n  = len(matrix[0])-1
        s1 = []
        t1 = []
        while m>0 and n>0:
            moves  = [(m-1,n),(m,n-1),(m-1,n-1)]
            scores = [matrix[m-1][n]+indel_cost,
                      matrix[m][n-1]+indel_cost,
                      matrix[m-1][n-1] + (0 if s[m-1]==t[n-1] else replace_cost(s[m-1],t[n-1]))]
            ss     = [s[m-1],'-',s[m-1]]
            ts     = ['-',t[n-1],t[n-1]]
            index  = argmin(scores)
            m,n    = moves[index]
            s1.append(ss[index])
            t1.append(ts[index])
        s1.reverse()
        t1.reverse()
        return ''.join(s1),''.join(t1)
    d,matrix = edit(s,t,indel_cost,replace_cost)
    s1,t1    = extract([s0 for s0 in s], [t0 for t0 in t],matrix)
    return (d,s1,t1)

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
    
        return distance,v1[::-1],w1[::-1]
    
    score,u1,v1=dynamic_programming([vv for vv in v],[ww for ww in w])
    return score,''.join(u1),''.join(v1)
    

    
# BA5N 	Find a Topological Ordering of a DAG 
#
# Input: The adjacency list of a graph (with nodes represented by integers).
#
# Return: A topological ordering of this graph.

def topological_order(graph):
    def number_incoming(node):
        n=0
        for out in graph.values():
            if node in out:
                n+=1
        return n
    
    ordering=[]
    candidates=[node for node in graph.keys() if number_incoming(node)==0]
    while len(candidates)>0:
        a=candidates.pop()
        ordering.append(a)
        if a in graph:
            bs=[b for b in graph[a]]
            del graph[a]
            for b in bs:
                if number_incoming(b)==0:
                    candidates.append(b)
                    
    if len(graph)>0:
        raise RosalindException('Input graph is not a DAG')
    
    return ordering


def unwind_moves(moves,score,i,j):
    ss = []
    ts = []

    while i>0 and j > 0:
        i,j,s0,t0=moves[(i,j)]
        ss.append(s0)
        ts.append(t0)
    return score,ss[::-1],ts[::-1]
    


# FindHighestScoringMultipleSequenceAlignment
#
# BA5M.py Find a Highest-Scoring Multiple Sequence Alignment 

def FindHighestScoringMultipleSequenceAlignment (u,
                                                 v,
                                                 w,
                                                 score=lambda x,y,z: 1 if x==y and y==z and x!='-' else 0):
    def build_matrix():
        s = [[[0 for i in range(len(w)+1)] for j in range(len(v)+1)] for k in range(len(u)+1) ]
        path = {}
                  
        for i in range(1,len(u)+1):
            for j in range(1,len(v)+1):
                for k in range(1,len(w)+1):
                    scores     = [
                        s[i-1][j-1][k-1] + score(u[i-1], v[j-1], w[k-1]),
                        s[i-1][j][k]     + score(u[i-1], '-',    '-'),
                        s[i][j-1][k]     + score('-',    v[j-1], '-'),
                        s[i][j][k-1]     + score('-',    '-',    w[k-1]),
                        s[i][j-1][k-1]   + score('-',    v[j-1], w[k-1]),
                        s[i-1][j][k-1]   + score(u[i-1], '-',    w[k-1]),
                        s[i-1][j-1][k]   + score(u[i-1], v[j-1], '-'),
     
                    ]
                    moves = [
                        (-1, -1, -1),
                        (-1,  0,  0),
                        ( 0, -1,  0),
                        ( 0,  0, -1),
                        ( 0, -1, -1),
                        (-1,  0, -1),
                        (-1, -1,  0),
     
                    ]
                    index          = argmax(scores)
                    s[i][j][k]     = scores[index]
                    path[(i,j,k)] = moves[index]
        return s,path
    
    def backtrack(path):
        i  = len(u)
        j  = len(v)
        k  = len(w)
        u1 = []
        v1 = []
        w1 = []
        while i>0 and j>0 and k>0:
            di,dj,dk = path[(i,j,k)]
            i        += di
            j        += dj
            k        += dk
            if dj==0 and dk==0:
                u1.append(u[i])
                v1.append('-')
                w1.append('-')
            elif di==0 and dk==0:
                u1.append('-')
                v1.append(v[j])
                w1.append('-')
            elif di==0 and dj==0:
                u1.append('-')
                v1.append('-')
                w1.append(w[k])
            elif di==0:
                u1.append('-')
                v1.append(v[j])
                w1.append(w[k])
            elif dj==0:
                u1.append(u[i])
                v1.append('-')
                w1.append(w[k])
            elif dk==0:
                u1.append(u[i])
                v1.append(v[j])
                w1.append('-')
            else:
                u1.append(u[i])
                v1.append(v[j])
                w1.append(w[k])        
        while i>0:
            i-=1
            u1.append(u[i])
            v1.append('-')
            w1.append('-')
        while j>0:
            j-=1
            u1.append('-')
            v1.append(v[j])
            w1.append('-')
        while k>0:
            k-=1
            u1.append('-')
            v1.append('-')
            w1.append(w[k])
        return u1,v1,w1
    
    s,path   = build_matrix()
    u1,v1,w1 = backtrack(path)
    
    return s[len(u)][len(v)][len(w)],''.join(u1[::-1]),''.join(v1[::-1]),''.join(w1[::-1])             
 
         

                    
