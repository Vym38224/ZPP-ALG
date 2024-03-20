def enqueue(queue, value):
    new_node = {"key": value, "next": None}
    if "tail" not in queue:
        queue["head"] = new_node
        queue["tail"] = new_node
    else:
        queue["tail"]["next"] = new_node
        queue["tail"] = new_node

def dequeue(queue):
    if "head" not in queue:
        return None
    else:
        dequeued_value = queue["head"]["key"]
        queue["head"] = queue["head"]["next"]
        if queue["head"] is None:
            queue["tail"] = None
        return dequeued_value

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

# Vytvoření prázdné fronty
my_queue = {}

# Přidání prvků do fronty
enqueue(my_queue, 10)
enqueue(my_queue, 5)
enqueue(my_queue, 12)
enqueue(my_queue, 8)
enqueue(my_queue, 15)

# Vypsání obsahu fronty
print("Obsah fronty:")
display(my_queue)

# Odebrání prvků z fronty
print("Odebrané prvky:")
print(dequeue(my_queue))
print(dequeue(my_queue))

# Vypsání obsahu fronty po odebrání prvků
print("Obsah fronty po odebrání:")
display(my_queue)
