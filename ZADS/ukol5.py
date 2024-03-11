def vytvor_seznam(key):
    return {"key": key, "left": None, "right": None, "parent": None}

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

def tisk_seznamu(node):
    if node:
        tisk_seznamu(node.get("left"))
        print(node["key"], end=" ")
        tisk_seznamu(node.get("right"))

def odeber_ze_seznamu(seznam, jmeno):
    node = seznam["root"]
    while node is not None and node["key"] != jmeno:
        if jmeno < node["key"]:
            node = node["left"]
        else:
            node = node["right"]
    if node is None:
        print(f"{jmeno} nenalezeno v seznamu.")
        return
    if node.get("left") is None:
        node_swap(seznam, node, node.get("right"))
    elif node.get("right") is None:
        node_swap(seznam, node, node.get("left"))
    del node

def tree_min(x):
    while x["left"] is not None:
        x = x["left"]
    return x

def tree_swap(t, u, v):
    if t["root"] == u:
        t["root"] = v
    elif u == u["parent"]["left"]:
        u["parent"]["left"] = v
    else:
        u["parent"]["right"] = v
    if v:
        v["parent"] = u["parent"]

def node_swap(t, u, v):
    if t["root"] == u:
        t["root"] = v
    elif u == u["parent"]["left"]:
        u["parent"]["left"] = v
    else:
        u["parent"]["right"] = v
    if v:
        v["parent"] = u["parent"]

# Příklad použití
seznam = ["Pavel", "Jitka", "Alice", "Karel", "David"]
osoby = {"root": None}

for i in seznam:
    vloz_do_seznamu(osoby, vytvor_seznam(i))

# Tisk seznamu
print("Seznam osob:", end=" ")
tisk_seznamu(osoby["root"])
print()
odeber_ze_seznamu(osoby, "Alice")
print("Seznam osob:", end=" ")
tisk_seznamu(osoby["root"])
