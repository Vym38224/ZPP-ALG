for i in range(2, 100):
    prvocislo_x = False
    prvocislo_x2 = False

    if i <= 1:
        prvocislo_x = False
    elif i <= 3:
        prvocislo_x = True
    else:
        if i % 2 == 0 or i % 3 == 0:
            prvocislo_x = False
        else:
            j = 5
            while j * j <= i:
                if i % j == 0 or i % (j + 2) == 0:
                    prvocislo_x = False
                    break
                j += 6
            else:
                prvocislo_x = True

    if i + 2 <= 1:
        prvocislo_x2 = False
    elif i + 2 <= 3:
        prvocislo_x2 = True
    else:
        if (i + 2) % 2 == 0 or (i + 2) % 3 == 0:
            prvocislo_x2 = False
        else:
            j = 5
            while j * j <= (i + 2):
                if (i + 2) % j == 0 or (i + 2) % (j + 2) == 0:
                    prvocislo_x2 = False
                    break
                j += 6
            else:
                prvocislo_x2 = True

    if prvocislo_x and prvocislo_x2:
        print(f"Prvočíselná dvojice: {i}, {i + 2}")