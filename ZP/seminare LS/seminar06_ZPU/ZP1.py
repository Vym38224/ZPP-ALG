def prvni_struktura(m,n):
    matice.extend([m, n , [], []])

def vytvor_matici(m, n):
    # 1.typ Struktury
    info_matice = [m, n, None, None]

    # řádky a sloupce
    radky = [None] * m
    sloupce = [None] * n

    
    # pro každý řádek vytvoříme první strukturu druhého typu a uložíme ji do seznamu řadky a sloupce (2.typ Struktury)
    # řadky
    for i in range(m):
        radky[i] = [i, None]  # index řádku, odkaz na první hodnotu v řádku
        radky[i][1] = None # první prvek každého řádku jako None
    # sloupce
    for i in range(n):
        sloupce[i] = [i, None]  # index sloupce, odkaz na první hodnotu ve sloupci
        sloupce[i][1] = None  # první prvek každého sloupce jako None
    return info_matice, radky, sloupce

def vytvor_prvek(hodnota, radek, sloupec):
    # vytvoření nového prvku matice s nenulovou hodnotou, indexem řádku a sloupce (3.typ Struktury) 
    return [hodnota, radek, sloupec, None, None]

def pridej_prvek_do_radku(aktualni_prvek, novy_prvek):
    # přidání prvku do konce řádku
    while aktualni_prvek[3] is not None:
        aktualni_prvek = aktualni_prvek[3]
    aktualni_prvek[3] = novy_prvek

def pridej_prvek_do_sloupce(aktualni_prvek, novy_prvek):
    # přidání prvku do konce sloupce
    while aktualni_prvek[4] is not None:
        aktualni_prvek = aktualni_prvek[4]
    aktualni_prvek[4] = novy_prvek

def pridej_prvek_na_zacatek_seznamu(seznam, novy_prvek):
    # seznam je prázdný, přidej nový prvek
    if seznam[1] is None:
        seznam[1] = novy_prvek
    else:
        # seznam není prázdný, 
        novy_prvek[3] = seznam[1]
        seznam[1] = novy_prvek

def vloz_prvek(matice, hodnota, radek, sloupec):
    info_matice, radky, sloupce = matice
    m, n, _, _ = info_matice  

    if radek < 0 or radek >= m or sloupec < 0 or sloupec >= n:
        print("Index řádku nebo sloupce mimo rozsah matice")
        return

    novy_prvek = vytvor_prvek(hodnota, radek, sloupec)

    # přidání prvku pouze do seznamu řádků
    pridej_prvek_na_zacatek_seznamu(radky[radek], novy_prvek)

def ziskej_hodnotu(matice, sloupec, radek):
    info_matice, radky, sloupce = matice
    m, n, _, _ = info_matice  

    if radek < 0 or radek >= m or sloupec < 0 or sloupec >= n:
        print("Index řádku nebo sloupce mimo rozsah matice")
        return

    aktualni_radkovy_prvek = radky[radek][1]

    while aktualni_radkovy_prvek is not None:
        if aktualni_radkovy_prvek[2] == sloupec:
            return aktualni_radkovy_prvek[0]
        aktualni_radkovy_prvek = aktualni_radkovy_prvek[3]
    return 0

def zobraz_matici(matice):
    info_matice, radky, sloupce = matice
    m, n, _, _ = info_matice  

    for radek in range(m):
        for sloupec in range(n):
            print(ziskej_hodnotu(matice, sloupec, radek), end="    ")
        print()

# příklad použití:
matice = vytvor_matici(3, 4)
print(matice)
"""vloz_prvek(matice, 1, 0, 1)
vloz_prvek(matice, 18, 0, 2)
vloz_prvek(matice, 3, 2, 2)
zobraz_matici(matice)
"""
