# graph = load_graph(f"./Project3/codes_for_students/test_bench_students/test_09.txt")

# print(eulerian_path_finder(graph))

# for file in os.listdir("./Project3/codes_for_students/test_bench_students"):
#     graph = load_graph(f"./Project3/codes_for_students/test_bench_students/{file}")
#     print(eulerian_path_finder(graph))


"""
Loads the graph contained in file.
"""
def load_graph(file_name):
    graph = []
    with open(file_name,'r') as file:
        txt = file.read().split("\n")
        for line in txt[1:-1]:
            adj = []
            for node in line.split(","):
                adj.append(int(node))
            graph.append(adj)
        while(len(graph) != int(txt[0])):
            graph.append([])
    return graph

"""
Translate a graph from adjacency list to file representation.
"""
def from_adj_to_str(graph):
    output = str(len(graph))
    for line in graph:
        output += "\n"
        for adj in line:
            output += str(adj) + ","
        output = output[:-1]
    output += "\n"
    return output

"""
Writes a graph into file_name.
"""
def save_graph(file_name,graph):
    with open(file_name,'w') as file:
        file.write(from_adj_to_str(graph))
        
        
print(load_graph("./codes_for_students/test_bench_students/test_01.txt"))
