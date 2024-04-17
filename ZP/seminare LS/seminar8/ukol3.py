def rotate_right(number, count):
    binary = bin(number)[2:]
    rotated = binary[-count:] + binary[:-count]  
    p =  bin(int(rotated, 2))
    return p

number = 0b100100111
count = 2
print(rotate_right(number, count))  


# Neuznáno, protože to není blbě ale není to na uznání



