def preved_cislo_na_bajty(x, pocet_bajtu):
    bytes_array = []
    for _ in range(pocet_bajtu):
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

def zapis_cisla(soubor, pocet_bajtu, cisla):
    f = open(soubor, "wb")
    f.write(bytes([pocet_bajtu]))
    for cislo in cisla:
        bajty = preved_cislo_na_bajty(cislo, pocet_bajtu)
        f.write(bytes(bajty))
    f.close()

# Příklad použití
cisla = [9308, 255, 65535]
soubor = "ZP/seminare LS/seminar11_ZPU2/cisla.bin"
pocet_bajtu = 2
zapis_cisla(soubor, pocet_bajtu, cisla)

def precti_cisla(soubor):
    f = open(soubor, "rb")
    pocet_bajtu = ord(f.read(1))
    cisla = []
    while True:
        bajty = f.read(pocet_bajtu)
        if not bajty:
            break
        cisla.append(preved_bajty_na_cislo(bajty))
    return cisla

# Příklad použití
soubor = "ZP/seminare LS/seminar11_ZPU2/cisla.bin"
cisla = precti_cisla(soubor)
print(cisla)

