def Insertion_Sort(arr):
    for j in range(1, len(arr)):
        t = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > t:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = t

my_array = [7,2,4,8,1,3]
Insertion_Sort(my_array)
print("Seřazené pole:", my_array)
