def reverse_diagonal_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if j == n - i - 1:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

n = 8
result_matrix = reverse_diagonal_matrix(n)
for row in result_matrix:
    print(row)
