def caesar_sifra(sifrovany_text, posun):
    try:
        abeceda = "abcdefghijklmnopqrstuvwxyz"
        text = ""
        for char in sifrovany_text:
            if char.isalpha():      
                index = abeceda.index(char) - posun
                desifrovany_char = abeceda[index]
            text += desifrovany_char
        return text
    except IndexError:
        return("Přístup na neexistující index v kolekci")

# Zadaná šifrovaná zpráva
sifrovany_text = "mrwfvqbfcryivfiqborxqlfrmnqanmirpvpbfvcerwrfarqnxbhcvgibopubqr"

# Test, prozkoušení všech možných klíčů (posunů)
for posun in range(1, 30):
    text = caesar_sifra(sifrovany_text, posun)
    print(f"Klíč {posun}: {text}")

