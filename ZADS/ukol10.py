import random
import unicodedata

N=10
P=13

def h1(k):
    return k%N

def list_insert(l,k):
    l.append(k)

def list_search(l,k):
    for i in l:
        if i==k:
            return True
    return False

def list_delete(l,k):
    if list_search(l,k)==True:
        l.remove(k)

def insert(T, k):
    i=T["hash"](k)
    list_insert(T["data"][i], k)

def search(T, k):
    i = T["hash"](k)
    return list_search(T["data"][i], k)

def delete(T, k):
    i=T["hash"](k)
    list_delete(T["data"][i], k)

def print_table(T):
    for r in T["data"]:
        print(r)

t=[[] for i in range(N)]
table={"data":t,"hash":h1}
s = [i for i in range(100)]
random.shuffle(s)
for i in s:
    insert(table,i)

print_table (table)
print(search(table,12))
print()
delete(table,12)
print_table (table)
print()

#Otevřené adresování
N=19
C1=0
C2=1
def h1(k):
    return k%N

def h2(k):
    return 1 + (k%N - 1)

def g1(k,i):
    return  (h1(k) + i)% N

def g2(k, i):
    return (h1(k) + C1*i + C2*i^2)%N

def g3(k, i):
    return (h1(k) + i*h2(k))%N
   
def insert(T, k):
    for i in range(len(T["data"])):
        j=T["g"](k,i)
        if T["data"][j] == None:
            T["data"][j]=k
            return

def search(T,k):
    for i  in range(len(T["data"])):
        j=T["g"](k,i)
        if T["data"][j] == k:
            return k
        if T["data"][j] == None:
            break
    return None

t=[None for i in range(N)]
table2={"data":t,"g":g1}
t=[None for i in range(N)]
table3={"data":t,"g":g2}
t=[None for i in range(N)]
table4={"data":t,"g":g3}
s = [random.randint(1,100) for i in range(10)]
random.shuffle(s)
print(s)
for i in s:
    insert(table2,i)
    insert(table3,i)
    insert(table4,i)

print(table2["data"])

print(table3["data"])

print(table4["data"])
print()
#Mazání

N=19
def h1(k):
    return k%N

def g1(k,i):
    return  (h1(k) + i)% N

def insert(T, k):
    for i in range(len(T["data"])):
        j=T["g"](k,i)
        if T["data"][j][0] == None or T["data"][j][1]==False:
            T["data"][j][0]=k
            T["data"][j][1]=True
            return

def search(T,k):
    for i  in range(len(T["data"])):
        j=T["g"](k,i)
        if T["data"][j][0] == k:
            return k
        if T["data"][j][0] == None:
            break
    return None

def delete(T,k):
    for i  in range(len(T["data"])):
        j=T["g"](k,i)
        if T["data"][j][0] == k:
            T["data"][j][1] =False
            return
        if T["data"][j][0] == None:
            break
    return None

t=[[None,False] for i in range(N)]
table5={"data":t,"g":g1}

s = [random.randint(1,100) for i in range(N)]
random.shuffle(s)
for i in s:
    insert(table5,i)
print(table5["data"])
delete(table5,s[5])
print(s[5])
print(table5["data"])


#
N = 1000
data =[None for i in range(N)]
table={"data": data,"hash": h1}
s = [i for i in range(100)]
random.shuffle(s)
for i in s:
    insert(table,i)
"""800;Lýkurgovy zákony ve Spartě
776;první olympijské hry
650;první vlády tyranů
621;Drakon se stává archontem a zavádí přísné zákony
594;Solón archontem, reforma politického systému
546;Peisistratos uchvacuje moc v Athénách jako tyran
508;k moci se dostává Kleisthenes, otevírá cestu k demokracii
494;Peršané potlačují iónskou revoltu
490;Peršané útočí na Řecko, bitva u Marathónu
480;bitva u Thermopyl
480;bitva Artemisia
479;bitva u Platají, bitva u mysu Mykalé; Peršané vyhnáni z Řecka
478;Athény a další městské státy zakládají delský spolek proti Persii
449;uzavřen mír s Persií, definitivní konec řecko;perských válek
432;dokončen Parthénon
430;umírá dějepisec Hérodotos
429;umírá asi Feidiás
413;zničení flotily Athén na Sicílii
405;bitva u Aigospotamoi
404;v Athénách po porážce nastolena vláda třiceti tyranů
399;začátek války mezi Spartou a Persií, Sokrates odsouzen k smrti
395;umírá historik Thúkydidés
395;korintská válka
371;bitva u Leuktry, thébská hegemonie
362;Athény se Spartou poráží Théby u Mantineie
359;Filippos II. zvolen králem Makedonie
347;smrt Platóna
338;bitva u Chairóneie, Řecko sjednoceno pod nadvládou Makedonců
336;smrt Filippa a nástup Alexandra III. Velikého
334;bitva u Gráníku
333;bitva u Issu
331;bitva u Gaugamély
327;Alexandr si podrobuje Persii
326;bitva u Hydaspu
323;Alexandr umírá v Babylóně
323;lamijská válka, řecké státy nezískávají samostatnost
323;války diadochů
322;umírají Démosthenés a Aristoteles
315;v Makedonii začíná vládnout dynastie Antigonovců
301;bitva u Ipsu a vznik království čtyř diadochů
281;bitva u Korupedia, konec válek diadochů a vznik tří nástupnických království
275;Pyrrhos poražen Římany
215;Filippos se spojuje s Hanibalem
215;první makedonská válka
212;zabit Archimédes
202;druhá makedonská válka, Filippos poražen a ztrácí Řecko
168;bitva u Pydny
147;achajská válka, po porážce Řeků ničí Římané Korint a zřizují provincie"""