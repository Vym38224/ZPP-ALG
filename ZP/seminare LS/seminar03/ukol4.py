def aplikuj(f, sekvence):
    vysledek = sekvence[0]   
    for prvek in sekvence[1:]:
        vysledek = f(vysledek, prvek)  
    return vysledek

# Test
print(aplikuj(lambda x, y: x + y, [1, 2, 3, 4, 5]))  
