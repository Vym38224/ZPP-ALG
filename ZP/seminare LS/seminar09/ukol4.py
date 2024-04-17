def convert_bytes_to_number(bytes_array):
        try:
            f = open("ZP/seminare LS/seminar09/soubor.bin", "wb")
            f.write(bytes(bytes_array))
        except Exception as e:
            # ošetření výjimek
            print("Chyba při práci se souborem bytes:", e)
        finally:
            f.close()

        number = 0
        if bytes_array:
            for byte in bytes_array:
                number = (number << 8) + byte
        return number

def convert_number_to_bytes(number):
        try:
            f1 = open("ZP/seminare LS/seminar09/soubor.bin", "rb")
            f1.read()
        except Exception as e:
            # ošetření výjimek
            print("Chyba při práci se souborem number:", e)
        finally:
            f1.close()

        bytes_array = []
        if number:
            while number:
                byte = number & 0xff
                bytes_array.append(byte)
                number = number >> 8
        else:
            bytes_array.append(0)
        return bytes_array[::-1]
        
bytes_array = [36,92]

number = convert_bytes_to_number(bytes_array)
print(number)

bytes_array = convert_number_to_bytes(number)
print(bytes_array)

number = convert_bytes_to_number(bytes_array)
print(number)







