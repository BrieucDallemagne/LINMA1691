import pathfinder_hw as pf


"""
Loads the graph contained in file.
"""
def load_graph(file_name):
    graph = []
    with open(file_name,'r') as file:
        txt = file.read().split("\n")
        for line in txt[1:-1]:
            adj = []
            for node in line.split(","):
                adj.append(int(node))
            graph.append(adj)
        while(len(graph) != int(txt[0])):
            graph.append([])
    return graph

"""
Translate a graph from adjacency list to file representation.
"""
def from_adj_to_str(graph):
    output = str(len(graph))
    for line in graph:
        output += "\n"
        for adj in line:
            output += str(adj) + ","
        output = output[:-1]
    output += "\n"
    return output

"""
Writes a graph into file_name.
"""
def save_graph(file_name,graph):
    with open(file_name,'w') as file:
        file.write(from_adj_to_str(graph))

"""
test if the eulerian_path_finder function works correctly
Pour vous aider, quelques graphes vous sont donnés dans des fichiers textes 2
. Dans chacun des fichier, la
première ligne annonce le nombre de noeuds et chacune des lignes suivantes donne la liste d’adjacence du
noeud correspondant. Une fonction de lecture des fichier test donnant un input utilisable vous est également
fourni. Les solutions n’étant pas uniques pour un graphe donné, il ne tient qu’à vous de vérifier les réponses
de votre fonction.
"""
def test_eulerian_path_finder():
    graph = load_graph("test_01.txt")
    print(pf.eulerian_path_finder(graph))
    graph = load_graph("test_02.txt")
    print(pf.eulerian_path_finder(graph))
    graph = load_graph("test_03.txt")
    print(pf.eulerian_path_finder(graph))
    graph = load_graph("test_04.txt")
    print(pf.eulerian_path_finder(graph))
    graph = load_graph("test_05.txt")
    print(pf.eulerian_path_finder(graph))
    graph = load_graph("test_06.txt")
    print(pf.eulerian_path_finder(graph))
    graph = load_graph("test_07.txt")
    print(pf.eulerian_path_finder(graph))
    graph = load_graph("test_08.txt")
    print(pf.eulerian_path_finder(graph))
    graph = load_graph("test_09.txt")
    print(pf.eulerian_path_finder(graph))

test_eulerian_path_finder()
