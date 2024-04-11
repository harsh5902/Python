# Happens only on Directed Acyclic Graph (DAG)
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, v1, v2):
        if v1 not in self.adj_list:
            self.adj_list[v1] = []
        if v2 not in self.adj_list:
            self.adj_list[v2] = []
        self.adj_list[v1].append(v2)

graph = Graph()
graph.add_node(5, 0)
graph.add_node(4, 0)
graph.add_node(5, 2)
graph.add_node(4, 1)
graph.add_node(2, 3)
graph.add_node(3, 1)

print(graph.adj_list)

stack = []
def dfs(vertex, v_list, visited):
    visited.add(vertex)

    for nv in v_list:
        if nv not in visited:
            dfs(nv, v_list, visited) 
    stack.append(vertex)

visited = set()
for vertex in sorted(graph.adj_list.keys()):
    if vertex not in visited:
        dfs(vertex, graph.adj_list[vertex], visited)

print(stack[::-1])



