def count_leading_zeros(binary_str):
    count = 0
    for bit in binary_str:
        if bit == '0':
            count += 1
        else:
            break
    return count

# Testování funkce
binary_number_str = '0b001111'  # Používáme řetězcovou reprezentaci binárního čísla
binary_str = binary_number_str[2:]  # Odstraníme předponu '0b'
num_zeros = count_leading_zeros(binary_str)
print("Počet nul na začátku binárního čísla:", num_zeros)  # Vypíše: Počet nul na začátku binárního čísla: 2
