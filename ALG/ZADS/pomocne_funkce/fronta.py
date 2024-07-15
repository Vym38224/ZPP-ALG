#Fronta = FIFO
def init_queue(n):
    k=[None for x in range(n)]
    s={"data":k,"head":0,"tail":0}
    return s

def empty(Q):
    return Q["head"] == Q["tail"]

def full(Q):
    return (Q["tail"] + 1)%len(Q["data"]) == Q["head"]

def enqueue(Q,x):
    if not full(Q):
        Q["data"][Q["tail"]]=x
        Q["tail"]=(Q["tail"] + 1)%len(Q["data"])

def dequeue(Q):
    if not empty(Q):
        x=Q["data"][Q["head"]]
        Q["head"]=(Q["head"] + 1)%len(Q["data"])
        return x
    else:
        return None

queue=init_queue(20)
enqueue(queue,6)
enqueue(queue,12)
enqueue(queue,18)
print(dequeue(queue))
print(dequeue(queue))
print(dequeue(queue))
print(dequeue(queue))