LABEL = 0
EDGES = 1

def add_node(graph, label):
    graph.append([label, []])


def vytvor_matici(pocet_radku, pocet_sloupcu):
    root = [" ",pocet_radku, pocet_sloupcu]
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

def treti_struktura_radku(prvek,radek,sloupec,dalsi_radek):
    root=[prvek,radek,sloupec]
    add_node(root,dalsi_radek)
    return root

def treti_struktura_sloupce(prvek,radek,sloupec,dalsi_sloupec):
    root=[prvek,radek,sloupec]
    add_node(root,dalsi_sloupec)
    return root

def vloz_prvek(matice, prvek, radek, sloupec):
    pass

def zobraz_matici(matice):
    pass
    
# Testování
matice = vytvor_matici(3, 3)
print(matice)
print(treti_struktura_radku(1, 0, 1, None))
print(treti_struktura_sloupce(1, 0, 1, 2))
vloz_prvek(matice, 1, 0, 1)

