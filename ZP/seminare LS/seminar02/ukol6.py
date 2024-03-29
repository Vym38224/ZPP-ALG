def pascal(row, col):
    if row >= col:
        if col == 0 or col == row:
            return 1
        else:
            return pascal(row - 1, col) + pascal(row - 1, col - 1)

# Test
row_index = 4
col_index = 2
print(pascal(row_index, col_index))

