def convert(letter):
    # Unicode hodnoty pro písmena 'a' a 'A'
    lowercase_a = 97
    uppercase_A = 65
    
    # Unicode hodnota zadaného písmene
    unicode_letter = ord(letter)
    
    # velká a malá písmena se liší v pátém bitu
    mask = 1 << 5 
    
    # Pokud je písmeno malé, přepneme 5. bit na 0 
    if lowercase_a <= unicode_letter <= lowercase_a + 25:
        return chr(unicode_letter & ~mask)
    
    # Pokud je písmeno velké, přepneme 5. bit na 1 
    elif uppercase_A <= unicode_letter <= uppercase_A + 25:
        return chr(unicode_letter | mask)
    
    else:
        return letter

# Test
print(convert('a'))  
print(convert('Z'))  
print(convert('4'))  
