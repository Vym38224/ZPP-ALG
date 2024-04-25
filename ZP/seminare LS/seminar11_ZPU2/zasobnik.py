def preved_cislo_na_bajty(x, pocet_bajtu):
    bytes_array = []
    for i in range(pocet_bajtu):
        byte = x & 0xff
        bytes_array.insert(0, byte)
        x >>= 8
    if x != 0:
        print(ValueError("Zadané číslo se nevejde do daného počtu bajtů."))
        return bytes_array[-pocet_bajtu:] 
    return bytes_array[-pocet_bajtu:]

def preved_bajty_na_cislo(bytes_array):
        number = 0
        if bytes_array:
            for byte in bytes_array:
                number = (number << 8) + byte
        return number

def zapis_do_souboru(soubor, zasobnik):
    pocet_bajtu = zasobnik[0]
    cisla = zasobnik[1]
    f = open(soubor, "wb")
    f.write(bytes([pocet_bajtu]))
    while cisla:
        cislo = cisla[0]
        bajty = preved_cislo_na_bajty(cislo, pocet_bajtu)
        f.write(bytes(bajty))
        cisla = cisla[1]
    f.close()

def nacti_ze_souboru(soubor):
    f = open(soubor, "rb")
    pocet_bajtu = ord(f.read(1))
    cisla = []
    while True:
        bajty = f.read(pocet_bajtu)
        if not bajty:
            break
        cislo = preved_bajty_na_cislo(bajty)
        cisla.append(cislo)
    f.close()
    zasobnik = vytvor_zasobnik(pocet_bajtu)
    for cislo in cisla:
        pridej_do_zasobniku(zasobnik, cislo)
    return zasobnik

def vytvor_zasobnik(max_bajty):
    return [max_bajty, []]

def pridej_do_zasobniku(seznam, x):
    max_bajty, zasobnik = seznam
    if 0 < x < 2**(max_bajty * 8):
        while zasobnik:
            zasobnik = zasobnik[1]
        zasobnik.extend([x, []])
    else:
        print(f"hodnota {x} je mimo povolený rozsah.")

def odeber_ze_zasobniku(seznam):
    max_bajty, zasobnik = seznam
    if not zasobnik:
        return None
    predchozi = []
    aktualni = zasobnik
    while aktualni and aktualni[1]:
        predchozi = aktualni
        aktualni = aktualni[1]
    if not predchozi :
        odebrany_prvek = zasobnik[0]
        zasobnik[:] = [] 
    else:
        odebrany_prvek = predchozi[1][0]
        predchozi[1] = []  
    return odebrany_prvek





