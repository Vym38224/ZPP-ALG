def create_stack():
    return []

def is_empty(stack):
    return stack == []

def push(stack, item):
    stack.append(item)

def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        return None

def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        return None

def size(stack):
    return len(stack)

# Použití zásobníku
stack = create_stack()
push(stack, 1)
push(stack, 2)
push(stack, 3)
print("Zásobník:", stack)
print("Vrchol zásobníku:", peek(stack))
print("Velikost zásobníku:", size(stack))
print("Odstranění vrcholu zásobníku:", pop(stack))
print("Zásobník po odebrání:", stack)
