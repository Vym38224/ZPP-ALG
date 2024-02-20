def create_array(n):
    k = [{"key": None, "data": None} for x in range(n)]
    s = {"keys": k, "top": 0}
    return s

def insert(array, key, data):
    if array["top"] < len(array["keys"]):
        array["keys"][array["top"]] = {"key": key, "data": data}
        array["top"] += 1
    return array  

f = create_array(40)
insert(f,371, "Bitva u Leuktry, thébská hegemonie")
insert(f,362, "Athény se Spartou poráží Théby u Mantineie")
insert(f,359,"Filippos II. zvolen králem Makedonie")
insert(f,347,"smrt Platóna")
insert(f,338,"bitva u Chairóneie, Řecko sjednoceno pod nadvládou Makedonců")
insert(f,336,"smrt Filippa a nástup Alexandra III. Velikého")
insert(f,334,"bitva u Gráníku")
insert(f,333,"bitva u Issu")
insert(f,331,"bitva u Gaugamély")
insert(f,327,"Alexandr si podrobuje Persii")
insert(f,326,"bitva u Hydaspu")
insert(f,323,"Alexandr umírá v Babylóně")
insert(f,323,"lamijská válka, řecké státy nezískávají samostatnost")
insert(f,323,"války diadochů")
insert(f,322,"umírají Démosthenés a Aristoteles")
insert(f,315,"v Makedonii začíná vládnout dynastie Antigonovců")
insert(f,301,"bitva u Ipsu a vznik království čtyř diadochů")
insert(f,281,"bitva u Korupedia, konec válek diadochů a vznik tří nástupnických království")
insert(f,275,"Pyrrhos poražen Římany")
insert(f,215,"Filippos se spojuje s Hanibalem")
insert(f,215,"první makedonská válka")
insert(f,212,"zabit Archimédes")
insert(f,202,"druhá makedonská válka, Filippos poražen a ztrácí Řecko")
insert(f,168,"bitva u Pydny")
insert(f,147,"achajská válka, po porážce Řeků ničí Římané Korint a zřizují provincie")


def key_sort(i):
    return i["key"]

l = f['keys'][:f['top']]
l.sort(key=key_sort)
f['keys'][:f['top']] = l

def binary_search(array, key):
    filtered_array = [item for item in array if item["key"] is not None]# Filtrujeme prvky s None klíči
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
    return "Tento rok se nic nestalo"  

# Test
array_set = f['keys']
print("Rok 371: " + binary_search(array_set, 371))
print("Rok 100: " + binary_search(array_set, 100))
