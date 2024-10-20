
# https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1

# time complexity = o(n)
# N,X = map(int,input().split())
#
# arr =[map(int,input().split())]
#
# count = 0
#
# for i in range(N):
#     if arr[i]==X:
#         count+=1
#
# print(f"{count}")

# important : Number of in array The number of elements between two indices (inclusive) can be calculated as :
# number_of_elements = (last_index−first_index)+1

# same complexity with another way

def count_occurrences(arr, n, x):
    # Create a hash map to count occurrences
    occurrence_map = {}

    # Count occurrences of each element in the array
    for number in arr:
        if number in occurrence_map:
            occurrence_map[number] += 1
        else:
            occurrence_map[number] = 1

    # Alternative way to retrieve the count of x
    if x in occurrence_map:
        return occurrence_map[x]  # Return the count of x
    else:
        return 0  # Return 0 if x is not present

# Example usage:
N = 7
X = 2
Arr = [1, 1, 2, 2, 2, 2, 3]
print(count_occurrences(Arr, N, X))  # Output: 4

X = 4
print(count_occurrences(Arr, N, X))  # Output: 0


# time complexit = 0(log(n))
# using binary search
def count_occurrences(arr, n, x):
    # Helper function to find the first occurrence of x
    def first_occurrence(arr, n, x):
        low, high = 0, n - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                first = mid
                high = mid - 1  # Move left to find the first occurrence
            elif arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return first

    # Helper function to find the last occurrence of x
    def last_occurrence(arr, n, x):
        low, high = 0, n - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                last = mid
                low = mid + 1  # Move right to find the last occurrence
            elif arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return last

    # Find the first and last occurrence of x
    first = first_occurrence(arr, n, x)
    if first == -1:  # If x is not found in the array
        return 0

    last = last_occurrence(arr, n, x)

    # The number of occurrences is the difference between last and first index + 1
    return last - first + 1


# Example usage:
N = 7
X = 2
Arr = [1, 1, 2, 2, 2, 2, 3]
print(count_occurrences(Arr, N, X))  # Output: 4

X = 4
print(count_occurrences(Arr, N, X))  # Output: 0


# using bisect function in python
import bisect


def count_occurrences(arr, n, x):
    # Find the first position where x can be inserted
    first = bisect.bisect_left(arr, x)

    # Find the position just after the last occurrence of x
    last = bisect.bisect_right(arr, x)

    # The number of occurrences is the difference between last and first indices
    # If x is not found, first == last, so the result will be 0
    return last - first
# bisect_left(arr, x): Finds the index of the first occurrence of X in the array (or the position where it could be inserted to maintain the order).
# bisect_right(arr, x): Finds the index just after the last occurrence of X in the array (or where it could be inserted to maintain the order).
# The difference between bisect_right() and bisect_left() gives the count of X in the array. If X is not present, both functions return the same index, and the difference will be 0.

# to understand clearly

# bisect_left(arr, X): Think of it as the position where you would insert X in the array so that everything remains sorted, while keeping X's duplicates on the right. This returns the index of the first occurrence of X (if it exists) or the first element greater than X (if it doesn’t exist). Example: In [1, 1, 2, 2, 2, 2, 3], bisect_left(arr, 2) returns 2 because 2 first appears at index 2. bisect_right(arr, X): This finds the index where you can insert X in the array while keeping the array sorted, but this time, it pushes X’s duplicates to the left. It returns the position just after the last occurrence of X. Example: In [1, 1, 2, 2, 2, 2, 3], bisect_right(arr, 2) returns 6, which is right after the last 2.

# Example usage:

N = 7
X = 2
Arr = [1, 1, 2, 2, 2, 2, 3]
print(count_occurrences(Arr, N, X))  # Output: 4

X = 4
print(count_occurrences(Arr, N, X))  # Output: 0

        
    
    