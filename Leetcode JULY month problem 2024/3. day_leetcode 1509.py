# Greate explanation : https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/?envType=daily-question&envId=2024-07-03
    


def minDifference(A):
    n = len(A)
    if n < 5:
        return 0
    A.sort()
    return min(A[n - 1] - A[3], A[n - 2] - A[2], A[n - 3] - A[1], A[n - 4] - A[0])

# Example usage:
A = [1, 5, 6, 14, 15, 16, 18, 19, 20]
print(minDifference(A))  # Output: 1
