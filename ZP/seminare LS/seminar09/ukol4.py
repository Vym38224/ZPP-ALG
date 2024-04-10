def convert_bytes_to_number(bytes):
    pass

def convert_number_to_bytes(number):
        bytes_array = []
        if number:
            while number:
                byte = number & 0xff
                bytes_array.append(byte)
                number = number >> 8
        else:
            bytes_array.append(0)
        return bytes_array[::-1]
    
# Použití
bytes_array = convert_number_to_bytes(2161) # vrátí: [36, 92]
try:
    f = open("ZP/seminare LS/seminar09/soubor.bin","wb")
    f.write(bytes(bytes_array))
except:
    # ošetření výjimek
    print("Chyba při práci se souborem.")
finally:
    # uzavření souboru
    f.close()

print(bytes_array)