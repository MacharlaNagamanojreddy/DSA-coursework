#!/usr/bin/env python3
# O(1) Constant Time Example

array = [1, 2, 3, 4, 5]
print("Array:", array)
print("Constant time access array[3]:", array[3])
print("Time Complexity: O(1) - always same time regardless of size")


#!/usr/bin/env python3
# O(n) Linear Time Example

array = [1, 2, 3, 4, 5]
print("Array:", array)
print("Linear time loop:")
for i in array:
    print(i)
print("Time Complexity: O(n) - n iterations")

#!/usr/bin/env python3
# O(n^2) Quadratic Time Example

n = 4  # Small n to avoid too much output
print(f"n = {n}")
for i in range(n):
    for j in range(n):
        print(f"{{i}}, {{j}}")
print("Time Complexity: O(n^2) - n * n iterations")
