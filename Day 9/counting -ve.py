def linear_search(arr):
    negatives = [] 
    for num in arr:
        if num < 0:
            negatives.append(num) 
    return negatives
arr = [10, -5, 20, -3, 30, -1,-69,-78]
print(f"Negative numbers: {linear_search(arr)}")   
