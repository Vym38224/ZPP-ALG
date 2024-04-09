RED=0
BLACK=1

NIL={"c":BLACK,"key":None}

def set_left_child(p,c):
    p["left"]=c
    if c["key"] != None:
        c["parent"]=p

def set_right_child(p,c):
    p["right"]=c
    if c["key"] != None:
        c["parent"]=p

def set_root(t, x):
    t["root"] = x
    if x != None:
        x["parent"] = None

def transplant_tree(t, u, v):
    if u["parent"] == None:
        set_root(t, v)
    else:
        x = u["parent"]
        if u == x["left"]:
            set_left_child(x, v)
        else:
            set_right_child(x, v)

def rotate_left(t, x):
    y = x["right"]
    set_right_child(x, y["left"])
    transplant_tree(t, x, y)
    set_left_child(y, x)

def rotate_right(t, x):
    y = x["left"]
    set_left_child(x, y["right"])
    transplant_tree(t, x, y)
    set_right_child(y, x)

def tree_insert(T, z):
    y = None
    x = T["root"]
    while x["key"] != None:
        y = x 
        if z["key"] < x["key"]: 
            x = x["left"]
        else:
            x=x["right"]
    z["parent"]=y
    if y == None:
        T["root"]=z
    else:
        if z["key"] < y["key"]:
            y["left"]=z
        else:
            y["right"]=z

def tree_search(x, k):
    if x is None or x["key"] is None:
        return None 
    if k == x["key"]:
        return x
    elif k < x["key"]:
        return tree_search(x["left"], k)
    else:
        return tree_search(x["right"], k)


def uncle(z):
    if z["parent"]["parent"]["left"]["key"]==z["parent"]["key"]:
        return z["parent"]["parent"]["right"]
    else:
        return z["parent"]["parent"]["left"]
    
def local_fix(t,z):
    u=uncle(z)
    if u["c"]==RED:
            z["parent"]["c"]=BLACK
            z["parent"]["parent"]["c"]=RED
            u["c"]=BLACK
            return z["parent"]["parent"]
    else:
        if(z["parent"]["parent"]["left"]==z["parent"]):
            if z["parent"]["right"]["key"]==z["key"]:
                rotate_left(t,z["parent"])
            z["parent"]["c"]=BLACK
            z["parent"]["parent"]["c"]=RED
            rotate_right(t,z["parent"]["parent"])
        else:
            if z["parent"]["left"]==z:
                rotate_right(t,z["parent"])
            z["parent"]["c"]=BLACK
            z["parent"]["parent"]["c"]=RED
            
            rotate_left(t,z["parent"]["parent"])
        return z["parent"]
            
def rb_fixup(t,z):
    while (z != t["root"]):
        if z["parent"]["c"] == BLACK:
            break #algoritmus končí
        z = local_fix(t,z) # procedura pro opravy, viz dalsi slajdy
    t["root"]["c"] = BLACK

def rb_insert(t,added):
    added["left"]={"c":BLACK,"key":None,"parent":added}
    added["right"]={"c":BLACK,"key":None,"parent":added}
    added["c"] = RED
    tree_insert(t, added)
    rb_fixup(t, added)

def print_tree(x,i):
    if x["key"] != None:
        print("-"*(2*i),x["key"],"(",x["c"],")")
        i+=1
        print_tree(x["left"],i)
        print_tree(x["right"],i)

t={"root":{"c":BLACK,"body": None, "key":None,"parent":None}}

def body_celkem(s, jmeno):
    node = tree_search(s["root"], jmeno)
    if node and node["key"] == jmeno:
        print(f"Student {jmeno} má: {node['body']} bodů")
    else:
        print("Student není v seznamu")

def pridej_body(s, jmeno, body):
    existing_node = tree_search(s["root"], jmeno)
    if existing_node and existing_node["key"] == jmeno:
        existing_node["body"] += body
    else:
        u = {"parent": None, "body": body, "key": jmeno}
        rb_insert(s, u)

    print_tree(s["root"], 0)
    print()

pridej_body(t,"Pavel",2)
pridej_body(t,"Jirka",1)
pridej_body(t,"Alena",3)
pridej_body(t,"Pavel",4)
pridej_body(t,"Pavel",6)
pridej_body(t,"Jirka",2)

body_celkem(t,"Pavel")
body_celkem(t,"Karel")





