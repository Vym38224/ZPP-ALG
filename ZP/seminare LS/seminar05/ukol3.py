
LABEL = 0
EDGES = 1
def add_edge(graph, f, to, value):
        for node in graph:
            if node[LABEL] == f:
                v = node
            elif node[LABEL] == to:
                w = node
            
        v[EDGES].append((w,value))
        w[EDGES].append((v,value))

def add_node(graph, label):
        graph.append([label, []])

# Test
root = []
add_node(root, 16)
add_node(root, 15)
add_node(root, 42)
print(root)
add_edge(root, 16, 15, 1)
add_edge(root, 16, 42, 2)

print(root)
