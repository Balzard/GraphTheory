from collections import deque

# recursive kosaraju
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
                
    def computeComponents(self):
        for i in range(self.N):
            self._visit(i)
            
        while self.stack:
            u = self.stack.pop()
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


def iterativeKosaraju(adj):
    
    N = len(adj)
    transpose = [[] for _ in range(N)]
    visited = [False] * N
    L = deque()
    components = [None] * N

    for vertex in range(N):
        if not visited[vertex]:
            visited[vertex], stack = True, [vertex]
            while stack:
                vertex = stack[-1]
                for neighbor in adj[vertex]:
                    transpose[neighbor].append(vertex)
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
                        break
                    
                else:
                    stack.pop()
                    L.append(vertex)
                    
    while L:
        root = L.pop()
        stack = [root]
        if visited[root]:
            visited[root], components[root] = False, root
        while stack:
            for neighbor in transpose[stack[-1]]:
                if visited[neighbor]:
                    visited[neighbor] = False
                    stack.append(neighbor)
                    components[neighbor] = root
                    break
            else:
                stack.pop()
    
    return components


def getMinNbOfKots(components, adj):
    nbSCC = len(set(components)) 
    sccWithIncomingEdges = [0 for _ in range(len(adj))]

    for vertex in range(len(adj)): 
        for neighbor in adj[vertex]: 
            if components[neighbor] != components[vertex]: # not in the same SCC
                sccWithIncomingEdges[components[neighbor]] = 1
                
    return nbSCC - sum(sccWithIncomingEdges)


def solve(adj):
    components = iterativeKosaraju(adj)
    return getMinNbOfKots(components, adj)