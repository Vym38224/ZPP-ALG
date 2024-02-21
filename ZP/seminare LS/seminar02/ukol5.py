def delka(seznam):
    if not seznam:
        return 0
    else:
        return 1 + delka(seznam[1:])  

# Test
test_seznam = []
print(delka(test_seznam))  
