'''
# def heapify(Arr, n, i):
#     smallest = i
#     left = 2 * i + 1
#     right = 2 * i + 2

#     # Check if left child exists and is smaller
#     if left < n and Arr[left] < Arr[smallest]:
#         smallest = left

#     # Check if right child exists and is smaller
#     if right < n and Arr[right] < Arr[smallest]:
#         smallest = right

#     # If smallest is not the current node, swap and recurse
#     if smallest != i:
#         Arr[i], Arr[smallest] = Arr[smallest], Arr[i]
#         heapify(Arr, n, smallest)

from collections import deque

def bfs(graph, start):
    # Set to keep track of visited nodes
    visited = set()
    
    # Queue for BFS
    queue = deque([start])
    
    # Mark the start node as visited
    visited.add(start)
    
    # Loop until queue is empty
    while queue:
        # Pop from the front of the queue
        node = queue.popleft()
        print(node, end=" ")
        
        # Add all unvisited neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

print("BFS Traversal starting from A:")
bfs(graph, 'A')
'''
'''
from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}
print("Weighted graph:")
for node in graph:
    print(node, "->", graph[node])

def bfs_weighted(graph,start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
print("\nBFS on weighted graph:")
bfs_weighted(graph, 'A')


import heapq
def dijkstra(graph, source):
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        current_dist, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight   

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist   
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],   
    'C': [('D', 1)],
    'D': []
}
result = dijkstra(graph, 'A')
print(result)

def two_sum(arr, target):
    left=0
    right=len(arr) - 1
    
    while left < inset-inline-end:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < inset-inline-end:
            left += 1
        else:
            right -= 1
    return None
arr = [1,2,3,4,6,8,9]
target = 10
print(two_sum(arr, target))

def reverse(arr):
    left=0
    right=len(arr)-1
    while left < inset-inline-end:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
arr = [1,2,3,4,5]
print(reverse(arr))

def remove_duplicates(arr):
    if not arr:
        return []
    
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i+1
arr = [1, 1, 2, 2, 3, 4, 4]
length = remove_duplicates(arr)
print(arr[:length])

def max_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum
arr = [2,1,5,1,3,2]
k = 3
print(max_sum(arr, k))


#2,1,5,1,3,2

#2,1,5 = 8
#1,5,1 = 7
#5,1,3 = 9
#1,3,2 = 6

#1) fixed size window
#2) variable size window

#finding longest charcter Substring without repitition.

def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

s = "abcabcbb"
print(longest_unique_substring(s))

# def two_sum(arr , target):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i+1 , n):
#             if arr[i] + arr[j] == target:
#                 return (i , j)
#     return -1
# arr = [2 , 7 ,11 ,15]
# target = 9
# print(two_sum(arr , target))


# def two_sum(arr , target):
#     hashmap = {}
#     for i in range(len(arr)):
#         complement = target- arr[i]
#         if complement in hashmap:
#             return (hashmap[complement] , i)
        
#         hashmap[arr[i]] = i
#     return -1 
# arr = [2 , 7, 11 , 15]
# target = 9
# print(two_sum(arr , target))

def permutation(nums):
    result = []
    
    def backtrack(path, used):
        # base condition
        if len(path) == len(nums):
            result.append(path[:])  # add a copy of the current path
            return
        
        for i in range(len(nums)):
            if not used[i]:
                # choose
                used[i] = True
                path.append(nums[i])
                
                # explore
                backtrack(path, used)
                
                # un-choose (backtrack)
                path.pop()
                used[i] = False
    
    backtrack([], [False] * len(nums))
    return result

# Example usage:
nums = [1,2,3]
print(permutation(nums))

def coin_change(coins,amount):
    coins.sort(reverse=True)
    count = 0
    result = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
            count += 1 
    
    return coin,  result

coins = [1,2,5,10,20]
amount = 63
print(coin_change(coins, amount))
'''

def final_peak(arr):
    left,right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
    return arr[left]
arr = [1,3,8,12,4,2]
print(final_peak(arr))