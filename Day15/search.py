def search_rotated_arr(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        
        if arr[low] <= arr[mid]:  # Left half is sorted
            if arr[low] <= target < arr[mid]:  # Target is in the left half
                high = mid - 1
            else:  # Target is in the right half
                low = mid + 1
        else:  # Right half is sorted
            if arr[mid] < target <= arr[high]:  # Target is in the right half
                low = mid + 1
            else:  # Target is in the left half
                high = mid - 1
    return -1
arr = [4, 5, 6, 7, 0, 1, 2]
target = 6
print("Index:", search_rotated_arr(arr, target))
