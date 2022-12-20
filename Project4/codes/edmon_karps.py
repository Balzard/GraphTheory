from typing import List, Tuple
from template import get_residual

class Edge:
    def __init__(self, u: int, v: int, capa: int, weight: int, residual: "Edge" = None):
        self.u = u
        self.v = v
        self.capa = capa
        self.weight = weight
        self.residual = residual

def min_cost_max_flow(s: int, t: int, graph_residual: List[List[Edge]]) -> Tuple[int, int]:
    # Initialize the maximum flow and minimum cost to 0
    max_flow = 0
    min_cost = 0
    
    # Initialize the distances and predecessor arrays for the Bellman-Ford algorithm
    distances = [float("inf")] * len(graph_residual)
    predecessor = [None] * len(graph_residual)
    
    # Run the Bellman-Ford algorithm to find the shortest path from s to t in the residual graph
    while True:
        updated = False
        
        # For each node in the residual graph
        for u in range(len(graph_residual)):
            # For each edge leaving from the node u
            for e in graph_residual[u]:
                # If the edge has residual capacity and the distance to the destination can be improved
                if e.capa > 0 and distances[e.v] > distances[u] + e.weight:
                    # Update the distance and the predecessor for the destination node
                    distances[e.v] = distances[u] + e.weight
                    predecessor[e.v] = e
                    updated = True
        
        # If no updates have been made, the algorithm has converged and we can stop
        if not updated:
            break
    
    # If a path from s to t has been found
    print(t)
    if distances[t] != float("inf"):
        # Compute the flow increment by following the predecessor chain from t to s
        flow_increment = float("inf")
        edge = predecessor[t]
        while edge is not None:
            flow_increment = min(flow_increment, edge.capa)
            edge = predecessor[edge.u]
        
        # Update the maximum flow and the minimum cost
        max_flow += flow_increment
        min_cost += flow_increment * distances[t]
        
        # Update the residual capacities and the flow along the path from s to t
        edge = predecessor[t]
        while edge is not None:
            edge.capa -= flow_increment
            edge.residual.capa += flow_increment
            edge = predecessor[edge.u]
    
    # Return the maximum flow and the minimum cost
    return max_flow, min_cost

if __name__ == "__main__":
    graph = [[Edge(0,1,16,0), Edge(0,2,13,0)], [Edge(1,2,10,0), Edge(1,3,12,0)], [Edge(2,1,4,0), Edge(2,4,14,0)],
             [Edge(3,2,9,0), Edge(3,5,20,0)], [Edge(4,3,7,0), Edge(4,5,4,0)], []]
    
    graph1 = [[Edge(0,1,8,0), Edge(0,4,3,0)], [Edge(1,2,9,0)], [Edge(2,5,2,0)], [Edge(3,5,5,0)], [Edge(4,3,4,0), Edge(4,2,7,0)], []]
    
    graph2 = [[Edge(0,1,4,0), Edge(0,2,3,0)], [Edge(1,3,4,0)], [Edge(2,4,6,0)], [Edge(3,2,3,0), Edge(3,5,2,0)], [Edge(4,5,6,0)], []]
    
    graph3 = [[Edge(4,0,2,0), Edge(4,1,2,1)], [Edge(0,1,4,0), Edge(0,2,1,0)], [Edge(1,3,1,0), Edge(1,5,2,1000)], [Edge(2,3,4,0)], [Edge(3,5,2,0)], []]
    
    graph_residual = [
    # Node 0
    [
        Edge(0, 1, 3, 5, residual=Edge(1, 0, 0, -5)),  # Edge 0' going from node 0 to node 1
        Edge(0, 2, 2, 2, residual=Edge(2, 0, 0, -2)),  # Edge 1' going from node 0 to node 2
    ],
    # Node 1
    [
        Edge(1, 2, 1, 1, residual=Edge(2, 1, 0, -1)),  # Edge 2' going from node 1 to node 2
        Edge(1, 3, 2, 3, residual=Edge(3, 1, 0, -3)),  # Edge 3' going from node 1 to node 3
    ],
    # Node 2
    [
        Edge(2, 3, 1, 2, residual=Edge(3, 2, 0, -2)),  # Edge 4' going from node 2 to node 3
        Edge(2, 4, 2, 1, residual=Edge(4, 2, 0, -1)),  # Edge 5' going from node 2 to node 4
    ],
    # Node 3
    [
        Edge(3, 4, 2, 1, residual=Edge(4, 3, 0, -1)),  # Edge 6' going from node 3 to node 4
    ],
    # Node 4
    [],  # No outgoing edges for node 4
]

    
    max_flow, min_cost = min_cost_max_flow(0,4,graph_residual=graph_residual)
    print(max_flow, min_cost)
