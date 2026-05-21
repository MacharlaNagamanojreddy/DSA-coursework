'''
def isBalanced(s):
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
s = input("Enter a string of brackets: ")

if isBalanced(s):
    print("Valid Parentheses")
else:
    print("Invalid Parenteses") 
'''
'''

def removeOuterParentheses(s):
    result = ""
    count = 0

    for ch in s:
        if ch == '(':
            if count > 0:
                result += ch
            count += 1
        else:
            count -= 1
            if count > 0:
                result += ch
    return result
s = "(()())"
print(removeOuterParentheses(s))
'''
