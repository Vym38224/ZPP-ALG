def push(stack, value):
    new_node = {"key": value, "next": None}
    if "head" not in stack:
        stack["head"] = new_node
    else:
        new_node["next"] = stack["head"]
        stack["head"] = new_node

def pop(stack):
    if "head" not in stack:
        return None
    else:
        popped_value = stack["head"]["key"]
        stack["head"] = stack["head"]["next"]
        return popped_value

def display(queue):
    output = "["
    current = queue["head"]
    while current:
        output += str(current["key"])
        if current["next"]:
            output += ", "
            output += "["
        else:
            output += ", [None]"  
        current = current["next"]
    output += "]" * (output.count("[") - output.count("]")) + "]" 
    print(output)

# Vytvoření prázdného zásobníku
my_stack = {}

# Přidání prvků do zásobníku
push(my_stack, 10)
push(my_stack, 8)
push(my_stack, 15)

# Vypsání obsahu zásobníku
print("Obsah zásobníku:")
display(my_stack)

# Odebrání prvků ze zásobníku
print("Odebrané prvky:")
print(pop(my_stack))
print(pop(my_stack))

# Vypsání obsahu zásobníku po odebrání prvků
print("Obsah zásobníku po odebrání:")
display(my_stack)

