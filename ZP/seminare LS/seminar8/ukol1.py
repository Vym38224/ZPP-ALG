def set_bit(number, bit):
        mask = 1 << bit
        return number | mask
    
def delete_bit(number, bit):
    mask = ~(1 << bit)
    return number & mask

# použít funkce set_bit()
a= set_bit(0, 0) # vrací: 1 (0b1)
b =set_bit(0, 7) # vrací: 128 (0b10000000)

# použít funkce delete_bit()
c= delete_bit(255, 0) # vrací: 254 (0b11111110)
d= delete_bit(255, 2) # vrací: 251 (0b11111011)

print(a)
print(b)
print(c)
print(d)