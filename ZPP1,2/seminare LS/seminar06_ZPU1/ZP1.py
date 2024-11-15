def vytvor_matici(x, y):
    nova_matice = [x, y, [], []]

    radky = nova_matice[2]
    for i in range(x):
        novy_radek = [i, [], []]
        if radky == []:
            radky[:] = novy_radek
        else:
            while radky[2]:
                radky = radky[2]
            radky[2] = novy_radek

    sloupce = nova_matice[3]
    for i in range(y):
        novy_sloupec = [i, [], []]
        if sloupce == []:
            sloupce[:] = novy_sloupec
        else:
            while sloupce[2]:
                sloupce = sloupce[2]
            sloupce[2] = novy_sloupec
    return nova_matice

def vloz_prvek_do_radku(aktualni_radek, novy_uzel, pozice):
    if not aktualni_radek:
        return novy_uzel

    if pozice < aktualni_radek[2]:
        novy_uzel[3] = aktualni_radek
        return novy_uzel

    predchozi = None
    aktualni = aktualni_radek
    while aktualni and pozice >= aktualni[2]:
        predchozi = aktualni
        aktualni = aktualni[3]

    predchozi[3] = novy_uzel
    novy_uzel[3] = aktualni

    return aktualni_radek

def vloz_prvek_do_sloupce(aktualni_sloupec, novy_uzel, pozice):
    if not aktualni_sloupec:
        return novy_uzel

    if pozice < aktualni_sloupec[1]:
        novy_uzel[4] = aktualni_sloupec
        return novy_uzel

    predchozi = None
    aktualni = aktualni_sloupec
    while aktualni and pozice >= aktualni[1]:
        predchozi = aktualni
        aktualni = aktualni[4]

    predchozi[4] = novy_uzel
    novy_uzel[4] = aktualni

    return aktualni_sloupec

def vloz_prvek(matice, hodnota, x, y):
    novy_uzel = [hodnota, x, y, [], []]

    if 0 <= x < matice[0] and 0 <= y < matice[1]:
        # Vložení do řádku
        radek = matice[2]
        for i in range(x):
            radek = radek[2]
        radek[1] = vloz_prvek_do_radku(radek[1], novy_uzel, y)

        # Vložení do sloupce
        sloupec = matice[3]
        for i in range(y):
            sloupec = sloupec[2]
        sloupec[1] = vloz_prvek_do_sloupce(sloupec[1], novy_uzel, x)
    else:
        print(f"Pozor na správný počet řádku nebo sloupců matice! Prvek s hodnotou {hodnota} nebyl přidán do naší matice typu {matice[0]}x{matice[1]}")
        print()

def najdi_prvek(matice, x, y):
    radek = matice[2]
    for i in range(x):
        radek = radek[2]
    uzel = radek[1]
    while uzel:
        if uzel[2] == y:
            return uzel
        uzel = uzel[3]
    return None

def zobraz_matici(matice):
    for i in range(matice[0]):
        for j in range(matice[1]):
            prvek = najdi_prvek(matice, i, j)
            if prvek is None:
                print(0, end="  ")
            else:
                print(prvek[0], end="  ")
        print()

matice = vytvor_matici(3,4)
vloz_prvek(matice,1,0,0)
vloz_prvek(matice,1,2,2)
vloz_prvek(matice,1,2,3)

zobraz_matici(matice)
print()
print(matice)
