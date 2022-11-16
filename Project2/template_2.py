"""
    Student template for the third homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""


import math
import random

class Union_Find():
    """
    Disjoint sets data structure for Kruskal's or Karger's algorithm.
  
    It is useful to keep track of connected components (find(a) == find(b) iff they are connected).  
  
    """
    
    def __init__(this, N):
        """
        Corresponds to MakeSet for all the nodes
        INPUT :
            - N : the initial number of disjoints sets
        """
        this.N = N
        this.p = list(range(N))
        this.size = [1]*N
        
    def union(this, a, b):
        """
        INPUT :
            - a and b : two elements such that 0 <= a, b <= N-1
        OUTPUT:
            - return nothing
            
        After the operation, the two given sets are merged
        """
        a = this.find(a)
        b = this.find(b)
       
        if a == b:
            return
       
        # Swap variables if necessary
        if this.size[a] > this.size[b]:
            a,b = b,a
        
        this.size[b] += this.size[a]
        this.p[a] = b
        
    def find(this, a):
        """
        INPUT :
            - a : one element such that 0 <= a <= N-1
        OUTPUT:
            - return the root of the element a
        """
        if a != this.p[a]: 
            this.p[a] = this.find(this.p[a])
        return this.p[a]
    

def min_cut(N, edges):
    """ 
    INPUT : 
        - N the number of nodes
        - edges, list of tuples (u, v) giving an edge between u and v

    OUTPUT :
        - return an estimation of the min cut of the graph
        
    This method has to return the correct answer with probability bigger than 0.999
    See project homework for more details
    """
    def karger(nodes, edges):
        """ 
        INPUT : 
            - N the number of nodes
            - edges, list of tuples (u, v) giving an edge between u and v

        OUTPUT :
            - return an estimation of the min cut of the graph
              
        See project homework for more details
        """
        
        this_min_cut, currentEdge = 0, 0
        uf = Union_Find(N)
        
        # TO COMPLETE
        
        def getSubsets(edge, uf):
            return uf.find(edge[0]), uf.find(edge[1])
        
        while nodes > 2:
            edge = edges[int((random.random()*10) % len(edges))]
            subset1, subset2 = getSubsets(edge, uf)
            if subset1 != subset2:
                uf.union(subset1, subset2)
                nodes -= 1
                currentEdge += 1
                this_min_cut += 1
            
                # if currentEdge == N-2:
                #     break
                
        # for edge in edges:
        #     subset1, subset2 = getSubsets(edge, uf)
        #     if subset1 != subset2:
        #         this_min_cut += 1

        return this_min_cut 
    
    # TO COMPLETE (apply karger several times)
    # Probability to return the true min cut should be at least 0.9999
    best = karger(N, edges)
    p = 2/(N*(N-1))
    k = -4/math.log10(1 - p)
    best = math.inf
    for _ in range(math.ceil(k) - 1):
        best = min(best, karger(N, edges))
    return best
    
   
if __name__ == "__main__":

    # Read Input for the second exercice
    
    with open('./for_student/Project2/in2.txt', 'r') as fd:
        l = fd.readline()
        l = l.rstrip().split(' ')
        
        n, m = int(l[0]), int(l[1])
        
        edges = []
        for edge in range(m):
        
            l = fd.readline().rstrip().split()
            edges.append(tuple([int(x) for x in l]))
            
    # Compute answer for the second exercice
     
    ans = min_cut(n, edges)
     
    # Check results for the second exercice

    with open('./for_student/Project2/out2.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)
        
        if expected_output == ans:
            print("Exercice 2 : Correct")
        else:
            print("Exercice 2 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans, expected_output))