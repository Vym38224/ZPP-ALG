def mocnina(zaklad, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / mocnina(zaklad, -exponent)
    else:
        return zaklad * mocnina(zaklad, exponent - 1)


# počítá výsledek v každém kroku až do dosažení exponentu 0
def mocnina_koncove(zaklad, exponent, vysledek=1):
    if exponent == 0:
        return vysledek
    elif exponent < 0:
        return mocnina_koncove(zaklad, exponent + 1, vysledek / zaklad)
    else:
        return mocnina_koncove(zaklad, exponent - 1, vysledek * zaklad)

# Test
print(mocnina(3,3))  
print(mocnina_koncove(3,3))

