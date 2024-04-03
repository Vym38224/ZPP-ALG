def vytvor_matici(x, y):
    radky = [[i, [], []] for i in range(x)]
    sloupce = [[i, [], []] for i in range(y)]
    nova_matice = [x, y, radky, sloupce]
    return nova_matice


def vloz_prvek(matice, hodnota, x, y):
    novy_prvek = [hodnota, x, y, None, None]

    # Vložení prvku do řádku
    if  x < matice[0] and x >= 0 and y < matice[1] and y >= 0:
        ukazatel_radku = matice[2][x]
        if not ukazatel_radku[1] or y < ukazatel_radku[1][2]:
            novy_prvek[3] = ukazatel_radku[1]
            ukazatel_radku[1] = novy_prvek
        else:
            ukazatel_sloupce = ukazatel_radku[1]
            while ukazatel_sloupce[3] and y > ukazatel_sloupce[3][2]:
                ukazatel_sloupce = ukazatel_sloupce[3]
            novy_prvek[3] = ukazatel_sloupce[3]
            ukazatel_sloupce[3] = novy_prvek

        # Vložení prvku do sloupce
        ukazatel_sloupce = matice[3][y]
        if not ukazatel_sloupce[1] or x < ukazatel_sloupce[1][1]:
            novy_prvek[4] = ukazatel_sloupce[1]
            ukazatel_sloupce[1] = novy_prvek
        else:
            ukazatel_radek = ukazatel_sloupce[1]
            while ukazatel_radek[4] and x > ukazatel_radek[4][1]:
                ukazatel_radek = ukazatel_radek[4]
            novy_prvek[4] = ukazatel_radek[4]
            ukazatel_radek[4] = novy_prvek
    else:
        print(f"Pozor na správný počet řádku nebo sloupců matice! Prvek s hodnotou {hodnota} nepřidán do naší matice typu {matice[0]}×{matice[1]}")
        print()
        

def zobraz_matici(matice):
    ukazatel_radku = matice[2]
    for i in range(matice[0]):
        ukazatel_prvku = ukazatel_radku[i][1]
        for j in range(matice[1]):
            if ukazatel_prvku == []:
                print(0, end="  ")
            elif ukazatel_prvku[2] == j:
                print(ukazatel_prvku[0], end="  ")
                ukazatel_prvku = ukazatel_prvku[3]
            else:
                print(0, end="  ")
        print()

# Test
matice = vytvor_matici(3, 4)
vloz_prvek(matice, 1, 0, 0)
vloz_prvek(matice, 2, 1, 1)
vloz_prvek(matice, 3, 1, 2)
vloz_prvek(matice, 4, 2, 2)
vloz_prvek(matice, 5, -2, 0)
vloz_prvek(matice, 6, 3, 0)
zobraz_matici(matice)
print()
print(matice)
