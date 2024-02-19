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
    
n = 8
result_matrix = reverse_diagonal_matrix(n)
for radek in result_matrix:
    print(radek)

