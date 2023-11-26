from datetime import date

def vytvor_osobu(jmeno,prijmeni,adresa,den,mesic,rok,telefon,mail):
    return {
        "jmeno": jmeno,
        "prijmeni": prijmeni,
        "adresa": adresa,
        "datum_narozeni": date(rok, mesic, den),
        "telefon": telefon,
        "email": mail
    }

def vloz(s,o):
    s.append(o)

def tisk_osoby(o):
    print(f"Jméno: {o['jmeno']}, Příjmení: {o['prijmeni']}, Adresa: {o['adresa']}, Datum narození: {o['datum_narozeni']}, Telefon: {o['telefon']}, Email: {o['email']}")

def tisk(s):
    for osoba in s:
        tisk_osoby(osoba)

def najdi_osobu(kde,co,s):
    for osoba in s:
        hodnota = osoba[kde]
        if co.lower() in str(hodnota).lower():
            return True
    return False

def nejmladsi(s):
    return max(s, key=lambda osoba: osoba["datum_narozeni"])

seznam_osob=[]

o1 = vytvor_osobu("Alice", "Pokorna", "Holicka 62", 2, 1, 1992, "214 145 478", "alice.pokorna@email.cz")
o2 = vytvor_osobu("Pavel", "Novak", "tr. 17 listopadu 24", 13, 1, 1992, "654 784 478", "pavel.novak@seznam.cz")
o3 = vytvor_osobu("Ales", "Maly", "Holicka 62", 6, 5, 1989, "772 847 457", "ales.maly@upol.cz")

vloz(seznam_osob, o1)
vloz(seznam_osob, o2)
vloz(seznam_osob, o3)

print("\nSeznam osob:")
tisk(seznam_osob)

if (najdi_osobu("jmeno", "Alice", seznam_osob)):
    print("\nAlice nalezena.\n")
else: 
    print("\nAlice nenalezena.\n")

if (najdi_osobu("prijmeni", "Novotny", seznam_osob)):
    print("Novotny nalezen.\n")
else: 
    print("Novotny nenalezen.\n")

o = nejmladsi(seznam_osob)
print("Nejmladsi osobou v seznamu je:")
tisk_osoby(o)
print("\n")
