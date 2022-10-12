from collections import deque

# recursive kosaraju
class Kosaraju:
    
    def __init__(self, adj) -> None:
        self.adj = adj
        self.N = len(adj)
        self.transpose = [[] for _ in range(self.N)]
        self.visited = [False] * self.N
        self.L = deque()
        self.components = [None] * self.N
        
    def _visit(self, vertex):
        if not self.visited[vertex]:
            self.visited[vertex] = True
            for neighbor in self.adj[vertex]:
                self._visit(neighbor)
                self.transpose[neighbor].append(vertex)
            self.L.append(vertex)
            
    def _assign(self, u, r):
        if self.visited[u]:
            self.visited[u] = False
            self.components[u] = r
            for neighbor in self.transpose[u]:
                self._assign(neighbor, r)
                
    def computeComponents(self):
        for i in range(self.N):
            self._visit(i)
            
        while self.L:
            u = self.L.pop()
            self._assign(u,u)
            
        return self
    
    def getNbSCC(self):
        return len(set(self.components))
    
    def getMinNbOfKots(self):
        # need to compute nb of SCC with incoming edges
        nbSCC = self.getNbSCC() 
        sccWithIncomingEdges = [0 for _ in range(self.N)]

        for i in range(self.N): 
            for x in self.adj[i]: 
                if self.components[x] != self.components[i]: # not in the same SCC
                    sccWithIncomingEdges[self.components[x]] = 1
                    
        return nbSCC - sum(sccWithIncomingEdges)
    
    
class IterativeKosaraju(Kosaraju):
    
    def __init__(self, adj) -> None:
        super().__init__(adj)
        
    def computeComponents(self):
        for vertex in range(self.N):
            if not self.visited[vertex]:
                self.visited[vertex], stack = True, [vertex]
                while stack:
                    vertex = stack[-1]
                    for neighbor in self.adj[vertex]:
                        self.transpose[neighbor].append(vertex)
                        if not self.visited[neighbor]:
                            self.visited[neighbor] = True
                            stack.append(neighbor)
                            break
                    else:
                        stack.pop()
                        self.L.append(vertex)
                        
        while self.L:
            root = self.L.pop()
            stack = [root]
            if self.visited[root]:
                self.visited[root], self.components[root] = False, root
            while stack:
                for neighbor in self.transpose[stack[-1]]:
                    if self.visited[neighbor]:
                        self.visited[neighbor] = False
                        stack.append(neighbor)
                        self.components[neighbor] = root
                        break
                else:
                    stack.pop()
        
        return self

def solve(adj):
    graph = IterativeKosaraju(adj)
    return graph.computeComponents().getMinNbOfKots()