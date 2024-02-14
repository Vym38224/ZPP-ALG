knihovna = []
def pridej_knihu(nazev, autor_jmeno, autor_prijmeni):
    kniha = {"nazev": nazev, "autor_jmeno": autor_jmeno, "autor_prijmeni": autor_prijmeni, "pujcena": False}
    knihovna.append(kniha)
    
def vypujceni(nazev):
    for kniha in knihovna:
        if kniha["nazev"] == nazev:
            if not kniha["pujcena"]:
                kniha["pujcena"] = True

def vraceni(nazev):
    for kniha in knihovna:
        if kniha["nazev"] == nazev:
            if kniha["pujcena"]:
                kniha["pujcena"] = False

def vypujcene_knihy():
    vypujcene = [kniha["nazev"] for kniha in knihovna if kniha["pujcena"]]
    return vypujcene

# Příklad použití
pridej_knihu("Algoritmy v C", "Robert", "Sedgewick")
pridej_knihu("The Art of Computer Programming, Volume 1", "Donald", "Knuth")
pridej_knihu("The Art of Computer Programming, Volume 2", "Donald", "Knuth")

vypujceni("The Art of Computer Programming, Volume 1")
vypujceni("The Art of Computer Programming, Volume 2")

vypujcene_knihy = vypujcene_knihy()
print("Seznam vypůjčených knih:")
for nazev in vypujcene_knihy:
    print(nazev)
