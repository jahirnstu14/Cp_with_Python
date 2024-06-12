# // 1 2 3    7 2 1    7 4 1
# // 4 5 6 => 4 5 6 => 8 5 2
# // 7 8 9    9 8 7    9 6 3

# brute force method 

n = int(input())

matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Initialize the result matrix with 0s
ans = [[0] * n for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         ans[j][n - 1 - i] = matrix[i][j]

# Print the resulting matrix
# print(ans)


# 2 Steps to rotate image without new list or array  for shorting the space complexity to 0(1)

# Transpose the matrix
# reverse the row 

matrix.reverse()
    
    # Transpose the matrix
n = len(matrix)
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print(matrix)











