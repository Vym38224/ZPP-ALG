LABEL = 0
EDGES = 1
def add_edge(graph, f, to):
        for node in graph:
            if node[LABEL] == f:
                v = node
            elif node[LABEL] == to:
                w = node
            
        v[EDGES].append(w)
        w[EDGES].append(v)

def add_node(graph, label):
        graph.append([label, []])

def prvni_struktura(pocet_radku, pocet_sloupcu):
    radky = 0
    sloupce = 0
    root = [pocet_radku, pocet_sloupcu]
    if pocet_radku > 0:
        add_node(root, radky)
    if pocet_sloupcu > 0:
        add_node(root, sloupce)
    return root

def druha_struktura_radku(index, pocet_radku):
    radky = [index]
    if index+1 < pocet_radku:
        add_node(radky, druha_struktura_radku(index + 1, pocet_radku))
    return radky

def druha_struktura_sloupce(index, pocet_sloupcu):
    sloupce = [index]
    if index+1 < pocet_sloupcu:
        add_node(sloupce, druha_struktura_sloupce(index + 1, pocet_sloupcu))
    return sloupce

def treti_struktura(hodnota,radek,sloupec):
    root = [hodnota,sloupec,radek]
    add_node(root,"uzel")
    add_node(root,"uzel")
    return root

# Test
"""root = []
add_node(root, 16)
add_node(root, 15)
add_node(root, 42)
print(root)
add_edge(root, 16, 15, 1)
add_edge(root, 16, 42, 2)

print(root)"""
add_edge(,0,0)

print(prvni_struktura(3,3))
print()
print(druha_struktura_radku(0,3))
print()
print(treti_struktura(1,0,1))

