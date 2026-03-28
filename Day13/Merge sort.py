def merge_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr 
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # Call the renamed 'merge' function here
    return merge(left, right)
# Renamed this function from merge_sort to merge
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr = [5, 2, 4, 1]
sorted_arr = merge_sort(arr)
print("Original Array: ", arr)
print("Sorted Array: ", sorted_arr)