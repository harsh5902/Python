class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_edge(self, v1, v2):
        if v1 not in self.adj_list:
            self.adj_list[v1] = []
        if v2 not in self.adj_list:
            self.adj_list[v2] = []
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
    
    def __str__(self):
        out = ""
        for vertex, neighbors in self.adj_list.items():
            out += f"{vertex}: {neighbors}\n"
        return out

graph = Graph()
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,5)
graph.add_edge(2,6)
graph.add_edge(3,4)
graph.add_edge(3,7)
graph.add_edge(4,8)
graph.add_edge(7,8)

print(graph)

def DFS(graph, start_vertex, dfs_trav, visited):
    visited.add(start_vertex)
    dfs_trav.append(start_vertex)
    for neighbor in graph.adj_list[start_vertex]:
        if neighbor not in visited:
            DFS(graph, neighbor, dfs_trav, visited)
    return dfs_trav

print("DFS traversal: ", DFS(graph, 1, [], set()))

