def mocnina(zaklad, exponent):
    try:
        if exponent == 0:
            return 1
        elif exponent < 0:
            return 1 / mocnina(zaklad, -exponent)
        else:
            result = 1
            for i in range(exponent):
                result *= zaklad
            return result
    except TypeError:
            return("nekompatibilní datové typy")
            
# Test
print(mocnina(3,1)) 

print(mocnina(3,"a"))


