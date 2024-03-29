def decimal_to_binary(decimal):
    binary = ""
    if decimal == 0:
        binary = "0"
    while decimal > 0:
        binary = str(decimal%2) + binary
        decimal = decimal//2
    return binary

# Test
try:
    decimal_number = int(16/2)
    decimal_number = int(16/0)
except ZeroDivisionError:
    print("Druhý operand operace dělení nebo modulo je roven nule")

binary_number = decimal_to_binary(decimal_number)
print("Binární číslo:", binary_number)
