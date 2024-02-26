def factorial(n, vysledek):
    if n == 0:
        return vysledek
    else:
        return factorial(n - 1, n * vysledek)

print(factorial(5,1))
