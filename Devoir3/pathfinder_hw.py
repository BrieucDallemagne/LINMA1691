import copy

"""
Calcule un chemin eulérien dans graph et le retourne comme une liste de noeuds visités.
Si aucun chemin eulérien n'existe, la fonction retourne None.
L'argument graph ne doit pas être modifié lors de l'exécution de la fonction.
"""
def eulerian_path_finder(graph):
    new_graph = copy.deepcopy(graph)
    n = len(new_graph)

    eulerian_path = []
    current_node = 0
    lst = n*[False]
    lst[current_node] = True
    eulerian_path.append(current_node)
    while len(eulerian_path) < n:
        for i in range(n):
            if new_graph[current_node][i] == 1 and lst[i] == False:
                current_node = i
                lst[i] = True
                eulerian_path.append(current_node)
                break
        else:
            return None


    return eulerian_path
