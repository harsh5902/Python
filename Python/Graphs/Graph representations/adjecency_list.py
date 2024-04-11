class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, v1, v2):
        # Assuming the graph is undirected
        if v1 not in self.adj_list:
            self.adj_list[v1] = []
        if v2 not in self.adj_list:
            self.adj_list[v2] = []
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def remove_edge(self, v1, v2):
        # Assuming the graph is undirected
        if v2 in self.adj_list.get(v1, []):
            self.adj_list[v1].remove(v2)
        if v1 in self.adj_list.get(v2, []):
            self.adj_list[v2].remove(v1)

    def __str__(self):
        output = ""
        for vertex, neighbors in self.adj_list.items():
            output += f"{vertex}: {neighbors}\n"
        return output


# Example usage:
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
print("Adjacency List:")
print(graph)