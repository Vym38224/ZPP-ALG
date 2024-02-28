def enqueue(Q, x):
    if not full(Q):
        Q["stack1"].append(x)

def dequeue(Q):
    if not empty(Q):
        if not Q["stack2"]:
            while Q["stack1"]:
                Q["stack2"].append(Q["stack1"].pop())
        return Q["stack2"].pop()

def empty(Q):
    return len(Q["stack1"]) + len(Q["stack2"]) == 0

def full(Q):
    return len(Q["stack1"]) + len(Q["stack2"]) == Q["top"]

# Inicializace fronty
Q = {"stack1": [],"stack2": [],"top": 10}

# Test
for i in range(10):
    enqueue(Q, i)
for i in range(10):
    print(dequeue(Q), end=",")
