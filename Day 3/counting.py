# ============================================
# COUNTING PROBLEMS - Simple & Easy Version
# ============================================

# --------------------------------------------
# COUNT EVEN NUMBERS 1 TO N
# --------------------------------------------
def count_even(n):
    count = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            count += 1
    return count


# --------------------------------------------
# COUNT ODD NUMBERS 1 TO N
# --------------------------------------------
def count_odd(n):
    count = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            count += 1
    return count


# --------------------------------------------
# COUNT DIGITS IN A NUMBER
# --------------------------------------------
def count_digits(n):
    n = abs(n)  # handle negative
    count = 0
    if n == 0:
        return 1
    while n > 0:
        n //= 10
        count += 1
    return count


# --------------------------------------------
# COUNT PRIME NUMBERS 1 TO N
# --------------------------------------------
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(n):
    count = 0
    for i in range(2, n+1):
        if is_prime(i):
            count += 1
    return count


# --------------------------------------------
# COUNT VOWELS IN STRING
# --------------------------------------------
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


# --------------------------------------------
# COUNT CONSONANTS IN STRING
# --------------------------------------------
def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in s:
        if char in consonants:
            count += 1
    return count


# --------------------------------------------
# COUNT CHARACTER OCCURRENCE
# --------------------------------------------
def count_char(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count


# --------------------------------------------
# SUM OF DIGITS
# --------------------------------------------
def sum_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


# --------------------------------------------
# REVERSE COUNT (Digits in reverse)
# --------------------------------------------
def reverse_number(n):
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


# --------------------------------------------
# MAIN FUNCTION - Test all functions
# --------------------------------------------
def main():
    # Test count even
    n = int(input("Enter a number: "))
    print("Even count:", count_even(n))
    print("Odd count:", count_odd(n))
    
    # Test count digits
    n = int(input("Enter a number: "))
    print("Digit count:", count_digits(n))
    
    # Test count primes
    n = int(input("Enter a number: "))
    print("Prime count:", count_primes(n))
    
    # Test vowels
    s = input("Enter a string: ")
    print("Vowel count:", count_vowels(s))
    print("Consonant count:", count_consonants(s))
    
    # Test char occurrence
    s = input("Enter a string: ")
    char = input("Enter character to count: ")
    print(f"'{char}' appears:", count_char(s, char), "times")
    
    # Test sum digits
    n = int(input("Enter a number: "))
    print("Sum of digits:", sum_digits(n))
    
    # Test reverse
    n = int(input("Enter a number: "))
    print("Reversed:", reverse_number(n))


if __name__ == "__main__":
    main()

