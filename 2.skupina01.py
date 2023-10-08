#úkol: add (3, 4) => 7
def add(x, y):
    while (y > 0):
        x = x + 1
        y = y - 1
        #print(x, y)
    return x

#funkce sub - odečítání čísel (předpoklad, že y <= x)
def sub(x, y):
    while y > 0:
        x = x - 1
        y = y - 1
    return x

#fce mult(3, 4) => 12
def mult(x, y):
    z = 0 
    while x > 0:
        x = x - 1
        z = add(z, y)
    return z

#fce leq (menší nebo rovno) (2, 5) => tru
def leq(x, y):
    while x > 0 and y > 0:
        x = x - 1
        y = y - 1
    return x == 0


"""tam kde to jde použít for"""

#eq (rovnost) (2, 2) => true
"""def eq(x, y):
    while x > 0 and y > 0:
        x = x - 1
        y = y - 1
"""
#div(7, 2) => 3

#mod(7, 2) => 1

#power(2, 3) => 8


#fce sum_up_to(5) = 0 + 1 + 2 + 3 + 4 = 10
def sum_up_to(x):
    z = 0
    for y in range(x):
        z = z + y
        print(z, y)
    return z

#sum_squares_up_to(3) => (0 * 0) + (1 * 1) + (2 * 2) = 5
def sum_squares_up_to(x):
    z = 0
    for y in range(x):
        z = z + (y * y)
        print(z, y)
    return z

#fce faktoriál (kde 0! = 1; n! = n * (n - 1)!); př. factorial(3) => 6
#def factorial(x):
    
