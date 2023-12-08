import random
import time

selection_sort_comparisons = 0
quick_sort_comparisons = 0

def Selection_Sort(arr):
    global selection_sort_comparisons
    for j in range(len(arr)-1):
        iMin = j       
        for i in range(j+1, len(arr)):
            selection_sort_comparisons += 1  
            if arr[i] < arr[iMin]:
                iMin = i
        arr[j], arr[iMin] = arr[iMin], arr[j]

def Quick_Sort(arr):
    global quick_sort_comparisons
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        quick_sort_comparisons += len(less) + len(greater)  
        return Quick_Sort(less) + equal + Quick_Sort(greater)

def generate_array(size):
    return [random.randint(0, 9) for _ in range(size)]

def copy_array(original):
    return original.copy()

array_size = 10

for i in range(1, 4):
    array_size = array_size * 10

    original_array = generate_array(array_size)
    copied_array = copy_array(original_array)

    #Reset
    selection_sort_comparisons = 0
    quick_sort_comparisons = 0

    print(f"\n{i}. měření:")
    
    start_time = time.time()
    Selection_Sort(original_array)
    end_time = time.time()
    selection_sort_time = end_time - start_time
    print(f"(velikost pole {array_size}) Selection Sort trval: {selection_sort_time} sekundy, počet porovnání: {selection_sort_comparisons}")

    start_time = time.time()
    Quick_Sort(copied_array)
    end_time = time.time()
    quick_sort_time = end_time - start_time
    print(f"(velikost pole {array_size}) Quick Sort trval: {quick_sort_time} sekundy, počet porovnání: {quick_sort_comparisons}")
