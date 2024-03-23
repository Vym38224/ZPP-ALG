def vytvor_strukturu_matice(m, n):
    # První struktura: uchovává počet řádků, počet sloupců, odkaz na první řádek a první sloupec v matici
    info_matice = [m, n, None, None]

    # Inicializace řádků a sloupců
    radky = [None] * m
    sloupce = [None] * n

    # Pro každý řádek vytvoříme první strukturu druhého typu a uložíme ji do seznamu radky
    for i in range(m):
        radky[i] = [i, None]  # index řádku, odkaz na první hodnotu v řádku

    # Pro každý sloupec vytvoříme první strukturu druhého typu a uložíme ji do seznamu sloupce
    for i in range(n):
        sloupce[i] = [i, None]  # index sloupce, odkaz na první hodnotu ve sloupci

    return info_matice, radky, sloupce

def vytvor_prvek(hodnota, radek, sloupec):
    # Vytvoření nového prvku matice s nenulovou hodnotou, indexem řádku a sloupce
    return [hodnota, radek, sloupec, None, None]

def pridej_prvek_do_radku(aktualni_prvek, novy_prvek):
    # Přidání prvku do konce řádku
    while aktualni_prvek[3] is not None:
        aktualni_prvek = aktualni_prvek[3]
    aktualni_prvek[3] = novy_prvek

def pridej_prvek_do_sloupce(aktualni_prvek, novy_prvek):
    # Přidání prvku do konce sloupce
    while aktualni_prvek[4] is not None:
        aktualni_prvek = aktualni_prvek[4]
    aktualni_prvek[4] = novy_prvek

def pridej_prvek_na_zacatek_seznamu(seznam, novy_prvek):
    # Pokud seznam je prázdný, přidej nový prvek na začátek
    if seznam[1] is None:
        seznam[1] = novy_prvek
    else:
        # Pokud seznam není prázdný, nastav nový prvek jako první a přidej starý první prvek jako druhý
        novy_prvek[3] = seznam[1]
        seznam[1] = novy_prvek

def vloz_prvek(info_matice, radky, sloupce, hodnota, radek, sloupec):
    m, n, _, _ = info_matice  # Rozbalení informací o matici

    if radek < 0 or radek >= m or sloupec < 0 or sloupec >= n:
        print("Index řádku nebo sloupce mimo rozsah matice")
        return

    novy_prvek = vytvor_prvek(hodnota, radek, sloupec)

    # Přidání prvku do řádku a sloupce
    pridej_prvek_na_zacatek_seznamu(radky[radek], novy_prvek)
    pridej_prvek_na_zacatek_seznamu(sloupce[sloupec], novy_prvek)

def ziskej_hodnotu(info_matice, radky, sloupc, radek):
    m, n, _, _ = info_matice  

    if radek < 0 or radek >= m or sloupc < 0 or sloupc >= n:
        print("Index řádku nebo sloupce mimo rozsah matice")
        return

    aktualni_radkovy_prvek = radky[radek][1]

    while aktualni_radkovy_prvek is not None:
        if aktualni_radkovy_prvek[2] == sloupc:
            return aktualni_radkovy_prvek[0]
        aktualni_radkovy_prvek = aktualni_radkovy_prvek[3]
    return 0


def ukaz_matici(info_matice, radky, sloupce):
    m, n, _, _ = info_matice  

    for radek in range(m):
        for sloupec in range(n):
            print(ziskej_hodnotu(info_matice, radky, sloupec, radek), end=" ")
        print()

# Příklad použití:
info_matice, radky, sloupce = vytvor_strukturu_matice(4, 4)
vloz_prvek(info_matice, radky, sloupce, 1, 0, 0)
vloz_prvek(info_matice, radky, sloupce, 2, 1, 1)
vloz_prvek(info_matice, radky, sloupce, 3, 2, 2)
vloz_prvek(info_matice, radky, sloupce, 4, 3, 3)
ukaz_matici(info_matice, radky, sloupce)
