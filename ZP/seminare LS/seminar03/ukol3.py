def mapovani(f, sekvence):
    sekvence_f=[]
    for i in sekvence:
        sekvence_f.append(f(i))
    return sekvence_f

print(mapovani(lambda x: x+x, [1,2,3,4,5])) 

