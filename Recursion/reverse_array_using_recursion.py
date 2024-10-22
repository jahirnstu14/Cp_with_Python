def reverse_recursive(arr):
    if len(arr) == 0:
        return []
    return [arr[-1]] + reverse_recursive(arr[:-1])

# Example usage
arr = [1, 2, 3, 4, 5]
print(reverse_recursive(arr))  # Output: [5, 4, 3, 2, 1]



