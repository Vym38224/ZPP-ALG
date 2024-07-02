def save_matrix(file, matrix):
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
    finally:
        f.close()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
save_matrix("ZP/seminare LS/seminar09/matrix.csv", matrix)
