class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, v1, v2):
        # Assuming the graph is undirected
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        # Assuming the graph is undirected
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.adj_matrix])


# Example usage:
num_vertices = 5
graph = Graph(num_vertices)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
print("Adjacency Matrix:")
print(graph)