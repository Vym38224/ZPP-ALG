n = int(input("Zadejte číslo n (1-11): "))

if n >= 1 and n <= 11: 
    for i in range(1, n + 1):
        if i < 3:
            for _ in range(i):
                print("* " * i)
        else:
            for _ in range(i):
                if _ == 0 or _ == i - 1:
                    print("* " * i)
                else:
                    print("* " + "  " * (i - 2) + "*")
        print()
else:
    print("Neplatná hodnota n. Zadej číslo v rozmezí 1 až 11.")