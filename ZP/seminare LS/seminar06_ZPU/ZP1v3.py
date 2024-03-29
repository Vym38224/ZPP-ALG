# Struktura pro prvek matice
def create_element(hodnota, radek, sloupec):
    return {"hodnota": hodnota, "radek": radek, "sloupec": sloupec, "dalsi": None}

# Struktura pro řádek nebo sloupec
def create_row_column(index):
    return {"index": index, "prvni_prvek": None, "dalsi": None}

# Funkce pro vytvoření matice
def create_matrix(pocet_radku, pocet_sloupcu):
    prvni_radek = None
    prvni_sloupec = None

    # Vytvoření prázdných řádků
    for i in range(pocet_radku):
        radek = create_row_column(i)
        if prvni_radek is None:
            prvni_radek = radek
        else:
            akt_radek = prvni_radek
            while akt_radek["dalsi"] is not None:
                akt_radek = akt_radek["dalsi"]
            akt_radek["dalsi"] = radek

    # Vytvoření prázdných sloupců
    for i in range(pocet_sloupcu):
        sloupec = create_row_column(i)
        if prvni_sloupec is None:
            prvni_sloupec = sloupec
        else:
            akt_sloupec = prvni_sloupec
            while akt_sloupec["dalsi"] is not None:
                akt_sloupec = akt_sloupec["dalsi"]
            akt_sloupec["dalsi"] = sloupec

    return prvni_radek, prvni_sloupec

# Funkce pro vložení prvku do matice
def insert_element(matice, hodnota, radek, sloupec):
    novy_prvek = create_element(hodnota, radek, sloupec)

    # Vložení prvku do řádku
    akt_radek = matice[0]
    for _ in range(radek):
        akt_radek = akt_radek["dalsi"]
    if akt_radek["prvni_prvek"] is None:
        akt_radek["prvni_prvek"] = novy_prvek
    else:
        akt_prvek = akt_radek["prvni_prvek"]
        while akt_prvek["dalsi"] is not None:
            akt_prvek = akt_prvek["dalsi"]
        akt_prvek["dalsi"] = novy_prvek

    # Vložení prvku do sloupce
    akt_sloupec = matice[1]
    for _ in range(sloupec):
        akt_sloupec = akt_sloupec["dalsi"]
    if akt_sloupec["prvni_prvek"] is None:
        akt_sloupec["prvni_prvek"] = novy_prvek
    else:
        akt_prvek = akt_sloupec["prvni_prvek"]
        while akt_prvek["dalsi"] is not None:
            akt_prvek = akt_prvek["dalsi"]
        akt_prvek["dalsi"] = novy_prvek

# Funkce pro zobrazení matice
def display_matrix(matice, pocet_radku, pocet_sloupcu):
    for i in range(pocet_radku):
        akt_radek = matice[0]
        for _ in range(i):
            akt_radek = akt_radek["dalsi"]

        for j in range(pocet_sloupcu):
            akt_prvek = akt_radek["prvni_prvek"]
            while akt_prvek is not None:
                if akt_prvek["sloupec"] == j:
                    print(akt_prvek["hodnota"], end="\t")
                    break
                akt_prvek = akt_prvek["dalsi"]
            if akt_prvek is None or akt_prvek["sloupec"] != j:
                print("0", end="\t")
        print()

# Příklad použití
matice = create_matrix(3, 4)
insert_element(matice, 1, 0, 1)
display_matrix(matice,3,4)
print(matice)
