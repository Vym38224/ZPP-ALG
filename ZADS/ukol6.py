def vloz_do_zebricku(strom, jmeno, body):
    z = {"left": None, "right": None, "parent": None, "key": jmeno, "hodnota": body}  
    y = None
    x = strom["root"]
    
    while x is not None:
        y = x
        if z["key"] < x["key"]:
            x = x["left"]
        else:
            x = x["right"]
    
    z["parent"] = y
    if y is None:
        strom["root"] = z
    elif z["key"] < y["key"]:
        y["left"] = z
    else:
        y["right"] = z

def select(r, k):#najde k-tý prvek ve stromu
    if r["left"] == None:
        t=0
    else:
        t=r["left"]["count"]
    if t > k - 1:
        return select(r["left"], k)
    elif t < k - 1:
        return select(r["right"], k - t - 1)
    else:
        return r

zebricek = {"root": None}

vloz_do_zebricku(zebricek,"Garcia Caroline",4415)
vloz_do_zebricku(zebricek,"Swiatek Iga",11025)
vloz_do_zebricku(zebricek,"Pegula Jessica",5000)
vloz_do_zebricku(zebricek,"Sabalenka Aryna",4340)
vloz_do_zebricku(zebricek,"Gauff Cori",3871)
vloz_do_zebricku(zebricek,"Kudermetova Veronika",2715)
vloz_do_zebricku(zebricek,"Keys Madison",2597)
vloz_do_zebricku(zebricek,"Sakkari Maria",3921)
vloz_do_zebricku(zebricek,"Jabeur Ons",5180)
vloz_do_zebricku(zebricek,"Kasatkina Darya",3380)

def najdi_poradi(s, k):
    return select(s["root"], k)["key"]  # Vrátí klíč (jméno) vybraného hráče

print("1. hráčkou žebříčku WTA je", najdi_poradi(zebricek, 1))
#print("8. hráčkou žebříčku WTA je", najdi_poradi(zebricek, 8))
