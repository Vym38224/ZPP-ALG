LABEL = 0
EDGES = 1

def add_node(graph, label):
    graph.append([label, []])

def add_value(graph, label):
    graph.append([label])

def vytvor_matici(pocet_radku, pocet_sloupcu):
    root = [pocet_radku, pocet_sloupcu]
    if pocet_radku > 0:
        add_node(root, druha_struktura_radku(0, pocet_radku))
    if pocet_sloupcu > 0:
        add_node(root, druha_struktura_sloupce(0, pocet_sloupcu))
    return root
    
def druha_struktura_radku(index, pocet_radku):
    root = [index]
    if index < pocet_radku:
        add_node(root, druha_struktura_radku(index + 1, pocet_radku))
    return root

def druha_struktura_sloupce(index, pocet_sloupcu):
    root = [index]
    if index < pocet_sloupcu:
        add_node(root, druha_struktura_sloupce(index + 1, pocet_sloupcu))
    return root

def vloz_prvek(matice, prvek, radek, sloupec):
    pass
    
# Testování
matice = vytvor_matici(2, 2)
print(matice)
vloz_prvek(matice,1,0,1)
print(matice)





