# Simplified bubble sort (iterative): prints sorted array and iteration count
# Supports ascending (default) and descending order

def bubble_sort(arr, descending=False):
    n = len(arr)
    count = 0
    order = "descending" if descending else "ascending"
    for i in range(n):
        for j in range(n - i - 1):
            if (arr[j] > arr[j + 1]) != descending:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
    print(f"Sorted array ({order}): {arr}")
    print(f"Swaps: {count}")

# Example usage
arr = [8, 4, 2, 6]
bubble_sort(arr.copy())  # ascending
arr = [8, 4, 2, 6]
bubble_sort(arr.copy(), descending=True)  # descending