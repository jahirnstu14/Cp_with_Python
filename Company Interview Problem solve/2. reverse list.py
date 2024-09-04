def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap the elements at the left and right pointers
        arr[left], arr[right] = arr[right], arr[left]
        # Move the pointers towards the center
        left += 1
        right -= 1

# Example usage
arr = [1, 2, 3, 4, 5]
reverse_array(arr)

print("Reversed array:", arr)


# another way 
arr = [1, 2, 3, 4, 5]
n = len(arr)
for i in range(n // 2):
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

print("Reversed array:", arr)



#another  shortly 
print(arr[::-1])