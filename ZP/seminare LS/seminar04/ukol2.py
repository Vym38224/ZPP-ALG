PREDCHOZI_PRVEK = 0
HODNOTA = 1
DALSI_PRVEK = 2


def pridej_do_obousmerneho_seznamu(seznam, x):
    predchozi_prvek = []
    while seznam:
        predchozi_prvek = seznam
        seznam = seznam[DALSI_PRVEK]
    seznam.extend([predchozi_prvek, x, []])

obousmerny_seznam = []
pridej_do_obousmerneho_seznamu(obousmerny_seznam,1)
pridej_do_obousmerneho_seznamu(obousmerny_seznam,2)
pridej_do_obousmerneho_seznamu(obousmerny_seznam,3)
print("Obousměrný seznam:")
print(obousmerny_seznam)


def odeber_z_obousmerneho_seznamu(seznam,x):
    if seznam[HODNOTA] == x:
        if seznam[DALSI_PRVEK]:
            seznam[DALSI_PRVEK][PREDCHOZI_PRVEK]=[]
        return seznam[DALSI_PRVEK]

    y=seznam[DALSI_PRVEK]
    while y:
        if y[HODNOTA] == x:
            y[PREDCHOZI_PRVEK][DALSI_PRVEK] = y[DALSI_PRVEK]
            if y[DALSI_PRVEK]:
                y[DALSI_PRVEK][PREDCHOZI_PRVEK] = y[PREDCHOZI_PRVEK]
            return seznam
        y = y[DALSI_PRVEK]
    return seznam

obousmerny_seznam = odeber_z_obousmerneho_seznamu(obousmerny_seznam,1)
obousmerny_seznam = odeber_z_obousmerneho_seznamu(obousmerny_seznam,3)
obousmerny_seznam = odeber_z_obousmerneho_seznamu(obousmerny_seznam,2)
print("Obousměrný seznam po odebrání prvků:")
print(obousmerny_seznam)