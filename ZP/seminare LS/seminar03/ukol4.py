def aplikuj(f, sekvence):
    vysledek = 0
    if len(sekvence) % 2 != 0:
        sekvence.append(0)
    for i in range(0,len(sekvence),2):  
        vysledek += f(sekvence[i],sekvence[i+1])
    return vysledek

print(aplikuj(lambda x,y: x+y, [1,2,3,4,5]))


#2.verze
def aplikuj(f, sekvence):
    if len(sekvence) % 2 != 0:
        sekvence.append(0)
    return sum(f(sekvence[i], sekvence[i+1]) for i in range(0, len(sekvence), 2))

print(aplikuj(lambda x, y: x + y, [1, 2, 3, 4, 5]))
