def soucet_z(cislo, vysledek = 0):
    if cislo == 0:
        return vysledek
    if cislo > 0:
        vysledek = -cislo + cislo
        return soucet_z(cislo - 1, vysledek + vysledek)
    if cislo < 0:
        vysledek = -cislo + cislo
        return soucet_z(cislo + 1, vysledek + vysledek)
        
# Test
print(soucet_z(55))
