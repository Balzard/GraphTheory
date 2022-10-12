from collections import deque
from pydoc import visiblename

class Kosaraju:
    
    def __init__(self, adj) -> None:
        self.adj = adj
        self.transpose = [[x for x in range(len(adj)) if y in adj[x]] for y in range(len(adj))]
        self.N = len(adj)
        self.visited = [False] * self.N
        self.stack = deque()
        self.components = [None] * self.N
        
    def _visit(self, vertex):
        if not self.visited[vertex]:
            self.visited[vertex] = True
            for neighbor in self.adj[vertex]:
                self._visit(neighbor)
            self.stack.append(vertex)
            
    def _assign(self, u, r):
        if self.visited[u]:
            self.visited[u] = False
            self.components[u] = r
            for neighbor in self.transpose[u]:
                self._assign(neighbor, r)
                
    def getComponents(self):
        for i in range(self.N):
            self._visit(i)
            
        while self.stack:
            u = self.stack.pop()
            self._assign(u,u)
            
        return self.components
    
    
class IterativeKosaraju(Kosaraju):
    
    def __init__(self, adj) -> None:
        super().__init__(adj)
    
    def getComponents(self):
        for vertex in range(self.N):
            if not self.visited[vertex]:
                self.visited[vertex], S = True, [vertex]
                while S:
                    vertex, done = S[-1], True
                    for neighbor in self.adj[vertex]:
                        if not self.visited[neighbor]:
                            self.visited[neighbor], done = True, False
                            S.append(neighbor)
                            break
                        if done:
                            S.pop()
                            self.stack.append(vertex)
                            
        while self.stack:
            r = self.stack.pop()
            S = [r]
            if self.visited[r]:
                self.visited[r], self.components[r] = False, r
            while S:
                u, done = S[-1], True
                for neighbor in self.transpose[u]:
                    if self.visited[neighbor]:
                        self.visited[neighbor] = done = False
                        S.append(neighbor)
                        self.components[neighbor] = r
                        break
                    
                if done:
                    S.pop()
                    
        return self.components



def kosaraju_iterative(G):
    
    # postorder DFS on G to transpose the graph and push root vertices to L
    N = len(G)
    T, L, U = [[] for _ in range(N)], [], [False] * N
    for u in range(N):
        if not U[u]:
            U[u], S = True, [u]
            while S:
                u, done = S[-1], True
                for v in G[u]:
                    T[v].append(u)
                    if not U[v]:
                        U[v], done = True, False
                        S.append(v)
                        break
                if done:
                    S.pop()
                    L.append(u)
    
    # postorder DFS on T to pop root vertices from L and mark SCCs
    C = [None] * N
    while L:
        r = L.pop()
        S = [r]
        if U[r]:
            U[r], C[r] = False, r
        while S:
            u, done = S[-1], True
            for v in T[u]:
                if U[v]:
                    U[v] = done = False
                    S.append(v)
                    C[v] = r
                    break
            if done:
                S.pop()
    
    return C

def SCC_to_min_kot(sol,adj):
    unique= len(set(sol)) # number of scc in graph
    tmp = [0 for _ in range(max(sol)+1)]  #tmp is used to keep track of the SCC which have an incoming node

    for i in range(len(adj)): #we loop over the edges knowing it starts from node i
        for x in adj[i]: #This means that there is an edge from i to x
            if (sol[x] != sol[i]): #If they are not in the same SCC
                tmp[sol[x]]=1
    return(unique-sum(tmp)) #(nb min kot) = (nb SCC) - (nbr SCC which have incoming edge)
      
def solve(adj):
    g = IterativeKosaraju(adj)
    l = g.getComponents()
    return SCC_to_min_kot(l, adj)  

# adj = [[1], [0, 2], [0, 3, 4], [4], [5], [6], [4], [6]]
# g = IterativeKosaraju(adj)
# c = g.getComponents()
# print(c)

# class Graph:
    
#     def __init__(self, matrix) -> None:
#         self.matrix = matrix
#         self._visited = [False] * len(self.matrix)
#         self._stack = deque()
#         self.nbSCC = 0
#         self.transpose = [[x for x in range(len(matrix)) if y in matrix[x]] for y in range(len(matrix))]
        
#     def dfs(self, vertex: int) -> None:
#         self._visited[vertex] = True
#         for i in self.transpose[vertex]:
#             if not self._visited[i]:
#                 self.dfs(i)
        
            
#     def fillOrder(self, vertex: int) -> None:
#         self._visited[vertex] = True
#         for i in self.matrix[vertex]:
#             if not self._visited[i]:
#                 self.fillOrder(i)
#         self._stack.append(vertex)
        
    
#     def getNbSCC(self) -> int:
#         sol = [0 for _ in range(len(self.matrix))]
#         #1
#         for i in range(len(self.matrix)):
#             if not self._visited[i]:
#                 self.fillOrder(i)
        
#         self._visited = [False] * len(self.matrix)
        
#         #3
#         tmp = 0
#         while self._stack:
#             i = self._stack.pop()
#             if not self._visited[i]:
#                 self.dfs(i) # make with transpose
#                 sol[i] = tmp
#                 self.nbSCC += 1
#             tmp += 1
                
#         return sol


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
