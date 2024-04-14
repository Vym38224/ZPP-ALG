def rotate_right(number, count):
    p = number >> count
    binary = ""
    posunute = bin_to_list(p)
    for i in posunute:
        if posunute[i-1] == 1:
            binary += "1"
        else:
            binary += "0"
    return ztracene_bity(number,count) + binary

def bin_to_list(n):
    b = []
    while n:
        b = [n & 1] + b
        n >>= 1
    return b or [0]

def ztracene_bity(number, count):
    vysledek = ""
    number = bin_to_list(number)
    for i in range(len(number)-1, len(number)-1-count, -1):
        if number[i] == 1:
            vysledek = "1" + vysledek
        else:
            vysledek = "0" + vysledek
    return vysledek


number = 0b0010011 
count = 2
print(rotate_right(number,count))




