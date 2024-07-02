def test_all(f, sekvence):
    for i in sekvence:
        if not f(i):
            return False
    return True

sekvence = [1,2,5,4,2]
mensi_nez_5 = lambda x: x < 5

print(test_all(mensi_nez_5, sekvence))
