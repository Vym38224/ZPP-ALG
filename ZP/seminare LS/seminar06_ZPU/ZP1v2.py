PRVNI_PRVEK = 0
DALSI_PRVEK = 1

def druha_struktura(seznam, index):
    new_item = [index, [], []]
    if not seznam:
        seznam.extend(new_item)
    else:
        current_item = seznam
        while current_item[DALSI_PRVEK]:
            current_item = current_item[DALSI_PRVEK]
        current_item[DALSI_PRVEK] = new_item
    return new_item

def vytvor_matici(m, n):
    info_matice = [m, n, [], []]  
    if not info_matice[2]:
        for i in range(m):
            druha_struktura(info_matice[2], i)

    if not info_matice[3]:
        for i in range(n):
            druha_struktura(info_matice[3], i)
    return info_matice

def vloz_prvek(hodnota, i_radek, i_sloupec, matice):
    matice_info = matice[:]  # Kopie matice

    # Hledání správného řádku
    radek = matice_info[2]
    if not radek or radek[PRVNI_PRVEK] != i_radek:
        radek = druha_struktura(matice_info[2], i_radek)
    else:
        while radek[DALSI_PRVEK] and radek[PRVNI_PRVEK] != i_radek:
            radek = radek[DALSI_PRVEK]

    # Hledání správného sloupce
    sloupec = matice_info[3]
    if not sloupec or sloupec[PRVNI_PRVEK] != i_sloupec:
        sloupec = druha_struktura(matice_info[3], i_sloupec)
    else:
        while sloupec[DALSI_PRVEK] and sloupec[PRVNI_PRVEK] != i_sloupec:
            sloupec = sloupec[DALSI_PRVEK]

    # Aktualizace indexů řádku a sloupce
    radek_index = radek[PRVNI_PRVEK]
    sloupec_index = sloupec[PRVNI_PRVEK]

    # Vytvoření nového prvku
    new_item = [hodnota, i_radek, i_sloupec, [], []]

    # Přidání nového prvku na správné místo v řádku
    if radek_index == i_radek:
        current_item = radek
        while current_item[DALSI_PRVEK]:
            current_item = current_item[DALSI_PRVEK]
        current_item[DALSI_PRVEK] = new_item
    else:
        current_item = radek
        while current_item[DALSI_PRVEK]:
            current_item = current_item[DALSI_PRVEK]
        current_item[DALSI_PRVEK] = [i_radek, [], new_item]

    # Přidání nového prvku na správné místo ve sloupci
    if sloupec_index == i_sloupec:
        current_item = sloupec
        while current_item[DALSI_PRVEK]:
            current_item = current_item[DALSI_PRVEK]
        current_item[DALSI_PRVEK] = new_item
    else:
        current_item = sloupec
        while current_item[DALSI_PRVEK]:
            current_item = current_item[DALSI_PRVEK]
        current_item[DALSI_PRVEK] = [i_sloupec, [], new_item]

    return matice_info



# Testování
matice = vytvor_matici(3, 4)
vloz_prvek(1, 1, 2, matice)
print(matice)
