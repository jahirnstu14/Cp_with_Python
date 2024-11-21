t = int(input())

for _ in range(t):
    k = int(input())
    a = list(map(int, input().split()))
    a.sort()
    left, right = 0, len(a) - 1  # Use indices for pointers

    while left < right:
        if a[left] * a[right] == k - 2:
            print(a[left], a[right])
            break
        elif a[left] * a[right] < k - 2:
            left += 1
        else:
            right -= 1  # Reduce the upper pointer