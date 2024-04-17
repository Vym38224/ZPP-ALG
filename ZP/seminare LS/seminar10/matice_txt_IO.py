def uloz_matici(file, matrix):
    try:
        f = open(file, "w")
        for row in matrix:
            row_str = ""
            for i in range(len(row)):
                row_str += str(row[i])
                if i < len(row) - 1:
                    row_str += ","
            f.write(row_str + "\n")
    except:
        print("Chyba při práci se souborem")

def nacti_matici(file):
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