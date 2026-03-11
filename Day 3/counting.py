#counting problem approach  in DSA
'''

def count_even(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            count+=1
    return count    
def main():
    n=int(input("Enter the number: "))
    print("The count of even numbers from 1 to",n,"is:",count_even(n))
if __name__ == "__main__":
    main()

'''
#count digits in a number in DSA
'''

def count_digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
def main():
    n=int(input("Enter the number: "))
    print("The count of digits in the number",n,"is:",count_digits(n))
if __name__ == "__main__":
    main()
'''



