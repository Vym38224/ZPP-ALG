def Selection_Sort(arr):
    for j in range(len(arr)-2):
        iMin = j       
        for i in range(j+1, len(arr)):
            if arr[i] < arr[iMin]:
                iMin = i
            arr[j], arr[iMin] = arr[iMin], arr[j]

my_array = [7,3,2,4,8,1]
Selection_Sort(my_array)
print("Seřazené pole:", my_array)
