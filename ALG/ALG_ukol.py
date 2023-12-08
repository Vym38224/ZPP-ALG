import random

def Selection_Sort(arr):
    for j in range(len(arr)-2):
        iMin = j       
        for i in range(j+1, len(arr)):
            if arr[i] < arr[iMin]:
                iMin = i
            arr[j], arr[iMin] = arr[iMin], arr[j]
    print("\nSorted Array:",arr)

def generate_array(size):
    return [random.randint(0,9) for _ in range(size)]

def copy_array(original):
    return original.copy()

array_size = 100

original_array = generate_array(array_size)

copied_array = copy_array(original_array)

print("Original Array:", original_array)
#print("Copied Array:", copied_array)

Selection_Sort(original_array)


