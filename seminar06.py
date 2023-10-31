cislo = int(input("Zadejte přirozené číslo: "))
print(f"Prvočíselný rozklad čísla {cislo} je:", end=" ")

d = 2
while cislo > 1:
    if cislo % d == 0:
        print(d, end=" ")
        cislo //= d
    else:
        d += 1