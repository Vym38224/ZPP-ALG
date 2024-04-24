PRVNI_PRVEK = 0
DALSI_PRVEK = 1

def vytvor_zasobnik():
    Zasobnik = []
    return Zasobnik

def pridej_do_zasobniku(seznam, x):
    while seznam:
        seznam = seznam[DALSI_PRVEK]
    seznam.extend([x, []])


def odeber_ze_zasobniku(seznam):
    if not seznam:
        return None
    
    predchozi = None
    aktualni = seznam

    while aktualni is not None and aktualni[DALSI_PRVEK]:
        predchozi = aktualni
        aktualni = aktualni[DALSI_PRVEK]
    
    if predchozi is None:
        odebrany_prvek = seznam[PRVNI_PRVEK]
        seznam[PRVNI_PRVEK] = None  
    else:
        odebrany_prvek = predchozi[DALSI_PRVEK][PRVNI_PRVEK]
        predchozi[DALSI_PRVEK] = None  

    return odebrany_prvek






