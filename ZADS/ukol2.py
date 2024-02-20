def create_array(n):
    k = [{"key": None, "data": None} for x in range(n)]
    s = {"keys": k,"top":0}
    return s

def insert(array, key, data):
    if array["top"] < len(array["keys"]):
        array["keys"][array["top"]] = {"key": key, "data": data}
        array["top"] += 1

f = create_array(10)
insert(f,371,"Bitva u Leuktry, thébská hegemonie")
insert(f,100,"Nějaká událost v roce 100")

def binary_search(array, key):
    # Filtrujeme prvky s None klíči
    filtered_array = [item for item in array if item['key'] is not None]

    low = 0
    high = len(filtered_array) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_key = filtered_array[mid]['key']

        if mid_key == key:
            return filtered_array[mid]['data']  # Vracíme popis události
        elif mid_key < key:
            low = mid + 1  
        else:
            high = mid - 1  

    return "Tento rok se nic nestalo"  # Klíč nenalezen


# Použití binárního vyhledávání na poli
array_set = f["keys"]
print("Rok 371:" + binary_search(array_set, 371))
print("Rok 100:" + binary_search(array_set,100))

