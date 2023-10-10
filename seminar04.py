import math

a = float(input("Zadejte číslo a: "))
b = float(input("Zadejte číslo b: "))
c = float(input("Zadejte číslo c: "))

D = b**2 - 4*a*c

if a!=0:
    if D > 0:
        x1 = ((-b + math.sqrt(D))/(2*a))
        x2 = ((-b - math.sqrt(D))/(2*a))
        print(f"Rovnice má dva reálné kořeny: {x1} a {x2} .")
    elif D == 0:
        x1 = (-b / 2*a)
        print(f"Rovnice má jeden dvojnásobný reálný kořen: {x1} .")
    else:
        print(f"Rovnice nemá v oboru reálných čísel řešení.")
else:
    print("Rovnice není kvadratická, ale lineární.")