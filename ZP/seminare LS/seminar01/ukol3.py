def reverse_diagonal_matrix(n):
    matrix = []
    for i in range(n):
        radek = []
        for j in range(n):
            if j == n - i - 1:
                radek.append(1)
            else:
                radek.append(0)
        matrix.append(radek)
    return matrix
    
try:
    n = 4
    n = a
    result_matrix = reverse_diagonal_matrix(n)
    for radek in result_matrix:
        print(radek)
except NameError:
    print("Přístup k nedefinované proměnné")

