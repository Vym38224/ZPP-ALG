import bit_set

mnozina = bit_set.create_bit_set(10)
print(mnozina)  # Output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

mnozina_s_hodnotou = bit_set.create_bitset_with_values(10, [2, 5, 7])
print(mnozina_s_hodnotou)  # Output: [0, 0, 1, 0, 0, 1, 0, 1, 0, 0]

mnozina_upto = bit_set.create_bitset_with_range(10, 8)
print(mnozina_upto)  # Output: [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]

pridej = bit_set.insert(mnozina, 3)  # změní index 3 hodnotu 1
print(mnozina)  

odeber = bit_set.remove(mnozina, 3)  # změní index 3 hodnotu 0
print(mnozina)  

pridej = bit_set.insert(mnozina, 3)  # změní index 3 hodnotu 1
print(mnozina)  

zkontroluj = bit_set.contains(mnozina, 3)  # zkontroluje zda je na indexu 3 1/0 (True/False)
print(zkontroluj)  

left_set = [1, 0, 1, 1]
right_set = [1, 0, 1, 1, 0]

print(bit_set.intersection(left_set, right_set))  # průnik
print(bit_set.union(left_set, right_set))         # sjednocení
print(bit_set.difference(left_set, right_set))    # rozdíl pokud size(left) >= size(right)
print(bit_set.is_subset(left_set, right_set))     # být podmnožinou (left podmnožinou right)

A = [[1, 3, 5, 7, 9, 20],[4,5,7]]

bit_set.save_bitsets_to_file("ZP/seminare LS/seminar11_ZPU2/bit_sets.txt", A)

loaded_bitsets = bit_set.load_bitsets("ZP/seminare LS/seminar11_ZPU2/bit_sets.txt")
print(loaded_bitsets)

condition =  lambda bitset: max(bitset) <= 10 
filtered_bitsets = bit_set.load_bitsets_if(condition,"ZP/seminare LS/seminar11_ZPU2/bit_sets.txt")
print(filtered_bitsets)