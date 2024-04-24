def h1(k):
    return k % N

def h2(k):
    return 1 + (k % (N - 1))

def g1(k, i):
    return (h1(k) + i * h2(k)) % N

def g2(k, i):
    return (h1(k) + i) % N


def insert(T, year, event):
    for i in range(N):
        j = g1(year, i)
        if T["data"][j] is None:
            T["data"][j] = (year, event)
            return

def search(T, year):
    for i in range(N):
        j = g1(year, i)
        if T["data"][j] is not None and T["data"][j][0] == year:
            return T["data"][j][1]
        elif T["data"][j] is None:
            return "Tento rok se nic nestalo."

N = 1000 
t = [None] * N
table = {"data": t}

historical_data = [
    (800, "Lýkurgovy zákony ve Spartě"),
    (776, "první olympijské hry"),
    (650,"první vlády tyranů"),
    (621,"Drakon se stává archontem a zavádí přísné zákony")]

print(historical_data)

for year, event in historical_data:
    insert(table, year, event)

# Příklad použití
print("Rok 650: " + search(table, 650))
print("Rok 100: " + search(table, 100))
