
from collections import deque

def reverse_recursive(arr):
    d = deque(arr)
    queue = deque()

    while d:
        queue.appendleft(d.popleft())
    return list(queue)

# Example usage
arr = [1, 2, 3, 4, 5]
print(reverse_recursive(arr))  # Output: [5, 4, 3, 2, 1]


# queue funcion
#
# from collections import deque
#
# # Creating a deque
# d = deque([1, 2, 3, 4])
#
# # Appending elements
# d.append(5)       # [1, 2, 3, 4, 5]
# d.appendleft(0)   # [0, 1, 2, 3, 4, 5]
#
# # Popping elements
# d.pop()           # [0, 1, 2, 3, 4] (removes 5)
# d.popleft()       # [1, 2, 3, 4] (removes 0)
#
# it can be used as list . like to find first element i can use d[0]