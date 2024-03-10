PREDCHOZI_PRVEK = 0
HODNOTA = 1
DALSI_PRVEK = 2

def pridej_do_cyklickeho_seznamu(seznam, x):
    if not seznam:
        seznam.extend([x, seznam, seznam])
    else:
        prvni_prvek_seznamu = seznam
        seznam[DALSI_PRVEK] = [seznam[HODNOTA], seznam[DALSI_PRVEK], prvni_prvek_seznamu]
        seznam[HODNOTA] = x

def pridej_do_obousmerneho_seznamu(seznam, x):
    predchozi_prvek = []
    while seznam:
        predchozi_prvek = seznam
        seznam = seznam[DALSI_PRVEK]
    seznam[DALSI_PRVEK] = [predchozi_prvek, x, []]

# Vytvoření spojového seznamu
muj_seznam = []
pridej_do_cyklickeho_seznamu(muj_seznam, 1)
pridej_do_cyklickeho_seznamu(muj_seznam, 2)
pridej_do_cyklickeho_seznamu(muj_seznam, 3)
pridej_do_cyklickeho_seznamu(muj_seznam, 4)
print(f"Seznam před odebráním: {muj_seznam}")
