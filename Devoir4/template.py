from collections import deque

class Edge:
    def __init__(self, u, v, capa, weight, residual=None):
        self.u = u
        self.v = v
        self.capa = capa  # capacity that there is left to the edge
        self.weight = weight  # weight of the edge
        self.residual = residual  # corresponding edge in the residual graph


def create_graph(capacities, costs, green_sources: dict, gas_centrals: dict, consumers: dict):

    # TODO

    graph = [[] for _ in range(len(capacities) + 2)]
    s = len(graph)-2
    t = len(graph)-1

    for i in range (len(capacities)) :
        for j in range (len(capacities)) :
            if (capacities[i][j] > 0) : graph[i].append(Edge(i, j, capacities[i][j], costs[i][j]))

    for key, val in green_sources.items() : graph[s].append(Edge(s, key, val, 0))
    for key, val in gas_centrals.items() :
        previous = (0,0)
        for node in val[1:] :
            graph[s].append(Edge(s, key, node[0]-previous[0], (node[1]-previous[1])/(node[0]-previous[0])))
            previous = node

    for key, val in consumers.items() : graph[key].append(Edge(key, t, val, 0))
    return s, t, graph


def get_residual(graph):

    # TODO

    graph_residual = graph
    return graph_residual


def min_cost_max_flow(s, t, graph_residual):

    def BellmanFord():
    
        dist = [float('inf')] * len(graph_residual)
        dist[s] = 0 
        parents = [None] * len(graph_residual)
        marked = [False] * len(graph_residual)

        Q = deque()
        Q.append(s)
        marked[s] = True
        while Q:
            u = Q.pop()
            marked[u] = False
            for edge in graph_residual[u]:
                if edge.capa > 0 and dist[edge.v] > dist[u] + edge.weight:
                    dist[edge.v] = dist[u] + edge.weight
                    parents[edge.v] = edge
                    if not marked[edge.v] :
                        Q.append(edge.v)
                        marked[edge.v] = True

        path = deque()
        if parents[t] == None : return path
        current = parents[t]
        while (current.u != s) :
            path.append(current)
            current = parents[current.u]
        path.append(current)
        return path
    
    while True :
        path = BellmanFord()
        if (not path) : break
        flow = float('inf')
        for edge in path : flow = min(flow, edge.capa)
        for edge in path :
            if (edge.residual == None) : 
                residual = Edge(edge.v, edge.u, 0, -edge.weight, edge)
                edge.residual = residual
                graph_residual[edge.v].append(residual)
            edge.residual.capa += flow
            edge.capa -= flow
    
    maximum_flow = 0
    for edge in graph_residual[s] :
        if (edge.residual != None) : maximum_flow += edge.residual.capa

    minimum_cost = 0
    for node in graph_residual :
        for edge in node :
            if (edge.weight < 0 and edge.capa > 0) : minimum_cost -= edge.weight*edge.capa

    return maximum_flow, minimum_cost