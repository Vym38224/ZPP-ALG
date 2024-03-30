HLAVICKA_ID = 0
HLAVICKA_HODNOTA = 1
HLAVICKA_DALSI_PRVEK = 2


def pridej_do_hlavicky_hodnotu(puvodni_hlavicka,k):
    if puvodni_hlavicka == []:
        return [k,[],[]]
    x=puvodni_hlavicka

    while x[HLAVICKA_DALSI_PRVEK]:
        x=x[HLAVICKA_DALSI_PRVEK]
    x[HLAVICKA_DALSI_PRVEK]=[k,[],[]]
    return puvodni_hlavicka


MATICE_SLOUPCE = 3
MATICE_RADKY = 2
MATICE_POCET_SLOUPCU = 1
MATICE_POCET_RADKU = 0

def vytvor_matici(x,y):
    radky = []
    sloupce = []
    for i in range(x):
        radky=pridej_do_hlavicky_hodnotu(radky,i)
    for i in range(y):
        sloupce = pridej_do_hlavicky_hodnotu(sloupce,i)
    nova_matice=[x,y,radky,sloupce]
    return nova_matice

UZEL_HODNOTA=0
UZEL_X = 1
UZEL_Y = 2
UZEL_NASLEDUJICI_SLOUPCE = 3
UZEL_NASLEDUJICI_RADKY = 4

def zobraz_matici(matice):
    ukazatel_radky = matice[MATICE_RADKY]
    for i in range(matice[MATICE_POCET_RADKU]):
        ukazatel_uzel = ukazatel_radky[HLAVICKA_HODNOTA]
        for j in range(matice[MATICE_POCET_SLOUPCU]):
            if ukazatel_uzel==[]:
                print(0,end="  ")
            elif ukazatel_uzel[UZEL_Y] == j:
                print(ukazatel_uzel[UZEL_HODNOTA],end="  ")
                ukazatel_uzel=ukazatel_uzel[UZEL_NASLEDUJICI_SLOUPCE]
            else:
                print(0,end="  ")
        print()
        ukazatel_radky=ukazatel_radky[HLAVICKA_DALSI_PRVEK]

def vloz_prvek(matice,hodnota,x,y):
    novy_uzel=[hodnota,x,y,[],[]]

    ukazatel_radek = matice[MATICE_RADKY]
    for i in range(x):
        ukazatel_radek=ukazatel_radek[HLAVICKA_DALSI_PRVEK]
    
    if ukazatel_radek[HLAVICKA_HODNOTA]==[] or y < ukazatel_radek[HLAVICKA_HODNOTA][UZEL_Y]:
        novy_uzel[UZEL_NASLEDUJICI_SLOUPCE] =ukazatel_radek[HLAVICKA_HODNOTA]
        ukazatel_radek[HLAVICKA_HODNOTA] = novy_uzel

    else:
        ukazatel_y = ukazatel_radek[HLAVICKA_HODNOTA]
        while ukazatel_y[UZEL_NASLEDUJICI_SLOUPCE] and y>ukazatel_y[UZEL_NASLEDUJICI_SLOUPCE][UZEL_Y]:
            ukazatel_y=ukazatel_y[UZEL_NASLEDUJICI_SLOUPCE]
        novy_uzel[UZEL_NASLEDUJICI_SLOUPCE] = ukazatel_y[UZEL_NASLEDUJICI_SLOUPCE]
        ukazatel_y[UZEL_NASLEDUJICI_SLOUPCE] = novy_uzel

matice = vytvor_matici(3,4)
vloz_prvek(matice,4,1,0)
vloz_prvek(matice,5,0,1)
vloz_prvek(matice,6,1,1)
vloz_prvek(matice,2,0,0)
vloz_prvek(matice,9,0,2)
vloz_prvek(matice,18,2,3)

zobraz_matici(matice)
print()
print(matice)