def vytvor_seznam(key):
    return {"key": key, "left": None, "right": None, "parent": None}

def tree_search(x,k):
    if x == None or k == x["key"]:
        return x
    if k < x["key"]:
        return tree_search(x["left"], k)
    else:
        return tree_search(x["right"], k)

def vloz_do_seznamu(T, z):
    y = None
    x = T["root"]
    while x is not None:
        y = x
        if z["key"] < x["key"]:
            x = x.get("left")
        else:
            x = x.get("right")
    z["parent"] = y
    if y is None:
        T["root"] = z
    elif z["key"] < y["key"]:
        y["left"] = z
    else:
        y["right"] = z

def tisk_seznamu(x):
    if x != None:
        tisk_seznamu(x["left"])
        print(x["key"],end=" ")
        tisk_seznamu(x["right"])

def odeber_ze_seznamu(seznam, jmeno):
    nalezenenec = tree_search(seznam["root"],jmeno)
    tree_delete(seznam,nalezenenec)

def tree_swap(t,u,v):
    if t["root"] == u:
        t["root"] = v
        return
    y = u["parent"]
    if u==y["left"]:
        y["left"]=v
    if u==y["right"]:
        y["right"]=v

def node_swap(t,u,v):
    v["left"]=u["left"]
    v["right"]=u["right"]
    if t["root"]==u:
        t["root"]=v
        return
    y=u["parent"]
    if u==y["left"]:
        y["left"]=v
    if u==y["right"]:
        y["right"]=v

def tree_delete(t,z):
    if z["left"] == None:
        tree_swap(t,z,z["right"])
        return
    if z["right"] == None:
        tree_swap(t,z,z["left"])
        return
    y=tree_min(z["right"])
    tree_delete(t,y)
    node_swap(t,z,y)

def tree_min(x):
    while x["left"] != None:
        x=x["left"]
    return x

seznam = ["Pavel", "Jitka", "Alice", "Karel", "David"]
osoby = {"root": None}

for i in seznam:
    vloz_do_seznamu(osoby, vytvor_seznam(i))

print("Seznam osob:", end=" ")
tisk_seznamu(osoby["root"])
print()
odeber_ze_seznamu(osoby, "Alice")
print("Seznam osob:", end=" ")
tisk_seznamu(osoby["root"])
