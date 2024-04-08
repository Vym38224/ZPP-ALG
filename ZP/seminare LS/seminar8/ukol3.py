def rotate_right(number, count):
    # Počet nul v našem číslu
    b = []
    for bit in number:
        if bit == '1':
            b.append(1)
        elif bit == '0':
            b.append(0)

    pocet_nul=""
    for i in range(len(b)-count):
        if b[i] == 0:
            pocet_nul += "0"
        else:
            break

    # Binární číslo po posunu do prava
    number = int(number,2)
    p = number >> count
    binary = ""
    if p == 0:
        binary = ""
    while p > 0:
        binary = str(p%2) + binary
        p= p//2

    # Vrácení ztracených prvků z posunu na začátek binárního čísla
    vysledek = ""
    for i in range(len(b)-1, len(b)-1-count, -1):
        if b[i] == 1:
            vysledek = "1" + vysledek
        else:
            vysledek = "0" + vysledek

    return vysledek + pocet_nul + binary



number = 0b10010011 
# když to vezme tohle číslo tak automaticky převede na int a když ho pak zpátky ve funkci převedu na binární tak ztratí počet nul před první jedničkou
# pak se blbě přidává na začátek to co bylo posunuto do prava, jak to opravit?
str_number = "10010011"
count = 2
print(rotate_right(str_number,count))




