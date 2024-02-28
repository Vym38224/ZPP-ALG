def test_any(f,sekvence):
    for i in sekvence:
        if f(i):
            return True
    return False

sekvence = [7,6,5,5]
mensi_nez_5 = lambda x: x < 5

print(test_any(mensi_nez_5, sekvence))
