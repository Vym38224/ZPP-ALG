def load_matrix(file):
    matrix = []
    f = open(file)
    for line in f:
        row = []
        element = ""
        for char in line:
            if char == ",":
                row.append(int(element))
                element = ""
            else:
                element += char
        row.append(int(element)) 
        matrix.append(row)
    return matrix

matrix = load_matrix("ZP/seminare LS/seminar09/matrix.csv")
print(matrix)
