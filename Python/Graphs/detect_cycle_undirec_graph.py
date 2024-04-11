class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, v1, v2):
        if v1 not in self.adj_list:
            self.adj_list[v1] = []
        if v2 not in self.adj_list:
            self.adj_list[v2] = []
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
        return self.adj_list
    

graph = Graph()
graph.add_node(1, 2)
graph.add_node(1, 4)
graph.add_node(2, 3)
graph.add_node(4, 5)
graph.add_node(3, 5)
graph.add_node(6, 5)
graph.add_node(7, 6)
print(graph.adj_list)

#Intution: the nodes from particlar level of bfs when touches the same node the cycle gets detected
def bfs(graph, start_index, visited):
    q = [(start_index, -1)]
    
    while q:
        vertex, parent = q.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph.adj_list.get(vertex, []):
                if neighbor not in visited:
                    q.append((neighbor, vertex))
                elif parent != neighbor:
                    return True

def isCycle(graph):
    visited = set()
    for vertex in graph.adj_list:
        if vertex not in visited:
            if bfs(graph, 1, visited):
                return True
    return False

print(isCycle(graph))