def vytvor_matici(x, y):
    radky = [[i, [], []] for i in range(x)]
    sloupce = [[i, [], []] for i in range(y)]
    nova_matice = [x, y, radky, sloupce]
    return nova_matice

def vloz_prvek_do_radku(radek, novy_prvek, y):
    if not radek[1]:
        radek[1] = novy_prvek
    elif y < radek[1][2]:
        novy_prvek[3] = radek[1]
        radek[1] = novy_prvek
        radek[1] = rekurzivne_vloz_prvek_do_radku(radek[1], novy_prvek, y)

def rekurzivne_vloz_prvek_do_radku(aktualni_prvek, novy_prvek, y):
    if not aktualni_prvek or y < aktualni_prvek[2]:
        novy_prvek[3] = aktualni_prvek
        return novy_prvek
    aktualni_prvek[3] = rekurzivne_vloz_prvek_do_radku(aktualni_prvek[3], novy_prvek, y)
    return aktualni_prvek

def vloz_prvek_do_sloupce(sloupec, novy_prvek, x):
    if not sloupec[1]:
        sloupec[1] = novy_prvek
    elif x < sloupec[1][2]:
        novy_prvek[3] = sloupec[1]
        sloupec[1] = novy_prvek
    else:
        sloupec[1] = rekurzivne_vloz_prvek_do_sloupce(sloupec[1], novy_prvek, x)

def rekurzivne_vloz_prvek_do_sloupce(aktualni_prvek, novy_prvek, x):
    if not aktualni_prvek or x < aktualni_prvek[1]:
        novy_prvek[4] = aktualni_prvek
        return novy_prvek
    aktualni_prvek[4] = rekurzivne_vloz_prvek_do_sloupce(aktualni_prvek[4], novy_prvek, x)
    return aktualni_prvek

def vloz_prvek(matice, hodnota, x, y):
    novy_prvek = [hodnota, x, y, None, None]
    if x < matice[0] and x >= 0 and y < matice[1] and y >= 0:
        # Vložení prvku do řádku
        radek = matice[2][x]
        vloz_prvek_do_radku(radek, novy_prvek, y)
        # Vložení prvku do sloupce
        sloupec = matice[3][y]
        vloz_prvek_do_sloupce(sloupec, novy_prvek, x)
    else:
        print(f"Pozor na správný počet řádku nebo sloupců matice! Prvek s hodnotou {hodnota} nebyl přidán do naší matice typu {matice[0]}×{matice[1]}")
        print()

def zobraz_matici(matice):
    for i in range(matice[0]):
        for j in range(matice[1]):
            prvek = matice[2][i][1]
            while prvek is not None:
                if prvek[2] == j:
                    print(prvek[0], end="  ")
                    break
                prvek = prvek[3]
            else:
                print(0, end="  ")
        print()

# Test
matice = vytvor_matici(3, 4)
vloz_prvek(matice, 1, 0, 0)



zobraz_matici(matice)
print()
print(matice)