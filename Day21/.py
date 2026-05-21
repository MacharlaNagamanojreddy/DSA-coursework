#reversing a queue

from collections import deque

q = deque([1,2,3,4,5])
stack = []

#step1 :push ino stack
while q:
    stack.append(q.popleft())

#step2 : push back to queue
while stack:
    q.append(stack.pop())

print("reversed queue: ", q)

