from collections import deque


"""
    Solves the problem defined in the statement for adj an adjacency list of the dispersion dynamics of rumors in LLN
        adj is a list of length equal to the number of kots
        adj[i] gives a list of kots touched by i with direct edges (0-based)
    You are free to change the code below and to not use the precompleted part. The code is based on the high-level description at https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm
    You can also define other sub-functions or import other datastructures from the collections library
"""
def solve(adj):
   
    adj_out = adj
    adj_in = transpose(adj_out)

 
    N = len(adj_in)

  
    visited = [False]*N

    L = []
    
    q = deque()

    for x in range(N):
        q.append((x,False))

        while q:
            x,to_append = q.pop()

            if to_append:
                L.append(x)
                continue

            q.append((x,True))
            for e in adj_in[x]:
                if not visited[e]:
                    q.append((e,False))
                    visited[e] = True
            
    

        


    ### reverse the list to obtain the post-order
    L.reverse()


    ### find the strongly connected components

    assigned = [False]*N
    SCC = list()
    q = deque()

    for x in L:
        if assigned[x]: continue
        else: SCC.append(x)
        assigned[x] = True
        q.append(x)
        while q:
            x = q.pop()
            for e in adj_out[x]:
                if assigned[e]: continue
                assigned[e] = True
                q.append(e)
    
    # TODO : Find the kap at the roots of the SCC
    new_adj = [list() for _ in range(len(SCC))]
    for i in range(len(SCC)):
        for j in range(len(adj_out[SCC[i]])):
            if adj_out[SCC[i]][j] in SCC:
                new_adj[i].append(SCC.index(adj_out[SCC[i]][j]))

    q = deque()
    visited = [False]*len(new_adj)
    sources = len(new_adj)
    for i in range(len(new_adj)):
        if visited[i]: continue
        visited[i] = True
        q.append(i)
        while q:
            x = q.pop()
            for e in new_adj[x]:
                if visited[e]: continue
                visited[e] = True
                q.append(e)
            sources -= 1
    
    return sources


"""
    Transpose the adjacency matrix
        Construct a new adjacency matrix by inverting all the edges: (x->y) becomes (y->x) 
"""
def transpose(adj) :
    adj_T = [list() for _ in range(len(adj))]
    for i in range (len(adj)) :
        for j in range (len(adj[i])) :
            adj_T[adj[i][j]].append(i)
    return adj_T