VALUE = 0
LEFT_CHILD = 1
RIGHT_CHILD = 2

def tree_add(node, x):
    if not node:
        node.extend([x, [], []])
        return
        
    while node[VALUE] != x:
        parent = node[VALUE]
        if x < node[VALUE]:
            if not node[LEFT_CHILD]:
                node[LEFT_CHILD] = [x, [], [], [parent]]
                return
            node = node[LEFT_CHILD]
        elif x > node[VALUE]:
            if not node[RIGHT_CHILD]:
                node[RIGHT_CHILD] = [x, [], [], [parent]]
                return
            node = node[RIGHT_CHILD]

LABEL = 0
EDGES = 1
def add_edge(graph, from_label, to_label, value):
    v = None
    w = None
    for node in graph:
        if isinstance(node, list):
            if node[LABEL] == from_label:
                v = node
            elif node[LABEL] == to_label:
                w = node      
    v[EDGES].append((w, value))  
    w[EDGES].append((v, value))

def add_node(graph, label):
        graph.append([label, []])

# Test
root = []
add_node(root, 16)
add_node(root, 15)
add_node(root, 42)
add_edge(root, 16, 15, 1)
add_edge(root, 16, 42, 2)

print(root)
