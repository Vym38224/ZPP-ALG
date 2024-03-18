PRVNI_PRVEK = 0
DALSI_PRVEK = 1

def pridej_do_seznamu(seznam, x):
    while seznam:
        seznam = seznam[DALSI_PRVEK]
    seznam.extend([x, []])

def odeber_ze_seznamu(seznam, x):
    if not seznam:
        return  
    predchozi = None
    aktualni = seznam
    while aktualni[PRVNI_PRVEK] != x:
        predchozi = aktualni
        aktualni = aktualni[DALSI_PRVEK]

    if predchozi is None:
        seznam[:] = aktualni[DALSI_PRVEK]
        return seznam
    else:
        predchozi[DALSI_PRVEK]=aktualni[DALSI_PRVEK]
        seznam = predchozi
        return seznam

# Vytvoření spojového seznamu
muj_seznam = []
pridej_do_seznamu(muj_seznam, 1)
pridej_do_seznamu(muj_seznam, 2)
pridej_do_seznamu(muj_seznam, 3)
pridej_do_seznamu(muj_seznam, 4)
print(f"Seznam před odebráním: {muj_seznam}")

# Odstranění prvku
odeber_prvek = 2
odeber_ze_seznamu(muj_seznam, odeber_prvek)
odeber_ze_seznamu(muj_seznam, 1)
odeber_ze_seznamu(muj_seznam, 3)
odeber_ze_seznamu(muj_seznam, 4)
odeber_ze_seznamu(muj_seznam, 4)
pridej_do_seznamu(muj_seznam, 7)
print(f"Seznam po odebrání: {muj_seznam}")
