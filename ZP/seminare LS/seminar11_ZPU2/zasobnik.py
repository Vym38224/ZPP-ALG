
PRVNI_PRVEK = 0
DALSI_PRVEK = 1

def convert_number_to_bytes(number):
    bytes_array = []
    if number:
        while number:
            byte = number & 0xff
            bytes_array.append(byte)
            number = number >> 8
    else:
        bytes_array.append(0)
    return bytes_array[::-1]

def vytvor_zasobnik(max_bajty):
    return max_bajty, []

def pridej_do_zasobniku(seznam, x):
    max_bajty, zasobnik = seznam
    if 0 < x < 2**(max_bajty * 8):
        while zasobnik:
            zasobnik = zasobnik[DALSI_PRVEK]
        zasobnik.extend([x, []])
    else:
        print(f"hodnota {x} je mimo povolený rozsah.")

def zapis_do_souboru(nazev_souboru, zasobnik):
    max_bajty, data = zasobnik
    with open(nazev_souboru, "wb") as file:
        file.write(bytes([max_bajty]))
        file.write(bytes(data))

def nacti_ze_souboru(nazev_souboru):
    with open(nazev_souboru, "rb") as file:
        max_bajty = int.from_bytes(file.read(1), byteorder='big')
        zasobnik = list(file.read())
    return max_bajty, zasobnik

def odeber_ze_zasobniku(seznam):
    max_bajty, zasobnik = seznam
    if not zasobnik:
        return None
    
    predchozi = []
    aktualni = zasobnik

    while aktualni and aktualni[DALSI_PRVEK]:
        predchozi = aktualni
        aktualni = aktualni[DALSI_PRVEK]
    
    if not predchozi :
        odebrany_prvek = zasobnik[PRVNI_PRVEK]
        zasobnik[:] = [] 
    else:
        odebrany_prvek = predchozi[DALSI_PRVEK][PRVNI_PRVEK]
        predchozi[DALSI_PRVEK] = []  

    return odebrany_prvek





