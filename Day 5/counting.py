#count if string as vowels all vowels in the string and return the count of vowels in the string
'''
 def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
string = input("Enter a string: ")
vowel_count = count_vowels(string)
print(f"The number of vowels in the string is: {vowel_count}")

#reversing a text string and return the reversed string
def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string
string = input("Enter a string: ")
reversed_string = reverse_string(string)
print(f"The reversed string is: {reversed_string}")
'''