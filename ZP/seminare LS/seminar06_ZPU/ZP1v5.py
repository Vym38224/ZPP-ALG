# pomocná funkce 
def extend_list(original_header, k):
    if not original_header:
        return [k, [], []]
    x = original_header

    while x[2]:
        x = x[2]
    x[2] = [k, [], []]
    return original_header

def vytvor_matici(x, y):
    rows = []
    columns = []
    for i in range(x):
        rows = extend_list(rows, i)
    for i in range(y):
        columns = extend_list(columns, i)
    new_matrix = [x, y, rows, columns]
    return new_matrix

def vloz_prvek(matrix, value, x, y):
    new_node = [value, x, y, [], []]

    row_pointer = matrix[2]
    for i in range(x):
        row_pointer = row_pointer[2]

    if not row_pointer[1] or y < row_pointer[1][2]:
        new_node[3] = row_pointer[1]
        row_pointer[1] = new_node
    else:
        column_pointer = row_pointer[1]
        while column_pointer[3] and y > column_pointer[3][2]:
            column_pointer = column_pointer[3]
        new_node[3] = column_pointer[3]
        column_pointer[3] = new_node

def zobraz_matici(matrix):
    row_pointer = matrix[2]
    for i in range(matrix[0]):
        node_pointer = row_pointer[1]
        for j in range(matrix[1]):
            if node_pointer == []:
                print(0, end="  ")
            elif node_pointer[2] == j:
                print(node_pointer[0], end="  ")
                node_pointer = node_pointer[3]
            else:
                print(0, end="  ")
        print()
        row_pointer = row_pointer[2]

# test
matice = vytvor_matici(3, 4)
vloz_prvek(matice, 1, 0, 1)
vloz_prvek(matice, 18, 0, 2)
vloz_prvek(matice, 3, 2, 2)
zobraz_matici(matice)

print(matice)
