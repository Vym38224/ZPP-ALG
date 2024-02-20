def create_array(n):
    k = [{"key": None, "data": None} for x in range(n)]
    s = {"keys": k,"top":0}
    return s

def insert(array, key, data):
    if array["top"] < len(array["keys"]):
        array["keys"][array["top"]] = {"key": key, "data": data}
        array["top"] += 1
        
f = create_array(800)

insert(800,"Lýkurgovy zákony ve Spartě")
insert(776,"první olympijské hry")
insert(399,"začátek války mezi Spartou a Persií, Sokrates odsouzen k smrti")
insert(395,"umírá historik Thúkydidés")
insert(395,"korintská válka")
insert(371,"bitva u Leuktry, thébská hegemonie")
insert(362,"Athény se Spartou poráží Théby u Mantineie")
insert(359,"Filippos II. zvolen králem Makedonie")
insert(347,"smrt Platóna")
insert(338,"bitva u Chairóneie, Řecko sjednoceno pod nadvládou Makedonců")
insert(336,"smrt Filippa a nástup Alexandra III. Velikého")
insert(334,"bitva u Gráníku")
insert(333,"bitva u Issu")
insert(331,"bitva u Gaugamély")
insert(327,"Alexandr si podrobuje Persii")
insert(326,"bitva u Hydaspu")
insert(323,"Alexandr umírá v Babylóně")
insert(323,"lamijská válka, řecké státy nezískávají samostatnost")
insert(323,"války diadochů")
insert(322,"umírají Démosthenés a Aristoteles")
insert(315,"v Makedonii začíná vládnout dynastie Antigonovců")
insert(301,"bitva u Ipsu a vznik království čtyř diadochů")
insert(281,"bitva u Korupedia, konec válek diadochů a vznik tří nástupnických království")
insert(275,"Pyrrhos poražen Římany")
insert(215,"Filippos se spojuje s Hanibalem")
insert(215,"první makedonská válka")
insert(212,"zabit Archimédes")
insert(202,"druhá makedonská válka, Filippos poražen a ztrácí Řecko")
insert(168,"bitva u Pydny")
insert(147,"achajská válka, po porážce Řeků ničí Římané Korint a zřizují provincie")


def binary_search(array, key):
    # Filtrujeme prvky s None klíči
    filtered_array = [item for item in array if item["key"] is not None]

    low = 0
    high = len(filtered_array) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_key = filtered_array[mid]["key"]

        if mid_key == key:
            return filtered_array[mid]["data"]  
        elif mid_key < key:
            low = mid + 1  
        else:
            high = mid - 1  

    return "Tento rok se nic nestalo"  # Klíč nenalezen


# Použití binárního vyhledávání na poli
array_set = f["keys"]
print("Rok 371:" + binary_search(array_set, 371))
print("Rok 100:" + binary_search(array_set,100))

