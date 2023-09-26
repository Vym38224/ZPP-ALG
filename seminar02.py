
a = 3
b = 4
c = 5

### without fce if (součást zadání) ###

#1
print(a**2 + b**2 == c**2)

#2
vysledek = "číslo a náleží do intervalu (b,c)" if a >= b and a <= c else "není pravda, že číslo a náleží do intervalu (b,c)"
print(vysledek)

#3
print((a+b>c) and (a+c>b) and (b+c>a))


### with fce if ###

a= 8
b= 3
c= 2

#1
if a**2 + b**2 == c**2 == True:   
    print("Platí Pythagorova věta")
else:
    print("Neplatí Pythagorova věta")

#2
if a >= b and a <= c:
    print("Číslo a náleží do intervalu (a,b)")
else:
    print("Není pravda, že číslo a náleží do intervalu (a,b)")

#3
if a!=0 and b!= 0 and c!= 0 and a+b>c and a+c>b and b+c>a:
    print("Daný trojúhelník lze sestrojit")
else:
    print("Daný trojúhelník nelze sestrojit")







