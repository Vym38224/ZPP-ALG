def rozklad(n, max_scitanec=None):
    if n == 0:
        return [[]]
    
    if max_scitanec is None:
        max_scitanec = n

    rozklady = []
    for i in range(1, min(max_scitanec, n) + 1):
        podrozklady = rozklad(n - i, i)
        for podrozklad in podrozklady:
            rozklady.append([i] + podrozklad)

    return rozklady

# Příklad pro n=6
n = 6
výsledek = rozklad(n)
for rozklad in výsledek:
    print(rozklad)