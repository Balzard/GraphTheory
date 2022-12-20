from collections import deque
import math

class Edge:
    def __init__(self, u, v, capa, weight, residual=None):
        self.u: int = u # noeud source
        self.v: int = v # noeud dest
        self.capa: int = capa  # capacity that there is left to the edge
        self.weight: int = weight  # weight of the edge, cost
        self.residual: Edge = residual  # corresponding edge in the residual graph


def create_graph(capacities, costs, green_sources: dict, gas_centrals: dict, consumers: dict):

    # TODO

    s = 0
    t = 0
    graph = []
    return s, t, graph


def get_residual(graph: list[Edge]) -> list[Edge]:
    graph_residual = [[] for _ in range(len(graph))]
    for vertex in graph:
        edge: Edge
        for edge in vertex:
            edge.residual = Edge(edge.v, edge.u, 0, - edge.weight)
            graph_residual[edge.u].append(edge)
            graph_residual[edge.v].append(Edge(edge.v, edge.u, 0, - edge.weight, edge))
    return graph_residual


def min_cost_max_flow(s: int, t: int, graph_residual: list[Edge]):
    
    # La recherche de ce chemin augmentant optimal revient à un problème de plus court chemin où les arêtes sont pondérées par leurs coûts
    # on va choisir le chemin augmentant minimisant le coût par unité de flot

    def BreadthFirstSearch(graph_residual: list[Edge], s: int, t: int, parents: list[int]) -> bool:
        visited = [False]*(len(graph_residual) + 1)
        Q = deque()
        Q.append(s)
        visited[s] = True
        distance = [math.inf] * (len(graph_residual) + 1)
        distance[s] = 0

        while Q:
            u = Q.popleft()

            edge: Edge
            for edge in graph_residual[u]:
                if visited[edge.v] == False and edge.capa > 0 and edge.weight + distance[edge.u] < distance[edge.v]:
                    distance[edge.v] = edge.weight + distance[edge.u]
                    if edge.v not in Q:
                        Q.append(edge.v)
                    visited[edge.v] = True
                    parents[edge.v] = u
                    if edge.v == t:
                        return True
        return False

    maximum_flow = 0
    minimum_cost = 0
    parents = [-1] * (len(graph_residual) + 1)
    visited = []
    
    while BreadthFirstSearch(graph_residual, s, t, parents):
        pathFlow = float("Inf")
        j = t
        while(j != s):
            edge: Edge
            for edge in graph_residual[parents[j]]:
                if edge.v == j:
                    pathFlow = min(pathFlow, edge.capa)
                    j = parents[j]
                    break
        
        maximum_flow += pathFlow

        v = t
        while(v != s):
            u = parents[v]
            for edge in graph_residual[u]:
                if edge.v == v:
                    minimum_cost += edge.capa * edge.weight
                    edge.capa -= pathFlow
                    edge.residual.capa += pathFlow
            v = parents[v]

    return maximum_flow, minimum_cost


if __name__ == "__main__":
    graph = [[Edge(0,1,16,0), Edge(0,2,13,0)], [Edge(1,2,10,0), Edge(1,3,12,0)], [Edge(2,1,4,0), Edge(2,4,14,0)],
             [Edge(3,2,9,0), Edge(3,5,20,0)], [Edge(4,3,7,0), Edge(4,5,4,0)], []]
    
    graph1 = [[Edge(0,1,8,0), Edge(0,4,3,0)], [Edge(1,2,9,0)], [Edge(2,5,2,0)], [Edge(3,5,5,0)], [Edge(4,3,4,0), Edge(4,2,7,0)], []]
    
    graph2 = [[Edge(0,1,4,0), Edge(0,2,3,0)], [Edge(1,3,4,0)], [Edge(2,4,6,0)], [Edge(3,2,3,0), Edge(3,5,2,0)], [Edge(4,5,6,0)], []]
    
    graph3 = [[Edge(4,0,2,0), Edge(4,1,2,1)], [Edge(0,1,4,0), Edge(0,2,1,0)], [Edge(1,3,1,0), Edge(1,5,2,1000)], [Edge(2,3,4,0)], [Edge(3,5,2,0)], []]
    
    max_flow, min_cost = min_cost_max_flow(4,5,graph_residual=get_residual(graph3))
    print(max_flow, min_cost)
    
    
    
    # def BellmanFord():
    # distance = [math.inf] * (len(graph_residual) + 1)
    # distance[s] = 0
    # parents = [None] * len(graph_residual + 1)
    # for _ in range(len(graph_residual) + 1):
    #     for edge in graph_residual:
    #         if distance[edge.u] + edge.weight < distance[edge.v]:
    #             distance[edge.v] = edge.weight + distance[edge.u]
    #             parents[edge.v] = edge.u
        
    # return parents
    
    # # Check for negative weight cycles
    # for u, v, weight in graph.edges():
    #     if distances[u] + weight < distances[v]:
    #         raise ValueError("Graph contains a negative weight cycle")

    # # Create a dictionary to store the shortest paths
    # shortest_paths = {}

    # # Find the shortest path for each destination node
    # for destination in graph:
    #     # Start from the destination node and trace back through the predecessors
    #     # until you reach the source node
    #     path = []
    #     node = destination
    #     while node is not None:
    #         path.append(node)
    #         node = predecessors[node]

    #     # Reverse the path to get the correct order
    #     path = path[::-1]

    #     # Add the path to the dictionary
    #     shortest_paths[destination] = path

