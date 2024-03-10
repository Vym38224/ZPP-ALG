def create_queue():
    return []

def is_empty(queue):
    return queue == []

def enqueue(queue, item):
    queue.append(item)

def dequeue(queue):
    if not is_empty(queue):
        return queue.pop(0)
    else:
        return None

def size(queue):
    return len(queue)

# Použití fronty
queue = create_queue()
enqueue(queue, 1)
enqueue(queue, 2)
enqueue(queue, 3)
print("Fronta:", queue)
print("Velikost fronty:", size(queue))
print("Odstranění prvního prvku fronty:", dequeue(queue))
print("Fronta po odebrání:", queue)
