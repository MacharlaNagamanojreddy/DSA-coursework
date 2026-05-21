class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def delete_from_begining(self):
        if self.head:
            self.head = self.head.next
        
    def delete_from_end(self):
        # Case 1: List is empty
        if self.head is None:
            return
        
        # Case 2: Only one node in the list
        if self.head.next is None:
            self.head = None
            return 
        
        # Case 3: More than one node
        # We need to stop at the second-to-last node
        temp = self.head
        while temp.next.next: 
            temp = temp.next

        # Disconnect the last node
        temp.next = None
        
    def search(self, key):
        temp = self.head
        while temp:
            if temp.value == key:
                return True
            temp = temp.next
        return False
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end=' -> ')
            temp = temp.next
        print("None") 

# Testing the code
l1 = LinkedList()
l1.insert_at_begining(10)
l1.insert_at_begining(20)
l1.insert_at_end(30)
l1.insert_at_end(40)
l1.display()           # Output: 20 -> 10 -> 30 -> 40 -> None

print(l1.search(30))   # Output: True

l1.delete_from_begining()
l1.display()           # Output: 10 -> 30 -> 40 -> None

l1.delete_from_end()
l1.display()           # Output: 10 -> 30 -> None