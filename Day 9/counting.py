def linear_search(arr, target):
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            count += 1
    return count
arr = [50, 40, 30, 20, 30, 10, 30]
target = 30
print("Count: ", linear_search(arr, target))
