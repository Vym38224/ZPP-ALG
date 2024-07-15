def Quick_Sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return Quick_Sort(less) + [pivot] + Quick_Sort(greater)

my_array = [7, 3, 2, 4, 8, 1]
my_array = Quick_Sort(my_array)
print("Seřazené pole:", my_array)
