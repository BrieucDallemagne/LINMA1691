"""
    Student template for the third homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""

import math
import heapq
    
def prim_mst(N, roads):
    """ 
    INPUT : 
        - N, the number of crossroads
        - roads, list of tuple (u, v, s) giving a road between u and v with satisfaction s
    OUTPUT :
        - return the maximal satisfaction that can be achieved
        
        See homework statement for more details
    """

    satisfaction = 0
    sum_satisfaction = 0

    dict_adj = {}
    for i in range(N):
        dict_adj[i] = []

    for i,j,k in roads:
        dict_adj[i].append((j,k))
        dict_adj[j].append((i,k))
        sum_satisfaction += k
    
    visited = [False]*N
    heap = []
    heapq.heappush(heap,(0,0))
    while heap:
        s, u = heapq.heappop(heap)
        if not visited[u]:
            visited[u] = True
            satisfaction += s
            for v, s in dict_adj[u]:
                if not visited[v]:
                    heapq.heappush(heap,(s,v))
                    
    satisfaction = sum_satisfaction - satisfaction

    return satisfaction

    
if __name__ == "__main__":

    # Read Input for the first exercice
    
    with open('in1.txt', 'r') as fd:
        l = fd.readline()
        l = l.rstrip().split(' ')
        
        n, m = int(l[0]), int(l[1])
        
        roads = []
        for road in range(m):
        
            l = fd.readline().rstrip().split()
            roads.append(tuple([int(x) for x in l]))
            
    # Compute answer for the first exercice
     
    ans1 = prim_mst(n, roads)
     
    # Check results for the first exercice

    with open('out1.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)
        
        if expected_output == ans1:
            print("Exercice 1 : Correct")
        else:
            print("Exercice 1 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans1, expected_output)) 
        

