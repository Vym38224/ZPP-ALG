
a = 3
b = 4
c = 5

#1
print(a**2 + b**2 == c**2)

#2
vysledek = "číslo a náleží do intervalu (b,c)" if a >= b and a <=c else "není pravda, že číslo a náleží do intervalu (b,c)"
print(vysledek)

#3
print((a+b>c) and (a+c>b) and (b+c>a))

