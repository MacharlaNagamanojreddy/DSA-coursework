# ============================================
# NUMBER OPERATIONS - Simple & Easy Version
# ============================================

import math


# --------------------------------------------
# CHECK EVEN OR ODD
# --------------------------------------------
# Even: divisible by 2 (no remainder)
# Odd: not divisible by 2 (has remainder)

def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is EVEN")
    else:
        print(num, "is ODD")


# --------------------------------------------
# FIND BIGGEST AND SMALLEST (3 numbers)
# --------------------------------------------

def find_max_min(a, b, c):
    # Find biggest
    if a >= b and a >= c:
        max_num = a
    elif b >= a and b >= c:
        max_num = b
    else:
        max_num = c

    # Find smallest
    if a <= b and a <= c:
        min_num = a
    elif b <= a and b <= c:
        min_num = b
    else:
        min_num = c

    print("Biggest:", max_num)
    print("Smallest:", min_num)


# --------------------------------------------
# CHECK IF PRIME NUMBER
# --------------------------------------------
# Prime: only divisible by 1 and itself
# Examples: 2, 3, 5, 7, 11, 13...

def is_prime(num):
    if num < 2:
        return False
    
    # Check if divisible by any number from 2 to square root
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True


# --------------------------------------------
# CHECK POSITIVE, NEGATIVE OR ZERO
# --------------------------------------------

def check_sign(num):
    if num > 0:
        print(num, "is POSITIVE")
    elif num < 0:
        print(num, "is NEGATIVE")
    else:
        print(num, "is ZERO")


# --------------------------------------------
# CHECK ARMSTRONG NUMBER
# --------------------------------------------
# Armstrong: sum of digits each raised to power of number of digits
# Example: 153 = 1^3 + 5^3 + 3^3 = 153

def is_armstrong(num):
    # Count number of digits
    num_str = str(num)
    n = len(num_str)
    
    # Calculate sum of digits raised to power n
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** n
        temp //= 10
    
    return total == num


# --------------------------------------------
# CHECK PERFECT NUMBER
# --------------------------------------------
# Perfect: sum of proper divisors equals the number
# Example: 6 = 1 + 2 + 3

def is_perfect(num):
    if num <= 1:
        return False
    
    # Sum of proper divisors
    total = 1  # 1 is always a proper divisor
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            total += i
            if i != num // i:
                total += num // i
    
    return total == num

# --------------------------------------------
# SUM OF N NUMBERS
# --------------------------------------------

def calculate_sum(N):
    total = 0
    for i in range(1, N + 1):
        total += i
    return total


# --------------------------------------------
# SUM OF N EVEN NUMBERS
# --------------------------------------------

def calculate_even_sum(N):
    total = 0
    for i in range(2, N * 2 + 1, 2):
        total += i
    return total


# --------------------------------------------
# MAIN FUNCTION - Test all functions
# --------------------------------------------
def main():
    # Test even/odd
    num = int(input("Enter a number to check even/odd: "))
    check_even_odd(num)
    
    # Test max/min
    print("\n--- Find Max and Min ---")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    find_max_min(a, b, c)
    
    # Test prime
    print("\n--- Check Prime ---")
    p = int(input("Enter a number to check if prime: "))
    print(p, "is prime:", is_prime(p))
    
    # Test sign
    print("\n--- Check Sign ---")
    s = int(input("Enter a number to check sign: "))
    check_sign(s)
    
    # Test Armstrong
    print("\n--- Check Armstrong ---")
    arm = int(input("Enter a number to check if Armstrong: "))
    print(arm, "is Armstrong:", is_armstrong(arm))
    
    # Test Perfect
    print("\n--- Check Perfect ---")
    perf = int(input("Enter a number to check if perfect: "))
    print(perf, "is perfect:", is_perfect(perf))
    
    
    # Test sum functions
    print("\n--- Sum Functions ---")
    N = int(input("Enter a number for sum: "))
    print("The sum of first", N, "numbers is:", calculate_sum(N))
    print("The sum of first", N, "even numbers is:", calculate_even_sum(N))


if __name__ == "__main__":
    main()

