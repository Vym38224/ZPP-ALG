def soucet_intervalu_rekurze(start, end):
    if start > end:
        return 0
    else:
        return start + soucet_intervalu_rekurze(start + 1, end)

# Příklad použití funkce:
start = 1
end = 4
vysledek = soucet_intervalu_rekurze(start, end)
print(f"Součet čísel od {start} do {end} je: {vysledek}")
