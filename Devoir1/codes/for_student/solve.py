from collections import deque

"""
    Solves the problem defined in the statement for adj an adjacency list of the dispersion dynamics of rumors in LLN
        adj is a list of length equal to the number of kots
        adj[i] gives a list of kots touched by i with direct edges (0-based)

    You are free to change the code below and to not use the precompleted part. The code is based on the high-level description at https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm
    You can also define other sub-functions or import other datastructures from the collections library
"""
def solve(adj) :
    ### Initialization
    N = len(adj) # number of nodes
    visited = [False]*N # is a node already visited?
    L = [] # list of node to process in the second step
    q = deque() # queue of nodes to process with their associated status (i,False/True) i is the node index and True/False describes if we are appending the node to L or not when processing it

    ### Step 1 : Depth-first search on adj
    for u in range(N) :
        if visited[u] : continue
        visited[u] = True
        q.append((u,False))
        while q :
            x,to_append = q.pop()

            if to_append:
                L.append(x)
                continue

            q.append((x,True)) # When we will have process all the nodes linked to x, we can append x to L
            for e in adj[x] : 
                if not visited[e] :
                    q.append((e,False))
                    visited[e] = True

    ### reverse the list to obtain the post-order
    L.reverse()
    adj_T = transpose(adj) # transpose of adj

    ### Step 2 : Depth-first search on adj_T : find the strongly connected components
    assigned = [False]*N # is a node already visited?
    SCC = list() # List of the roots of the strongly connected components
    q = deque()

    for u in L :
        if assigned[u] : continue
        else : SCC.append(u)
        assigned[u] = True
        q.append(u)
        while q :
            x = q.pop()
            for e in adj_T[x] :
                if assigned[e] : continue
                assigned[e] = True
                q.append(e)
        
    # TODO : Find the kap at the roots of the SCC
    """
    i = 0
    while (i < len(SCC)) :
        start = list[i]
        for j in range (len(SCC)) :
            if i==j : continue
    """

    return len(SCC)

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