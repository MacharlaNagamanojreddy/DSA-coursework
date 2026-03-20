#palindrome = input("Enter a word: ")
'''
palindrome = input("Enter a word: ")
palindrome = palindrome.lower()
if palindrome == palindrome[::-1]:
    print("The word is a palindrome.")
else:    print("The word is not a palindrome.")
'''


#palindrome = input("Enter a word: ")
def is_palindrome(string):
    left = 0
    right = len(string) - 1
    
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True
String = "Codegnan"
print("Palindrome: ", is_palindrome(String))
