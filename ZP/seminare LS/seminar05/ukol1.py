VALUE = 0
LEFT_CHILD = 1
RIGHT_CHILD = 2

def tree_add(node, x):
        if not node:
            node.extend([x, [], []])
            return
            
        while node[VALUE] != x:
            if x < node[VALUE]:
                if node[LEFT_CHILD]:
                    node = node[LEFT_CHILD]
                else:
                    node[LEFT_CHILD] = [x, [], []]
                    return
                    
            elif x > node[VALUE]:
                if node[RIGHT_CHILD]:
                    node = node[RIGHT_CHILD]
                else:
                    node[RIGHT_CHILD] = [x, [], []]
                    return

def tree_find(root, x):
    if not root:
        return False
    
    node = root
    while node:
        if node[VALUE] == x:
            return True
        elif x < node[VALUE]:
            node = node[LEFT_CHILD]
        else:
            node = node[RIGHT_CHILD]      
    return False

# Test
root = []
tree_add(root, 8)
tree_add(root, 4)
tree_add(root, 16)
tree_add(root, 15)
tree_add(root, 42)
tree_add(root, 23)
print(root)
print(tree_find(root, 15))  # Vypíše: True
print(tree_find(root, 10))  # Vypíše: False
