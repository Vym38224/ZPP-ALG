def sachovnice(s):
    print("  a b c d e f g h")

    for i in range(8):
        row = str(1 + i) + " "
        for j in range(8):
            if s[i][j] == 1:
                row += "o "
            elif s[i][j] == 2:
                row += "* "
            else:
                row += ". "
        print(row + str(1 + i))
    print("  a b c d e f g h")

s1 = [[0, 1, 0, 1, 0, 1, 0, 1],
      [1, 0, 1, 0, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 1, 0, 1],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 2, 0, 2, 0, 2, 0, 2],
      [2, 0, 2, 0, 2, 0, 2, 0],
      [0, 2, 0, 2, 0, 2, 0, 2]]

sachovnice(s1)
