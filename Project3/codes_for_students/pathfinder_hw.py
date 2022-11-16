import copy
from collections import deque

"""
Calcule un chemin eulérien dans graph et le retourne comme une liste de noeuds visités.
Si aucun chemin eulérien n'existe, la fonction retourne None.
L'argument graph ne doit pas être modifié lors de l'exécution de la fonction.
"""
def eulerian_path_finder(graph):
    eulerian_path = []
    stack = deque()
    graphCopy = copy.deepcopy(graph)
    evenDegree, oddDegree = 0, []
    
    for vertex, edges in enumerate(graph):
        if len(edges) % 2 == 0:
            evenDegree += 1
        else:
            oddDegree.append(vertex)
        
    if evenDegree == len(graph):
        currentVertex = 0
    elif len(oddDegree) == 2:
        currentVertex = oddDegree[0]     
    else:
        return None
    
    while len(stack) > 0 or len(graph[currentVertex]) > 0:
        
        if len(graphCopy[currentVertex]) == 0:
            eulerian_path.append(currentVertex)
            if(len(stack) > 0):
                currentVertex = stack.pop()
            else:
                break
            
        else:
            stack.append(currentVertex)
            neighbor = graphCopy[currentVertex][0]
            graphCopy[currentVertex].remove(neighbor)
            graphCopy[neighbor].remove(currentVertex)     
            currentVertex = neighbor
    
    assert len(eulerian_path) == (sum([len(sublist) for sublist in graph]) / 2) + 1

    eulerian_path.reverse()
    return eulerian_path
