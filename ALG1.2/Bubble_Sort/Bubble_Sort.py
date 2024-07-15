def Bubble_Sort(arr):
    for j in range(len(arr)):
        for i in range(0, len(arr)-j-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

my_array = [7,2,4,8,1,3]
Bubble_Sort(my_array)
print("Seřazené pole:", my_array)


