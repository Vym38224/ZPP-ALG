VALUE = 0
LEFT_CHILD = 1
RIGHT_CHILD = 2

def tree_add(node, x):
    if not node:
        node.extend([x, [], []])
        return
        
    while node[VALUE] != x:
        parent = node
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
# Test
root = []
tree_add(root, 16)
tree_add(root, 15)
tree_add(root, 42)
print(root)
