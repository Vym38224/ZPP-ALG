def factorial(n, vysledek=1):
    if n == 0:
        return vysledek
    else:
        return factorial(n - 1, n * vysledek)

print(factorial(5))
