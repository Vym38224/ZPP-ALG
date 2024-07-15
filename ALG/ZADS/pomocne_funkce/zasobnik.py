#Zásobník = LIFO
def length(array):
    return len(array)

def init_stack(n):
    k=[None for x in range(n)]
    s={"data":k,"top":0}
    return s

def push(S, x):
    if S["top"] < length(S["data"]):
        S["data"][S["top"]]=x
        S["top"]=S["top"] + 1

def pop(S):
    if S["top"] > 0:
        S["top"]=S["top"] - 1
        return S["data"][S["top"]]
    return None

def empty(S):
    return S["top"] == 0

def full(S):
    return S["top"] == length(S["data"])

stack=init_stack(20)

if full(stack)!=True:
    push(stack,10)
if full(stack)!=True:
    push(stack,8)
if full(stack)!=True:
    push(stack,18)
if empty(stack)!=True:
    print(pop(stack))

