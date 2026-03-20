def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 
arr = [100, 200, 30, 400, 500]
target = 500
print("Found at index: ", linear_search(arr, target))