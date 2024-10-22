# https://www.hackerrank.com/challenges/30-arrays/problem


k = int(input())

n = list(map(int,input().split()))

for i in reversed(n):
    print(i,end=" ")


# most efficient way to reverse array
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Swap the elements
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))  # Output: [5, 4, 3, 2, 1]

arr = [2] + [5]
print(arr)