f = open("ZP/seminare LS/seminar09/soubor.txt","r")
precteni_celeho = f.read()
kolik_znaku = len(precteni_celeho)
f.seek(0)
i = kolik_znaku
while i > 0:
    p = f.read(1)
    i -= 1
    print(p,end="")