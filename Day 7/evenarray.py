#count even digits in a array 
'''
arr = [1, 2, 3, 4, 5, 6]
def countEvenDigits(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count
print(countEvenDigits(arr)) 
'''
#count maximum value in an array of an unknown size
def findMax(arr):
    max_value = float('-inf')  # Initialize max to the smallest possible value
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value
arr = [3, 1, 4, 1, 5, 9929, 2, 6, 5, 3, 5]
print(findMax(arr))
