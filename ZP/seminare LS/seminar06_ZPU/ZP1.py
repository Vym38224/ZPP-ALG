
def vytvor_matici(m, n):
    # počet řádků, počet sloupců, odkaz na první řádek a první sloupec v matici (1.typ Struktury)
    info_matice = [m, n, None, None]

    # Inicializace řádků a sloupců
    radky = [None] * m
    sloupce = [None] * n

    # pro každý řádek vytvoříme první strukturu druhého typu a uložíme ji do seznamu radky (2.typ Struktury)
    for i in range(m):
        radky[i] = [i, None]  # index řádku, odkaz na první hodnotu v řádku
        # Inicializujeme první prvek každého řádku jako None
        radky[i][1] = None

    # pro každý sloupec vytvoříme první strukturu druhého typu a uložíme ji do seznamu sloupce
    for i in range(n):
        sloupce[i] = [i, None]  # index sloupce, odkaz na první hodnotu ve sloupci
        # Inicializujeme první prvek každého sloupce jako None
        sloupce[i][1] = None
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
    # pokud seznam je prázdný, přidej nový prvek na začátek
    if seznam[1] is None:
        seznam[1] = novy_prvek
    else:
        # pokud seznam není prázdný, nastav nový prvek jako první a přidej starý první prvek jako druhý
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
vloz_prvek(matice, 1, 0, 1)
vloz_prvek(matice, 18, 0, 2)
vloz_prvek(matice, 3, 2, 2)
zobraz_matici(matice)
