def soucet_z(a, b, vysledek=0):
    if a == 0 and b == 0:
        return vysledek
    elif a == 0 and b > 0:
        return soucet_z(a,b-b,vysledek+a+b)
    elif a > 0 and b == 0:
        return soucet_z(a-a,b,vysledek+a+b)
    elif a>b or b>a:
        return soucet_z(a-a,b-b,vysledek+a+b)
        
# Test
print(soucet_z(1,3))
