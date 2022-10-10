from collections import deque


class Graph:
    
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self._visited = [False] * len(self.matrix)
        self._stack = deque()
        self.nbSCC = 0
        self.transpose = [[x+1 for x in range(len(matrix)) if y+1 in matrix[x]] for y in range(len(matrix))]
        
    def dfs(self, vertex: int) -> None:
        self._visited[vertex] = True
        for i in self.transpose[vertex]:
            if not self._visited[i]:
                self.dfs(i)
        
            
    def fillOrder(self, vertex: int) -> None:
        self._visited[vertex] = True
        for i in self.matrix[vertex]:
            if not self._visited[i]:
                self.fillOrder(i)
        self._stack.append(vertex)
        
    
    def getNbSCC(self) -> int:
        #1
        for i in range(len(self.matrix)):
            if not self._visited[i]:
                self.fillOrder(i)
        
        self._visited = [False] * len(self.matrix)
        
        #3
        while self._stack:
            i = self._stack.pop()
            if not self._visited[i]:
                self.dfs(i) # make with transpose
                self.nbSCC += 1
                
        return self.nbSCC
    

def solve(adj):
    graph = Graph(adj)
    nbSCC = graph.getNbSCC()
    return nbSCC

matrix = [[2],[3],[4,5],[1],[6],[7],[5,8],[]]
graph = Graph(matrix)
transpose = graph.transpose
print(transpose)
nbSCC = graph.getNbSCC()
print(nbSCC)


# """
#     Solves the problem defined in the statement for adj an adjacency list of the dispersion dynamics of rumors in LLN
#         adj is a list of length equal to the number of kots
#         adj[i] gives a list of kots touched by i with direct edges (0-based)

#     You are free to change the code below and to not use the precompleted part. The code is based on the high-level description at https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm
#     You can also define other sub-functions or import other datastructures from the collections library
# """
# def solve(adj):
#     # adjacency of the graph and its transpose
#     adj_out = adj
#     adj_in = transpose(adj_out)

#     # number of nodes
#     N = len(adj_in)

#     # is a node already visited?
#     visited = [False]*N
#     # list of node to process in the second step
#     L = []
#     # queue of nodes to process with their associated status (i,False/True) i is the node index and True/False describes if we are appending the node to L or not when processing it
#     q = deque()

#     ### loop on every node and launch a visit of its descendants
#     for x in range(N):
#         q.append((x,False))

#         while q:
#             x,to_append = q.pop()

#             if to_append:
#                 L.append(x)

#             # TO COMPLETE


#     ### reverse the list to obtain the post-order
#     L.reverse()


#     ### find the strongly connected components
    
#     # TO COMPLETE


#     ### compute answer
#     ans = 0
#     # TO COMPLETE

#     return ans

# """
#     Transpose the adjacency matrix
#         Construct a new adjacency matrix by inverting all the edges: (x->y) becomes (y->x) 
# """
# def transpose(adj):

#     return [[x+1 for x in range(len(adj)) if y+1 in adj[x]] for y in range(len(adj))]
