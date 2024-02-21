def caesar_sifra(sifrovany_text, posun):
    abeceda = 'abcdefghijklmnopqrstuvwxyz'
    text = ""
    for char in sifrovany_text:
        if char.isalpha():      
            index = abeceda.index(char) - posun
            desifrovany_char = abeceda[index]
        text += desifrovany_char
    return text

# Zadaná šifrovaná zpráva
sifrovany_text = "mrwfvqbfcryivfiqborxqlfrmnqanmirpvpbfvcerwrfarqnxbhcvgibopubqr"

# Test, prozkoušení všech možných klíčů (posunů)
for posun in range(1, 26):
    text = caesar_sifra(sifrovany_text, posun)
    print(f"Klíč {posun}: {text}")
