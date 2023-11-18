import copy
from collections import deque

def eulerian_path_finder(graph):
    new_graph = copy.deepcopy(graph)
    n = len(new_graph)

    eulerian_path = []
    stack = deque()
    
    visited_edges = list()
    for i in range(n):
        visited_edges.append([False] * n)

    "mettre l'algo ici j'y arrive pas"

    
    if len(eulerian_path) != len(graph) + 1:
        return None
    


    return eulerian_path