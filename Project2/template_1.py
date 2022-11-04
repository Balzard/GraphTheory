"""
    Student template for the third homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""

import math
import heapq

def getAdj(N, roads):
    adj = {i: [] for i in range(N)}
    sumEdges = 0
    for u, v, s in roads:
        adj[u].append((v, s))
        adj[v].append((u, s))
        sumEdges += s
    return adj, sumEdges

def prim_mst(N, roads):
    """ 
    INPUT : 
        - N, the number of crossroads
        - roads, list of tuple (u, v, s) giving a road between u and v with satisfaction s
    OUTPUT :
        - return the maximal satisfaction that can be achieved
        
        See homework statement for more details
    """

    satisfaction = 0
    
    # TO COMPLETE
    
    adj, sumEdges = getAdj(N, roads)
    T = set()
    firstNode = list(adj.keys())[0]
    neighbours = []
    
    heapq.heappush(neighbours, (0, firstNode))
    # look at all neighbours of starting node
    for neighbour, costEdge in adj[firstNode]:
        heapq.heappush(neighbours, (costEdge, neighbour))
        
    while neighbours:
        costEdge, bestNode = heapq.heappop(neighbours)
        if bestNode not in T:
            T.add(bestNode)
            satisfaction += costEdge

            for neighbour, cost in adj[bestNode]:
                if neighbour not in T:
                    heapq.heappush(neighbours, (cost, neighbour))
               
    # substract min spanning tree satisfaction to get max spanning tree     
    return sumEdges - satisfaction

    
if __name__ == "__main__":

    # Read Input for the first exercice
    
    with open('./for_student/Project2/in1.txt', 'r') as fd:
        l = fd.readline()
        l = l.rstrip().split(' ')
        
        n, m = int(l[0]), int(l[1])
        
        roads = []
        for road in range(m):
        
            l = fd.readline().rstrip().split()
            roads.append(tuple([int(x) for x in l]))
            
    # Compute answer for the first exercice
     
    ans1 = prim_mst(n, roads)
     
    # Check results for the first exercice

    with open('./for_student/Project2/out1.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)
        
        if expected_output == ans1:
            print("Exercice 1 : Correct")
        else:
            print("Exercice 1 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans1, expected_output))
