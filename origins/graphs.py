class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.graph = self.make_dict()

    def make_dict(self):
        return {node: [b for a, b in self.edges if node == a] for node in self.nodes}

    
                
def dfs(graph, node, visited, component):
    visited.add(node)
    component.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, component)


def connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            dfs(graph, node, visited, component)
            components.append(component)

    return components


graph = {1: [2], 2: [4], 3: [5], 4: [], 5: []}

# dfs(graph, 1)

connected_components = connected_components(graph)
for component in connected_components:
print(component)
                

            
        

nodes = [1, 2, 3, 4, 5, 6]
edges = [(1, 2), (2, 3), (4, 5)]
graph = Graph(nodes, edges)
print(graph.connected_components())
