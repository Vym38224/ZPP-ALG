# Alokace prazdné množiny
def create_bit_set(size):
    return[0] * size

# Alokace množiny o velikosti size a obsahující hodnoty ze seznamu values.
def create_bitset_with_values(size, values):
    if size <= 0:
        return []
    bitset = [0] * size
    for value in values:
        bitset[value] = 1
    return bitset

# Alokace mnoziny o velikosti size a obsahujici hodnoty 0 az upto - 1
def create_bitset_with_range(size, upto):
    if size <= 0:
        return []
    bitset = [0] * size
    for i in range(upto):
        bitset[i] = 1
    return bitset

# Vlozi prvek do mnoziny
def insert(bitset, element):
    if element < len(bitset):
        bitset[element] = 1

# Odebere prvek v z mnoziny
def remove(bitset, element):
    if element < len(bitset):
        bitset[element] = 0

# Funkce pro test, zda je prvek v mnozine. 
# Funkce vraci True pokud prvek v mnozine je a jinak False
def contains(bitset, element):
    if element < len(bitset):
        return bitset[element] == 1
    return False

# Prunik dvou mnozin. Pokud má jedna z množin větší size i tak 
# provedeme operaci, ale výsledná množina bude mít size větší množiny
def intersection(left, right):
    size = max(len(left), len(right))
    result = [0] * size
    for i in range(min(len(left), len(right))):
        result[i] = left[i] & right[i]
    return result

# Sjednoceni dvou mnozin. Pokud má jedna z množin větší size i tak 
# provedeme operaci, ale výsledná množina bude mít size větší množiny
def union(left, right):
    size = max(len(left), len(right))
    result = [0] * size
    for i in range(len(left)):
        result[i] = left[i]
    for i in range(len(right)):
        result[i] |= right[i]
    return result

# Rozdil dvou mnozin. Operaci provedeme pouze pokud size(left) >= size(right)
def difference(left, right):
    if len(left) >= len(right):
        result = [0] * len(left)
        for i in range(len(right)):
            result[i] = left[i] & ~right[i]
        return result
    else:
        return ("Neplatí, že size(left) >= size(right)!")

# Test podmnoziny vraci True pokud je left podmnozinou right jinak False.
def is_subset(left, right):
    if len(left) > len(right):
        return False
    for i in range(len(left)):
        if left[i] & ~right[i] != 0:
            return False
    return True

# Ulozi pole mnozin do souboru kde kazda mnozina je na jednom radku
def save_bitsets_to_file(file, bitsets):
    f = open(file, 'w')
    for bitset in bitsets:
        line = ''
        for bit in bitset:
            line += str(bit) + ' '
        line = line[:-1]  
        line += '\n'
        f.write(line)
    f.close()

# Nacte n mnozin ze souboru ulozenych funkci save_bitsets_to_file
def load_bitsets(file):
    bitsets = []
    f = open(file, 'r')
    for line in f:
        bitset = []
        num = ''
        for char in line:
            if char.isdigit():
                num += char
            elif num:
                bitset.append(int(num))
                num = ''
        if num:  
            bitset.append(int(num))
        bitsets.append(bitset)
    f.close()
    return bitsets

# Nacte ze souboru pouze mnoziny splnujici predikat condition
def load_bitsets_if(condition, file):
    bitsets = []
    with open(file, 'r') as f:
        for line in f:
            bitset = []
            num = ''
            for char in line:
                if char.isdigit():
                    num += char
                elif num:
                    bitset.append(int(num))
                    num = ''
            if num:  
                bitset.append(int(num))
            if condition(bitset):
                bitsets.append(bitset)
    return bitsets