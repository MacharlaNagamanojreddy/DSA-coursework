'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
def height(root):
    if not root:
        return -1
    return 1 + max(height(root.left), height(root.right))
def level_order(root):
    if not root:
        return 
    from collections import deque
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.data, end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Total Nodes:", count_nodes(root))
    print("Height of Tree:", height(root))
    print("Level Order Traversal:", end=' ')
    level_order(root)
main()
'''
'''
import heapq
""" def k_largest(arr,k):
    return heapq.nlargest(k,arr)


def k_smallest(arr,k):
    return heapq.nsmallest(k,arr)

print(k_largest([10,20,30,50,80,90,11],3))
print(k_smallest([10,20,30,50,80,90,11],3))
 """

# Sort using heap
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

print(heap_sort([10,5,22,20,15,16]))

import heapq
heap=[]

# Insert
heapq.heappush(heap,10)
heapq.heappush(heap,5)
heapq.heappush(heap,20)

print(heap)

# Remove Smallest
print(heapq.heappop(heap))
# peek
print(heap[0])

import heapq
heap=[]
heapq.heappush(heap,-10)
heapq.heappush(heap,-50)
heapq.heappush(heap,-5)
heapq.heappush(heap,-20)

print(heap)
print(-heapq.heappop(heap))

# converting List to heap
# Heapify is the process of converting tree into ,min heap or max heap tree

import heapq


arr= [10,20,30,40,50]
heapq.heapify(arr)
print(arr)
'''