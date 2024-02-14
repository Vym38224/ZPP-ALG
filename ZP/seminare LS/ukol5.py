def decimal_to_binary(decimal):
    binary = ""
    if decimal == 0:
        return "0"
    while decimal > 0:
        binary = str(decimal%2) + binary
        decimal = decimal // 2
    return binary

# Test
decimal_number = 5

binary_number = decimal_to_binary(decimal_number)
print("Binární číslo:", binary_number)
