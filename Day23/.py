'''
# Implementation of deque 
""" 
Dequeue => Double ended Queue
Insertion and deletion from both ends
->Insert Front:
            appendleft()
->Insert Rear
            append()
->delete Front
            popleft()
->delete Rear
            pop()
"""

from collections import deque
dq = deque()
# Insering an element
dq.append(10)
dq.append(20)
dq.appendleft(20)
print("Deque after inserting: ",dq)
# delete Element
dq.pop()
print("Deque after pop: ",dq)
dq.popleft()
print("Deque after popleft: ",dq)
# Add more elements
dq.append(30)
dq.append(40)
print("final deque",dq)
# Peek
print("front Element", dq[0])
print("rear Element", dq[-1])

from collections import deque

def is_palindrome(s):
    dq =deque(s)

    while len(dq)> 1:
        if dq.popleft() != dq.pop():
            return False
    return True
    
s= "madam"
print("palindrome: ",is_palindrome(s))

""" 
Reversing first k element in the list 
input:
arr=[1,2,3,4,5,6,7]
userinput=5
o\p: [5,4,3,2,1,6,7]
arr=[1,2,3,4,5]
userinput=3
o\p: [3,2,1,4,5]
"""
from collections import deque
def reverse(dq,k):
    stack=[]
    for _ in range(k):
        stack.append(dq.popleft())
    
    while stack:
        dq.append(stack.pop())
        
    for _ in range(len(dq)-k):
        dq.append(dq.popleft())
        
    return dq
userinput=list(map(int,input().split()))
dq= deque(userinput)
k=int(input())
print(reverse(dq,k))
'''

