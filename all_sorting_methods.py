# quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []

    for i in arr[1:]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quicksort(left) + [pivot] + quicksort(right)
    
lst = [9,3,5,4,8,6,2,7,1,0]
sorted = quicksort(lst)
print(sorted)    


# shellsort

def shellsort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key
        gap //= 2
    return arr

array = [9, 3, 5, 4, 8, 6, 2, 7, 1, 0]
sorted = shellsort(array)
print(sorted)


# mergesort 
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) - 1
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    lefthalf = mergesort(lefthalf)
    righthalf = mergesort(righthalf)

    mergedarr = merge(lefthalf, righthalf)
    return mergedarr

def merge(left_arr, right_arr):
    merged_arr = []
    i = j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            merged_arr.append(left_arr[i])
            i += 1
        else:
            merged_arr.append(right_arr[j])
            j += 1
    
    merged_arr.extend(left_arr[i:])
    merged_arr.extend(right_arr[j:])

    return merged_arr

array = [9, 3, 5, 4, 8, 6, 2, 7, 1, 0]
sorted = mergesort(array)
print(sorted)




































