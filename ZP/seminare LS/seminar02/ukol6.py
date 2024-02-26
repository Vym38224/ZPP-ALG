def pascal(row, col):
    if row >= col:
        if col == 0 or col == row:
            return 1
        else:
            return pascal(row - 1, col) + pascal(row - 1, col - 1)
    else:
        return("Chyba, nelze mít více sloupců než řádků")

# Test
row_index = 6
col_index = 2
print(pascal(row_index, col_index))

