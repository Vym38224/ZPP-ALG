import re

roman_pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

roman_input = input("Zadej římské číslo: ")
roman_input = roman_input.upper()

if re.match(roman_pattern, roman_input):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic_result = 0
    prev_value = 0

    for numeral in roman_input[::-1]: # pozpátku
        value = roman_numerals[numeral]

        if value < prev_value:
            arabic_result -= value
        else:
            arabic_result += value

        prev_value = value

    print(arabic_result)
else:
    print("Řetězec není římské číslo.")