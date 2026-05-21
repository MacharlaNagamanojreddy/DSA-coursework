class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack")

    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print("Stack:", self.stack)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Top element:", s.peek())
print("Popped:", s.pop())
print("size")
s.display()

print("Stack size:", s.size())
