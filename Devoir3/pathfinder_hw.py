import copy

"""
Calcule un chemin eulérien dans graph et le retourne comme une liste de noeuds visités.
Si aucun chemin eulérien n'existe, la fonction retourne None.
L'argument graph ne doit pas être modifié lors de l'exécution de la fonction.
"""
def eulerian_path_finder(g) :
    graph = copy.deepcopy(g)
    eulerian_path = []
    n = len(graph)
    subpaths = set()

    nbr_odd = 0
    for i in range(n) :
        if len(graph[i]) % 2 == 1 :
            nbr_odd += 1
    if (nbr_odd not in (0, 2)) : return None

    for i in range (n) :
        subpath = [i]
        while (len(graph[subpath[-1]]) != 0) :
            subpath.append(graph[subpath[-1]][0])
            graph[subpath[-1]].remove(subpath[-2])
            graph[subpath[-2]].remove(subpath[-1])
        if (len(subpath) > 1) : subpaths.add(tuple(subpath))

    eulerian_path = list(subpaths.pop())
    while (len(subpaths) != 0) :
        subpath = list(subpaths.pop())
        if (subpath[0] == subpath[-1] and subpath[0] in eulerian_path) :
            x = eulerian_path.index(subpath[0])
            eulerian_path = eulerian_path[:x] + subpath + eulerian_path[x+1:]
        elif (eulerian_path[0] == eulerian_path[-1] and eulerian_path[0] in subpath) :
            x = subpath.index(eulerian_path[0])
            eulerian_path = subpath[:x] + eulerian_path + subpath[x+1:]
        else : subpaths.add(tuple(subpath))

    return eulerian_path