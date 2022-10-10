import sys
from collections import deque



"""
Prends comme inputs:
		-adj: liste d'adjacence du graphe dirigé décrivant la dynamique de dispersion des rumeurs
	output:
		-nombre solution du problème pour la dynamique donnée par adj
"""

def solve(adj):
    list_scc=kosaraju(adj) #retourne une liste de taille n (n le nombre de noeuds) ou iste_scc[i] = j signifie que i appartient a la scc numéro j
    sol=SCC_to_min_kot(list_scc,adj) #utilise la liste de scc pour trouver le nombre min de kots
    return sol


def kosaraju(adj): #DIRECT APPLICATION OF THE KOSARAJU ALGORITHM (IN ITERATIVE FORM)

    # postorder DFS on G to transpose the graph and push root vertices to L
    N = len(adj)
    T= [[] for _ in range(N)]
    L= []
    U= [False] * N
    for u in range(N):
        if not U[u]:
            U[u], S = True, [u]
            while S:
                u, done = S[-1], True
                for v in adj[u]:
                    T[v].append(u)
                    if not U[v]:
                        U[v], done = True, False
                        S.append(v)
                        break
                if done:
                    S.pop()
                    L.append(u)

    # postorder DFS on T to pop root vertices from L and mark SCCs
    sol = [None] * N
    while L:
        r = L.pop()
        S = [r]
        if U[r]:
            U[r], sol[r] = False, r
        while S:
            u, done = S[-1], True
            for v in T[u]:
                if U[v]:
                    U[v] = done = False
                    S.append(v)
                    sol[v] = r
                    break
            if done:
                S.pop()
    return sol

def SCC_to_min_kot(sol,adj):
    unique= len(set(sol)) # number of scc in graph
    tmp = [0 for _ in range(max(sol)+1)]  #tmp is used to keep track of the SCC which have an incoming node

    for i in range(len(adj)): #we loop over the edges knowing it starts from node i
        for x in adj[i]: #This means that there is an edge from i to x
            if (sol[x] != sol[i]): #If they are not in the same SCC
                tmp[sol[x]]=1
    return(unique-sum(tmp)) #(nb min kot) = (nb SCC) - (nbr SCC which have incoming edge)

matrix = [[1],[2],[3,4],[0],[5],[6],[4,7],[]]
sol = kosaraju(matrix)
print(sol)
