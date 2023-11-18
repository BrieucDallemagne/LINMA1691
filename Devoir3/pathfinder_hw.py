import copy

def eulerian_path_finder(graph):
    new_graph = copy.deepcopy(graph)
    n = len(new_graph)
    nbr_arete = 0
    eulerian_path = []
    nbr_odd = 0
    odd_node = []
    for i in range(n):
        if len(new_graph[i]) % 2 == 1:
            nbr_odd += 1
            odd_node.append(i)
        nbr_arete += len(new_graph[i])
    nbr_arete = nbr_arete // 2

    if nbr_odd > 2 or nbr_odd == 1:
        return None
    

    
    if odd_node:
        start = odd_node[0]
        end = odd_node[1] 
    else:
        start = 0
        end = 0

    
    
    eulerian_path.append(start)
    while new_graph[start]:
        if len(new_graph[end]) == 1 and end in new_graph[start] and len(new_graph[start]) > 1:
            new_graph[start].remove(end)
            next_node = new_graph[start].pop()
            new_graph[next_node].remove(start)
            eulerian_path.append(next_node)
            new_graph[start].append(end)
            start = next_node

        next_node = new_graph[start].pop()
        new_graph[next_node].remove(start)
        eulerian_path.append(next_node)
        start = next_node

    if len(eulerian_path) != nbr_arete + 1:
        return None
    
    return eulerian_path

