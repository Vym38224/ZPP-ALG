n = int(input("Zadej libovolné přirozené číslo: "))
puvodni_cislo = n
delka_cisla = 0
n_str = str(n)
je_palindron = True

while n != 0:
    n//=10
    delka_cisla += 1

i = 0
j = delka_cisla - 1

while i<j:
    if n_str[i] != n_str[j]:
        je_palindron = False
        break
    i += 1
    j -= 1

if je_palindron:
    print("Je palindron")
else:
    print("Není palindron")



    



    
    
