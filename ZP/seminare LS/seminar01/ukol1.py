def mocnina(zaklad, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / mocnina(zaklad, -exponent)
    else:
        result = 1
        for i in range(exponent):
            result *= zaklad
        return result
# Test
print(mocnina(3,0))  
