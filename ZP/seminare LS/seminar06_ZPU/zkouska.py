def add_node(row, col, value, next_row=None, next_col=None):
    return {"row": row, "col": col, "value": value, "next_row": next_row, "next_col": next_col}

def vytvor_matici(m, n):
    rows = [None] * m
    cols = [None] * n
    return rows, cols

def vloz_prvek(matice, prvek, row, col):
    rows, cols = matice  # Rozbalení matice na řádky a sloupce
    
    if row < 0 or row >= len(rows) or col < 0 or col >= len(cols):
        return("Index řádku nebo sloupce mimo rozsah matice")
    
    new_node = add_node(row, col, prvek, next_row=None, next_col=None)
    
    # Přidání prvku do řádku
    if rows[row] is None or rows[row]["col"] > col:
        new_node["next_row"] = rows[row]
        rows[row] = new_node
    else:
        current = rows[row]
        while current["next_row"] and current["next_row"]["col"] < col:
            current = current["next_row"]
        new_node["next_row"] = current["next_row"]
        current["next_row"] = new_node
    
    # Přidání prvku do sloupce
    if cols[col] is None or cols[col]["row"] > row:
        new_node["next_col"] = cols[col]
        cols[col] = new_node
    else:
        current = cols[col]
        while current["next_col"] and current["next_col"]["row"] < row:
            current = current["next_col"]
        new_node["next_col"] = current["next_col"]
        current["next_col"] = new_node

def get_value(matice, row, col):
    rows, cols = matice
    
    if row < 0 or row >= len(rows) or col < 0 or col >= len(cols):
        raise IndexError("Index řádku nebo sloupce mimo rozsah matice")
    
    current_row = rows[row]
    while current_row and current_row["col"] < col:
        current_row = current_row["next_row"]
    
    if current_row and current_row["col"] == col:
        return current_row["value"]
    else:
        return 0

def ukaz_matici(matice):
    rows, cols = matice
    for row in range(len(rows)):
        for col in range(len(cols)):
            print(get_value(matice, row, col), end=" ")
        print()  # Nový řádek po každém řádku matice

# Příklad použití:
matice = vytvor_matici(3, 3)
vloz_prvek(matice, 1, 0, 0)
vloz_prvek(matice, 5, 2, 1)
ukaz_matici(matice)
