def rotate_right(number, count):
    p = number >> count
    binary = ""
    if p == 0:
        binary = "0"
    while p > 0:
        binary = str(p%2) + binary
        p = p//2
    return binary
    

number = 0b10010010
count = 2
print(rotate_right(number,count))

