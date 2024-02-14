polozky = []

def pridej_polozku(den, mesic, rok, castka, kategorie):
    polozky.append({
        "den": den,
        "mesic": mesic,
        "rok": rok,
        "castka": castka,
        "kategorie": kategorie
    })

def prehled(mesic, rok):
    soucet_vydaju = {}
    for polozka in polozky:
        if polozka["mesic"] == mesic and polozka["rok"] == rok:
            kategorie = polozka["kategorie"]
            castka = polozka["castka"]           
            if kategorie in soucet_vydaju:
                soucet_vydaju[kategorie] += castka
            else:
                soucet_vydaju[kategorie] = castka

    return soucet_vydaju

# Příklad použití
pridej_polozku(15, 10, 2022, 150, "jídlo")
pridej_polozku(16, 11, 2022, 250, "jídlo")
pridej_polozku(17, 11, 2022, 300, "bydlení")
pridej_polozku(18, 11, 2022, 500, "jídlo")
pridej_polozku(19, 11, 2022, 150, "domáctnost")

print(prehled(11, 2022))

