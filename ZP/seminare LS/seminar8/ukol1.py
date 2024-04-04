def bits_count(decimal):
    count = 0
    while decimal > 0:
        decimal = decimal//2
        count += 1
    return count

# Test
print(bits_count(2))
print(bits_count(8))
print(bits_count(16))



