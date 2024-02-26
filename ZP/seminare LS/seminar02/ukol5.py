def delka(seznam):
    if not seznam:
        return 0
    else:
        return 1 + delka(seznam[1:])  

# Test
test_seznam = [1,4]
print(delka(test_seznam))  
