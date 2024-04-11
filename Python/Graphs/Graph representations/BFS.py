class Graph:
    def __init__(self):
        self.adjecency_list = {}
    
    def add_edge(self, v1, v2):
        if v1 not in self.adjecency_list:
            self.adjecency_list[v1] = []
        if v2 not in self.adjecency_list:
            self.adjecency_list[v2] = []
        
        self.adjecency_list[v1].append(v2)
        self.adjecency_list[v2].append(v1)
        return self.adjecency_list

    def __str__(self):
        output = ""
        for vertex, neighbors in self.adjecency_list.items():
            output += f"{vertex}: {neighbors}\n"
        return output

graph = Graph()
graph.add_edge(1,2)
graph.add_edge(1,6)
graph.add_edge(2,3)
graph.add_edge(2,4)
graph.add_edge(6,7)
graph.add_edge(6,9)
graph.add_edge(4,5)
graph.add_edge(7,8)
graph.add_edge(5,8)
print(graph)

def BFS(graph, start_vertex):
    visited = set()
    queue = [start_vertex]
    traversal = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            for neighbor in graph.adjecency_list.get(vertex, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal

bfs_trav = BFS(graph, 1)
print("BFS traversal: ", bfs_trav)


