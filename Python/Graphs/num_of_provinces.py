class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0]*num_vertices for _ in range(num_vertices)]

    def add_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1
    
    def remove_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

graph = Graph(3)
graph.add_edge(0, 1)
graph.add_edge(2, 2)

print("Adjecency matrix:", graph.adj_matrix)

adj_list = {}
provinces = 0
# converting adj_matrix to adj_list
for i in range(len(graph.adj_matrix[0])):
    for j in range(len(graph.adj_matrix)):
        if graph.adj_matrix[i][j] == 1 and i!=j:
            if i not in adj_list:
                adj_list[i] = []
            if j not in adj_list:
                adj_list[j] = []

            if j not in adj_list[i]:
                adj_list[i].append(j)
            if i not in adj_list[j]:
                adj_list[j].append(i)

for i in range(len(graph.adj_matrix[0])):
    for j in range(len(graph.adj_matrix)):
        if graph.adj_matrix[i][j] == 1 and i == j:
            provinces += 1

print("Adjecency list:", adj_list)
visited = set()
def dfs(start_vertex, visited, adj_list):
    visited.add(start_vertex)
    for neighbor in adj_list[start_vertex]:
        if neighbor not in visited:
            dfs(neighbor, visited, adj_list)
    return

for key, val in adj_list.items():
    if key not in visited:
        dfs(key,visited, adj_list)
        provinces += 1

print("Number of provinces: ", provinces)
